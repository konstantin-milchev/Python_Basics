degrees = int(input())
time_of_day = input()
outfit = ""
shoes = ""
if time_of_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")