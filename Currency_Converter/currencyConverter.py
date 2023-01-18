def usd_to_gbp():
    print("This will convert USD to GBP")
    print()

    dollars = eval(input("enter the amount of USD to convert: "))

    pounds = convert_to_gbp(dollars)

    print(dollars, " to GBP is: £", pounds)


def convert_to_gbp(dollars): return dollars*0.82


def gbp_to_usd():
    print("this will convert GBP to USD")
    print()

    pounds = eval(input("enter the amount of GBP to convert: "))

    dollars = convert_to_usd(pounds)

    print(pounds, " to USD is: $", dollars)


def convert_to_usd(pounds): return pounds*1.23


def options():
    option = input("what whould you like to do? :")

    print("1. Convert USD To GBP")
    print("2. convert GBP to USD")
    print("X. Exit")

    if option == "1":
        usd_to_gbp()
    elif option == "2":
        gbp_to_usd()
    elif option.lower() == "x".lower():
        print("Exiting Programme")
        quit(0)
    else:
        print("invalid option")
        options()


options()
