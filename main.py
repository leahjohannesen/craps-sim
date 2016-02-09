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
print("A. Pass bet: %d" % gamesettings["pass"])
print("B. Pass odds bet: %d" % gamesettings["passodds"])

i = 1
winnings = gamesettings["starting"]

while i < 5:
    minamt = gamesettings["pass"] + gamesettings["passodds"]
    if winnings < minamt:
        print("YOU OUT OF DOLLARS")
        break
    winnings = rolling.startroll(winnings, gamesettings)
    print("Round %d: Total: %d" % (i, winnings))
    i += 1

print("FINAL WINNINGS: %d" % winnings)
