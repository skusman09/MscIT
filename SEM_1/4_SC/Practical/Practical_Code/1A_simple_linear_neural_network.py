# A:- Aim: Design a simple neural network model

# w,b,x takes the value of weight, bias and input respectively
w = float(input("Enter the value for weight: "))
b = float(input("Enter the value for bias: "))
x = float(input("Enter the value for input: "))

# The net input is calculated with the formula yin = b + wx
print("The net input (yin): ")
yin = float(b + (w * x))
print(yin)