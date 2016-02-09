import random

def startroll(winnings, gamesettings):
    roundwinnings = comeoutroll(gamesettings)
    print("Round Winnings: %d" % roundwinnings)
    return winnings + roundwinnings

def comeoutroll(gamesettings):
    roll = random.randrange(2,12)
    if roll == 2 or roll == 3 or roll == 12:
        comewinnings = gamesettings["pass"]
    elif roll == 7 or roll == 11:
        comewinnings = gamesettings["pass"]
    else:
        comewinnings = pointroll(roll, gamesettings)

    return comewinnings


def pointroll(roll, gamesettings):
    diceroll = random.randrange(2,12)
    while diceroll != roll:
        if diceroll == 7:
            pointresult = gamesettings["pass"] - gamesettings["passodds"]
            return pointresult
        diceroll = random.randrange(2,12)

    if roll == 4 or roll == 10:
        pointresult = 2 * (gamesettings["pass"] + gamesettings["passodds"])
    elif roll == 5 or roll == 9:
        pointresult = 3 / 2 * (gamesettings["pass"] + gamesettings["passodds"])
    elif roll == 6 or roll == 8:
        pointresult = 6 / 5 * (gamesettings["pass"] + gamesettings["passodds"])
    return pointresult
