def is_number(str): 
    try:
        float(str)
        return True
    except ValueError:
        return False

def convert_number(str): 
    float_number = float(str) 
    return float_number


def is_valid_operator(operator):
    operators_list = ['+', '-', '*', '/']
    if operator in operators_list:
        return True
    else:
        return False

def ask_for_a_number(force_valid_input):
    # gdy is nnumber nie jest true petla sie powtarza do momentu podania prawidłowego stringa
    while True:
        str_num = input('Please provide a number! ')
        is_number(str_num)
        if is_number(str_num):
            return convert_number(str_num)
        elif not force_valid_input: # w przypadku podania force_valid_input = False wykona się ta instrukcja - elif = True
            return None
        print("This didn't look like a number, try again.")
        
    
      
def ask_for_an_operator(force_valid_input):
    while force_valid_input == True:
        input_operator = input('Please provide an operator (one of +, -, *, /)! ')
        is_valid_operator(input_operator)
        if is_valid_operator(input_operator):
            return input_operator
        elif not force_valid_input: 
            return None
        print("Unknown operator.")
    
def calc(operator, a, b):
    pass


def simple_calculator():
    while True:
        a = ask_for_a_number(0)
        if not a: #jezeli a bedzie False - zwrocone zostanie None z funkcji a_f_n, nastapi przerwanie programu
            break
        op = ask_for_an_operator(1)
        b = ask_for_a_number(1)
        result = calc(op, a, b)
        if result:
            print(f"The result is {result}")
        


if __name__ == '__main__':
    simple_calculator()


