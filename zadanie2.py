from math import*

# program 1
a=float(input('podaj a'))
b=float(input('podaj b'))
w=sqrt(7/(a**3+cos(b)))
print('wartosc wyrazenia',w)

# program 2
a=float(input('podaj a'))
b=float(input('podaj b'))
k=a**3+cos(b)*sqrt(a+b)
print('wartosc wyrazenia',k)

# program 3
a=float(input('podaj a'))
b=float(input('podaj b'))
z=fabs(a-b) +sin(a) *sqrt(a+b)
print('wartosc wyrazenia',z)

# program 4
a=float(input('podaj a'))
b=float(input('podaj b'))
h=(cos(a+1) /fabs(sqrt(5)-b) )
print('wartosc wyrazenia',h)
