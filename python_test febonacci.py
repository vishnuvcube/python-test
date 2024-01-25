num=int(input("enter the number: "))
x=0
y=1
z=0
print(x,y, end=",")
if num<=0:
    print("enter positive integer")
else:
    for i in range(2, num):
        z=x+y
        print(z, end="," )
        x=y 
        y=z 
