annual_fee = int(input())
if annual_fee < 0 or annual_fee > 9999:
    print(1)
    exit()
shoes_price = 0.6 * annual_fee
uniform_price = 0.8 * shoes_price
ball_price = 0.25 * uniform_price
accessories_price = 0.2 * ball_price
total_expenses = annual_fee + shoes_price + uniform_price + ball_price + accessories_price
print(total_expenses)
