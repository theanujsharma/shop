import display, order

print('Welcome to the shop')

menu = {"Pizza": 100, "Burger": 200, "Cookies": 300}

#prinitng menu 
display.print_list(menu)  # calling the function

#taking order
order.take_order(menu)