# name = input("Enter your name : ")
# age = int (input("Enter your age : "))

# print("Hello", name, "you are ", age , " years old!" )


# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# print("Sum : " , num1 + num2)
# print("Difference : " , num1 - num2)
# print("Product : " , num1 * num2)
# print("Quotient : " , num1 / num2)
# print(type(num1))




# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
# num3 = float(input("Enter one floating number : "))

# avg = float((num1 + num2 + num3)/3)
# print(avg)

# question no 4
'''
num = str(input("Enter number : "))

an_integer = int(num)
a_float = float(num)
a_string = str(num)
print("Type of num : ", type(num))
print("Integer : " , an_integer, " Type : " , type(an_integer))
print("Float : " , a_float, " Type : " , type(a_float))
print("String : " , a_string, " Type : " , type(a_string))
'''

# Question no 5

# print(10+3*2**2)



# Question 6
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print(num1, num2)

temp = num1
num1 = num2
num2 = temp

print(num1, num2)
'''


# Question no 7
'''
celsius = float(input("Enter temperature in Celsius : "))
farenheit = (celsius * (9/5)) + 32
print (farenheit)
'''

# Question no 8
''' 
r = float(input("Enter radius : "))
PI = 3.14
area = PI * r*r
print(area)
'''
# Question no 9
'''
p = float(input("Enter principal : "))
r = float(input("Enter rate : "))
t = float(input("Enter time : "))

si = (p*r*t)/100
print(si)
'''
# Question no 10
'''
num = float(input("Enter : "))

int_part = int(num)
fractional_part = num - int_part

print("integer part : ", int_part)
print("fractional part : ", fractional_part)
'''
# Question no 10 another approach
num = input("Enter  num : ")
part = num.split(".")
print("Integer part : ", part[0])
print("fraciional part : ", part[1])