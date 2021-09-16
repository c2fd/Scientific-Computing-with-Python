### **`for` loops**:
for x in [1,2,3]:
    print(x)

list = [1 ,3, 2, 4, 5]

for i in list:
    if i == 4:
        break
    print(i)

 # range(start,end,step)
for x in range(2,100,3):
    print(x)


x=[1,3,2,4,5,6,7,8,9]
for i in range(0, len(x), 3):
    print(x[i])

l_short = [x[i] for i in range(0, len(x), 3)]
print(l_short)

print(x[::3])