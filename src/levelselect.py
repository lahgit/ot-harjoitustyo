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



class SelectorForLevels:

    def __init__(self):

        self.selected_level = self.select()
        

    def select(self):
        print("Available levels: \n"
            "level 1 \n"
            "level 2 \n")
        while True:
            
            value = str(input("Select the level: "))
            if value == "1":

                return Level1
            
            if value == "2":
            
                return Level2
            
    def get_selected_level(self):
        return self.selected_level