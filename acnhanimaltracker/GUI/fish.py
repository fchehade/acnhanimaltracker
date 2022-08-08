import tkinter
import os
from tkinter import ttk
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 14)


class FishPage(tkinter.Canvas):
    """The FishPage lists all fish-type animals from the game.
    Every animal you can catch with a fishing rod is in this list.

    Args:
        parent (ttk.Frame):  The container frame from Application.
        controller (Applicatio): The Application itself.
    """

    def __init__(self, parent: ttk.Frame, controller):
        super().__init__(parent)
        self.controller = controller
        self.parent = parent

        img = tkinter.PhotoImage(file=os.path.join(os.path.dirname(__file__), "art/bg.png"))
        self.image = img
        self.create_image(0, 0, image=self.image, anchor="nw")
        self.create_text(641, 50, text="Fish - Wiki", anchor="center",
                         fill="black", font="Calibri 28 bold")
        self.create_text(639, 50, text="Fish - Wiki", anchor="center",
                         fill="black", font="Calibri 28 bold")
        self.create_text(640, 50, text="Fish - Wiki", anchor="center",
                         fill="white", font="Calibri 28 bold")

