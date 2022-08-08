import tkinter
from tkinter import ttk
from .start_page import StartPage
from .bugs import BugPage
from .fish import FishPage
from .sea_creatures import SeaCreaturePage

LARGE_FONT = ("Verdana", 12)


class Application(tkinter.Tk):
    """The root application hosting all subsequent frames and widgets.

    Args:
        animal_list (list): The list created by AnimalHandler.load_animals()
        root_directory (str): The root directory created in main.py
    """

    def __init__(self, animal_list, root_directory) -> None:
        super().__init__()
        # Initialize Base Configuration
        self.title("Animal Crossing New Horizons - Animal Tracker")
        self.geometry("1280x720")
        self.resizable(False, False)

        # Load in animals
        self.animal_list = animal_list

        self.root_directory = root_directory
        # Initialize Base Container
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.start_page = StartPage(container, self)
        self.start_page.pack(expand=True, fill="both")
        #self.fish_page = FishPage(container, self)
        #self.fish_page.grid(row=0, column=0, sticky="nsew")
        #self.bug_page = BugPage(container, self)
        #self.bug_page.grid(row=0, column=0, sticky="nsew")
        #self.sea_creature_page = SeaCreaturePage(container, self)
        #self.sea_creature_page.grid(row=0, column=0, sticky="nsew")

        # Load up StartPage
        #self.show_frame(self.start_page)

        #self.bind(
        #    "<BackSpace->",
       #     lambda event: self.show_frame(self.start_page, _=event),
        #)

    #def show_frame(self, frame, _=None):
    #    frame.tkraise()
