#calc the ticket price based on age
def calc_ticket_price(var_age):

    #ticket is 7.5 for under 16
    if var_age < 16:
        price = 7.5

    #ticket is 10.5 for user 16-64
    elif var_age < 65:
        price = 10.5

    #ticket is 6.5 for over 64
    else:
        price = 6.5

    return price

#loop for testing
while True:

    #get age
    age = int(input("Age: "))

    #calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))
