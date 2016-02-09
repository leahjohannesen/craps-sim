def display(gamesettings):
    print("A. Starting money: %d" % gamesettings["starting"])
    print("B. Pass bet: %d" % gamesettings["pass"])
    print("C. Pass odds bet: %d" % gamesettings["passodds"])
    print("Choose an option to modify, or type DONE to run:")

    choice = input("> ")
    return choice

def changebranch(choice, gamesettings):
    if choice == "A":
        newval = int(input("New starting amount: \n> "))
        gamesettings["starting"] = newval
    if choice == "B":
        newval = int(input("New pass bet: \n> "))
        gamesettings["pass"] = newval
    if choice == "C":
        newval = int(input("New odds bet: \n>"))
        gamesettings["passodds"] = newval
    return gamesettings
