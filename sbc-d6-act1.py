user = input("Please Enter a Word: ")

t = user.replace(" ", '').lower()
pal = True

for emt in range(len(t)//2):
    if t[emt] != t[-(emt + 1)]:
        pal = False
        break
print(f"{user} is a palindrome") if pal else print(f"{user} is not a palindrome")