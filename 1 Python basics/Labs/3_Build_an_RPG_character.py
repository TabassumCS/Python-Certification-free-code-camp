full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):
        return "The character name should be a string"
    
    if not name:
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance (charisma, int):
        return "All stats should be integers"
    
    if min(strength, intelligence, charisma) < 1:
        return "All stats should be no less than 1"

    if max(strength, intelligence, charisma) > 4:
        return "All stats should be no more than 4"
    

    sum = strength + intelligence +charisma

    if sum != 7:
        return "The character should start with 7 points"

    #---Build stat lines ---
    strength_line = "STR " + full_dot * strength + empty_dot *(10-strength)
    intelligence_line = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    charisma_line = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)

    # --- Combine lines into final string ---
    return f"{name}\n{strength_line}\n{intelligence_line}\n{charisma_line}"


print(create_character('ren', 4, 2, 1))
