
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

def validate_integer(str):
    value = input(('Please enter the {} integer: ').format(str))
    while value.lstrip("-").isdigit() != True:
        print("Error: incorrect integer input")
        value = input(('Please enter the {} integer: ').format(str))
    return value

def validate_operator(str):
    operator = input(('Please enter the {} operator: ').format(str))
    while operator not in operator_dict.keys():
        print("Error: incorrect operator input")
        operator = input(('Please enter the {} operator: ').format(str))
    return operator

def evaluate_expression(operator_list, integers_list): 
    value_list = []
    value_list = [int(i) for i in integers_list]

    if (operator_list[0] == '/') and (operator_list[1] == '/'):
        final_result = myDiv((myDiv(value_list[0], value_list[1])), value_list[2])
    if (operator_list[0] == '/') and (operator_list[1] == '*'):
        final_result = myMul((myDiv(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '/') and (operator_list[1] == '+'):
        final_result = myAdd((myDiv(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '/') and (operator_list[1] == '-'):
        final_result = mySub((myDiv(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '*') and (operator_list[1] == '*'):
        final_result = myMul((myMul(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '*') and (operator_list[1] == '/'):
        final_result = myDiv((myMul(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '*') and (operator_list[1] == '+'):
        final_result = myAdd((myMul(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '*') and (operator_list[1] == '-'):
        final_result = mySub((myMul(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '-') and (operator_list[1] == '-'):
        final_result = mySub((mySub(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '-') and (operator_list[1] == '/'):
        final_result = myDiv((mySub(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '-') and (operator_list[1] == '*'):
        final_result = myMul((mySub(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '-') and (operator_list[1] == '+'):
        final_result = myAdd((mySub(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '+') and (operator_list[1] == '+'):
        final_result = myAdd((myAdd(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '+') and (operator_list[1] == '-'):
        final_result = mySub((myAdd(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '+') and (operator_list[1] == '/'):
        final_result = myDiv((myAdd(value_list[0], value_list[1])), value_list[2]) 
    if (operator_list[0] == '+') and (operator_list[1] == '*'):
        final_result = myMul((myAdd(value_list[0], value_list[1])), value_list[2]) 

    return final_result

def display(operator_list, integers_list):
    final_result = evaluate_expression(operator_list, integers_list)
    operator_list.append('=')
    integers_list.append(final_result)
    print("\nThe result of the entered equation is:\n\t{} {} {} {} {} {} {}\n".format
    (integers_list[0], operator_list[0], integers_list[1], operator_list[1], integers_list[2], operator_list[2], integers_list[3]))
    return

def main():
    words = ['first', 'second', 'third']
    print("\nWelcome to the terminal calculator!\nYou will be asked to enter a number of integers and operators to perform a basic calculation.\nPlease follow the instructions provided.")
    integers_list = []
    operator_list = []
    integers_list.append(validate_integer(words[0]))
    operator_list.append(validate_operator(words[0]))
    integers_list.append(validate_integer(words[1]))
    operator_list.append(validate_operator(words[1]))
    integers_list.append(validate_integer(words[2]))

    display(operator_list, integers_list)
    print("Thank you for using this terminal calculator.")
    return

if __name__ == "__main__":
    main() 
