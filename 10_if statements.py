#   if it's hot
#       It's a hot day
#       Drink plenty of water
#   otherwise if it's cold
#       It's a cold day
#       Wear warm clothes
#   otherwise
#       It's a lovely day

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Ware warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")


#Practice:
#   Price of a house is $ 1M
#   If buyer has good credit
#   They need to put down 10%
#   Otherwise
#   They need to put down 20%
#   Print the down payment

good_credit = True
Price = 1_000_000

if good_credit:
    down_Payment = Price * 0.1
else:
    down_Payment = Price * 0.2
print(f'down_Payment: {down_Payment}')