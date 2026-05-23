from singleton import AucklandAquarium
from factory import FishFactory

def main():
    aquarium = AucklandAquarium()

    while True:
        print("\n1. Add Fish\n2. Remove Fish\n3. Display Stock\n4. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter fish name [Goldfish, Shark, Angelfish, Tuna, Salmon]: ").strip()
            try:
                qty = int(input("Enter quantity: "))
                fish = FishFactory.create_fish(name)
                aquarium.add_fish(fish.get_category(), qty)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            cat = input("Enter category to remove [Freshwater/Marine]: ").strip()
            qty = int(input("Enter quantity: "))
            aquarium.remove_fish(cat, qty)

        elif choice == "3":
            aquarium.display_stock()

        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()