import pickle
import os
import requests
from PIL import Image
from .animal import Fish, Bug, SeaCreature


class AnimalHandler:
    """AnimalHandler class to model behaviour and manage the state of all
    animals in the local storage.

    Capable of:
    * sending out requests to the various endpoint from
    https://acnhapi.com/v1/{endpoints}
    * resetting (redownloading) all data from the api, effectivly 'resetting'
    your progress
    * loading all Animals from local storage into a list
    Format: list[list[Fish], [Bug], [SeaCreature]]
    * saving all Animals with the current settings to local storage
    * downloading the associated images from the Animals and saving them
    """

    base_url = "https://acnhapi.com/v1/"
    fish_api_endpoint = "fish/"
    bug_api_endpoint = "bugs/"
    sea_api_endpoint = "sea/"
    api_endpoints = [fish_api_endpoint, sea_api_endpoint, bug_api_endpoint]

    data_path = "acnhanimaltracker/animals"
    directory_fish = "acnhanimaltracker/animals/animals/fish"
    directory_bugs = "acnhanimaltracker/animals/animals/bugs"
    directory_sea_creatures = "acnhanimaltracker/animals/animals/sea_creatures"

    def __init__(self, root_directory: str) -> None:
        self.root_directory = root_directory

    def send_request(self, endpoint: str) -> dict:
        """Sends out a request to the {endpoint}
        https://acnhapi.com/v1/{endpoint} and returns dictionary of specified
        animal

            Args:
                endpoint (str): Endpoint as described in api_endpoints

            Returns:
                dict: dictionary of a speficied animal
        """
        response = requests.get(self.base_url + endpoint)
        return response.json()

    def reset_animals(
        self, fish: bool = False, bug: bool = False, sea_creature: bool = False
    ) -> None:
        """'Resets' your current progress by simply redownloading all animals from
        the API. Mostly useful for testing at the moment.

        Args:
            fish (bool, optional): If Fish-Progress should be reset.
            Defaults to False.

            bug (bool, optional): If Bug-Progress should be reset.
            Defaults to False.

            sea_creature (bool, optional): If SeaCreature-Progress
            should be reset.
            Defaults to False.
        """
        if fish:
            response = self.send_request(self.fish_api_endpoint)
            for key in response.keys():
                fish_data = Fish(response[key], self.root_directory)
                with open(
                    f"{self.root_directory}/{self.directory_fish}/{fish_data.save_name}.pkl",
                    "wb",
                ) as file_handler:
                    pickle.dump(fish_data, file_handler)

        if bug:
            response = self.send_request(self.bug_api_endpoint)
            for key in response.keys():
                bug_data = Bug(response[key], self.root_directory)
                with open(
                    f"{self.root_directory}/{self.directory_bugs}/{bug_data.save_name}.pkl",
                    "wb",
                ) as file_handler:
                    pickle.dump(bug_data, file_handler)

        if sea_creature:
            response = self.send_request(self.sea_api_endpoint)
            for key in response.keys():
                sea_creature_data = SeaCreature(response[key], self.root_directory)
                with open(
                    f"{self.root_directory}/{self.directory_sea_creatures}/{sea_creature_data.save_name}.pkl",
                    "wb",
                ) as file_handler:
                    pickle.dump(sea_creature_data, file_handler)

    def load_animals(self) -> list[list[Fish | Bug | SeaCreature]]:
        """Loads all animals from local storage into a list

        Returns:
            list[list[Fish | Bug | SeaCreature]]: Loads all Animals into a list
        """
        animal_list = []

        for directory in [
            self.directory_fish,
            self.directory_bugs,
            self.directory_sea_creatures,
        ]:
            temp_list = []
            for file in os.listdir(f"{self.root_directory}/{directory}"):
                with open(
                    f"{self.root_directory}/{directory}/{file}", "rb"
                ) as file_handler:
                    animal_data = pickle.load(file_handler)
                    temp_list.append(animal_data)
            temp_list.sort(key=lambda animal: animal.id)
            animal_list.append(temp_list)
        return animal_list

    def save_animals(self, animal_list: list[list[Fish | Bug | SeaCreature]]) -> None:
        """Saves current progress and changes to Animals

        Args:
            animal_list (list[list[Fish  |  Bug  |  SeaCreature]]):
            The list you get from self.load_animals
        """
        for animal_type in animal_list:
            for animal in animal_type:
                if isinstance(animal, Fish):
                    with open(
                        f"{self.root_directory}/{self.directory_fish}/{animal.save_name}.pkl",
                        "wb",
                    ) as file_handler:
                        pickle.dump(animal, file_handler)
                if isinstance(animal, Bug):
                    with open(
                        f"{self.root_directory}/{self.directory_bugs}/{animal.save_name}.pkl",
                        "wb",
                    ) as file_handler:
                        pickle.dump(animal, file_handler)
                if isinstance(animal, SeaCreature):
                    with open(
                        f"{self.root_directory}/{self.directory_sea_creatures}/{animal.save_name}.pkl",
                        "wb",
                    ) as file_handler:
                        pickle.dump(animal, file_handler)

    def download_images(
        self, animal_list: list[list[Fish | Bug | SeaCreature]]
    ) -> None:
        """Download and save all images the animals from the animal_list.

        Args:
            animal_list (list[list[Fish  |  Bug  |  SeaCreature]]):
            The list you get from self.load_animals
        """
        for animal_type in animal_list:
            for animal in animal_type:
                response = requests.get(animal.image_url)
                if isinstance(animal, Fish):
                    with open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png",
                        "wb",
                    ) as file_handler:
                        file_handler.write(response.content)
                    image = Image.open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png"
                    )
                    image = self.resize_image(image)
                    image.save(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png"
                    )

                if isinstance(animal, Bug):
                    with open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png",
                        "wb",
                    ) as file_handler:
                        file_handler.write(response.content)
                    image = Image.open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png"
                    )
                    image = self.resize_image(image)
                    image.save(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png"
                    )
                if isinstance(animal, SeaCreature):
                    with open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png",
                        "wb",
                    ) as file_handler:
                        file_handler.write(response.content)
                    image = Image.open(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png"
                    )
                    image = self.resize_image(image)
                    image.save(
                        f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png"
                    )

    def download_animal_images(self, animal: Fish | Bug | SeaCreature):
        """Download and save all images the animals from the animal_list.

        Args:
            animal (Fish  |  Bug  |  SeaCreature):
        """
        response = requests.get(animal.image_url)
        if isinstance(animal, Fish):
            with open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png",
                "wb",
            ) as file_handler:
                file_handler.write(response.content)
            image = Image.open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png"
            )
            image = self.resize_image(image)
            image.save(
                f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{animal.save_name}.png"
            )

        if isinstance(animal, Bug):
            with open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png",
                "wb",
            ) as file_handler:
                file_handler.write(response.content)
            image = Image.open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png"
            )
            image = self.resize_image(image)
            image.save(
                f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{animal.save_name}.png"
            )
        if isinstance(animal, SeaCreature):
            with open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png",
                "wb",
            ) as file_handler:
                file_handler.write(response.content)
            image = Image.open(
                f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png"
            )
            image = self.resize_image(image)
            image.save(
                f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{animal.save_name}.png"
            )

    def resize_image(self, image: Image.Image):
        """Resizes an image to a specified width respecting the aspect ratio.

        Args:
            image (Image.Image): Original sized image to be resized by basewidth.

        Returns:
            Image.Image: Return a resized version of an image given
        """
        basewidth = 250
        wpercent = basewidth / float(image.size[0])
        hsize = int((float(image.size[1] * float(wpercent))))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)
        return image
