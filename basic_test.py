def int_division():
    """
    Task:
    - Perform integer division of 7 by 2.
    
    Return:
    - The result of the division (integer).
    """
    return 7 // 2


def float_multiplication():
    """
    Task:
    - Multiply 3.0 by 2.
    
    Return:
    - The result of the multiplication (float).
    """
    return 3.0 * 2


def combine_operations():
    """
    Task:
    - Add the result of integer division and multiplication.
    
    Return:
    - The combined result (float).
    """
    return 2 // 7 + 3.0 * 2

def extract_word():
    """
    Task:
    - Extract the word 'awesome' from the string 'Python is awesome!'.
    
    Return:
    - The extracted word ('awesome').
    """
    string = "Python is awesome!"
    split_string = string.split(" ")
    new_string = []
    for i in split_string[2]:
        if i == "!":
            continue
        else:
            new_string.append(i)
    return "".join(new_string)

def to_lowercase():
    """
    Task:
    - Convert the string 'Python is awesome!' to lowercase.
    
    Return:
    - The lowercase version of the string.
    """
    string = "Python is awesome!"
    lowered_string = string.lower()
    return lowered_string

def count_o():
    """
    Task:
    - Count how many times the letter 'o' appears in the string 'Python is awesome!'.
    
    Return:
    - The count of the letter 'o'.
    """
    string = "Python is awesome!"
    counter = 0
    split_string = string.split(" ")
    for word in split_string:
        for char in word:
            if char == "o":
                counter += 1
            else:
                continue
    return counter



def evaluate_boolean():
    """
    Task:
    - Evaluate the expression 'not (5 > 3) and (10 == 5 * 2)'.
    
    Return:
    - The boolean result of the expression.
    """
    if not (5 > 3) and (10 == 5 * 2):
        return True
    else:
        return False




print(evaluate_boolean())