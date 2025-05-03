import time

## consts
pi = 3.141592653589793
e = 2.718281828459045
tau = 6.283185307179586
inf = float("inf")
nan = float("nan")


## Power, exponential Functions
def pow(x,y):
    return x**y
def exp(x):
    return e**x 
def exp2(x):
    return 2**x
def expm(x):
    return (e**x)-1
def sqrt(x):
    return pow(x,0.5)
def cbrt(x):
    return pow(x, 1/3)



## sily funcs
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

def calculatemeaningofeverything():
    time.sleep(236682000000000)
    return 42

def owo():
    return ":3"
def prove_two_plus_two_is_five():
    x = 2
    y = 2
    z = (x * y)-(x * y - 4)+(y - x + 2)
    return z
## angular conversion
def degrees(x) -> float:
    return x*(180/pi)
def radians(x) -> float:
    return x*(pi/180)


# Floating point manipulation functions
def copysign(x: float, y: float) -> float:
    return float(abs(x) * (1 if y > 0 else -1 if y < 0 else 0))
def isinf(x: float)-> bool:
    return float("inf") == x
def isnan(x: float)-> bool:
    return float("nan") == x
def ldexp(x,i):
    return x * (2**i)
def nextafter(a,b,c):
    return a + (b-a)/c

def ulp(x):
    return x + 2**-52 - x

# Floating point arithmetic
def ceil(x: float) -> int:
    if x.is_integer():
        return x
    elif x<0:
        return int(x)
    else:
        return int(x)+1
def fabs(x: float)-> float:
    return float(abs(x))
def floor(x: float) -> int:
    if x >= 0 or x == int(x):
        return int(x)
    return int(x)
def fma(x: float,y: float,z: float) -> float:
    return (x*y)+z
def trunc(x: float)->int:
    return int(x)
def fmod(x:float, y: float) -> float:
    x - trunc(x / y) * y
def modf(x: float) -> tuple[float,float]:
    return (x-int(x),int(x))
def remainder(x: float,y: float) -> float:
    return x%y



## Number-theoretic functions
def isodd(x) -> bool:
    return x%2!=0
def iseven(x) -> bool:
    return x%2==0
def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a,b)
def comb(n, k):
    if k == 0 or k == n:
        return 1
    return factorial(n) // (factorial(k) * factorial(n - k))
def perm(n,k):
    return factorial(n)//(factorial(n-k))

def isqrt(x): # some random ahh dude on the internet gave me the code legit fr fr
    g = 0x8000
    c = 0x8000
    while True:
        if g * g > x:
            g ^= c
        c >>= 1
        if c == 0:
            return g
        g |= c
## trigonometric functions

def atan(x: float) -> float:
    if x < 0:
        return -atan(-x)  
    if x > 1:
        xi = 1/x
        return pi/2 - (
            xi - (xi**3)/3 + (xi**5)/5 - (xi**7)/7 + (xi**9)/9 -
            (xi**11)/11 + (xi**13)/13 - (xi**15)/15 + (xi**17)/17 -
            (xi**19)/19 + (xi**21)/21 - (xi**23)/23 + (xi**25)/25 -
            (xi**27)/27 + (xi**29)/29
        )
    elif x == 1:
        return pi/4 # idk why but every number except 1 is precise
    else:
        return (
            x - (x**3)/3 + (x**5)/5 - (x**7)/7 + (x**9)/9 -
            (x**11)/11 + (x**13)/13 - (x**15)/15 + (x**17)/17 -
            (x**19)/19 + (x**21)/21 - (x**23)/23 + (x**25)/25 -
            (x**27)/27 + (x**29)/29
        )
def atan2(y,x):
    return atan(y/x)
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
## Summation and product functions
def dist(p,q):
    result = 0
    i = 0
    while i<len(p):
        result += (p[i] - q[i])**2 + (p[i+1] - q[i+1])**2
        i+=2
    return sqrt(result)
def fsum(iterable):
    total = 0.0
    c = 0.0  
    for x in iterable:
        y = x - c      
        t = total + y  
        c = (t - total) - y 
        total = t
    return total 

def hypot(coordinates):
    return sqrt(sum(x**2 for x in coordinates))
def prod(iterable, start=1):
    result = start
    for num in iterable:
        result *= num
    return result
def sumprod(p,q):
    i = 0
    result = 0
    while i<len(p):
        result += p[i] *  q[i]
        i+=1
    return result

## Hyperbolic functions
def acosh(x):
    return ln(x+sqrt(pow(x,2)-1))
def asinh(x):
    return ln(x+sqrt(pow(x,2)+1))
def atanh(x):
    return ln((1+x)/(1-x))/2
def cosh(x):
    return (pow(e,x) + pow(e,-x)) / 2
def sinh(x):
    return (pow(e,x) - pow(e,-x)) / 2
def tanh(x):
    return sinh(x)/cosh(x)
## additional functions
# might be useful for certain scenarios
def mpow(x:int, y:int, p:int) -> int: 
    """
    Computes (x ^ y) % p using modular exponentiation.
        x (int): The base.
        y (int): The exponent.
        p (int): The modulus.
    """
    res = 1     
    x = x % p 
    if (x == 0) :
        return 0
    while (y > 0) :
        
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1      
        x = (x * x) % p
        
    return res

