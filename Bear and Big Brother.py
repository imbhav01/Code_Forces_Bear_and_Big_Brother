x = str(input()).split()
a = int(x[0])
b = int(x[1])
count = 0
for i in range (0,b):
    if a<=b:
        a = 3*a
        b = 2*b
        count += 1
    
print(count)
        