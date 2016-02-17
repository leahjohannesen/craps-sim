import setup
import rolling
import pandas as pd

choice = ""
winnings = 0
gamesettings = {
"starting": 1000,
"pass": 5,
"dontpass": 0,
"passodds": 10,
"dontpassodds": 0
}

#while choice != "DONE":
#    choice = setup.display(gamesettings)
#    gamesettings = setup.changebranch(choice, gamesettings)

print("Final settings:")
print("A. Starting amount: %d" % gamesettings["starting"])
print("B. Pass bet: %d" % gamesettings["pass"])
print("C. Pass odds bet: %d" % gamesettings["passodds"])



i = 1
winnings = gamesettings["starting"]
rounds = int(input("Number of rounds to sim: "))

roundframe = pd.DataFrame()

while i <= rounds:
    minamt = gamesettings["pass"] + gamesettings["passodds"]
    if winnings < minamt:
        print("YOU OUT OF DOLLARS")
        break
    winnings = rolling.startroll(winnings, gamesettings)
    tempdf = pd.DataFrame({ 'Round': [i],
                            'Winnings': [winnings]})
    print("Round %d: Total: %d" % (i, winnings))
    i += 1
    roundframe = roundframe.append(tempdf, ignore_index=True)


print("FINAL WINNINGS: %d" % winnings)

roundmean = roundframe.mean()
roundstdev = roundframe.std()

print('Final:', roundframe['Winnings'].iloc[-1])
print('Mean:', roundmean[1])
print('Std Dev:', roundstdev[1])
