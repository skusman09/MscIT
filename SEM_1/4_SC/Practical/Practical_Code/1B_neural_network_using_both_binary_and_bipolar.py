# B:- Calculate the o/p of neural network of both Binary and Bipolar

n=int(input("Enter the number of input neurons: "))
w=[]
x=[]
for i in range(0,n):
    a=float(input("Enter the input: "))
    x.append(a)
    b=float(input("Enter the weight: "))
    w.append(b)
print("The weight given are: ",w)
print("The given inputs are: ",x)
y=0.0
for i in range(0,n):
    y=y+(w[i]*x[i])
print("The net input is: ",round(y,3))