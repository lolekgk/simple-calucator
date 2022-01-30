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
    while True:
        str_num = input('Please provide a number! ')
        if is_number(str_num):
            return convert_number(str_num)
# w przypadku podania force_valid_input = False wykona się ta instrukcja - elif = True
        elif not force_valid_input: 
            return None
        print("This didn't look like a number, try again.")
        
    
def ask_for_an_operator(force_valid_input):
    while True:
        input_operator = input('Please provide an operator (one of +, -, *, /)! ')
        if is_valid_operator(input_operator):
            return input_operator
        elif not force_valid_input: 
            return None
        print("Unknown operator.")
    

def calc(operator, a, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero")
            return None
        


def simple_calculator():
    while True:
        a = ask_for_a_number(0)
#jezeli a = False - zwrocone zostanie None z funkcji a_f_n, nastapi przerwanie programu - None = False
        if not a: 
            break
        op = ask_for_an_operator(1)
        b = ask_for_a_number(1)
        result = calc(op, a, b)
        if result:
            print(f"The result is {result}")
        

if __name__ == '__main__':
    simple_calculator()


