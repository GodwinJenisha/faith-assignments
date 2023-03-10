
'''	Given an positive integer n, if you apply the following rules iteratively, you will eventually get a 1.
n---> n/2 (if n is even)
n---> 3*n+1 (if n is odd)
for example input 13
[13, 40, 20, 10, 5, 16, 8, 4, 2, 1]'''
'''
def generate_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

n = 13
sequence = generate_sequence(n)
print(sequence)
'''






'''	A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
I. At least 1 letter between [a-z]
II. At least 1 number between [0-9]
III. At least 1 letter between [A-Z]
IV. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1, a F1#,2w3E*, 2We3345
Then, the output of the program should be:
ABd1234@1'''
'''
import re
def validate_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

passwords = input("Enter passwords separated by commas:")

password_list = passwords.split(",")

valid_passwords = []
for password in password_list:
    password = password.strip()
    if validate_password(password):
        valid_passwords.append(password)
print(",".join(valid_passwords))

'''







'''	The denominations in Indian currency are: |1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000. Given an amount N, print how many coins/notes make up N Sample input: Enter the amount: 2640 Output: 
               2000  1
               500  1 
               100  1 
               10    4 
             Also test your program with N=3781, 4928, and 5134'''

'''
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
ammount = int(input("Enter the ammount:"))
result = {}
for d in denominations:
    count = ammount // d
    if count > 0:
       result[d] = count
       ammount -= count * d
for d, count in result.items():
    print(f"{d} {count}")

'''

# Create a simple calculator GUI app using TKinter framework.



import tkinter as tk
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create a text entry field for the calculator
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)

        # Create clear button
        self.create_button('C', 5, 0, columnspan=2)
        self.create_button('AC', 5, 2, columnspan=2)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, padx=10, pady=5,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.display.delete(-1)
        elif text == 'AC':
            self.display.delete(0, tk.END)
        elif text == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
calculator = CalculatorApp(root)
root.mainloop()






