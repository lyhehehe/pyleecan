# -*- coding: utf-8 -*-


def comp_masses(self):
    """Compute the masses of the Lamination

    Parameters
    ----------
    self : Lamination
        A Lamination object

    Returns
    -------
    M_dict: dict
        Lamination mass dictionnary (Mtot, Mlam) [kg]

    """
    rho = self.mat_type.struct.rho
    V_dict = self.comp_volumes()

    M_dict = dict()
    M_dict["Mlam"] = V_dict["Vlam"] * self.Kf1 * rho
    M_dict["Mtot"] = M_dict["Mlam"]

    return M_dict
