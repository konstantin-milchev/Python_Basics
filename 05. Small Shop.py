product = input()
city = input()
quantity = float(input())
price = 0
if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15