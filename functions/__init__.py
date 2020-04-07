from Operations import BasicOperations
def line():
    print('-' * 50)

def title(msg):
    line()
    print(msg.center(50))
    line()

def menu():
    print('CHOOSE YOUR OPTION:\n'
          '1 - SUM\n'
          '2 - SUBTRACTION\n'
          '3 - MULTIPLY\n'
          '4 - DIVISION\n'
          '5 - EXIT')
    line()
    option()

def option():
    op = str(input('WHAT THE OPTION THAT YOU CHOOSE?: '))
    while op not in '12345':
        op = str(input('WRONG OPTION!\n'
                       'CHOOSE A NEW OPTION: '))
    if op == '1':
        v1 = int(input('Insert 1ª value: '))
        v2 = int(input('Insert 2ª value: '))
        c = BasicOperations(v1, v2)
        c.some(v1, v2)
        print(f'{v1} + {v2} = {c.some(v1, v2)}')
        continous()
    elif op == '2':
        v1 = int(input('Insert 1ª value: '))
        v2 = int(input('Insert 2ª value: '))
        c = BasicOperations(v1, v2)
        c.subtr(v1, v2)
        print(f'{v1} - {v2} = {c.subtr(v1, v2)}')
        continous()
    elif op == '3':
        v1 = int(input('Insert 1ª value: '))
        v2 = int(input('Insert 2ª value: '))
        c = BasicOperations(v1, v2)
        c.mult(v1, v2)
        print(f'{v1} * {v2} = {c.mult(v1, v2)}')
        continous()
    elif op == '4':
        v1 = int(input('Insert 1ª value: '))
        v2 = int(input('Insert 2ª value: '))
        c = BasicOperations(v1, v2)
        c.division(v1, v2)
        print(f'{v1} + {v2} = {c.division(v1, v2)}')
        continous()
    elif op == '5':
        print('See you soon!')


# noinspection PyBroadException
def continous():
    try:
        answer = str(input('Do you want to continue? [Y/N]: ')).upper().strip()[0]
    except:
        print('Wrong Option!\n'
              'Try again.')
        return continous()
    else:
        while answer not in 'YN':
            print('Wrong Option!\n'
                  'Try again.')
            return continous()
        if answer == 'Y':
            return title('MENU CALCULATOR'), menu(), option()
        else:
            while answer == 'YN':
                print('See you soon!')
                break
