from tkinter import * 

root = Tk()

root.title("Calculator")

input = Entry(root, borderwidth=0, fg="blue", font=("Roboto",24))
input.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=0, ipady=20)

def button_click(char):
    string = input.get()
    input.delete(0,END)
    input.insert(0,string+str(char))

def all_clear():
    input.delete(0,END)

def delete():
    string = input.get()
    string = string.rstrip(string[-1])
    input.delete(0,END)
    input.insert(0,string)

def equal():
    string = input.get()
    input.delete(0,END)
    input.insert(0, eval(string))


img_1 = PhotoImage(file='images/n1.png')
img_2 = PhotoImage(file='images/n2.png')
img_3 = PhotoImage(file='images/n3.png')
img_4 = PhotoImage(file='images/n4.png')
img_5 = PhotoImage(file='images/n5.png')
img_6 = PhotoImage(file='images/n6.png')
img_7 = PhotoImage(file='images/n7.png')
img_8 = PhotoImage(file='images/n8.png')
img_9 = PhotoImage(file='images/n9.png')
img_0 = PhotoImage(file='images/n0.png')
img_00 = PhotoImage(file='images/n00.png')

img_ac = PhotoImage(file='images/ac.png')
img_del = PhotoImage(file='images/del.png')
img_mod = PhotoImage(file='images/mod.png')
img_div = PhotoImage(file='images/div.png')

img_mul = PhotoImage(file='images/mul.png')
img_sub = PhotoImage(file='images/sub.png')
img_add = PhotoImage(file='images/add.png')
img_dot = PhotoImage(file='images/eq.png')


img_eq = PhotoImage(file='images/img_eq.png')




b_all_clear = Button(root, image=img_ac, bg='white', borderwidth=0, command=all_clear)
b_backspace = Button(root, image=img_del,bg = 'white',borderwidth=0, command=delete)
b_modulus = Button(root,image=img_mod, bg='white',borderwidth=0, command=lambda : button_click('%'))
b_div = Button(root,image=img_div, bg='white',borderwidth=0, command=lambda : button_click('/'))

b_7 = Button(root,image=img_7, bg='white', borderwidth=0, command=lambda : button_click('7'))
b_8 = Button(root,image=img_8, bg='white',borderwidth=0, command=lambda : button_click('8'))
b_9 = Button(root,image=img_9, bg='white',borderwidth=0, command=lambda : button_click('9'))
b_mul = Button(root,image=img_mul, bg='white',borderwidth=0, command=lambda : button_click('*'))

b_4 = Button(root, image=img_4, bg='white', borderwidth=0, command=lambda : button_click('4'))
b_5 = Button(root,image=img_5, bg='white',borderwidth=0, command=lambda : button_click('5'))
b_6 = Button(root,image=img_6, bg='white',borderwidth=0, command=lambda : button_click('6'))
b_sub = Button(root,image=img_sub, bg='white',borderwidth=0, command=lambda : button_click('-'))

b_1 = Button(root,image=img_1, bg='white' , borderwidth=0, command=lambda : button_click('1'))
b_2 = Button(root,image=img_2, bg='white',borderwidth=0, command=lambda : button_click('2'))
b_3 = Button(root,image=img_3, bg='white',borderwidth=0, command=lambda : button_click('3'))
b_plus = Button(root,image=img_add, bg='white',borderwidth=0, command=lambda : button_click('+'))

double_zero = Button(root,image=img_00, bg='white', borderwidth=0, command=lambda : button_click('00'))
b_0 = Button(root, image=img_0, bg='white', borderwidth=0, command=lambda : button_click('0'))
b_dot = Button(root, image=img_dot, bg='white',borderwidth=0,command=lambda : button_click('.'))
b_equal = Button(root,image=img_eq, bg='white' ,borderwidth=0,command=lambda : equal())

#show the Buttons 

b_all_clear.grid(row=1, column=0)
b_backspace.grid(row=1, column=1)
b_modulus.grid(row=1, column=2)
b_div.grid(row=1, column=3)

b_7.grid(row=2, column=0)
b_8.grid(row=2, column=1)
b_9.grid(row=2, column=2)
b_mul.grid(row=2, column=3)

b_4.grid(row=3, column=0)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_sub.grid(row=3, column=3)

b_1.grid(row=4, column=0)
b_2.grid(row=4, column=1)
b_3.grid(row=4, column=2)
b_plus.grid(row=4, column=3)

double_zero.grid(row=5, column=0)
b_0.grid(row=5, column=1)
b_dot.grid(row=5, column=2)
b_equal.grid(row=5, column=3)
root.mainloop()


