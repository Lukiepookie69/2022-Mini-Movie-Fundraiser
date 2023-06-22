#functions go here

#checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        #if the response is blank, output error
        if response == "":
            print("Sorry this cant be blank. Please Try again")
        else:
            return response

#main routine start here
while True:
    name = not_blank("Enter your name (or 'xxx' to quit)")
    if name == "xxx":
        break

print("We are done")