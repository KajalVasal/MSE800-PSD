class AucklandAquarium:
    _instance = None
    MAX_CAPACITY = 150 # Limited area constraint

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AucklandAquarium, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.stock = {} # {category: count}
        self._initialized = True
        print(f"[Singleton] Auckland Aquarium created. Max capacity: {self.MAX_CAPACITY} fish")

    def add_fish(self, category, count):
        current_total = sum(self.stock.values())
        if current_total + count > self.MAX_CAPACITY:
            print(f"Cannot add {count} fish. Only {self.MAX_CAPACITY - current_total} spots left.")
            return False

        self.stock[category] = self.stock.get(category, 0) + count
        print(f"Added {count} {category} fish.")
        return True

    def remove_fish(self, category, count):
        if category not in self.stock or self.stock[category] < count:
            print(f"Not enough {category} fish to remove.")
            return False

        self.stock[category] -= count
        if self.stock[category] == 0:
            del self.stock[category]
        print(f"Removed {count} {category} fish.")
        return True

    def display_stock(self):
        print("\n--- Auckland Aquarium Stock ---")
        if not self.stock:
            print("No fish in the aquarium yet.")
        else:
            for category, count in self.stock.items():
                print(f"{category}: {count} fish")
            print(f"Total: {sum(self.stock.values())}/{self.MAX_CAPACITY}")
        print("-------------------------------\n")