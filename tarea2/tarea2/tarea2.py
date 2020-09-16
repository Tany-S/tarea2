s=int(input('ingrese los segundos que tardara en realizar la tarea:'))
print ('la tarea durara:')
x=int(input("segundos:"))
y=int(input('minutos:'))
z=int (input('hora:'))
if z>=1:
    c=z*3600
if y<=59:
    c1=y*60
c2=c+c1+x
if c2<=s:
    print('se puede realizar la tarea')
else:
    print('no se puede realizar la tarea')



