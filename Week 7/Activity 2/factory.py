from abc import ABC, abstractmethod

class Fish(ABC):
    @abstractmethod
    def get_category(self):
        pass

class Goldfish(Fish):
    def get_category(self): return "Freshwater"

class Angelfish(Fish):
    def get_category(self): return "Freshwater"

class Shark(Fish):
    def get_category(self): return "Marine"

class Tuna(Fish):
    def get_category(self): return "Marine"

class Salmon(Fish):
    def get_category(self): return "Marine"

class FishFactory:
    _fish_map = {
        "goldfish": Goldfish,
        "angelfish": Angelfish,
        "shark": Shark,
        "tuna": Tuna,
        "salmon": Salmon
    }

    @staticmethod
    def create_fish(fish_name):
        fish_class = FishFactory._fish_map.get(fish_name.lower())
        if not fish_class:
            raise ValueError(f"Fish '{fish_name}' not supported. Available: {list(FishFactory._fish_map.keys())}")
        return fish_class()