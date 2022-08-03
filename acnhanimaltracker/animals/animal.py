import os


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
        self.name = self._get_name()
        self.id = self._get_id()
        self.save_name = self.name + str(self.id)
        self.time = self._get_time()
        self.months = self._get_months()
        self.price = self._get_price()
        self.caught = False
        self.image_url = self._get_image_url()

    def __str__(self):
        return f"""
        Name: {self.name}
        ID: {self.id}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}
        Caught: {self.caught}"""

    def _get_name(self):
        if "name-USen" not in self.api_response["name"]:
            raise KeyError("Key 'name-USen' not found")
        return self.api_response["name"]["name-USen"]

    def _get_id(self):
        if "id" not in self.api_response:
            raise KeyError("Key 'id' not found")
        return self.api_response["id"]

    def _get_time(self):
        if "time-array" not in self.api_response["availability"]:
            raise KeyError("Key 'time-array' not found")
        return self.api_response["availability"]["time-array"]

    def _get_months(self):
        if "month-array-northern" not in self.api_response["availability"]:
            raise KeyError("Key 'month-array-northern' not found")
        return self.api_response["availability"]["month-array-northern"]

    def _get_price(self):
        if "price" not in self.api_response:
            raise KeyError("Key 'price' not found")
        return self.api_response["price"]

    def _get_image_url(self):
        if "image_uri" not in self.api_response:
            raise KeyError("Key 'image_uri' not found")
        return self.api_response["image_uri"]

    def switch_caught_status(self):
        self.caught = not self.caught

    def set_caught_status(self, boolean: bool):
        if not isinstance(boolean, bool):
            raise ValueError(f"{boolean} is not of type bool - type of {type(boolean)}")
        self.caught = boolean


class Fish(Animal):
    """Specified class to model the characteristics of a Fish in
    Animal Crossing New Horizons.

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.rarity = self._get_rarity()
        self.shadow = self._get_shadow()
        self.surcharge = self._get_surcharge()
        self.location = self._get_location()
        self.image_path = self._get_image_path()

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

    def _get_shadow(self):
        if "shadow" not in self.api_response:
            raise KeyError("Key 'shadow' not found")
        return self.api_response["shadow"]

    def _get_surcharge(self):
        if "price-cj" not in self.api_response:
            raise KeyError("Key 'price-cj' not found")
        return self.api_response["price-cj"]

    def _get_rarity(self):
        if "rarity" not in self.api_response["availability"]:
            raise KeyError("Key 'rarity' not found")
        return self.api_response["availability"]["rarity"]

    def _get_location(self):
        if "location" not in self.api_response["availability"]:
            raise KeyError("Key 'location' not found")
        return self.api_response["availability"]["location"]

    def _get_image_path(self):
        file = f"{self.root_directory}/acnhanimaltracker/animals/images/fish/{self.save_name}.png"
        if not os.path.exists(file):
            raise FileNotFoundError(f"{file} wasn't found at specified path.")
        return file


class Bug(Animal):
    """Specified class to model the characteristics of a Bug in
    Animal Crossing New Horizons.

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.surcharge = self._get_surcharge()
        self.rarity = self._get_rarity()
        self.location = self._get_location()
        self.image_path = self._get_image_path()

    def __str__(self):
        return f"""
        Name: {self.name}
        Rarity: {self.rarity}
        Location: {self.location}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}
        Surcharge: {self.surcharge}"""

    def _get_surcharge(self):
        if "price-flick" not in self.api_response["price-flick"]:
            raise KeyError("Key 'price-flick' not found")
        return self.api_response["price-flick"]

    def _get_rarity(self):
        if "rarity" not in self.api_response["availability"]:
            raise KeyError("Key 'rarity' not found")
        return self.api_response["availability"]["rarity"]

    def _get_location(self):
        if "location" not in self.api_response["availability"]:
            raise KeyError("Key 'location' not found")
        return self.api_response["availability"]["location"]

    def _get_image_path(self):
        file = f"{self.root_directory}/acnhanimaltracker/animals/images/bugs/{self.save_name}.png"
        if not os.path.exists(file):
            raise FileNotFoundError(f"{file} wasn't found at specified path.")
        return file


class SeaCreature(Animal):
    """Specified class to model the characteristics of a Sea Creatures in
    Animal Crossing New Horizons

    Args:
        Animal (BaseClass): See Animal Base Class for more information
    """

    def __init__(self, api_response: dict, root_directory: str) -> None:
        super().__init__(api_response, root_directory)
        self.speed = self._get_speed()
        self.shadow = self._get_shadow()
        self.image_path = self._get_image_path()

    def __str__(self):
        return f"""
        Name: {self.name}
        Speed: {self.speed}
        Shadow: {self.shadow}
        Time: {self.time}
        Months: {self.months}
        Price: {self.price}"""

    def _get_shadow(self):
        if "shadow" not in self.api_response:
            raise KeyError("Key 'shadow' not found")
        return self.api_response["shadow"]

    def _get_speed(self):
        if "speed" not in self.api_response:
            raise KeyError("Key 'speed' not found")
        return self.api_response["speed"]

    def _get_image_path(self):
        file = f"{self.root_directory}/acnhanimaltracker/animals/images/sea_creatures/{self.save_name}.png"
        if not os.path.exists(file):
            raise FileNotFoundError(f"{file} wasn't found at specified path.")
        return file
