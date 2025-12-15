# # rule 03:
#
# def num(number):
#     j=[1,0]
#     k=0
#     for i in number:
#         k=j[i]
#     return k
#
# print(num(0))
#
# maximum number from one number:
# num=input("enter your number:")         #num=1234
# print("num of your is:",int(max(num)))   #output:4
#
# //without using any return
# //without using any for loop or others
# //optional , you can use if, else but once
# //optional (print can use 2 times)
# //without using comparison
# //using single function
# 1. simple print
# print("hello world")
# from operator import truediv
# from http.cookiejar import user_domain_match
#
# 2.input
# name=input("Enter your name:")
#
# 3.get two inputs at once.
# name,age=input("Enter your name and age").split(",")
# print("Your name is",name,"and age is:",age)
# 4.find average.
# NUM1=int(input("Enter your 1st number"))
# NUM2=int(input("Enter your 2nd number"))
# NUM3=int(input("Enter your 3rd number"))
# AVG=(NUM1+NUM2+NUM3
# print(avg)
#
# 5.for print emoji we write this code
# print("\U0001F602")
# print("\U0001F604")
# print("\U0001F606")
# print("\U0001F606")
# print("\U0001F604")
#
# 6.STRING INDEXING (START:END-1)
# language ="python"
# print(language[2])
#
# 7.STRING SLICING (START:END-1)
# language="HELLOWORLD".
# print(language[1:3])                    # output: EL
# language="HELLOWORLD"
#  print(language[:])                     # output: HELLOWORLD
# print("HI! MY NAME IS RAO ABDUL REHMAN.")
# print(round(2393/23),2)
#
# 8.step string
# language="python"
# print(language[0:4:2])             #output: pt
#
# 9.reverse step string
# language="python"
# print("java"[-1::-1])                   #output :   nohtyp
# print("python"[::-1])                    #output: nohtyp
# name=input("enter your name:")
# print("your reverse name is:",name[::-1])
#
# 10.len method.
# name="arham"
# print(len(name))                            # output is: 5
# print(len("arslan"))                        #  output is: 6
# print(len("RAO ABDUL REHMAN"))                #OUTPUT IS :16
#                                                  REASON: ("Because len function also
#                                                           count the spaces."      )
#
# 11.LOWER method
# name="RAO ABDUL REHMAN"
# print(name.lower())                          #Output: rao abdul rehman
#
# 12. Upper method:
# name="rao abdul rehman"
# print(name.upper())                          #Output: RAO ABDUL REHMAN
#
# 13.Title method:
# name="rao abdul rehman"
# print(name.title())                          #Output: Rao Abdul Rehman
#
# 14.count method:
# name="rao abdul rehman"
# print(name.count("a"))                       #Output:3
#
# Exersice:
# name,marry=input("Enter your name and marry seprated by ',' .").split(",")
# print(name.lower().count(marry.lower()) )
#
# 15.Replace method:
# NAME="RAH         EEM            "
# print(NAME.replace(" ",""))
#
# 16.Find method:
# name="rao abdul rehman"
# print(name.find("a",3))
#
# 17.string immudable:
# string="string"
# string=string.replace("t","T")
# print(string)
#
# 18.IF STATEMENTS:
# age=int(input("Enter your age:"))
# if(age>14):
#     print("you are able for play this game.")
# else:
#     print("you are under_age so you can't play this game.")
#
# 19.pass statement.
# age=int(input("Enter your age"))
# if age>=18:
#     pass
# else:
#     print("under age")
#
# Exersice:
# num1=20;
# num2=int(input("Gusse number"))
# if num1==num2:
#     print("you are winner of the game.")
#
# else:
#     if num1 > num2:
#         print("you gusse too low.")
#     else:
#          print("you gusse too high.")
#
# Exersice:
# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# if name[0]=="A"or"a"and age>=18:
#     print("you can watch the movie coco.")
# else:
#     print("you can't watch this movie.")
#
# 20.Elif_statements:
# age=int(input("Enter your name:"))
# if age>0:
#     if age<=10:
#         print("Ticket price is:100")
#     elif age<=20:
#         print("Ticket price is:200")
#     elif age <= 30:
#         print("Ticket price is:300")
#     elif age <= 60:
#         print("Ticket price is:400")
#     else:
#         print("Ticket is Free.")
# else:
#     print("Enter correct age.")
#
# 21.In keyword:
# name=input("Enter your name:")
# if "R"in name:
#     print("Yes 'R' is available in name.")
# else:
#     print("sorry 'R' not present in name.")
#
# 22.EMPTY OR NOT:
# name=input("Enter your name:")
# if name:
#     print(" sting is not empty")
# else:
#     print("string is empty.")
#
# 23.while loop:
# i=1
# while i<=10:
#     print(i,".hellowirld")
#     i+=1
#
# 24.sum with while loop:
# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print("Sum of your loop is:",sum)
#
# Exersice:
# Question 01:
# i=1
# sum=0
# n=int(input("enter your num where you want to print:"))
# while i<=n:
#        sum+=i
#        i+=1
# print(sum)
#
# Question 02:
# first rule for addition:
# sum=0
# rem=0
# num=int(input("enter your number:"))
# while num>0:
#    rem= num%10
#    sum+=rem
#    num//=10
# print("Sum of your number is:",int(sum))
#
# Question 03:
# second rule for addition:
# num=input("enter your number:")
# sum=int(num[0])+int(num[1])+int(num[2])+int(num[3])
# print("sum of your is:",sum)
#
# Question 03:
# third rule for addition:
# num=input("Enter your number:")
# i=0
# sum=0
# while i<len(num):
#     sum+=int(num[i])
#     i+=1
# print("Sum is :",sum)
#
# Question 04:
# print all char occourance:
# name=input("Enter your name:")
# i=0
# k=""
# while i<len(name):
#     if name[i]not in k:
#       k+=name[i]
#       print("# ",name[i],name.count(name[i]))
#     i+=1
#
# 25.INFINITE LOOP:
# while True:
#     print("MY NAME IS RAO MUHAMMAD ABDUL REHMAN.")
#
# 26. FOR LOOP :
# Exp.1
# for i in range(10):
#     print(i,".Hi! whats up.")
#
# Exp.2
# for i in range(4,12):    # tell starting and ending point.
#  print(i, ".Hi! whats up.")
#
# Exp.3
# sum=0
# num=int(input("Enter your number."))
# for i in range(num+1):
#             sum+=i
#
# print("Sum of your number is:",sum)
#
# Exp.4
# Rule 1:
# rem =0
# sum=0
# num=int(input("Enter your number:"))
# for i in range(len (str(num))):
#
#         rem=num%10
#         sum+=rem
#         num//=10
# print("Final Sum of your num is:",sum)
#
# Rule 2:
#
# sum=0
# num=input("Enter your number:")
#
# for i in range(len (num)):
#       sum+=int(num[i])
#
# print("Final Sum of your num is:",sum)
#
# Exp.4
# k=""
# name=input("Enter your name:")
# for i in range(len(name)):
#     if name[i] not in k:
#         k+=name[i]
#         print("#",name[i],name.count(name[i]))
#
# 27. BREAK STATEMENT:
# for i in range(10):
#     if i==5:
#         break
#     print(i,".Hi! whats going on.")
#
# 28. Continue Statement:
# for i in range(10):
#     if i==5:
#         continue
#     print(i,".Hi! whats going on.")
#
#  Exersice:
# 29. DESINE A GAME:
#
# import random
# num=random.randint(1,100)
# for i in range(100):
#     if i<=5:
#        guessed=int(input("Guessed your number:"))
#        if guessed==num:
#             print("Congratulations! you win the game","\U0001F604","your try is",i)
#             break
#        elif guessed<num:
#             print("You guessed too low.try again.")
#        else:
#            print("You guessed too high.try again.")
#     else:
#           print("your attempts is over.")
#
#
# Rule 02:
# 30.
# import random
#
# num = random.randint(1, 100)
#
# for i in range(1, 6):
#     guess = int(input(f"Attempt {i}/5 - Guess the number: "))
#
#     if guess == num:
#         print(f"Congratulations!  You guessed the number in {i} tries!")
#         break
#     elif guess < num:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
#
# else:
#     print(f"Sorry, you've used all your attempts. The correct number was {num}.")
#
# 31.for loop with string:
# name=input("Enter your name:")
# for i in  name:
#     print(i)
#
# 32. SUM OF NUMBERS:
# num=input("Enter your num:")
# total=0
# for i in  num:
#     total+=int(i)
#
# print(total)
#
# 33. Functions in python:
# Exp 01:
# def avg(num1,num2,):
#     return int((num1+num2))/2
# num1,num2=input("Enter your numbers separated by commas:").split(",")
# ans=avg(num1,num2)
# print(ans)
#
# Exp 02:
#
# def attach(first_name,last_name):
#     full_name=first_name+last_name
#     return full_name
#
# first_name,last_name=input("Enter your first and last name:").split(",")
#
# print("Your name is :",attach(first_name,last_name))
#
# Exp 03:
# check even odd:
# def check(num):
#     if num%2==0:
#         return "Num is even."
#     else:
#         return "Num is odd."
#
# num=int(input("Enter your number:"))
#
# print(check(num))
#
# EXP 04:
# Check even odd with optimization:
#
# def check(num):
#
#     return num%2==0
#
# print(check(num=int(input("enter your num"))))
#
# EXP 05:
# GREATEST NUMBER:
# def find(num1,num2):
#     if num1>num2:
#         return print("num1 is greater than num2.")
#     return print("num2 is greater than num1.")
#
# num1,num2=input("Enter num1 and num2:").split(",")
# find(int(num1),int(num2))
#
# EXP 06:
# Find greatest from three numbers:
# def greatest(num1,num2,num3):
#
#     if num1>num2 and num3:
#         return num1
#     elif num2>num3 and num1:
#         return num2
#     elif num3>num1 and num2:
#         return num3
#
# num1,num2,num3=input("Enter your three numbers:").split(",")
# print("The biggest number from three numbers is:",greatest(int(num1),int (num2) ,int( num3)))
#
# OPTIMIZATION:
# def greatest(num1, num2, num3):
#     if num1 > num2 and num3:
#         return num1
#     elif num2 > num3 and num1:
#         return num2
#     elif num3 > num1 and num2:
#         return num3
# print("The biggest number:", greatest(10,40,29))
#
# 34. Nested Function:
#
# EXP 01:
# def greatest(num1, num2):
#     if num1 > num2 :
#         return num1
#     return num2
# def new_greater(num1,num2,num3):
#     bigger=greatest(num1,num2)
#     return greatest(bigger,num3)
#
# print("Greatest number is:",new_greater(90,45, 23))
#
# KISS: KEEP ITS SIMPLE STUPID.
#
# Question no:01
# palindrome string:
# def palindrome(string):
#     if string[-1::-1]==string:
#         return True,'palindrome'
#     return False,'not palindrome.'
# string=input("Enter any word:")
# print(palindrome(string))
#
# Question no 02:
# palindrome digit:
# def palindrome(num):
#     if num[-1::-1]==num:
#         return True,'palindrome'
#     return False,'not palindrome.'
# num=input("Enter any number:")
# print(palindrome(num))
#
# Question no 03:
# Fibonacci series:
# def fibonacci(num):
#     first = 0
#     last=1
#     print(first,",",last,end="")
#     for i in range (num-2):
#        temp=first+last
#        first=last
#        last=temp
#        print(",",temp,end="")
# num=int(input("Enter your number:"))
# fibonacci(num)
#
# 35. Default arguments:
# def show(first_name,last_name,age=None):
#     print("your full name is:",first_name+last_name)
#     print("your age is :",age)
# first_name,last_name=input("Enter your name:").split(",")
# age=int(input("Enter your age:"))
# show(first_name,last_name)
#
# 36.scope variable:
# n=10
# def show():
#    global n
#    print(n)
#    return n
#
# print(show())
# print(n)
#
# list:
# marks = [34,67,78,45]
# print(marks)
#
# insert method:
# marks=[2,4,3,2,5]
# marks.insert(3,9)
# print(marks)                          #Output:[2, 4, 3, 9, 2, 5]
#
# join method:
# fruits_1=["mango","banana","orange","pear"]
# fruits_2=["Apple","grapes","kiwi"]
# fruits=fruits_1+fruits_2
# print(fruits)           #Output:['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi']
#
# extend method:
# fruits_1=["mango","banana","orange","pear"]
# fruits_2=["Apple","grapes","kiwi"]
# fruits_1.extend(fruits_2)
# print("fruits:",fruits_1)           #Output:fruits: ['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi']
#
# append method:
# fruits=['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi']
# fruits.append("guava")
# print(fruits)                       #Output:['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
#
# delete data from list:
# pop method:
# fruits=['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
# fruits.pop()
# print(fruits)                       #Output:['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi']
#
# exp:
# fruits=['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
# fruits.pop(0)
# print(fruits)                        #Output:['banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
#
# delete operator:
# fruits=['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
# del fruits[4]
# print(fruits)                           #Output:['mango', 'banana', 'orange', 'pear', 'grapes', 'kiwi', 'guava']
#
# remove method:
# fruits=['mango', 'banana', 'orange', 'pear', 'Apple', 'grapes', 'kiwi', 'guava']
# fruits.remove("Apple")
# print(fruits)                              #Output:['mango', 'banana', 'orange', 'pear', 'grapes', 'kiwi', 'guava']
#
# In keyword used in list:
#
# fruits=['mango', 'banana', 'orange', 'pear', 'grapes', 'kiwi', 'guava']
# if 'mango' in fruits:
#     print("Mango is present in list fruit")
# else:
#     print("mango not present in fruit list.")
#
# count method in list:
# fruits=["mango","banana","apple","pear"]
# print(fruits.count('mango'))         #Output:1
#
# sort method:
# in sort method our list will be changed.if we print again it show sort list.
# marks=[3,5,4,2,3,1,0]
# marks.sort()
# print(marks)    #[0, 1, 2, 3, 3, 4, 5]
#
# sorted function:
# in sorted function our list will be not changed.if we print again it show simple list.
# marks=[2,4,3,5,6,6,1,0]
# print(sorted(marks))    #Output:[0,1,2,3,4,5,6,6]
# print(marks)          #Output:[2,4,3,5,6,6,1,0]
#
# clear method:
# marks=[3,5,4,2,1,9]
# marks.clear()
# print(marks)            #Output:  []
#
# copy method:
# marks=[3,5,4,2,1,9]
# mark=marks.copy()
# print(mark)
# marks.sort()
# print(marks)
#
# is vs '=='
#
# '=='
# marks=12
# mark=12
# if(marks == mark):
#     print("hello")
# else:
#     print("world")             #Output : hello
#
# 'is'
# marks=12
# no=12
# if(marks is no):
#     print("hello")
# else:
#     print("world")                 #Output : hello
#
# split method:
# change string into list.
# user_info="arslan,24".split(",")
# print(user_info)              #['arslan', '24']
#
# exp:
# name,age="arslan,24".split(",")
# print(name,"\n",age)            # Output:arslan
#                                           24
#
# join method:
# join the list to convert into string
# user_info=["Arslan,24"]
# print(",".join (user_info))        #Arslan,24
#
# loop in list:
# for loop:
# fruits=["mango","orange","banana","pear"]
# for fruit in fruits:
#     print(fruit)               #Output: mango
#                                       orange
#                                       banana
#                                       pear
#
# while loop:
# fruits=["mango","orange","banana","pear"]
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1                  #Output: same output as in for loop:
#
# list to list:
# exp:
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for sublist in matrix:
#     for i in sublist:
#         print(i ,end="") #Output: 123456789
#
# exp:
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[2][0])     #Output: 7
#
# checking of type:
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(type(matrix))
#
# generate list with range function:
# num=list(range(1,11))
# print(num)        #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# pop method return pop value:
# num=list(range(1,11))
# print(num.pop())  #     pop_value=num.pop(). we also want to asign this to another variable
# print(num)
#
# index method:
# num=list(range(1,11))
# print(num.index(6))
#
# pass list to function:
# num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nums=[2,5,4,3,2,1,3,3]
# def negative(l):
#     negative=[]
#     for i in l:
#         negative.append(-i)
#     return negative
#
# print(negative(num))
#
# pass list to function return square value:
# num=[2,4,3,1,5,0]
# nums=(range(1,11))
# def square(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square
#
# print(square(nums))
#
# pass list to function return reverse value:
#
# rule 01:
# def square(l):
#
#     nums=l[-1::-1]
#     return nums
# num=[2,4,3,1,5,0]
# num.sort()
# print(square(num))
#
# rule 02:
# num=[2,4,3,1,5,0]
# def reverse(l):
#     reverse=[]
#     for i in range(len(l)):
#         reverse.append(l.pop())
#     return reverse
#
# print(reverse(num))
#
# rule 03:
# num=[2,4,3,1,5,0]
# def reverse(l):
#     l.reverse()
#     return l
# print(reverse(num))
#
# Question 01:
# num=[2,4,3,1,5,0]
# num=["abc","def","ghi","jkl"]
# def revers(l):
#     revers=[]
#     for i in l:
#         revers.append(i[::-1])
#     return revers
# print(revers(num))
#
#
# 01: Linked in
# def Rotate(num):
#     revers = []
#     k=3
#     for i in  range(k):
#         revers.append(num.pop())
#         revers.reverse()
#     rotate=revers
#     rotate+=num
#     return rotate
# num=[1,2,3,4,5]
# print(Rotate(num))
#
# 02:  Linked in
# word = "swiss"
# for i in range(len(word)):
#     if word.count(word[i]) == 1:
#         print("The first letter that appears only once is:",word[i])
#         break
#
# 03:  Linked in
# num=[1,2,3,4,5,6,7,8,9,10]
# target=5
# for i in range(len(num)):
#     for k in range(i+1,len(num)):
#         if num[i]+num[k]==target:
#             print(num[i],"+",num[k],"=",target)
#             print("index is:",i," and ",k)
#
# 04: Linked in
# def join(l):
#     output=[]
#     for i in l:
#         if type(i)!=list:
#             output.append(i)
#         else:
#             output.extend(i)
#     return output
# l=[1,2,3,[4,5,6],[7,8,9],[10,11,12]]
# print(join(l))
#
# 05:Linked in
# def list(l):
#     for i in range(len(l)):
#         l.sort()
#     return l
# l=[(1,5),(2,1),(0,2)]
# print(list(l))
#
# Bhai waqar ka question.
# find number which have same sum of numbers around it.
# def find(l):
#     total_sum = sum(l)
#     left_sum = 0
#     for i in range(len(l)):
#         total_sum -= l[i]
#         if left_sum == total_sum:
#             return i
#         left_sum += l[i]
#     return -1
# l = [6, 2,3,6,4,1,0,4,7,11]
# index = find(l)
# if index != -1:
#     print(l[index])
# else:
#     print("No  index found.")
#
#
# Question:02
# def num_filter(l):
#     even=[]
#     odd=[]
#     for i in range(len(l)):
#         if l[i]%2==0:
#             even.append(l[i])
#         else:
#             odd.append(l[i])
#     output=[even,odd]
#     return output
# num=[1,2,3,4,5,6,7,8]
# print(num_filter(num))
#
# Question 03:
# def commun(l1,l2):
#     l=[]
#     for i in l1:
#         if i in l2:
#             l.append(i)
#     return l
# l1=[1,2,3,4,5]
# l2=[5,3,4,2,1]
# print(commun(l1,l2))
#
# Question 04:
# def find(l):
#     Min=min(l)
#     Max=max(l)
#     return Min,Max
# l=[1,4,8,9,0,5,-1]
# print(find(l))
#
# Question 05:
# count sublist:
# def checkout(l):
#     count=0
#     for i in l:
#         if type(i)==list:
#             count+=1
#     return count
# l=[1,2,3,[4,5,6],[7,8,9],[10,11,12]]
# print("There are ",checkout(l),"sublist in your list")
#
# Question 06:
# input a list:
# l=[]
# l=input("enter numbers of your list")
# print(l)
#
# Tuples:
# days=("monday","tuesday","friday")
# print(type(days))
#
# we can never change add or delete the tuple:
# but also can use these functions (min,max,sum)
# num=(8,9,6,5,4,9,0)
# print(min(num))
# print(type(num))
# print(max(num))
# print(sum(num))
#
# function returning values:
# def num(num1,num2):
#     add=num1+num2
#     multi=num1*num2
#     return add,multi
# num1=12
# num2=10
# # print(num(num1,num2))       #Output:(22,120). it returns tuple values.
# # so, if we want to convert in the form variable we write this
# add,multi=num(num1,num2)
# print(add,multi)
#
# create tuple:
# this is for list:
# nums=list((range(1,11)))
# print(nums)       #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# this for tuple:
# nums=tuple(range(1,11))
# print(nums)       #Output:(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# list in a tuple:
# we can't change the tuple but change list in the tuple:
# mixed=(1,2,3,4,5,[6,8,9])
# mixed[5].pop()
# mixed[5].append(44)
# print(mixed)      #Output:(1, 2, 3, 4, 5, [6, 8, 44])
#
# Dictionary:
# Unordered collections of data in key : value pair.
# There is no index of data because unordered collections of data.
# for asses the data we use keys.
# we can store any type of data in dictionary.
# we can also store a list into a dictionary.
# we can also store a dictionary into a dictionary.
#
# 1st method for create dictionary:
# user={"Name":"Rao Abdul Rehman","Age":18,"education":"Fsc"}
# print(user)
# print(type(user))
#
# 2nd method for create dictionary:
# user=dict(Name="Rao Abdul Rehman",Age=18,education="Fsc")
# print(user)
# print(type(user))                                     # these two method have same output:
#                                                       {'Name': 'Rao Abdul Rehman', 'Age': 18, 'education': 'Fsc'}
#                                                       <class 'dict'>
#
# How access the data with  using the keys.
# Using this  method we access the data.;
# user=dict(Name="Rao Abdul Rehman",Age=18,education="Fsc")
# print(user["Name"])          #Output will be this: Rao Abdul Rehman
#
# How to store a list in a dictionary:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# print(user["movie"])
#
# we also create many users data in dictionary:
# users={
# user:{"name":"abdullah","age":10,"educ":"4th standard","movie":[None]},
# user1:
# {"name":"abdul rehman","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# ,user2:
# {"name":"abdul wasy","age":-10,"educ":"None","movie":[None]}
# }
#
# How to add the data in dictionary:
# users={}
# users["Name"]="rao"
# users["Age"]=18
# print(users)
#
# Looping and In keyword in dictionary:
#
# 01. check if key exist in dictionary:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# if "age" in user:
#    print("name keyword is present in the dictionary.")
# else:
#     print("Have you no manners")                 #Outout will be as: name keyword is present in the dictionary.
#
# 01. check if value exist in dictionary:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# if "abdullah" in user.values():
#    print( " keyword is present in the dictionary.")
# else:
#     print("Have you no manners")
#
#
# 02.loops in dictionary:
# 01:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# for i in user:
#     print(user[i])           #abdullah
#                              18
#                              Fsc
#                              ['Coco', 'Krish', 'Tiger', 'Liger']
#
# 02:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# user_info=user.items()
# print(user_info)
# print(type(user_info))  #dict_items([('name', 'abdullah'), ('age', 18), ('educ', 'Fsc'),
#                         ('movie', ['Coco', 'Krish', 'Tiger', 'Liger'])])
#                         <class 'dict_items'>
# 03:
# user={"name":"arslan","age":22,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# for i,j in user.items():
#     print("key is:",i,"values is:",j)
#
# 04:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# print(user.values())                #Output :dict_values(['abdullah', 18, 'Fsc', ['Coco', 'Krish', 'Tiger', 'Liger']])
#
#
# How to add data in dictionary:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# user["city"]=["vehari","50 w/b"]
# print(user.items())
#
# How to pop data in dictionary:
# As compare to list when we just write that pop() it automatically delete the last data from list
# but in dictionary when we write pop() it occur error .at least one arguments is important to pass.
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# popped=user.pop("movie")
# print(popped)
# print(user)
#
# How to pop item method:
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# popped=user.popitem()
# print(type(popped))    # type of popped will be tuple.
# print(user)      #Output :('movie', ['Coco', 'Krish', 'Tiger', 'Liger'])
#                 #         {'name': 'abdullah', 'age': 18, 'educ': 'Fsc'}
#
# update dictionary:
# if we write  any key again which is exist first then it update the first key
# user1={"hobby":["cricket","racing","cycling","visiting"]}
# user={"name":"abdullah","age":18,"educ":"Fsc","movie":["Coco","Krish","Tiger","Liger"]}
# user.update(user1)
# print(user)         #Output:{'name': 'abdullah', 'age': 18, 'educ': 'Fsc',
#                      'movie': ['Coco', 'Krish', 'Tiger', 'Liger'],
#                      'hobby': ['cricket', 'racing', 'cycling', 'visiting']}
#
# From key usage in the dictionary
# from list:
# d=dict.fromkeys(["Name","Age","Educ","City"],"Unknown")
# print(d)
#
# from tuple:
# o1:
# d=dict.fromkeys(("Name","Age","Educ","City"),"Unknown")
# print(d)
# print(type(d))     #Output:{'A': 'Unknown', 'B': 'Unknown', 'C': 'Unknown'}
#
# 02:
# d=dict.fromkeys("ABC",'Unknown')
# print(d)        #Output:{'A': 'Unknown', 'B': 'Unknown', 'C': 'Unknown'}
#
# 03:
# d=dict.fromkeys(range(1,11),"unknown")
# print(d)     #Output :{1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown'
# , 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}
#
# 04:
# d=dict.fromkeys(["name","age"],["unknown","unknown"])
# print(d)           #Output will be this:{'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}
#
# Get method:
# 01:
# simple method for get any key:
# d={"name":"unknown","age":"unknown"}
# print(d["name"])     #output:unknown
#
# 02:
# use get method for get value of any key:
# # d={"name":"unknown","age":"unknown"}
# print(d.get("name"))   #output :unknown
#
# if i write there that any key which is not
# exist than it not give any error as compare to simple getting the key.this get method give none value.
# For example:
# d={"name":"unknown","age":"unknown"}
# print(d.get("names"))      #output will be this: None
#
# second method for use the get method:
#
# d={"name":"unknown","age":"unknown"}
# if d.get("name"):
#     print("present")
# else:
#     print("not present")       #output :present
#
# Clear method in dictionary:
# d={"name":"unknown","age":"unknown"}
# d.clear()
# print(d)       #Output :{}
#
# for copy the dictionary:
# d={"name":"unknown","age":"unknown"}
# d1=d.copy()
# print(d1)       #Output :{'name': 'unknown', 'age': 'unknown'}
# d1.popitem()    #         {'name': 'unknown', 'age': 'unknown'}
#                           {'name': 'unknown'}
# print(d)
# print(d1)
#
#
# But if we use this :
# d={"name":"unknown","age":"unknown"}
# d1=d
# d1.popitem()
# print(d)
# print(d1)     #Output:{'name': 'unknown'}
#                     {'name': 'unknown'}
#
# dict copy is not same:
# d={"name":"unknown","age":"unknown"}
# d1=d.copy()
# print( d is d1)    #Output:False
#
# dict copy == not same:
# d={"name":"unknown","age":"unknown"}
# d1=d.copy()
# print( d == d1)    #Output:True
#
# Because 'is' check the location in memory but '==' is check out the values:
#
# but in assign have same values and memory:
# it gave same output in same operator 'is' or '==':
# d={"name":"unknown","age":"unknown"}
# d1=d
# print(d is d1)     #True
#
# in get methode if any key was not exist then if we want to print some another
# message then we write this code in get methode.if exist it gave the real value of key:
#
# d={"name":"arslan","age":20}
# print(d.get("names","this key was not exist.")) #Output :this key was not exist.
#
# What if i write two same key in the dictionary.when i write the same name of any dictionary then it
# overhead the first key and show the second key .
# For example:
# d={"name":"arslan","age":20,"name":"adnan"}
# print(d)             #Output will be this:{'name': 'adnan', 'age': 20}
#
# EXERSICE:01
# find out the cube of all these number which is writing in the function parameters:
# def find_cube(num):
#     nums={}
#     for i in range(1,num+1):
#        nums[f"{i}"]=[f"{i**3}"]  # or write this nums[i]=i**3 .its output will be this: {1: 1, 2: 8, 3: 27}
#     return nums
# num=int(input("Enter your number:"))
# print(find_cube(num))          #Output: if num=3 then {'1': ['1'], '2': ['8'], '3': ['27']}
#
# word count in dictionary:
# def word_count(word):
#     count={}
#     for i in word:
#         count[i]=word.count(i)
#     return count
# word=input("Enter your word:")
# print(word_count(word))
#
# user input for dictionary:
# # simple print:
# name=input("Enter your name:")
# age=input("Enter your age:")
# fav_movies=input("Enter your favorite movies separated names with ',':").split(",")
# fav_songs=input("Enter your favorite songs separated names with ',':").split(",")
# user={}
# user["name"]=name
# user["age"]=age
# user["fav_movies"]=fav_movies
# user["fav_songs"]=fav_songs
#
# print(user)
#
# Print with loop:
# IT PRINT LINE BY LINE IN THE DICTIONARY:
# name=input("Enter your name:")
# age=input("Enter your age:")
# fav_movies=input("Enter your favorite movies separated names with ',':").split(",")
# fav_songs=input("Enter your favorite songs separated names with ',':").split(",")
# user={}
# user["name"]=name
# user["age"]=age
# user["fav_movies"]=fav_movies
# user["fav_songs"]=fav_songs
# for key,value in user.items():  #there key is the name of key and value is the value which is writen in dictionary:
#     print(key,":",value)
#
# popitem() method delete the last key of the dictionary:
# user.popitem()
# print(user)
#
# SET in PYTHON:
#            set is unordered collections of data and unique data:
#            it means that there is no item is repeated in the set .
#            why we use this ? because, it has unique values .
#            if we want to print unique values than we use set
#            we create this with curly brackets.
#            And not write any key just write values.
#            we cant store a list are dictionary into the set.
#            when print our set  its output will be unordered.
# s={1,2,3,4,5,6,7,8,3,2,1,1}
# print(s)       #output will be unique:{1, 2, 3, 4, 5, 6, 7, 8}
#
# how to convert the list into set:
# l=[1,2,3,4,5,6,7,8,8,2]
# s=set(l)
# print(s)     #now output will be this that all the items are unique in set.
#              Output:{1, 2, 3, 4, 5, 6, 7, 8}
# how to convert set into list:
# l=[1,2,3,4,5,6,7,8,8,2]
# s=list(set(l))
# print(s)      #now first it become set and in set item are unique and then convert into list:
#               Output:[1, 2, 3, 4, 5, 6, 7, 8]
#
# Add method in sets:
# s={1,2,3,4,5}
# s.add(4)   #  it adds the value 4 at the end of the set items.
# s.add(4)       # if we add 4 two or many times it just adds once
# print(s)    #Output:{1, 2, 3, 4, 5}
#
# Remove method in sets:
# s={1,2,3,4,5}
# s.remove(4)     # it removes this number 4.if we write the number which is not exist it gave key error.
# print(s)       #Ouptput:{1, 2, 3, 5}
#
# Discard method:
# s={1,2,3,4,5}
# s.discard(4)    # it removes this number 4.if we write the number which is not exist it don't give any error.
# print(s)          #output:{1, 2, 3, 5}
#
# clear method:
# s={1,2,3,4}
# s.clear()
# print(s)
# print(type (s))  #  set()
#                    <class 'set'>
#
# copy method:
# it is also work as copy method work in dictionary
# i mean that copy method make new and different set but assign operator
# have same memory location of these set and for doing any changes
# it also effects those both set.
# s={1,2,3,4}
# s1=s.copy()
# print(s1)
#
# In keyword:
# for checking the values that it is exists are not we use the in keyword:
#
# check with if else:
# s={'a','b','c'}
# if 'c' in s:
#     print("present")
# else:
#     print('Not present')     #Output: present
#
# check with for loop:
# s={'a','b','c'}
# for i in s:
#     print(i,",",end="")     #Output:c ,b ,a
#                             because sets is unordered collections of data.
#                             As we run this again and again its values were
#                             changed automatically because unordered collections of data.
#
# for remove the duplicate from list we also use sets.
# l=[1,2,3,3,2,1]
# s=set(l)
# print(s)     #Output :{1,2,3} it remove the repeated values.
#
# Operations on sets:
# UNION and INTERSECTION:
# UNION:
# s1={1,2,3,4}
# s2={3,4,5,6}
# s=s1|s2        #this is union operator.all the repeated values are remove.
# print(s)      #Output:{1, 2, 3, 4, 5, 6}
#
# INTERSECTION:
# s1={1,2,3,4}
# s2={3,4,5,6}
# s=s1 & s2        #this is intersection operator.all the repeated values are printed.
# print(s)         # Output:{3, 4}     Note:we also write as print(s1 & s2) output will be same.
#
# CHAPTER 09:
# COMPREHENSION:
#
# i) #create a list of square from 1,10.
# simple methode:
# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)        #output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# Comprehension method in list:
# square=[i**2 for i in range(1,11)]
# print (square)       #Output:[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Output will be same of both method but comprehension is very easy and sort form of code.
#
# ii) #create a list of negative from 1,10.
# simple methode:
# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative)        #output:[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
#
# Comprehension method in list:
# negative=[-i for i in range(1,11)]
# print (negative1)       #Output:[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
# Output will be same of both method but comprehension is very easy and sort form of code.
#
# iii) #create a list of first character from name list.
# simple methode:
# name=['arslan','adnan','arham']
# list=[]
# for i in name:
#     list.append(i[0])
# print(list)        #output:['a', 'a', 'a']
#
# Comprehension method in list:
# list=[i[0] for i in name]
# print (list)       #Output:['a', 'a', 'a']
# Output will be same of both method but comprehension is very easy and sort in form of code.
#
#
# iv)iii) #create a list of first character from name list.
# simple methode:
# word=['abc','def','ghi']
# list=[]
# for i in word:
#     list.append(i[::-1])
# print(list)        #output:['cba', 'fed', 'ihg']
#
# Comprehension method in list:
# word=['abc','def','ghi']
# list=[i[::-1] for i in word]
# print (list)       #Output:['cba', 'fed', 'ihg']
# Output will be same of both method but comprehension is very easy and sort in form of code.
#
# list comprehension with if else statements:
# if number is even than power of this else odd return -1:
# simple method:
# def change(l):
#     list=[]
#     for i in l:
#         if i%2==0:
#             list.append(i**2)
#         else:
#             list.append(-1)
#     return list
# l=[1,2,3,4,5,6]
# print(change(l))    #output:[-1, 4, -1, 16, -1, 36]
#
# comprehension:
# l=[1,2,3,4,5,6]
# list=[i**2 if (i%2==0) else -1 for i in l ]
# print(list)           #output:[-1, 4, -1, 16, -1, 36]
#
#
# Nested list:
# list with in a list is nested list:
# nested list with comprehension:
# for example we want to create a list and then print this:
# l=[[1,2,3],[1,2,3],[1,2,3]]
# nested_list=[[i for i in range(1,4)] for j in range(3)]
# print(nested_list)           #Output:[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
#
# how tuple are faster than list:
#  Tuples vs Lists (Speed & Performance)
# Tuples are immutable, meaning their size and contents don’t change after creation.
# Lists are mutable, which means Python needs to allocate extra memory for dynamic resizing.
# Tuple operations (like iteration and indexing) are faster than lists because:
# They don’t need to account for modifications.
# Python optimizes tuple storage since their size is fixed.
#
# For example:
# import timeit
#
# # Test execution time
# list_time = timeit.timeit(stmt="x = [1,2,3,4,5,6,7,8,9,10]", number=1000000)
# tuple_time = timeit.timeit(stmt="x = (1,2,3,4,5,6,7,8,9,10)", number=1000000)
#
# print(f"List creation time: {list_time}")
# print(f"Tuple creation time: {tuple_time}")
# output: List creation time: 0.0802663000067696
#        Tuple creation time: 0.021101899968925864
#
# how to tuple are faster than dictionary:
# import timeit
#
# data_tuple = (1, 2, 3, 4, 5)
# data_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
#
# # Measure lookup time
# tuple_lookup = timeit.timeit(stmt="3 in data_tuple", globals=globals(), number=1000000)
# dict_lookup = timeit.timeit(stmt="3 in data_dict", globals=globals(), number=1000000)
#
# print(f"Tuple lookup time: {tuple_lookup}")
# print(f"Dictionary lookup time: {dict_lookup}")
#             output:    Tuple lookup time: 0.06434719997923821
#                        Dictionary lookup time: 0.04902799997944385
#
#  which is fast dict or list:
# import timeit
#
# data_list = list(range(1000000))
# data_dict = {i: True for i in range(1000000)}
#
# # Searching for 999999 in list
# list_time = timeit.timeit(stmt="999999 in data_list", globals=globals(), number=100)
# # Searching for 999999 in dictionary
# dict_time = timeit.timeit(stmt="999999 in data_dict", globals=globals(), number=100)
#
# print(f"List lookup time: {list_time}")
# print(f"Dictionary lookup time: {dict_time}")
# output:List lookup time: 1.2510153000475839
# Dictionary lookup time: 1.2500036973506212e-05
#
# Memory Usage
# Dictionaries use more memory because they store keys, values, and hash metadata.
# import sys
#
# list_data = list(range(1000))
# dict_data = {i: i for i in range(1000)}
#
# print(f"List memory: {sys.getsizeof(list_data)} bytes")
# print(f"Dictionary memory: {sys.getsizeof(dict_data)} bytes")
#
# output:List memory: 8056 bytes
# Dictionary memory: 36952 bytes
#
# list=[i for i in range(1,11) if i%2!=0]
# print(list)
#
# list=[[i for i in range(1,4)] for j in range(3)]
# print(list)
#
# Dictionary comprehension:
# list={1:1,2:4,3:9,4:16} 1st index then index square
# simple method:
# list={}
# for i in range(1,11):
#     list[i]=i*i
# print(list)           #output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
#
# comprehension:
# list={i:i*i for i in range(1,11)}
# for key,value in list.items():
#    print(key," square is:",value)
#    output:1  square is: 1
#    2  square is: 4
#    3  square is: 9
#    4  square is: 16
#    5  square is: 25
#    6  square is: 36
#    7  square is: 49
#    8  square is: 64
#    9  square is: 81
#    10  square is: 100
#
#    count word in dictionary:
# word="  rehman"
# word_count={i:word.count(i) for i in word}
# print(word_count)
#
#
# if else statements in dictionary comprehension:
# list=[1,2,3,4,5,6]
# name={i:("even" if i%2==0 else "odd" )for i in list}
# print(name) #output:{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even'}
#
# set comprehension:
#
# square={i**2 for i in range(1,11)}
# print(square)
#                 output:{64, 1, 4, 36, 100, 9, 16, 49, 81, 25} Because, sets are unordered collections of data.
#
# *args
#
# def all(*nums):
#     total=0
#     for i in nums:
#         total+=i
#     return total
# print(all(1,2,3,4,5,6))     #output:21
#
#
# *args in simple parameters:
# def multiply(*args):
#     multiply=1
#     for i in args:
#         multiply*=i
#     return multiply
# print(multiply(2,3,4))  #output:24
#
# def sum(num,*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(sum(1,2,3,4))  #output:9
# because num is not part of args so it is different arguments and after 1st parameters all the part of the args.
#
# args as arguments:
# def num(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total
# nums=[1,2,3,4]
# print(num(*nums))  #output:10
# because * doing the unpack this list and pass as a parameters
# we also pass the tuple with using *.
#
#
# exersice:
# simple method:
# def num(num,*args):
#     if args:
#         list = []
#         for i in args:
#             list.append(i ** num)
#         return list
#     else:
#         print("hy you ds'nt pass any args")
# nums=[1,2,3,4,5]
# print(num(2,*nums))
#
# comprehension:
# def num(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "hy you don't pass any args"
# nums=[1,2,3,4,5]
# print(num(2,*nums))
#
# kwargs:
# args return the answer in tuple and kwargs create in dictionary:
# def num(**kwargs):
#    print(kwargs)
# nums=[1,2,3,4,5]
# num(name="arslan",age=22)  #output:{'name': 'arslan', 'age': 22}
#
# def num(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
#
# num(name="arslan",age=22)
#
# unpacking the dictionary:
# def num(**kwargs):
#    print(kwargs)
# d={"name":"arslan","age":22}
# num(**d)     #output :{'name': 'arslan', 'age': 22}
#
# def func(l,**kwargs):
#      if kwargs.get("revers"):
#         return [i[::-1].title() for i in l]
#      else:
#         return [i.title() for i in l]
# l=["arham","madam","arslan"]
# print(func(l,revers=True))     #output:['Mahra', 'Madam', 'Nalsra']
#
# names=["arslan","arham","abid"]
# length=list(map(len,names))
# print(length)
# for i in length:
#     print (i)        #outpu:[6,5,4]
#
#
# lambda function:
# simple function:
# def add(a,b):
#     return a+b
# print(add(2,4)) #output:6
# upper programme is right but if numbers given in parameters are
# increase then this programme not work correctly so, for this
# we want to use lambda it auto go to function and perform the task
#
# with lambda:
#
# add=lambda a,b:a+b
# print(add(2,3)) #output :5
# output will be same but method are different.
# after the colon we tell that what is we want to return and
# before the colon we say that what we want to pass in the parameters.
#
#
#
# simple function:
# def avg(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average
# print(avg([1,2,3],[4,5,6],[7,8,9]))   #output:[4.0, 5.0, 6.0]
#
# Advance functions:
# average=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
# print(average([1,2,3],[4,5,6],[7,8,9]))    #output:[4.0, 5.0, 6.0]
#
# both have same output but there are many shortness in upper programme.
#
#
#
#
#
#
# Exersice:
#
#
#
# Task 1: Square Numbers using map() and lambda
#
# map and lambda:
# def square(a):
#     return a*a
# num=[1,2,3,4,5,6,7,9,10]
# square=list(map(square,num))
# print(square)
#
# 02:Write a Python program that filters out only
# the even numbers from a given list using filter() and lambda.
#
# simple :
# def even(a):
#     return a%2==0
# num=[1,2,3,4,5,6]
# l=list(filter(even,num))
# print(l)       #output:[2, 4, 6, 8]
#
# using filter and lambda:
# num=[1,2,3,4,5,6,7,8]
# l=list(filter(lambda a:a%2==0,num))
# print(l)         #output:[2, 4, 6, 8]
#
# filter and lambda:
# num=[1,2,3,4,5,6,7,8,9,10]
# even_num=list(filter(lambda x :x%2==0,num))
# print(even_num)         #output:[2, 4, 6, 8, 10]
#
# filter and lambda:
# num=[24,54,34,76,87,98,12,34,56]
# numbers=list(filter(lambda x:x>35,num))
# print("student which are pass in the exam:",numbers)
#
# map and lambda:
# num=[1,2,3,4,5,6,7,8,9]
# square=list(map(lambda x:x**2,num))
# print(square)
#
# Task 3: Add Corresponding Elements using zip() and map()
# Write a Python program that takes two lists of the
# same length and returns a new list containing the sum of corresponding elements using zip() and map().
#
# map , lambda  and zip:
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# result = list(map(lambda x: x[0] + x[1], zip(list1, list2)))
# print(result)
#
# with simple :
# def num(a):
#     return a**2
# nums=[1,2,3,4,5,6]
# l=list(map(num,nums))
# print(l)        #output:[1, 4, 9, 16, 25, 36]
#
# list ,map and lambda:
# num=[1,2,3,4,5,6]
# square=list(map(lambda x:x**2,num))
# print(square)           #output:[1, 4, 9, 16, 25, 36]
#
# lambda,list and map:
# in upper case:
# word={1:"hello world",2:"goodbye moon",3:"welcome the sun"}
# cap_word=list(map(lambda x:x.upper(),word.values()))
# print(cap_word)        #output:['HELLO WORLD', 'GOODBYE MOON', 'WELCOME THE SUN']
#
# lambda,list and map:
# title:
# word={1:"hello world",2:"goodbye moon",3:"welcome the sun"}
# cap_word=list(map(lambda x:x.title(),word.values()))
# print(cap_word)   #output:['Hello World', 'Goodbye Moon', 'Welcome The Sun']
#
# zip function
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# l=list(zip(list1,list2))
# print(l)   output:[(1,6),(2,7),(3,8)..........]
#
#
# zip function full name:
# list1 = ["abdul","abdul","haseeb","hafiz"]
# list2 = ["rehman","wasy","ghafar","waqar"]
#
# result = list(map(lambda x: x[0].title() + x[1].title(), zip(list1, list2)))
# print(result)
#
# 10. zip() with More than Two Lists
# Question:
# Given three lists:
# list1 = [10, 20, 30]
# list2 = [1, 2, 3]
# list3 = [5, 10, 15]
#
# Write a program that uses zip() to calculate the sum of corresponding elements from the three lists.
#
# list1 = [10, 20, 30]
# list2 = [1, 2, 3]
# list3 = [5, 10, 15]
# result=(list(map(lambda x: x[0]+x[1]+x[2],zip(list1,list2,list3))))
# print(result)
#
# write code for three list and print there first and then all the left string add all three:
# list1 = ["rao ","rao ","muhammad "]
# list2= ["abdul","abdul","haseeb ","hafiz "]
# list3 = ["_rehman","_wasy","ghafar ","waqar "]
# result=(list(map(lambda x: x[0].title()+x[1].title()+x[2].title(),zip(list1,list2,list3))))
# print(result)
#
# write code for two list and create dictinary:
#
# keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'New York']
# result = dict(zip(keys, values))
# print(result)
#
# 16. zip() and Conditionals
# Question:
# You are given two lists:
# list1 = [3, 8, 15, 20]
# list2 = [2, 6, 10, 25]
#
# Write a program to return a new list with the sum of corresponding elements from list1 and list2 only if the sum is even.
#
#
# list1 = [3, 8, 15, 20]
# list2 = [2, 6, 10, 25]
# # result=list(map(lambda x:x[0]+x[1],filter(lambda x: (x[0]+x[1])%2==0,zip(list1,list2))))
#
# # result = list(map(lambda x: x[0] + x[1], filter(lambda x: (x[0] + x[1]) % 2 == 0, zip(list1, list2))))
# # .list1 = [3, 8, 15, 20]
# # list2 = [2, 6, 10, 25]
# result = [x[0] + x[1] for x in zip(list1, list2) if (x[0] + x[1]) % 2 == 0]
# print(result)
#
#
# Keywords in python:
# import keyword
# print(keyword.kwlist)
# help("del")
#
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# from email.utils import UEMPTYSTRING
# from operator import indexOf

# Task programme:
#
# Task 01: Square Numbers using map and lambda
# Write a Python program that takes a list of numbers and returns a new list with each number squared.
#
# number=[1,2,3,4,5,6]
# l=list(map(lambda x:x**2,number))
# print("square of your list is: \n",l)
# print(type(l))                            #Output:square of your list is:
#                                                      [1, 4, 9, 16, 25, 36]
#                                                      <class 'list'>


# Task 02: Combine Two Lists using zip
# You have two lists:
#
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 78]
# l=list(zip(names,scores))
# print(l)                                 #Ouput:[('Alice', 85), ('Bob', 90), ('Charlie', 78)]


# Task 3: Filter Even Numbers using filter and lambda
# Write a program that filters out only the even numbers from a list using filter.
#
# numbers=[1,2,3,4,5,6,7,8,9,10]
# l=list(filter(lambda x: x%2!=0 ,numbers))
# print(l)                                                         #Output:[2,4,6,8,10]


# Task 4: Find Common Elements using zip and filter
# Given two lists:
#
# list1 = [1.0, 20, 30, 40]
# list2 = [1, 25, 30.0, 50]
# l=list(filter(lambda x: x[0]==x[1],zip(list1,list2)))
# print(l)                                                          #Output:[(1.0,1),(30,30.0)]


# Task 5: Convert Temperatures using map
# Convert a list of temperatures from Celsius to Fahrenheit using map.
# Formula: F=C×9/5+32
#
# celsius_temps = [0, 20, 30, 40]
# l=list(map(lambda x:x*9/5+32,celsius_temps))
# print(l)                                                          #Output:[32.0, 68.0, 86.0, 104.0]


# Task 6: Multiply Corresponding Elements using map and lambda
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# l=list(map(lambda x:x[0]*x[1],zip(list1,list2)))
 # print(l)                                                         #output:[6, 14, 24, 36, 50]


# Task 7: Find Lengths of Words using map and lambda
# words=["apple","banana","watermelon","pineapple","date","orange","grapes"]
# l=list(map(lambda x:len(x),words))
# print(l)                                                            #Output:[5, 6, 10, 9, 4, 6, 6]


# Task 8: Remove Negative Numbers using filter and lambda
# list1=[1,-2,3,4,-5,6,7,-8,9]
# l=list(filter(lambda x:x>0,list1))
# print(l)                                                             #Output:[1, 3, 4, 6, 7, 9]


#Task 10: Filter Words with More than 5 Letters using filter and lambda
# words=["apple","banana","watermelon","pineapple","date","orange","grapes"]
# l=list(filter(lambda x:len(x)>5,words))
# print(l)                                                             #Output:['banana', 'watermelon', 'pineapple', 'orange', 'grapes']


# Task 11: Calculate the Square Root of Each Number using map
# list1=[1,2,3,4,5,6,7,8,9]
# l=list(map(lambda x:x**2,list1))
# print(l)                                                            #Output:[1, 4, 9, 16, 25, 36, 49, 64, 81]


# Task 13: Find Maximum in Each Pair using map
# list1=[1,2,9,4,5]
# list2=[4,6,7,8,9]
# l=list(map(lambda x,y: max(x,y), list1,list2))
# print(l)
                                                                   #output:[4, 6, 9, 8, 9]

#Task 14: Remove Even Numbers from a List using filter and lambda
# list1=[1,2,3,4,5,6,7,8,9,10]
# l=list(filter(lambda x: x%2!=0,list1))
# print(l)                                                   #Output:[1, 3, 5, 7, 9]


#Task 15: Create Dictionary from Two Lists using zip
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 78]
# l=dict(zip(names,scores))
# print(l)                                                #Output:{'Alice': 85, 'Bob': 90, 'Charlie': 78}


# Task 16: Convert List of Strings to Uppercase using map
# list1=["rao muhammad nabi bakhas","rao muhammad shafi",
#        "rao muhammad iftikhar ahmad","rao muhammad abdul rehman","rao abdullah"]
# l=list(map(lambda x : x.upper(),list1))
# print(l)
                                       #output:['RAO MUHAMMAD NABI BAKHAS', 'RAO MUHAMMAD SHAFI',
                                       # 'RAO MUHAMMAD IFTIKHAR AHMAD', 'RAO MUHAMMAD ABDUL REHMAN', 'RAO ABDULLAH']

# Task 17: Check if All Numbers are Positive using filter and lambda

# list1 = [1, 2, -3, 4, 1]
# l=list(filter(lambda x:x<0,list1))
# print(len(l)==0)
                                         #output:False

#Task 21: Filter Names Starting with 'A' using filter and lambda
# names = ["Alice", "Bob", "Anna", "Charlie", "Amanda", "David"]
# l=list(filter(lambda x:x[0]=='A',names))
# print(l)
                                       #output:['Alice', 'Anna', 'Amanda']


# Task 22: Extract Odd-Indexed Elements using filter and lambda
# list1=[1,2,3,4,55,44,33,23,45,89]
# l = [x for i, x in enumerate(list1) if i % 2 == 0]
# print(l)
                     #output:[1, 3, 55, 33, 45]


# task
# List of numbers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5
# seen = {}
# for i, value in enumerate(nums):
#     difference = target - value
#     if difference in seen:
#         print(f"{difference} + {value} = {target}")
#         print(f"Indices are: {seen[difference]} and {i}")
#         break # Stop after finding the first pair
#     seen[value] = i
#
#
# num=[1,2,3,4,5,6,7,8,9,10]
# target=5
# for i in range(len(num)):
#     for k in range(i+1,len(num)):
#         if num[i]+num[k]==target:
#             print(num[i],"+",num[k],"=",target)
#             print("index is:",i," and ",k)
#
#     break


# help("lambda")
#
# # def modify_list(lst):
# #     lst.append(4)  # Modifies the original list
# #     print("Inside function:", lst)
# my_list = [1, 2, 3]
# modify_list(my_list)
# print("Outside function:", my_list)  # Output: [1, 2, 3, 4] (Modified)

# list1=[1,2,3,4,5]
# list2=[5,3,2,1,4,6]
# list1.extend(list2)
# list1=sorted(set(list1))
# print(list1)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 3, 2, 1, 4, 6]
 # Merge both lists
list1.extend(list2)

# Remove duplicates using list comprehension
l = []
 [l.append(x) for x in list1 if x not in l]
# Sort the list
l.sort()

print(l)

