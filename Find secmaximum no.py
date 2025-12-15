print("HI! YOUR NAME IS RAO MUHAMMAD ABDUL REHMAN.")
Max = 0
secmax = 0
arr = [1, 2, 6, 13, 9, 5]
for i in arr:
    if i > Max:
        secmax = Max
        Max = i
    elif secmax < i < Max:
             secmax = i

print("Maximum no is:", Max,
" \n Second maximum no is:", secmax)
print("Programme is ending.")
print("\U0001F602")
print("\U0001F604")
print("\U0001F606")