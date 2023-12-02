import re

with open("2\input_2.1.txt", "r") as games:
	games = games.readlines()

maxRed = 12
maxGreen = 13
maxBlue= 14
possible = 0

for game in games:
    gameId = game.split(": ")[0].split(" ")[1]
    cubeSets = game.split(": ")[1]
    cubeSets = cubeSets.split(";")
    red = True
    green = True
    blue = True
    for cubeSet in cubeSets:
        
        cubeSet = cubeSet.strip()
        if "red" in cubeSet:
            numberOf =re.findall(r"(\d+) red", cubeSet)[0]
            if int(numberOf) > maxRed:
                red = False
        if "green" in cubeSet:
            numberOf = re.findall(r"(\d+) green", cubeSet)[0]
            if int(numberOf) > maxGreen:
                green = False
        if "blue" in cubeSet:
            numberOf = re.findall(r"(\d+) blue", cubeSet)[0]
            if int(numberOf) > maxBlue:
                blue = False
    if red & green & blue:
        possible = possible + int(gameId)
print(possible)
        
            
