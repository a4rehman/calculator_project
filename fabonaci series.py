first=0
second=1
next=0
size=int(input("Enter size of series"))
print(first,",",second,end="")
for i in range(size-2):
    next=first+second
    first=second
    second=next
    print(",",next,end="")

print("\n programme is finished.")