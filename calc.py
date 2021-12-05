from tkinter import *
root = Tk()
root.title("simple calculater")
e=Entry(root, width = "20" , borderwidth=2)
e.grid(row =0, column =0, columnspan=3,padx=10,pady=10)

def get_button(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def bt_clear():
    e.delete(0,END)
def add():
  first_num = e.get()
  global f_num
  global operation
  operation="add"
  f_num=int(first_num)
  e.delete(0,END)
def multiply():
  first_num = e.get()
  global f_num
  global operation
  operation="multiply"
  f_num=int(first_num)
  e.delete(0,END)
def sub():
  first_num = e.get()
  global f_num
  global operation
  operation="subtract"
  f_num=int(first_num)
  e.delete(0,END)
def divide():
  first_num = e.get()
  global f_num
  global operation
  operation="divide"
  f_num=int(first_num)
  e.delete(0,END)


def bt_equal():
    second_num =int(e.get())
    e.delete(0, END)
    if operation=="add":
       e.insert(0, f_num+second_num)
    elif operation=="subtract":
       e.insert(0, f_num-second_num)
    elif operation == "divide":
       e.insert(0, f_num / second_num)
    elif operation=="multiply":
      e.insert(0, f_num * second_num)

# Define buttons
b1= Button(root, text="1" , padx=40, pady=20 , command=lambda:get_button(1))
# we cant give arguements in command ,so used lambda function
b2= Button(root, text="2" , padx=40, pady=20 , command= lambda:get_button(2))
b3= Button(root, text="3" , padx=40, pady=20 , command=lambda:get_button(3))
b4= Button(root, text="4" , padx=40, pady=20 , command=lambda:get_button(4))
b5= Button(root, text="5" , padx=40, pady=20, command=lambda:get_button(5))
b6= Button(root, text="6" , padx=40, pady=20, command=lambda:get_button(6))
b7= Button(root, text="7" , padx=40, pady=20, command=lambda:get_button(7))
b8= Button(root, text="8" , padx=40, pady=20, command=lambda:get_button(8))
b9= Button(root, text="9" , padx=40, pady=20, command=lambda:get_button(9))
b0= Button(root, text="0" , padx=40, pady=20, command=lambda:get_button(0))
b_add =Button(root, text="+" , padx=39, pady=20,command= add )
b_equalto =Button(root, text="=" , padx=90, pady=20,command=bt_equal )
b_clr = Button(root, text="clear" , padx=80, pady=20,command=bt_clear )
b_sub = Button(root,text="-",padx=40,pady=20,command=sub)
b_div = Button(root,text="/",padx=40,pady=20,command=divide)
b_multiply = Button(root,text="*",padx=40,pady=20,command = multiply)
#position of buttons

b1.grid(row =3 , column=0)
b2.grid(row =3 , column=1)
b3.grid(row =3 , column=2)

b4.grid(row =2, column=0)
b5.grid(row =2 , column=1)
b6.grid(row =2 , column=2 )

b7.grid(row =1 , column=0 )
b8.grid(row =1 , column=1 )
b9.grid(row =1 , column= 2)

b0.grid(row =4 , column=0 )

b_add.grid(row = 5 , column=0 )
b_equalto.grid(row = 5, column=1 , columnspan=2  )
b_clr.grid(row =4 , column=1,columnspan=2 )

b_sub.grid(row =6 , column=0 )
b_div.grid(row =6, column=1 )
b_multiply.grid(row =6 , column= 2)




root.mainloop()