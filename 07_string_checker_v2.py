#check that user enter a valid response
#cash / credit based on a list of options
def string_check(question, num_letters, valid_responses):

    error = "please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        responses = input(question).lower()

        for item in valid_responses:
            if responses == item[:short_version] or responses == item:
                return item

        print(error)

#main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_check("Do you want to read the "
                                     "instructions (y/n):",
                                     1, yes_no_list)
    print("You chose",want_instructions)

for case in range(0, 5):
    pay_method = string_check("...",
                              2, payment_list)
    print("You chose", pay_method)