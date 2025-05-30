
# 10 means mines
# 11, 22, 33... means unseen numbered tiles
# 99 means empty unseen tiles.

# need to also tell manually how many mines to flag and how many tiles to clear for now

from tkinter import Tk, ttk, StringVar
Level1 = [[10, 22, 99, 99, 99, 99, 99, 99],
          [10, 33, 99, 11, 11, 11, 99, 99],
          [10, 22, 99, 11, 10, 22, 11, 11],
          [22, 22, 11, 11, 11, 22, 10, 11],
          [11, 10, 11, 11, 11, 22, 11, 11],
          [11, 11, 11, 11, 10, 22, 11, 11],
          [11, 22, 11, 33, 22, 33, 10, 11],
          [10, 22, 10, 22, 10, 22, 11, 11]]

level1mines = 11
level1tiles = 53


Level2 = [[10, 22, 10, 11, 11, 22, 10],
          [22, 33, 11, 11, 11, 10, 22],
          [10, 22, 11, 11, 22, 11, 11],
          [10, 22, 11, 10, 11, 99, 99]]

level2mines = 7
level2tiles = 21

Level3 = [[10, 10, 10, 22, 99, 11, 10, 10, 22, 10, 22, 10],
          [10, 66, 10, 22, 99, 22, 33, 33, 22, 11, 22, 11],
          [10, 44, 22, 22, 99, 11, 10, 11, 99, 99, 99, 99],
          [11, 22, 10, 11, 99, 11, 11, 11, 99, 99, 99, 99]]


level3mines = 12
level3tiles = 36


selected_level_value_global = 0


def ui_start():

    """Käynnistää käyttöliittymän.

        Funktio luo käyttöliittymä olion ja aloittaa sen silmukan.
        """
    
    window = Tk()
    window.title("Level select")

    ui = UI(window)
    ui.start()

    window.mainloop()


class UI:

    """Käyttöliittymä olio.


        """

    def __init__(self, root):
        self._root = root
        self._entry = None
        self._label_var = StringVar()
        self._label_var.set("0")
        root.geometry("400x200")

        self.button1 = None
        self.button2 = None
        self.button3 = None

    def start(self):
        self._entry = ttk.Entry(master=self._root)

        self.button1 = ttk.Button(
            master=self._root,
            text="Level 1",
            command=self._choose1
        )

        self.button2 = ttk.Button(
            master=self._root,
            text="Level 2",
            command=self._choose2
        )

        self.button3 = ttk.Button(
            master=self._root,
            text="Level 3",
            command=self._choose3
        )

        heading_label = ttk.Label(
            master=self._root, text="Select a level by pressing one of the buttons")

        heading_label.grid(row=0, column=0, columnspan=2,
                           padx=10, pady=10, sticky="ew")

        self.button1.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.button2.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.button3.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def _choose3(self):
        global selected_level_value_global
        value = self._label_var.get()
        increased_value = str(3)
        selected_level_value_global = 3

        self._label_var.set(increased_value)
        print(self._label_var.get())
        self._root.destroy()

    def _choose2(self):
        global selected_level_value_global
        value = self._label_var.get()
        increased_value = str(2)
        selected_level_value_global = 2

        self._label_var.set(increased_value)
        print(self._label_var.get())
        self._root.destroy()

    def _choose1(self):
        global selected_level_value_global
        value = self._label_var.get()
        increased_value = str(1)
        selected_level_value_global = 1

        self._label_var.set(increased_value)
        print(self._label_var.get())
        self._root.destroy()

# moved the ui start to a function
# print(selected_level_value_global)


Levellist = {"Level 1": Level1, "Level 2": Level2, "Level 3": Level3}


class SelectorForLevels:

    """Luokka, joka valitsee tason viemällä käyttäjän käyttöliittymälle.


        """

    def __init__(self):

        """Luokan konstruktori, joka käynnistaa tason.

        Args:
            levelinfo: aloittaa kayttoliittyman
            selected_level, level_mines, level_tiles: tarvittuja tietoja valitusta tasosta.
        """

        self.levelinfo = self.select()
        self.selected_level = self.levelinfo[0]
        self.level_mines = self.levelinfo[1]
        self.level_tiles = self.levelinfo[2]

    def select(self):

        """Ottaa valitun tason.
        """

        while True:

            # value = selected_level_value_global #str(input("Select the level: "))
            if str(selected_level_value_global) == "1":

                return (Level1, level1mines, level1tiles)

            if str(selected_level_value_global) == "2":

                return (Level2, level2mines, level2tiles)

            if str(selected_level_value_global) == "3":

                return (Level3, level3mines, level3tiles)

    def get_selected_level(self):

        """Funktio pelkästään palauttaa tason

        Returns:
            Matriisin tasosta
        """

        return self.selected_level
