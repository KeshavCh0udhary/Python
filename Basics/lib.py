n = int(input())
charge = 0
if(n > 5 and n <= 10):
    charge = 2*n
elif(n > 10 and n <= 15):
    charge =  10 + 3*(n-10)
else:
    charge = 25 + 5*n (n -15)

print("Your due amount is: ", charge)