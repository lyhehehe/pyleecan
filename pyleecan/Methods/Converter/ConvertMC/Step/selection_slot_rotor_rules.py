from pyleecan.Converter.Rules.rule_rotor_parallel_tooth_slotW11 import (
    add_rule_rotor_parallel_tooth_slotW11,
)


def selection_slot_rotor_rules(self):
    slot_rotor_type = self.other_dict["[Design_Options]"]["Top_Bar_Type"]

    if slot_rotor_type == 0:
        pass

    elif slot_rotor_type == 1:
        pass

    elif slot_rotor_type == 2:
        self.rules_list = add_rule_rotor_parallel_tooth_slotW11(self.rules_list)
    elif slot_rotor_type == 3:
        pass
        # add_rules_parallel_slot_slotW11

    return self.rules_list
