#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.age = age

# Creating some plants to show
plants = [
    Plant("Rose", "25cm", 30),
    Plant("Sunflower", "80cm", 45),
    Plant("Cactus", "15cm", 120)
]

# Print all info of our plants
print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}, {plant.age} days old")
