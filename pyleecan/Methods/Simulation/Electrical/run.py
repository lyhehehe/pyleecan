from numpy import angle

from ....Classes.EEC_SCIM import EEC_SCIM
from ....Classes.EEC_PMSM import EEC_PMSM
from ....Classes.MachineSCIM import MachineSCIM
from ....Classes.MachineSIPMSM import MachineSIPMSM
from ....Classes.MachineIPMSM import MachineIPMSM

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the Electrical module"""
    if self.parent is None:
        raise InputError("The Electrical object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    self.get_logger().info("Starting Electric module")

    output = self.parent.parent

    machine = output.simu.machine

    if self.eec is None:
        # Init EEC depending on machine type
        if isinstance(machine, MachineSCIM):
            self.eec = EEC_SCIM()
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)):
            self.eec = EEC_PMSM()
    else:
        # Check that EEC is consistent with machine type
        if isinstance(machine, MachineSCIM) and not isinstance(self.eec, EEC_SCIM):
            raise Exception(
                "Cannot run Electrical model if machine is SCIM and eec is not EEC_SCIM"
            )
        elif isinstance(machine, (MachineSIPMSM, MachineIPMSM)) and not isinstance(
            self.eec, EEC_PMSM
        ):
            raise Exception(
                "Cannot run Electrical model if machine is PMSM and eec is not EEC_PMSM"
            )

    if self.LUT is not None:
        eec = self.LUT.get_eec(Tsa=self.Tsta)

    # Compute parameters of the electrical equivalent circuit if some parameters are missing in ELUT
    eec_param = self.eec.comp_parameters(
        machine, OP=output.elec.OP, Tsta=self.Tsta, Trot=self.Trot
    )

    if output.elec.PWM is None:
        # Solve the electrical equivalent circuit for fundamental only
        out_dict = self.eec.solve(eec_param)
    else:
        # Generate voltage signal (PWM signal generation is the only strategy for now)
        if output.elec.PWM.U0 is None:
            # Current driven mode
            # Solve the electrical equivalent circuit for fundamental current
            # to get fundamental phase voltage
            out_dict = self.eec.solve(eec_param)
            U0c = out_dict["Ud"] + 1j * out_dict["Uq"]
            output.elec.PWM.U0 = abs(U0c)
            output.elec.PWM.Phi0 = angle(U0c)

            # Calculate PWM voltage
            self.gen_drive(output)

        else:
            # Voltage driven mode
            # Calculate PWM voltage first
            self.gen_drive(output)

            # Solve the electrical equivalent circuit for fundamental voltage
            # to get fundamental current
            out_dict = self.eec.solve(eec_param)

        # Solve for each voltage harmonics in case of PWM
        out_dict["Is_PWM"] = self.eec.solve_PWM(output, eec_param)

    # Compute losses due to Joule effects
    out_dict = self.eec.comp_joule_losses(out_dict, machine)

    # Compute electromagnetic power
    out_dict = self.comp_power(out_dict, machine)

    # Compute torque
    self.comp_torque(out_dict, output.elec.OP.get_N0())

    # Store electrical quantities contained in out_dict in OutElec, as Data object if necessary
    output.elec.store(out_dict)
