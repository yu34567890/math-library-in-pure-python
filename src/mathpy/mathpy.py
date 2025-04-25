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
