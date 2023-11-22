from abc import ABC , abstractmethod

class CharacterState(ABC):
    @abstractmethod
    def respond(self, character):
        pass

# Concrete State - Great
class GreatState(CharacterState):
    def respond(self, character):
        print("Feeling great!")


# Concrete State - Good
class GoodState(CharacterState):
    def respond(self, character):
        print("Feeling good.")


# Concrete State - OK
class OKState(CharacterState):
    
    def respond(self, character):
        print("Feeling OK.")

# Concrete State - Bad
class BadState(CharacterState):
    def respond(self, character):
        print("Feeling bad.")


# Concrete State - Furious
class FuriousState(CharacterState):
    def respond(self, character):
        print("Feeling furious!")


# Context - Character
class Character:
    def __init__(self, mood:int):
        self.mood = mood
        self.state = self.chooseState()

    def moodChange(self , change:int ):
        self.mood = self.mood + change
        self.state = self.chooseState()
        self.respond()

    
    def respond(self):
        print(f"Character mood: {self.mood}")
        self.state.respond(self)

    def set_state(self):
        self.state = self.chooseState()
        
    def chooseState(self):
        if 80 <= self.mood :
            return GreatState()
        elif 60 <= self.mood <= 79:
            return GoodState()
        elif 40 <= self.mood <= 59:
            return OKState()
        elif 20 <= self.mood <= 39:
            return BadState()
        else:
            return FuriousState()


# Client

def sth():
    return input(
        """choose: 
            1 - Welcome My friend (most positive)
            2 - Hello budy (positive)
            3 - ... (bad)
            4 - move out of my way (the worst) 
            0 - to exit
        """)
    
def actionToMood(act:str) -> int:
    if act =="1":
        return 20
    if act =="2":
        return 10
    if act =="3":
        return -10
    if act == "4":
        return -20
    else :
        print ("no int")
        return 0


def main():
    character = Character(45)  # OK
    print("=======start=========")
    while(True):
        action = sth()
        if action =="0" :
            exit()
        change = actionToMood(action)
        character.moodChange(change)

main()
