# -*- coding: utf-8 -*-
from os.path import join

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from ....Classes.Frame import Frame
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.MachineDFIM import MachineDFIM
from ....Classes.Shaft import Shaft
from ....Classes.VentilationCirc import VentilationCirc
from ....Classes.VentilationPolar import VentilationPolar
from ....Classes.VentilationTrap import VentilationTrap
from ....Classes.Winding import Winding
from ....Classes.WindingUD import WindingUD
from ....Classes.WindingCW2LT import WindingCW2LT
from ....Classes.WindingDW2L import WindingDW2L
from ....Classes.MatMagnetics import MatMagnetics
from ....Classes.SlotW61 import SlotW61

from ....Tests import save_plot_path as save_path
from ....Tests.Plot.LamWind import wind_mat


"""unittest for Lamination with winding plot"""


def test_Lam_Wind_61():
    """Test machine plot with Slot 61
    """
    print("\nTest plot Slot 61")
    plt.close("all")
    test_obj = MachineDFIM()
    test_obj.rotor = LamSlotWind(
        Rint=0, Rext=0.1325, is_internal=True, is_stator=False, L1=0.9
    )
    test_obj.rotor.slot = SlotW61(
        Zs=12,
        W0=15e-3,
        W1=35e-3,
        W2=12.5e-3,
        H0=15e-3,
        H1=20e-3,
        H2=25e-3,
        H3=1e-3,
        H4=2e-3,
        W3=3e-3,
    )
    test_obj.rotor.winding = WindingCW2LT(qs=3, p=3, Lewout=60e-3)
    plt.close("all")

    test_obj.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s61_1-Rotor.png"))
    # 1 for Lam, Zs*2 for wind
    assert len(fig.axes[0].patches) == 25

    test_obj.rotor.slot.W3 = 0
    test_obj.rotor.slot.H3 = 0
    test_obj.rotor.slot.H4 = 0
    test_obj.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s61_2-Rotor Wind.png"))
    # 1 for Lam, Zs*2 for wind
    assert len(fig.axes[0].patches) == 25

    tooth = test_obj.rotor.slot.get_surface_tooth()
    tooth.plot(color="r")
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s61_Tooth_in.png"))
