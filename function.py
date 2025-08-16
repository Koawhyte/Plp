price = float(input("Enter the price of your Item"))
discount_percent = float(input("Enter the discount given on your Item "))

def calculate_discount(price, discount_percent):
  if discount_percent >=20:
    discount =price * (discount_percent/100)
    final_price = price - discount
    return final_price
  else:
    return price;

final_price = calculate_discount(price, discount_percent)

if final_price==price:
    print(f"Oh! No discount was applied. the price is: {price}, the final price is: {final_price}  ")

else:
     print(f"The final price after discount is: {final_price}")
  




 
  