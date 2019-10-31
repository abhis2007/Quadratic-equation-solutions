from math import sqrt
print("Please provide cofficient of your desired equation in form of a*x^2+b*x+c")
print("ENTER a,b,c")
a=input()
b=input()
c=input()
d=(int(b)*int(b)-4*int(a)*int(c))
if d<0:
 print("oops! your roots'r imaginary")
 print("Discriminant of your desired equation=",d)
 v=sqrt(int(-d));
 print("Under root of discriminant",v,"i")
 #y=v/(int(a)*2) it is (√d/2a)
 y=((-(int(b)))/(int(a)*2))
 #print(int(y)) it is b/2
 z=v/(int(a)*2)
 print("Your first root=",y,"+",z,"i")
 print("And other root= ",y,"-",z,"i")
 #print(y,"+",z)
 #print(y,"-",z)
 #print(z)
 #print(int(v)/(int(a)*2),"i")
else:
 g=sqrt(int(d));
 print("Discriminant of your desired equation=",d)
 k=-int(b)+int(g)
 n=int(a)*2
 m=int(k)/int(n)

 p=-int(b)-int(g)
 t=int(p)/int(n)

 if m==t:
  print(m or t)
 else:
  print("Your first root=",m)
  print("And other root= ",t)
