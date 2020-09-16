a=float (input())
b=float (input())
c=float (input())
if a!=0 and b!=0 and c!=0:
    x1=(-b+((b**2)-(4*a*c))**(1/2))/(2*a)
    x2=(-b-((b**2)-(4*a*c))**(1/2))/(2*a)
    print (x1, x2)
else:
    print ('no hay solucion')
