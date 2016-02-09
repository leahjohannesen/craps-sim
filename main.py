import setup
import rolling

choice = ""
winnings = 0
gamesettings = {
"starting": 100,
"pass": 5,
"dontpass": 0,
"passodds": 10,
"dontpassodds": 0
}

while choice != "DONE":
    choice = setup.display(gamesettings)
    gamesettings = setup.changebranch(choice, gamesettings)

print("Final settings:")
print("A. Starting amount: %d" % gamesettings["starting"])
print("B. Pass bet: %d" % gamesettings["pass"])
print("C. Pass odds bet: %d" % gamesettings["passodds"])

i = 1
winnings = gamesettings["starting"]
rounds = int(input("Number of rounds to sim: "))

while i < rounds:
    minamt = gamesettings["pass"] + gamesettings["passodds"]
    if winnings < minamt:
        print("YOU OUT OF DOLLARS")
        break
    winnings = rolling.startroll(winnings, gamesettings)
    print("Round %d: Total: %d" % (i, winnings))
    i += 1

print("FINAL WINNINGS: %d" % winnings)
