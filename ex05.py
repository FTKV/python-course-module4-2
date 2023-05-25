car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.setdefault("color", "white")

print(x)

car["color"] = "Black"

print(car)

x = car["color"] = "Black"

print(x)