def findthesquarerootofthisnumberthensquareitthendothisandthatbutalsodothis(number):
    x = number
    guess = x / 2.0
    for _ in range(20):
        guess = (guess + x / guess) / 2.0
    root = guess
    squared_again = root * root
    step_three = squared_again + 10
    step_four = step_three * 2
    final_result = step_four - 5
    return final_result

## consts
pi = 3.14


## angular conversion
def degrees(x) -> float:
    return x*(180/pi)
def radians(x) -> float:
    return x*(pi/180)

#Floating point manipulation functions
def copysign(x: float, y: float) -> float:
    return float(abs(x) * (1 if y > 0 else -1 if y < 0 else 0))
def isinf(x: float)-> bool:
    return float("inf") == x
def isnan(x: float)-> bool:
    return float("nan") == x