
import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def myAdd(value_one, value_two):
    result = operator_dict['+'](value_one, value_two)
    return result 

def mySub(value_one, value_two):
    result = operator_dict['-'](value_one, value_two)
    return result

def myMul(value_one, value_two):
    result = operator_dict['*'](value_one, value_two)
    return result

def myDiv(value_one, value_two):
    result = operator_dict['/'](value_one, value_two)
    return result

def validate_integer(value, str):
    while value != int(value):
        print("Error: incorrect integer input")
        value = input(('Please enter the {} integer: ').format(str))
    return 1

def validate_operator(operator, str):
    while operator not in operator_dict.keys():
        print("Error: incorrect operator input")
        operator = input(('Please enter the {} operator: ').format(str))
    return 1

def evaluate_expression(): 
    return

def display():
    return

def main():
    return

if __name__ == "__main__":
    main() 
