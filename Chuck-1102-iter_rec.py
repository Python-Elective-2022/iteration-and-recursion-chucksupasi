"""
Pseudocode:
Create function iterative_power(input base and exponent):
    If the power is 0, always return 1
    Set base to answer but don't change the value of base
    Multiply the answer base times
    Return the answer
Print the value of the function iterative_power

Create function recursive_power(input base and exponent):
    If the exponent is 0:
        Just return 1
    If the exponent is 1:
        Just return the base
    But if the exponent is more than 1:
        Return the base multiplied by the value of the function again / Repeat until the exponent is 1
Print out the value of the function recursive_power

Test Cases:
iterative_power(3, 3) : 27
recursive_power(3, 3) : 27

iterative_power(8, 10) : 1073741824
recursive_power(8, 10) : 1073741824

iterative_power(848, 1) : 848
recursive_power(848, 1) : 848

iterative_power(6, 0) : 1
recursive_power(6, 0) : 1
"""

def iterative_power(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        answer = base
        for i in range(1, exp):
            answer *= base
        return answer
print(iterative_power(2, 4))

def recursive_power(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recursive_power(base, exp - 1)
print(recursive_power(2, 4))