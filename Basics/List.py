# a = [1,2,3,4,5,6,7,8,9]
# x = list(map(int,input().split(' ')))
# a.sort(reverse=True)
# a.reverse()
# a = input().split()
# a = map(int, a)
# print(a)
# l = ['jenny','jhon','keshjav']
# for i in l:
#     if i[0] == 'j':
#       print(i)
# a = "pyt@567x"
# sum = 0
# for i in a:
#     if((i == '1') | (i == '2') | (i == '3') | (i == '4') | (i == '5') | (i == '6') | (i == '7') | (i == '8') | (i == '9')):
#        sum = sum + int(i)
# even = 0
# odd = 0
# for i in a:
#     if(i % 2 == 0):
#         even += 1
#     else: 
#         odd += 1
# print(x)
t = [(1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15)]
for i in t:
    x = [a for a in i]
    x[len(x)-1] = 10
    # print(x)
    t[t.index(i)] =  tuple(x)
print(t)
# sum = 0
# l = 0
# for i in t:
#     l += len(i)
#     for j in i:
#         sum += j

# p = [y for x in t for y in x ]

# print(sum(p)/len(p))
# a = set()
# print(type(a))

# print(sum(y for x in t for y in x))
# eco clint and eco server with time

