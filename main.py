
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
    while value.isnumeric() != True:
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
    words = ['first', 'second', 'third']
    first_integer = input('Please enter the first integer: ')
    if validate_integer(first_integer, words[0]) == 1:
        first_operator = str(input('Please enter the first operator: '))
        if validate_operator(first_operator, words[0]) == 1:
            second_integer = input('Please enter the second integer: ')
            if validate_integer(second_integer, words[1]) == 1:
                second_operator = str(input('Please enter the second operator: '))
                if validate_operator(second_operator, words[1]) == 1:
                    third_integer = input('Please enter the third integer: ')
                    if validate_integer(third_integer, words[2]) == 1:
                        operator_list = [first_operator, second_operator] 
                        integers_list = [first_integer, second_integer, third_integer]

    

if __name__ == "__main__":
    main() 
