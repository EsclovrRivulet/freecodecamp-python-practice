full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    elif not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return "All stats should be integers"
    elif not all(stat >= 1 for stat in (strength, intelligence, charisma)):
        return "All stats should be no less than 1"
    elif not all(stat <= 4 for stat in (strength, intelligence, charisma)):
        return "All stats should be no more than 4"
    elif sum((strength, intelligence, charisma)) != 7:
        return "The character should start with 7 points"
    else:
        str_line = f"STR {full_dot * strength}{empty_dot * (10 - strength)}"
        int_line = f"INT {full_dot * intelligence}{empty_dot * (10 - intelligence)}"
        cha_line = f"CHA {full_dot * charisma}{empty_dot * (10 - charisma)}"
        return f"{name}\n{str_line}\n{int_line}\n{cha_line}"

print(create_character('ren', 4, 2, 1))