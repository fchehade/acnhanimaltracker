import os
import tkinter
from .fish import FishPage
from .bugs import BugPage
from .sea_creatures import SeaCreaturePage
from tkinter import ttk


class StartPage(tkinter.Canvas):
    """Main Page of this Application. You can always return
    to this page by pressing the <Return-Key> on your keyboard.

    Args:
        parent (ttk.Frame): The Frame holding all successive frames,
        the container from Application.
        controller (Application): The Application itself.
    """

    def __init__(self, parent: ttk.Frame, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent
        img = tkinter.PhotoImage(file=os.path.join(os.path.dirname(__file__), "art/bg.png"))
        self.image = img
        self.create_image(0, 0, image=self.image, anchor="nw")
        self.create_text(641, 50, text="Animal Crossing New Horizons - Animal Tracker", anchor="center",
                         fill="black", font="Calibri 28 bold")
        self.create_text(639, 50, text="Animal Crossing New Horizons - Animal Tracker", anchor="center",
                         fill="black", font="Calibri 28 bold")
        self.create_text(640, 50, text="Animal Crossing New Horizons - Animal Tracker", anchor="center",
                         fill="white", font="Calibri 28 bold")

        button_style = ttk.Style()
        button_style.configure("StartPage.TButton", font="Calibri 20")
        self.fish_button = ttk.Button(self, text="Fish", style="StartPage.TButton", command=self.open_fish_page)
        self.bug_button = ttk.Button(self, text="Bugs", style="StartPage.TButton", command=self.open_bug_page)
        self.sea_button = ttk.Button(self, text="Sea Creatures", style="StartPage.TButton", command=self.open_sea_page)

        self.create_window(1200, 180, window=self.fish_button, anchor="ne")
        self.create_window(1200, 360, window=self.bug_button, anchor="ne")
        self.create_window(1200, 540, window=self.sea_button, anchor="ne")

    def open_fish_page(self):
        page = FishPage(self.parent, self.controller)
        page.pack(expand=True, fill="both")
        self.destroy()

    def open_bug_page(self):
        self.destroy()

    def open_sea_page(self):
        self.destroy()
