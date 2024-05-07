x = input()
count = 0
for i in x : 
    if((i == 'a') | (i == 'e') | (i == 'i') | (i == 'o') | (i == 'u')):
        count = count + 1;
print(count)
print(x.count('a') + x.count('e') + x.count('i') + x.count('o') + x.count('u'))