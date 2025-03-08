from tkinter import *#1 this modula is for making the window
import math#13

def click(value):#10 this for clicking function
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:

        if value == 'C':#11 this id for the button c as iff will slice the string as deleting the last digit
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)#this will first delet all writen
            entryField.insert(0, ex)#and the again paste it bu deletig the last digit
            return

        elif value == 'CE':#12 now for ce
            entryField.delete(0, END)#this will clear all the inction

        elif value == '√':#13for squer root method
            answer = math.sqrt(eval(ex))#this will get the squere root of the number writeng getting outform the module math

        elif value == 'π':#14 return the pi value
            answer = math.pi

        elif value == '2π':#15 multiply the pi value by 2
            answer = 2 * math.pi

        elif value == chr(8731):#16 gives the cube root of value
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # gives the c too the power y value
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3': # give the cube
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':# give the squre
            answer = eval(ex) ** 2

        elif value == 'ln':# gives the value of log
            answer = math.log2(eval(ex))

        elif value == 'log₁₀':#gives the log 10 value
            answer = math.log10(eval(ex))

        elif value == 'x!':#gives the factorial
            answer = math.factorial(ex)

        elif value == chr(247):  #for thhe division
            entryField.insert(END, "/")
            return

        elif value == '=': #for the result
            answer = eval(ex)

        else:#for the number counts
            entryField.insert(END, value)
            return

        entryField.delete(0, END)#after clicing the functions the eval function will auto mate the system
        entryField.insert(0, answer)

    except SyntaxError:#iff there any sinter error it will pass this is because if we click any function without any nreult itt wii show error
        pass

root = Tk()
root.title('Bunnyulator')#2 title for the window
root.config(bg='black')#3 color for window
root.geometry('680x486+100+100')#4 dimention

entryField = Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, relief=SUNKEN, width=30)#5 entry area
entryField.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "√", "+", "π", "θ-θ", "θ-θ", "θ-θ",
                    "1", "2", "3", "-", "2π", "θ-θ", "θ-θ", "θ-θ",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "θ-θ", "θ-θ", "θ-θ",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]#7for all the buttons
rowvalue = 1
columnvalue = 0
for i in button_text_list:#8 for placing the buttons

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                    font=('arial', 18, 'bold'), activebackground='black', command=lambda button=i: click(button))#6 for the buttons
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop() #this is main function call