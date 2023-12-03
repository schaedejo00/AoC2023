from collections import defaultdict

class CubeGameRound:
        
    def __init__(self):
        self.round: dict[str, int] = {}
        
    def increase(self, color:str, amount:int):
        if color not in self.round:
            self.round[color] = amount
        else:
            self.round[color] = self.round[color] + amount
            
    def getAmount(self, color:str)->int:
        if color in self.round:
            return self.round[color]
        return 0
    
    def __str__(self)->str:
        keys = self.round.keys()
        to_return = [{key: self.round[key]} for key in keys]
        return "round: " + str(to_return)

    def __repr__(self)->str:
        return self.__str__()

class CubeGame:      
    id_counter: int = 0

    def __init__(self):
        CubeGame.id_counter += 1        
        self.id:int = CubeGame.id_counter
        self.rounds:list[CubeGameRound] = []
        
    def isValid(self, colors: dict[str, int])->bool:
        for round in self.rounds:
            for colorName in colors.keys():
                currentAmount = round.getAmount(colorName)
                
                if currentAmount > colors[colorName]:
                    return False;
        return True;
    
    def getPower(self)->int:
        minCubes:dict[str, int] = {"red":0, "green":0, "blue":0}
        for round in self.rounds:
            for color in round.round.keys():
                if minCubes[color]<round.round[color]:
                    minCubes[color] = round.round[color]
        power:int=1
        for color in minCubes.keys():
            power *= minCubes[color]
        return power
            
        
            
        
    def __str__(self)->str:        
        return "game[" + str(self.id) + "]: " + str(self.rounds)

    def __repr__(self)->str:
        return self.__str__()
    
    


        
    
