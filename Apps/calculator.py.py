from tkinter import *

first_num=second_num=operator=None

def get_digit(digit):
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_num,operator
    first_num=int(result_label['text'])
    operator=op
    result_label.config(text='')

def get_result():
    global first_num,second_num,operator
    second_num=int(result_label['text'])
    if operator=='+':
        result_label.config(text=str(first_num + second_num))
    elif operator=='-':
        result_label.config(text=str(first_num - second_num))

    elif operator=='*':
        result_label.config(text=str(first_num * second_num))

    else:
        if second_num==0:
            print("Error in this code.")
        else:
                result_label.config(text=str(first_num / second_num))
root=Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root, text='', bg='black', fg='brown')
result_label.grid(row=0, column=1,columnspan=25 ,pady=(50, 25),sticky='w')
result_label.config(font=('verdana', 30, 'bold'))

btn7 = Button(root, text='7', bg='#00a65a', fg='black',command=lambda :get_digit(7))
btn7.grid(row=1, column=1)
btn7.config(width=5, height=2, font=('verdana', 14))

btn8 = Button(root, text='8', bg='#00a65a', fg='black',command=lambda :get_digit(8))
btn8.grid(row=1, column=2)
btn8.config(width=5, height=2, font=('verdana', 14))

btn9 = Button(root, text='9', bg='#00a65a', fg='black',command=lambda :get_digit(9))
btn9.grid(row=1, column=3)
btn9.config(width=5, height=2, font=('verdana', 14))

btn_add = Button(root, text='+', bg='#00a65a', fg='black',command=lambda :get_operator('+'))
btn_add.grid(row=1, column=4)
btn_add.config(width=5, height=2, font=('verdana', 14))

btn4 = Button(root, text='4', bg='#00a65a', fg='black',command=lambda :get_digit(4))
btn4.grid(row=2, column=1)
btn4.config(width=5, height=2, font=('verdana', 14))

btn5 = Button(root, text='5', bg='#00a65a', fg='black',command=lambda :get_digit(5))
btn5.grid(row=2, column=2)
btn5.config(width=5, height=2, font=('verdana', 14))

btn6 = Button(root, text='6', bg='#00a65a', fg='black',command=lambda :get_digit(6))
btn6.grid(row=2, column=3)
btn6.config(width=5, height=2, font=('verdana', 14))

btn_sub = Button(root, text='-', bg='#00a65a', fg='black',command=lambda :get_operator('-'))
btn_sub.grid(row=2, column=4)
btn_sub.config(width=5, height=2, font=('verdana', 14))

btn1 = Button(root, text='1', bg='#00a65a', fg='black',command=lambda :get_digit(1))
btn1.grid(row=3, column=1)
btn1.config(width=5, height=2, font=('verdana', 14))

btn2 = Button(root, text='2', bg='#00a65a', fg='black',command=lambda :get_digit(2))
btn2.grid(row=3, column=2)
btn2.config(width=5, height=2, font=('verdana', 14))

btn3 = Button(root, text='3', bg='#00a65a', fg='black',command=lambda :get_digit(3))
btn3.grid(row=3, column=3)
btn3.config(width=5, height=2, font=('verdana', 14))

btn_mul = Button(root, text='*', bg='#00a65a', fg='black',command=lambda :get_operator('*'))
btn_mul.grid(row=3, column=4)
btn_mul.config(width=5, height=2, font=('verdana', 14))

btn_clr = Button(root, text='C', bg='#00a65a', fg='black',command=lambda:clear())
btn_clr.grid(row=4, column=1)
btn_clr.config(width=5, height=2, font=('verdana', 14))

btn0 = Button(root, text='0', bg='#00a65a', fg='black',command=lambda :get_digit(0))
btn0.grid(row=4, column=2)
btn0.config(width=5, height=2, font=('verdana', 14))

btn_equals = Button(root, text='=', bg='#00a65a', fg='black',command= get_result)
btn_equals.grid(row=4, column=3)
btn_equals.config(width=5, height=2, font=('verdana', 14))

btn_div = Button(root, text='/', bg='#00a65a', fg='black',command=lambda :get_operator('/'))
btn_div.grid(row=4, column=4)
btn_div.config(width=5, height=2, font=('verdana', 14))
root.mainloop()


root.mainloop()