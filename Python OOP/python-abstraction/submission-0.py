class Superhero:
    def __init__(self, name: str):
       self._name = name
       self._power_level = 40
    
    def fly(self)->str:
        res:str =None 
        if self._power_level >= 20:
            res = "Up up and away!"
            self._power_level -= 20
        else:
            res = "Too tired to fly..."
        return res

    
# Do not modify the code below
hero = Superhero("Superman")
print(hero.fly())  
print(hero.fly())
print(hero.fly())  
