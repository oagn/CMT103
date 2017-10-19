# CMT103 Wk1, task 1
# times_3_num.py
# This program asks for three numbers, multiplies them together and prints the result using string formatting.

name = input("Hi, what is your name? ") #Might as well be polite
print('Hello', name, '!')

print('Give me three numbers, I will multiply them together.')
a = float(input('Please enter the first number: '))
b = float(input('Please enter the second number: '))
c = float(input('Please enter the third number: '))

print('Here is the answer:  {0:.3f} x {1:.3f} x {2:.3f} is {3:.3f}'.format(a, b, c, a*b*c))

