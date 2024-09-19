def calculate_discount(price, discount_percent):
    if discount_percent in range(0, 20):
        print(f"You will pay ${price}")
        return price
    
    discount_amount = price*(discount_percent/100)
    payment_amount = price - discount_amount
    print(f"You saved ${discount_amount:.2f}! You will pay ${payment_amount:.2f}")
    return payment_amount

price = float(input("Please enter the purchase price: "))
discount = float(input("Please enter the discount percentage: "))

calculate_discount(price, discount)
