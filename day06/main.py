from typing import List

class LanternFish(): 
    def __init__(self, timer=9): 
        self.timer: int = timer

    def age(self) -> bool: 
        # returns True if a new fish is added to the school 
        if self.timer == 0: 
            self.timer = 6
            return True
        else: 
            self.timer -= 1 
            return False

class School(): 
    def __init__(self):
         self.population: List[LanternFish] = []

    def new_fish(self, fish) -> None: 
        self.population.append(fish)

    def get_school(self) -> List[LanternFish]: 
        return [ fish.timer for fish in self.population ]

    def next_day(self) -> None: 
        for fish in self.population: 
            if fish.age(): 
                self.new_fish(LanternFish())

def partOne(fishes) -> int: 
    school = School()

    for fish in fishes: 
        school.new_fish(LanternFish(fish))
    
    print(f"Initial State: {school.get_school()}")

    days: int = 256
    for day in range(1, days+1): 
        school.next_day()
        print(f"After {day} days: {len(school.get_school())}")

    return len(school.get_school())

if __name__ == "__main__": 
    f = "test.txt"
    # read lines 
    # with open(f, "r") as input: 
        # input_lines: List[int] = [ int(n) for n in input.read().strip().split(",")]

    print(partOne([7]))