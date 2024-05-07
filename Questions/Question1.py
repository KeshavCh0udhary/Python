def divisible(numbers):
    for number in numbers:
        if(number % 5 == 0):
            if(number <= 150):
                print(number ,"is less then or equal to 150")
                continue
            elif(number > 500):
                print(number ,"is greater then to 500")
                break
            
numbers = [12, 75, 150, 180, 145, 525, 50]
divisible(numbers)