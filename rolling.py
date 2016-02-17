import random

def diceroll():
    return random.randrange(1,6) + random.randrange(1,6)

def startroll(winnings, gamesettings):
    roundwinnings = comeoutroll(gamesettings)
    print("Round Winnings: %d" % roundwinnings)
    return winnings + roundwinnings

def comeoutroll(gamesettings):
    roll = diceroll()
    if roll == 2 or roll == 3 or roll == 12:
        comewinnings = -gamesettings["pass"]
    elif roll == 7 or roll == 11:
        comewinnings = gamesettings["pass"]
    else:
        comewinnings = pointroll(roll, gamesettings)

    return comewinnings


def pointroll(roll, gamesettings):
    newroll = diceroll()
    while newroll != roll:
        if newroll == 7:
            pointresult = -(gamesettings["pass"] + gamesettings["passodds"])
            return pointresult
        newroll = diceroll()

    if roll == 4 or roll == 10:
        pointresult = 2 * (gamesettings["pass"] + gamesettings["passodds"])
    elif roll == 5 or roll == 9:
        pointresult = 3 / 2 * (gamesettings["pass"] + gamesettings["passodds"])
    elif roll == 6 or roll == 8:
        pointresult = 6 / 5 * (gamesettings["pass"] + gamesettings["passodds"])
    return pointresult
