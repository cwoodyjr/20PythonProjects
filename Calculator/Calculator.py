def add(a,b):
    answer = a + b
    print(str(a)+"+"+str(b)+"="+str(answer))

def sub(a,b):
    answer = a - b
    print(str(a)+"-"+str(b)+"="+str(answer))

def mult(a,b):
    answer = a * b
    print(str(a)+"*"+str(b)+"="+str(answer))

def div(a,b):
    answer = a / b
    print(str(a)+"/"+str(b)+"="+str(answer))
while True:
    def options():
        print('what would you like to do? ')
        print('1 - add')
        print('2 - subtract')
        print('3 - divide')
        print('4 - multiply')
        print('0 - exit')

    options()

    choice = int(input('choose an option: '))
    if choice == 0:
        print('Exiting Programme')
        quit()
    elif choice == 1:
        a = int(input('enter a number'))
        b = int(input('enter a number'))
        add(a,b)
    elif choice == 2:
        a = int(input('enter a number'))
        b = int(input('enter a number'))
        sub(a,b)
    elif choice == 3:
        a = int(input('enter a number'))
        b = int(input('enter a number'))
        div(a,b)
    elif choice == 4:
        a = int(input('enter a number'))
        b = int(input('enter a number'))
        mult(a,b)
    else:
        print('Invalid Option')






