'''
Problem 2: Simple Shopping Cart
Write a Python program that:
1. Takes the customer's name as input.
2. Takes the names and prices of 3 products as input.
3. Calculates:
o Subtotal
o Discount
o Final Total
4. Determines the discount using:
o 5000 or above → 20% discount
o 3000–4999 → 10% discount
'''

all_cart = []


def add_cart():
    c_name = input("Enter Customer Name: ")

    product1 = input("Enter Product 1 Name: ")
    price1 = int(input("Enter Product 1 Price: "))

    product2 = input("Enter Product 2 Name: ")
    price2 = int(input("Enter Product 2 Price: "))

    product3 = input("Enter Product 3 Name: ")
    price3 = int(input("Enter Product 3 Price: "))

    subtotal = price1 + price2 + price3
    discount = calculate_discount(subtotal)
    final_total = subtotal - discount

    cart_data = {
        "c_name": c_name,
        "product1": product1,
        "price1": price1,
        "product2": product2,
        "price2": price2,
        "product3": product3,
        "price3": price3,
        "subtotal": subtotal,
        "discount": discount,
        "final_total": final_total
    }

    all_cart.append(cart_data)
    print('Cart Added Successfully!')


def view_cart():
    for cart in all_cart:
        print(f"Customer Name: {cart['c_name']}")
        print(f"Product 1: {cart['product1']} - Price: {cart['price1']}")
        print(f"Product 2: {cart['product2']} - Price: {cart['price2']}")
        print(f"Product 3: {cart['product3']} - Price: {cart['price3']}")
        print(f"Subtotal: {cart['subtotal']}")
        print(f"Discount: {cart['discount']}")
        print(f"Final Total: {cart['final_total']}")   


def calculate_discount(subtotal):
    if subtotal >= 5000:
        return subtotal * 0.2
    elif 3000 <= subtotal < 5000:
        return subtotal * 0.1
    else:
        return 0


while True:
    print("Shopping Cart System")
    print("""
    1. Add Cart
    2. View Carts
    3. Exit
    """)
    select = int(input("Enter Your Choice: "))

    if select == 1:
        add_cart()
    elif select == 2:
        view_cart()
    elif select == 3:
        print("Done!")
        break
    else:
        print("Enter Valid Input (1 to 3)")