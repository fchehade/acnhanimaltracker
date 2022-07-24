class Animal:
    """Base class of every animal in Animal Crossing New Horizons. It tries to
    model relevant data based on the API https://acnhapi.com/v1/{endpoint}.
    For this purpose it currently models those attributes specified in the
    __init__ method.

    Requires
        api_response [dict]: A single json-response from the api-endpoint
        (e.g.: https://acnhapi.com/v1/fish/1)
        root_directory [str]: The root directory path to
        sort saving and loading."""

    def __init__(self, api_response: dict, root_directory: str) -> None:
        self.api_response = api_response
        self.root_directory = root_directory
        self.name = self.__get_name()
        self.id = self.__get_id()
        self.save_name = self.name + str(self.id)
        self.time = self.__get_time()
        self.months = self.__get_months()
        self.price = self.__get_price()
        self.caught = False
        self.image_url = self.__get_image_url()

    def __str__(self):
        return f"""
        Name: {self.name}
        ID: {self.id}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}
        Caught: {self.caught}"""

    def __get_name(self):
        return self.api_response["name"]["name-USen"]

    def __get_id(self):
        return self.api_response["id"]

    def __get_time(self):
        return self.api_response["availability"]["time-array"]

    def __get_months(self):
        return self.api_response["availability"]["month-array-northern"]

    def __get_price(self):
        return self.api_response["price"]

    def __get_image_url(self):
        return self.api_response["image_uri"]

    def switch_caught_status(self):
        self.caught = not self.caught

    def set_caught_status(self, boolean: bool):
        self.caught = boolean


class Fish(Animal):
    """Specified class to model the characteristics of a Fish in
    Animal Crossing New Horizons.

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.rarity = self.__get_rarity()
        self.shadow = self.__get_shadow()
        self.surcharge = self.__get_surcharge()
        self.location = self.__get_location()
        self.image_path = self.__get_image_path()

    def __str__(self):
        return f"""
        Name: {self.name}
        Rarity: {self.rarity}
        Shadow: {self.shadow}
        Location: {self.location}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}
        Surcharge: {self.surcharge}"""

    def __get_shadow(self):
        return self.api_response["shadow"]

    def __get_surcharge(self):
        return self.api_response["price-cj"]

    def __get_rarity(self):
        return self.api_response["availability"]["rarity"]

    def __get_location(self):
        return self.api_response["availability"]["location"]

    def __get_image_path(self):
        return f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{self.save_name}.png"


class Bug(Animal):
    """Specified class to model the characteristics of a Bug in
    Animal Crossing New Horizons.

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.surcharge = self.__get_surcharge()
        self.rarity = self.__get_rarity()
        self.location = self.__get_location()
        self.image_path = self.__get_image_path()

    def __str__(self):
        return f"""
        Name: {self.name}
        Rarity: {self.rarity}
        Location: {self.location}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}
        Surcharge: {self.surcharge}"""

    def __get_surcharge(self):
        return self.api_response["price-flick"]

    def __get_rarity(self):
        return self.api_response["availability"]["rarity"]

    def __get_location(self):
        return self.api_response["availability"]["location"]

    def __get_image_path(self):
        return f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{self.save_name}.png"


class SeaCreature(Animal):
    """Specified class to model the characteristics of a Sea Creatures in
    Animal Crossing New Horizons

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.speed = self.__get_speed()
        self.shadow = self.__get_shadow()
        self.image_path = self.__get_image_path()

    def __str__(self):
        return f"""
        Name: {self.name}
        Speed: {self.speed}
        Shadow: {self.shadow}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}"""

    def __get_shadow(self):
        return self.api_response["shadow"]

    def __get_speed(self):
        return self.api_response["speed"]

    def __get_image_path(self):
        return f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{self.save_name}.png"
