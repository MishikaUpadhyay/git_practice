p=int(input("enter principal amount:"))
r=int(input("enter rate of interest:"))
t=int(input("enter time:"))
S=p*r*t/100
print("simple interest:",S)
total=p+S
emi=total/t
print("EMI=",emi)
