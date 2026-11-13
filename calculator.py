
buy_price = float(input("購入価格（USD）: "))
current_price = float(input("現在価格（USD）: "))
shares = float(input("保有株数: "))

profit = (current_price - buy_price) * shares
return_rate = (current_price - buy_price) / buy_price * 100

print(f"評価損益: {profit:.2f} USD")
print(f"損益率: {return_rate:.2f}%")
