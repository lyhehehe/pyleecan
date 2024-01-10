from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleComplex import RuleComplex


def add_rule_slotM15(self):
    """Create and adapt all the rules related to slotM15
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : Bool
        A booleen to know, position in lamination
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Number"],
            P_obj_path=f"machine.rotor.slot.Zs",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Thickness"],
            P_obj_path=f"machine.rotor.slot.H1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", "Magnet_Arc_[ED]"],
            P_obj_path=f"machine.rotor.slot.W0",
            unit_type="ED",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    if self.machine.rotor.slot.H0 != 0:
        self.rules_list.append(
            RuleComplex(fct_name="inset_parallel_slotM15", folder="MotorCAD")
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=["[Dimensions]", "Magnet_Thickness"],
                P_obj_path=f"machine.rotor.slot.H0",
                unit_type="m",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    else:
        self.rules_list.append(
            RuleComplex(fct_name="surface_parallel_slotM15", folder="MotorCAD")
        )
