def fibonacci_series(number):
    if((number == 1) | (number == 0)):
        return 1
    
    return number + fibonacci_series(number-1)

print(fibonacci_series(10))