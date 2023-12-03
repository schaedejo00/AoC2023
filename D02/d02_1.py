from CubeGame import CubeGame, CubeGameRound


#with open('./D02/input.txt', 'r', encoding="utf-8") as f:
with open('./D02/example.txt', 'r', encoding="utf-8") as f:
    puzzleInput = f.read().split("\n")


games:list[CubeGame] = []
colorBounds:dict[str, int] = {"red":12, "green":13, "blue":14}


for line in puzzleInput:
    #print(line)
    start, rounds = line.split(": ")
    rounds = rounds.split(";")
    game: CubeGame = CubeGame()
    
    for round in rounds:
        #print(round)
        colors = round.split(",")
        cubeGameRound: CubeGameRound = CubeGameRound()
        
        for color in colors:
            color = color.lstrip()
            amount, color = color.split(" ")            
            cubeGameRound.increase(color, int(amount))
            
        game.rounds.append(cubeGameRound)
    
    games.append(game)
    #print(game)

sum = 0
for game in games:
    validGame = game.isValid(colorBounds)
    if validGame:
        sum += game.id
        
print(sum)
        



