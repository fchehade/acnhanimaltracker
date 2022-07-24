from tkinter import ttk
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 14)


class StartPage(ttk.Frame):
    """Main Page of this Application. You can always return
    to this page by pressing the <Return-Key> on your keyboard.

    Args:
        parent (ttk.Frame): The Frame holding all successive frames,
        the container from Application.
        controller (Application): The Application itself.
    """

    def __init__(self, parent: ttk.Frame, controller):
        super().__init__(parent)
        label = ttk.Label(
            self,
            text="Animal Crossing New Horizons - Animal Tracker - Main Menu",
            font=LARGE_FONT,
        )
        label.grid(column=0, columnspan=3, row=0, pady=20, padx=20)

        img1 = Image.open(
            f"{controller.root_directory}/acnhanimaltracker/animals/images/fish/arapaima44.png"
        )
        img1 = self.resize_image(img1)
        img1 = ImageTk.PhotoImage(img1)
        image_label1 = ttk.Label(self, image=img1)
        image_label1.image = img1  # type: ignore
        image_label1.grid(column=0, row=1)
        button1 = ttk.Button(
            self,
            text="Visit Fish Page",
            width=30,
            command=lambda: controller.show_frame(controller.fish_page),
        )
        button1.grid(column=0, row=2, pady=20, padx=20)

        img2 = Image.open(
            f"{controller.root_directory}/acnhanimaltracker/animals/images/bugs/centipede77.png"
        )
        img2 = self.resize_image(img2)
        img2 = ImageTk.PhotoImage(img2)
        image_label2 = ttk.Label(self, image=img2)
        image_label2.image = img2  # type: ignore
        image_label2.grid(column=1, row=1)
        button2 = ttk.Button(
            self,
            text="Visit Bug Page",
            width=30,
            command=lambda: controller.show_frame(controller.bug_page),
        )
        button2.grid(column=1, row=2, pady=20, padx=20)

        img3 = Image.open(
            f"{controller.root_directory}/acnhanimaltracker/animals/images/sea_creatures/vampire squid22.png"
        )
        img3 = self.resize_image(img3)
        img3 = ImageTk.PhotoImage(img3)
        image_label3 = ttk.Label(self, image=img3)
        image_label3.image = img3  # type: ignore
        image_label3.grid(column=2, row=1)
        button3 = ttk.Button(
            self,
            text="Visit Sea Creature Page",
            width=30,
            command=lambda: controller.show_frame(controller.sea_creature_page),
        )
        button3.grid(column=2, row=2, pady=20, padx=20)

    def resize_image(self, image: Image.Image) -> Image.Image:
        """Resizes an image to a specified width respecting the aspect ratio.

        Args:
            image (Image.Image): Original sized image to be resized by basewidth.

        Returns:
            Image.Image: Return a resized version of an image given
        """
        basewidth = 300
        wpercent = basewidth / float(image.size[0])
        hsize = int((float(image.size[1] * float(wpercent))))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)
        return image
