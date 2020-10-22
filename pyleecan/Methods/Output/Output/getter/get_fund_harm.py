# -*- coding: utf-8 -*-


def get_fund_harm(self, data_str):
    """Return the fundamental harmonic of the physical quantity given by data_str

    Parameters
    ----------
    self : Output
        an Output object

    Returns
    -------
    fund_harm: dict
        Dict containing axis name as key and frequency/order/wavenumber of fundamental harmonic as value

    """

    if data_str in ["B", "P", "Is", "Phi_wind_stator"]:

        fund_harm = dict()

        p = self.simu.machine.get_pole_pair_number()

        f_elec = self.simu.input.comp_felec()

        if data_str == "B":
            fund_harm["freqs"] = f_elec
            fund_harm["wavenumber"] = p
        elif data_str == "P":
            fund_harm["freqs"] = 2 * f_elec
            fund_harm["wavenumber"] = 2 * p
        elif data_str in ["Is", "Phi_wind_stator"]:
            fund_harm["freqs"] = f_elec

    else:
        fund_harm = None

    return fund_harm
