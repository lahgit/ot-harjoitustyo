Level2 =   [[1, 1, 1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0]]


Level1 =   [[1, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 0]]


Level3 =   [[1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]]

Level4 =   [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]


Levellist = {"Level 1":Level1, "Level 2":Level2, "Level 3":Level3, "Level 4":Level4}



class SelectorForLevels:

    def __init__(self):

        self.selected_level = self.select()
        

    def select(self):
        print("Available levels: \n")
        for stage in Levellist:
            print(stage)
            print("\n")
        while True:
            
            value = str(input("Select the level: "))
            if value == "1":

                return Level1
            
            if value == "2":
            
                return Level2
            
            if value == "3":
            
                return Level3
            
            if value == "4":
            
                return Level4
            
    def get_selected_level(self):
        return self.selected_level