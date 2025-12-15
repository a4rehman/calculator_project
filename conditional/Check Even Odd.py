# check even odd:
def check(num):
    if num%2==0:
        return "Num is even."
    else:
        return "Num is odd."

num=int(input("Enter your number:"))

print(check(num))