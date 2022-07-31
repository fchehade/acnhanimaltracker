import os
from concurrent.futures import ThreadPoolExecutor
from acnhanimaltracker.animals import AnimalHandler
from acnhanimaltracker.GUI import Application
from acnhanimaltracker.helper import is_folder_structure_intact

if __name__ == "__main__":
    root_directory = os.path.dirname(__file__)
    if not is_folder_structure_intact(root_directory):
        animal_handler = AnimalHandler(root_directory)
        animal_handler.reset_animals(True, True, True)
        animal_list = animal_handler.load_animals()
        for animal_type in animal_list:
            with ThreadPoolExecutor(max_workers=50) as executor:
                executor.map(animal_handler.download_animal_images, animal_type)
    else:
        animal_handler = AnimalHandler(root_directory)
        # animal_handler.reset_animals(True, True, True)
        animal_list = animal_handler.load_animals()
        # animal_handler.download_images(animal_list)

    app = Application(animal_list, root_directory)
    app.mainloop()
    animal_handler.save_animals(animal_list)
