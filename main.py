ADRESS_BOOK = {}


def decorator_input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IndexError:
            return f'Give me name and phone please!'
        except KeyError:
            return f'User not found!'
        
    return inner

@decorator_input_error
def add_handler(data: list):
    # ADRESS_BOOK[data[0]]= data[1]
    ADRESS_BOOK.update({data[0].title():data[1]})
    return f'new user "{data[0].title()}" with phone "{data[1]}" added'

@decorator_input_error
def exit_handler(data: list):
    return f'Good bye!'

@decorator_input_error
def change_handler(data: list):
    ADRESS_BOOK.update({data[0].title():data[1]})
    return f'user "{data[0].title()}" changed phone to "{data[1]}"'

@decorator_input_error
def phone_handler(data: list):
    phone =ADRESS_BOOK[data[0]]
    return f' phone "{data[0]}": {phone}'

@decorator_input_error
def show_all_handler(data: list):
    info = ''
    for name, phone in ADRESS_BOOK.items():
        info += f'|user: {name}, phone:{phone}|\n'
    return info


COMANDS = {
    add_handler : ['add', 'create', 'додай' ],
    exit_handler: ["good bye", "close", "exit"],
    change_handler: ['change', 'update', ],
    phone_handler: ["phone"],
    show_all_handler: ['show all']
}

@decorator_input_error
def comand_parser(user_input: str):
    data = user_input.split(' ')
    res = None
    for funk, values in COMANDS.items():
       for val in values:
            if val.startswith(data[0]):
                res = funk(data[1:])
    return res
           


def main():
    while True:
        user_input = input('Ведіть команду: ')
        result = comand_parser(user_input.lower())
        if result:
            print(result)
        else:
            print('Comand not found!')
        if result == 'Good bye!':
            break

if __name__ == '__main__':

    main()