

## consts
pi = 3.141592653589793
e = 2.718281828459045
tau = 6.283185307179586
inf = float("inf")
nan = float("nan")

## sily funcs
def isodd(x) -> bool:
    return x%2!=0
def iseven(x) -> bool:
    return x%2==0


## angular conversion
def degrees(x) -> float:
    return x*(180/pi)
def radians(x) -> float:
    return x*(pi/180)
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
def calculate_meaning_of_everything():
    return 42



# Floating point manipulation functions
def copysign(x: float, y: float) -> float:
    return float(abs(x) * (1 if y > 0 else -1 if y < 0 else 0))
def isinf(x: float)-> bool:
    return float("inf") == x
def isnan(x: float)-> bool:
    return float("nan") == x

## Number-theoretic functions
def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def isqrt(x):
    if x < 0:
        raise ValueError("Can't find square root of an negative numbers.")
    if x == 0 or x == 1:
        return x

    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared < x:
            low = mid + 1
            ans = mid  
        else:
            high = mid - 1
    return ans    

## trigonometric functions

def sine(x:float, terms:int=10) -> float:
    x = radians(x)
    sine_val = 0
    for n in range(terms):
        sign = (-1) ** n
        sine_val += sign * (x**(2*n+1)) / factorial(2*n+1)
    return sine_val

def cosine(x:float, terms:int=10) -> float:
    x = radians(x)
    cos_val = 0
    for n in range(terms):
        sign = (-1) ** n
        cos_val += sign * (x**(2*n)) / factorial(2*n)
    return cos_val

def tangent(x:float, terms:int=10) -> float:
    sin_val = sine(x, terms)
    cos_val = cosine(x, terms)
    if cos_val == 0:
        return float('nan')
    return sin_val / cos_val

## logarithmic functions

def ln(x:float, terms:int=20) -> float:
    if x <= 0:
        return None
    result = 0
    y = (x - 1) / (x + 1)
    for n in range(terms):
        result += (2 * (y ** (2 * n + 1))) / (2 * n + 1)
    return result

def log10(x:float, terms:int=20) -> float:
    if x <= 0:
        return float('nan')
    return ln(x, terms) / ln(10, terms)

def log2(x:float, terms:int=20) -> float:
    if x <= 0:
        return float('nan')
    return ln(x, terms) / ln(2, terms)

def log(x:float, b:int, terms:int=20) -> float:
    if x <= 0:
        return float('nan')
    return ln(x, terms) / ln(b, terms)