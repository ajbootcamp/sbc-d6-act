num = int(input("Please enter a number: "))

for i in range(num, 1, -1):
     print("*" * i)
for k in range(num-2):
     print("*" if k == 0 else'', end=" ")
for j in range(1, num+1):
     print("*" * j)