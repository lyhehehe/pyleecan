from matplotlib.patches import Patch, FancyArrowPatch
import matplotlib.pyplot as plt
from swat_em import datamodel
from numpy import (
    sqrt,
    pi,
    sign as np_sign,
    abs as np_abs,
    arccos,
    arctan,
    arcsin,
    angle as np_angle,
)

from ....Functions.labels import decode_label, WIND_LAB, BAR_LAB, LAM_LAB, WEDGE_LAB
from ....Functions.Winding.find_wind_phase_color import find_wind_phase_color
from ....Functions.Winding.gen_phase_list import gen_name
from ....Functions.init_fig import init_fig
from ....definitions import config_dict
from ....Classes.WindingSC import WindingSC

PHASE_COLORS = config_dict["PLOT"]["COLOR_DICT"]["PHASE_COLORS"]
ROTOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["ROTOR_COLOR"]
STATOR_COLOR = config_dict["PLOT"]["COLOR_DICT"]["STATOR_COLOR"]
if "WEDGE_COLOR" not in config_dict["PLOT"]["COLOR_DICT"]:
    config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"] = "y"
WEDGE_COLOR = config_dict["PLOT"]["COLOR_DICT"]["WEDGE_COLOR"]
PLUS_HATCH = "++"
MINUS_HATCH = ".."


def plot(
    self,
    fig=None,
    ax=None,
    is_lam_only=False,
    sym=1,
    alpha=0,
    delta=0,
    is_edge_only=False,
    edgecolor=None,
    is_add_arrow=False,
    is_display=True,
    is_add_sign=True,
    is_show_fig=True,
    save_path=None,
    win_title=None,
    is_legend=True,
    is_clean_plot=False,
    is_winding_connection=False,
):
    """Plot the Lamination in a matplotlib fig

    Parameters
    ----------
    self : LamSlotWind
        A LamSlotWind object
    fig : Matplotlib.figure.Figure
        existing figure to use if None create a new one
    ax : Matplotlib.axes.Axes object
        Axis on which to plot the data
    is_lam_only : bool
        True to plot only the lamination (remove the Winding)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation
    is_edge_only: bool
        To plot transparent Patches
    edgecolor:
        Color of the edges if is_edge_only=True
    is_display : bool
        False to return the patches
    is_add_sign : bool
        True to Add + / - on the winding
    is_show_fig : bool
        To call show at the end of the method
    save_path : str
        full path including folder, name and extension of the file to save if save_path is not None
    win_title : str
        Title for the window
    is_legend : bool
        True to add the legend
    is_clean_plot : bool
        True to remove title, legend, axis (only machine on plot with white background)
    is_winding_connection : bool
        True to display winding connections

    Returns
    -------
    patches : list
        List of Patches
    fig : Matplotlib.figure.Figure
        Figure containing the plot
    ax : Matplotlib.axes.Axes object
        Axis containing the plot
    """
    # Arrow style
    head = None
    style = "Simple, tail_width=2, head_width=8, head_length=12"
    kw = dict(arrowstyle=style, linewidth=0.8, edgecolor="k")

    if self.is_stator:
        color_lam = STATOR_COLOR
    else:
        color_lam = ROTOR_COLOR

    # Get the LamSlot surface(s)
    surf_list = self.build_geometry(sym=sym, alpha=alpha, delta=delta)

    patches = list()
    # getting the number of phases and winding connection matrix
    if self.winding is not None:
        if isinstance(self.winding, WindingSC):  # plot only one phase for WindingSC
            wind_mat = None
            qs = 1
        else:
            try:
                wind_mat = self.winding.get_connection_mat(self.get_Zs())
                qs = self.winding.qs
                if is_winding_connection and self.is_stator:
                    # generate a datamodel for the winding
                    wdg = datamodel()
                    # generate winding from inputs
                    wdg.genwdg(
                        Q=self.get_Zs(),
                        P=2 * self.get_pole_pair_number(),
                        m=qs,
                        layers=self.winding.Nlayer,
                        turns=self.winding.Ntcoil,
                        w=self.winding.coil_pitch,
                    )
                    head = wdg.get_wdg_overhang(optimize_overhang=False)
            except:
                wind_mat = None
                qs = 1
    else:
        wind_mat = None
        qs = 1

    for surf in surf_list:
        label_dict = decode_label(surf.label)
        if LAM_LAB in label_dict["surf_type"]:
            patches = surf.get_patches(
                color_lam, is_edge_only=is_edge_only, edgecolor=edgecolor
            )
            if head is not None:  # Add transparency to lamination when arrows are added
                for patch in patches:
                    patch._alpha = 0.2
            patches.extend(patches)
        elif WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
            if not is_lam_only:
                color, sign = find_wind_phase_color(wind_mat=wind_mat, label=surf.label)
                if sign == "+" and is_add_sign:
                    hatch = PLUS_HATCH
                elif sign == "-" and is_add_sign:
                    hatch = MINUS_HATCH
                else:
                    hatch = None
                patches.extend(
                    surf.get_patches(
                        color=color,
                        is_edge_only=is_edge_only,
                        hatch=hatch,
                        edgecolor=edgecolor,
                    )
                )
                if head is not None:
                    for phase in head:
                        if label_dict["S_id"] + 1 in [line[0][0] for line in phase]:
                            start_ind = [line[0][0] for line in phase].index(
                                label_dict["S_id"] + 1
                            )
                            start_point = [
                                surf.comp_point_ref().real,
                                surf.comp_point_ref().imag,
                            ]
                            end_point = None
                            for surf2 in surf_list:
                                label_dict2 = decode_label(surf2.label)
                                if (
                                    "S_id" in label_dict2
                                    and phase[start_ind][0][1]
                                    == label_dict2["S_id"] + 1
                                ):
                                    end_point = [
                                        surf2.comp_point_ref().real,
                                        surf2.comp_point_ref().imag,
                                    ]
                                    delta_indices = (
                                        phase[start_ind][0][1] - phase[start_ind][0][0]
                                    )
                                    if (
                                        abs(delta_indices) > self.get_Zs() / 2
                                    ):  # Handle connections like 43 with 2
                                        delta_indices = np_sign(delta_indices) * (
                                            abs(delta_indices) - self.get_Zs()
                                        )
                                    signe = np_sign(delta_indices)  # Arrow direction
                                    break
                            if end_point is not None:
                                dist_AB = sqrt(
                                    (end_point[0] - start_point[0]) ** 2
                                    + (end_point[1] - start_point[1]) ** 2
                                )
                                angle = signe * (1.5 * self.Rext) / dist_AB
                                line = FancyArrowPatch(
                                    start_point,
                                    end_point,
                                    connectionstyle="arc3,rad=" + str(angle),
                                    facecolor=color,
                                    zorder=2,
                                    **kw
                                )
                                patches.append(line)

                            break

        elif WEDGE_LAB in label_dict["surf_type"] and not is_lam_only:
            patches.extend(surf.get_patches(WEDGE_COLOR, is_edge_only=is_edge_only))
        else:
            patches.extend(
                surf.get_patches(is_edge_only=is_edge_only, edgecolor=edgecolor)
            )

    if is_display:

        # Display the result
        (fig, ax, patch_leg, label_leg) = init_fig(fig=fig, ax=ax, shape="rectangle")

        ax.set_xlabel("(m)")
        ax.set_ylabel("(m)")
        for ii, patch in enumerate(patches):
            ax.add_patch(patch)
        # Axis Setup
        ax.axis("equal")

        # Window title
        if self.is_stator:
            prefix = "Stator "
        else:
            prefix = "Rotor "
        if (
            win_title is None
            and self.parent is not None
            and self.parent.name not in [None, ""]
        ):
            win_title = self.parent.name + " " + prefix[:-1]
        elif win_title is None:
            win_title = prefix[:-1]
        manager = plt.get_current_fig_manager()
        if manager is not None:
            manager.set_window_title(win_title)

        # The Lamination is centered in the figure
        Lim = self.Rext * 1.5
        ax.set_xlim(-Lim, Lim)
        ax.set_ylim(-Lim, Lim)

        title = None

        # Add the legend
        if not is_edge_only:
            if self.is_stator and "Stator" not in label_leg:
                patch_leg.append(Patch(color=STATOR_COLOR))
                label_leg.append("Stator")
                title = "Stator with winding"
            elif not self.is_stator and "Rotor" not in label_leg:
                patch_leg.append(Patch(color=ROTOR_COLOR))
                label_leg.append("Rotor")
                title = "Rotor with winding"
            ax.set_title(title)
            # Add the wedges legend only if needed
            if (
                self.slot is not None
                and self.slot.wedge_mat is not None
                and not is_lam_only
            ):
                patch_leg.append(Patch(color=WEDGE_COLOR))
                label_leg.append("Wedge")
            # Add the winding legend only if needed
            if not is_lam_only:
                if isinstance(self.winding, WindingSC):
                    patch_leg.append(Patch(color=PHASE_COLORS[0]))
                    label_leg.append(prefix + "Bar")
                elif self.winding is not None:
                    phase_name = [prefix + n for n in gen_name(qs, is_add_phase=True)]
                    for ii in range(qs):
                        if not phase_name[ii] in label_leg and not is_add_sign:
                            # Avoid adding twice the same label
                            index = ii % len(PHASE_COLORS)
                            patch_leg.append(Patch(color=PHASE_COLORS[index]))
                            label_leg.append(phase_name[ii])
                        if not phase_name[ii] + " +" in label_leg and is_add_sign:
                            # Avoid adding twice the same label
                            index = ii % len(PHASE_COLORS)
                            patch_leg.append(
                                Patch(color=PHASE_COLORS[index], hatch=PLUS_HATCH)
                            )
                            label_leg.append(phase_name[ii] + " +")
                        if not phase_name[ii] + " -" in label_leg and is_add_sign:
                            # Avoid adding twice the same label
                            index = ii % len(PHASE_COLORS)
                            patch_leg.append(
                                Patch(color=PHASE_COLORS[index], hatch=MINUS_HATCH)
                            )
                            label_leg.append(phase_name[ii] + " -")

            if is_legend:
                ax.legend(patch_leg, label_leg)

        if save_path is not None:
            fig.savefig(save_path)
            plt.close(fig=fig)
        # Clean figure
        if is_clean_plot:
            ax.set_axis_off()
            ax.axis("equal")
            if ax.get_legend() is not None:
                ax.get_legend().remove()
            ax.set_title("")

        if is_show_fig:
            fig.show()
        return fig, ax
    else:
        return patches
