print("create your password")
pin=input("Enter your pin")
password=""
for i in range(len(pin)):
        if pin[i]=="1":
            password+=pin[i]
        elif pin[i]=="2":
            password+=pin[i]
        elif pin[i]=="3":
            password += pin[i]
        elif pin[i]=="4":
            password+=pin[i]
        elif pin[i]=="5":
            password+=pin[i]
        elif pin[i]=="6":
            password+=pin[i]
        elif pin[i]=="7":
            password+=pin[i]
        elif pin[i]=="8":
            password+=pin[i]
        elif pin[i]=="9":
            password+=pin[i]
        elif pin[i]=="0":
            password+=pin[i]
print("PASSWORD:",password)