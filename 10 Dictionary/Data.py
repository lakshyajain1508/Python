product = ['Red', 'Blue', 'Orange','Green']
price = [100, 50, 60,10]
quantity = [10, 20, 30,90]

# create a dictionary of product, price and quantity

Data = {'product': product, 'price': price, 'quantity': quantity}

# print the dictionary
print(Data)


# print the product, price and quantity of the product
for i in range(len(product)):
    print(f'{product[i]} = {price[i]} * {quantity[i]}')
    

# print total price of the product

total = 0
for i in range(len(price)):
    # total += price[i] * quantity[i]
    total += price[i]
    final_total = total * quantity[i]
print(f'Total Price = {final_total}')