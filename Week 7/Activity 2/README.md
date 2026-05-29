# Auckland Aquarium Management System

A Python console application to manage fish stock in a limited-area aquarium in Auckland.
Built using **Singleton** and **Factory** design patterns for clean, maintainable OOP design.

## Features
- Track fish stock by category: **Freshwater** and **Marine**
- Supports 5 fish types: Goldfish, Angelfish, Shark, Tuna, Salmon
- Enforces max capacity due to limited aquarium area
- Add/remove fish and view current stock counts
- Prevents duplicate aquarium instances using Singleton

## Design Patterns Used

### 1. Singleton Pattern
Ensures only one `AucklandAquarium` instance exists globally.
File: `aquarium.py`
This prevents conflicting stock data if the system is accessed from multiple places.

### 2. Factory Pattern
Creates the correct fish object based on user input without exposing instantiation logic.
File: `fish_factory.py`
Makes it easy to add new fish types later.

## How to Run
Run python main.py

Use the main menu
- Add fish
- Remove fish
- Display stock 
- Exit
```bash
git clone https://github.com/your-username/auckland-aquarium.git
cd auckland-aquarium
