# Python program to create a simple GUI
# calculator using Tkinter

# import everything from tkinter module
# from math import exp
import tkinter as tk  # library

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to delete last n char
def backspace():
    global expression

    expression = expression[:-1]  # ?
    equation.set(expression)

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(gui)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Nama Kelompok")
 
    # sets the geometry of toplevel
    newWindow.geometry("280x220")
 
    # A Label widget to show in toplevel
    tk.Label(newWindow,
          text ="Kelas: B\nKelompok: 2\n\nAnggota:\n\n1. Mohammad Ernico Suryo Wicaksono\n2. Budianto\n3. Joshua Fernaldy Sudarsono\n4. Ni Made Rai Nirmala Santhi\n5. Utoro Ardiyatno\n6. M. Faiz Triputra\n7. Samuel Aprilius Efendi\n8. Jauzaa Maylia Suhendro\n"
			).pack()
	
	
# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
        # print(total)
        equation.set(total)

        # initialize the expression variable
        # by empty string
        # expression = ""
        expression = total

    # if error is generate then handle
    # by the except block
    except Exception as e:
        print(e)
        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear_box():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window

    gui = tk.Tk()

    # set the background colour of GUI window
    gui.configure(background="#E3EFDB")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("275x220")

    # tk.StringVar() is the variable class
    # we create an instance of this class
    equation = tk.StringVar()

    # create the text entry box for
    # showing the expression .
    # expression_field = tk.Entry(gui, textvariable=equation)
    expression_field = tk.Entry(gui, textvariable=equation)
    expression_field.grid(
        rowspan=2, column=0, columnspan=5, sticky="E", ipadx=70, padx=3
    )  #

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .

    button1 = tk.Button(
        gui,
        text=" 1 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(1),
        height=1,
        width=7,
    )
    button1.grid(row=2, column=0, pady=2)

    button2 = tk.Button(
        gui,
        text=" 2 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(2),
        height=1,
        width=7,
    )
    button2.grid(row=3, column=0)

    button3 = tk.Button(
        gui,
        text=" 3 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(3),
        height=1,
        width=7,
    )
    button3.grid(row=4, column=0, pady=2)

    button4 = tk.Button(
        gui,
        text=" 4 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(4),
        height=1,
        width=7,
    )
    button4.grid(row=2, column=1)

    button5 = tk.Button(
        gui,
        text=" 5 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(5),
        height=1,
        width=7,
    )
    button5.grid(row=3, column=1)

    button6 = tk.Button(
        gui,
        text=" 6 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(6),
        height=1,
        width=7,
    )
    button6.grid(row=4, column=1)

    button7 = tk.Button(
        gui,
        text=" 7 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(7),
        height=1,
        width=7,
    )
    button7.grid(row=2, column=2)

    button8 = tk.Button(
        gui,
        text=" 8 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(8),
        height=1,
        width=7,
    )
    button8.grid(row=3, column=2)

    button9 = tk.Button(
        gui,
        text=" 9 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(9),
        height=1,
        width=7,
    )
    button9.grid(row=4, column=2)

    button0 = tk.Button(
        gui,
        text=" 0 ",
        fg="black",
        bg="#FFC000",
        command=lambda: press(0),
        height=1,
        width=7,
    )
    button0.grid(row=5, column=0 , pady=2)

    multiply = tk.Button(
        gui,
        text=" * ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("*"),
        height=1,
        width=7,
    )
    multiply.grid(row=4, column=3)

    minus = tk.Button(
        gui,
        text=" - ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("-"),
        height=1,
        width=7,
    )
    minus.grid(row=3, column=3)

    plus = tk.Button(
        gui,
        text=" + ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("+"),
        height=1,
        width=7,
    )
    plus.grid(row=2, column=3)

    divide = tk.Button(
        gui,
        text=" / ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("/"),
        height=1,
        width=7,
    )
    divide.grid(row=5, column=3, pady=2)

    equal = tk.Button(
        gui, 
		text=" = ", 
		fg="black", 
		bg="#FFC000", 
		command=equalpress, 
		height=1, 
		width=7
    )
    equal.grid(row=6, column=3)

    kurangi = tk.Button(
        gui, text=" <- ", fg="black", bg="#FFC000", command=backspace, height=1, width=7
    )
    kurangi.grid(row=5, column=2, pady=2)

    clear = tk.Button(
        gui,
        text="Clear",
        fg="black",
        bg="#FFC000",
        command=clear_box,
        height=1,
        width=7,
    )
    clear.grid(row=5, column=1, pady=2)

    Decimal = tk.Button(
        gui,
        text=".",
        fg="black",
        bg="#FFC000",
        command=lambda: press("."),
        height=1,
        width=7,
    )
    Decimal.grid(row=6, column=2)

    eksponen = tk.Button(
        gui,
        text=" X^n ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("**"),
        height=1,
        width=7,
    )
    eksponen.grid(row=6, column=0)

    modulus = tk.Button(
        gui,
        text=" % ",
        fg="black",
        bg="#FFC000",
        command=lambda: press("%"),
        height=1,
        width=7,
    )
    modulus.grid(row=6, column=1)

    eksponen2 = tk.Button(
        gui,
        text=" X^2 ",
        fg="black",
        bg="#FFC000",
        command=lambda: [press("**2"),equalpress()],
        height=1,
        width=7,
    )
    eksponen2.grid(row=7, column=0)

    eksponen3 = tk.Button(
        gui,
        text=" X^3 ",
        fg="black",
        bg="#FFC000",
        command=lambda: [press("**3"),equalpress()],
        height=1,
        width=7,
    )
    eksponen3.grid(row=7, column=1)

    credit = tk.Button(
        gui,
        text=" Kelompok ",
        fg="black",
        bg="#FFC000",
        command=openNewWindow,
        height=1,
        width=7,
    )
    credit.grid(row=8, column=3)
    # start the GUI
    gui.mainloop()
