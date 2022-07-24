import os
from acnhanimaltracker.animals import AnimalHandler
from acnhanimaltracker.GUI import Application

# On your first run make sure to also include line # and line # to download the data and images from the API-Endpoint and save it.
# In the GUI you can go back to the Start Page when hitting the backspace key on your keyboard
# You can click animals to select them as "caught"(green) or "uncaught"(red).
# Saving of your progress is done when closing the app.

if __name__ == "__main__":
    root_directory = os.path.dirname(__file__)
    animal_handler = AnimalHandler(root_directory)
    # animal_handler.reset_animals(True, True, True)
    animal_list = animal_handler.load_animals()
    # animal_handler.download_images(animal_list)
    app = Application(animal_list, root_directory)
    app.mainloop()
    animal_handler.save_animals(animal_list)
