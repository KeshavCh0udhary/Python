# year = int(input("Enter year: \n")),
# if((year % 4 == 0) and (year % 100 != 0) | (year % 400 == 0) ):,
#     print(year, " is leap year"),
# else:,
#     print(year, " is not leap year"),

# digit = input("Enter any character: \n"),

# if((digit == '0') | (digit == '1') | (digit == '2') | (digit == '3') | (digit == '4') | (digit == '5') | (digit == '6') | (digit == '7') | (digit == '8') | (digit == '9')):,
#    print(digit," is belongs to digit"),
# else :,
#    print(digit ," is not belongs to digit")

# string = input("Enter any string\n"),

# string = string.split(" "),

# for j in range(0, len(string)):,
#     bag = [],
#     for i in range(0, len(string[j])):,
#         if((i == 0) | (i == len(string[j])-1)):,
#             bag.append(string[j][i].capitalize()),
#         else:,
#             bag.append(string[j][i]),
#     string[j] = "".join(bag),

# print(string),
  
# string = input("Enter any string\n")

# string = string.split(" ")
# for j in range(0, len(string)):
#     string.split("")
        
# lis = [3,4,5,6,7,8,9,10,11,12,13],
# for el in lis:,
#     if (el % 2 == 0):,
#         lis.remove(el),
# print(lis)

# lis = [4,5,6,7,8,9,10,11,12,13],
# lis.sort(),
# print(lis[1])

# def generate_permutations(data, permutation=[], used=[]):,
#   if len(data) == len(permutation):,
#     print(permutation),
#     return,
  
#   for i in range(len(data)):,
#     if data[i] not in used:,
#       used.append(data[i]),
#       permutation.append(data[i]),
#       generate_permutations(data, permutation, used),
#       permutation.pop(),
#       used.pop(),

# lis = [1, 2, 3,4],
# generate_permutations(lis)

# a = int(input("Enter the first number: \n")),
# b = int(input("Enter the second number: \n")),

# if (a > b):, 
#     temp = b,
# else:,
#     temp = a,

# for i in range(1, temp + 1):, 
#     if (( a % i == 0) & (b % i == 0 )):,  
#         gcd = i,  
# print(gcd)

