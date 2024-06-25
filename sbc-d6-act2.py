row = int(input("Please enter a number row: "))
col = int(input("Please enter a number column: ")) 
n = 1
m = 1 

while n <= row:
    while m <= col:
        if n == 1 or m == 1 or n == row or m == col:
            print("*", end = "")
        else:
            print(" ", end = "")
        m += 1
    m = 1
    print(" ")
    n += 1