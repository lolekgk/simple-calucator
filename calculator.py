#is numeric przyjmuje tylko liczby bez - i 
def is_number(str): 
    if str.isnumeric() == True:
        return True
    else:
        return False

# wstawic powiazanie z is_number?
def convert_number(str): #num_string
    number = int(str) #num_string
    return number


def is_valid_operator(operator):
    operators_list = ['+', '-', '*', '/']
    if operator in operators_list:
        return True
    else:
        return False


def ask_for_a_number(force_valid_input):
    str_num = input('Please provide a number! ')
    is_number(str_num)
    while force_valid_input == True:
        if is_number(str_num):
            return print(convert_number(str_num))
        else:
            return print(None)


def ask_for_an_operator(force_valid_input):
    pass


def calc(operator, a, b):
    pass


def simple_calculator():
    pass


# if __name__ == '__main__':
#     simple_calculator()

ask_for_a_number(1)