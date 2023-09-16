

def roll_call_dwarves(dwarf_names):
    for index, name in enumerate(dwarf_names, start=1):
        print(f"{index}. {name}")


def summon_captain_planet(planeteers):
    new_list = [(f"{name.title()}!") for name in planeteers]
    planeteers = new_list
    return planeteers


def long_planeteer_calls(word_list):
    any_words_greater_than_4 = any(len(word) > 4 for word in word_list)
    if any_words_greater_than_4:
        return True
    else:
        return False


def find_the_cheese(snacks):
    for snack in snacks:
        if snack == "cheddar" or snack == "gouda" or snack == "camembert":
            return snack
    return None
