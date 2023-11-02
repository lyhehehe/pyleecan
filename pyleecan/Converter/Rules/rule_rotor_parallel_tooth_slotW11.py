from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.RuleComplex import RuleComplex


def add_rule_rotor_parallel_tooth_slotW11(rule_list):
    print("rotor_parallel_tooth_slotW11")

    rule_list.append(RuleComplex(fct_name="rotor_slotW11", src="pyleecan"))

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Bar_Opening_[T]"],
            pyleecan=f"machine.rotor.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Rotor_Tooth_Width"],
            pyleecan=f"machine.rotor.slot.W3",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Bar_Opening_Depth_[T]"],
            pyleecan=f"machine.rotor.slot.H0",
            unit_type="m",
            scaling_to_P=1,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Bar_Corner_Radius[T]"],
            pyleecan=f"machine.rotor.slot.R1",
            unit_type="m",
            scaling_to_P=0.5,
        )
    )

    rule_list.append(
        RuleSimple(
            other=["[Dimensions]", "Bar_Tip_Angle_[T]"],
            pyleecan=f"machine.rotor.slot.H1",
            unit_type="rad",
            scaling_to_P=1,
        )
    )

    rule_list.append(RuleComplex(fct_name="rotor_slotW11_H1", src="pyleecan"))

    rule_list.append(
        RuleEquation(
            param_other=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Bar_Depth_[T]"],
                    "variable": "y",
                },
            ],
            param_pyleecan=[
                {
                    "src": "pyleecan",
                    "path": f"machine.rotor.slot.H2",
                    "variable": "x",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.rotor.slot.H1",
                    "variable": "a",
                },
            ],
            unit_type="m",
            scaling_to_P="y = a+x",
        )
    )

    return rule_list
