# program od sprawdzania liczby pazystej
print('program sprawdza czy podana liczba jest pazysta')
a=int(input('podaj liczbe '))

if a%2==0:
    print('liczba  jest pazysta')

elif a%2!=0 :
    print('liczba nie jest pazysta')

else:
    print('podany nieprawidlowy input')

# program od sprawdzania czy da sie zbudowac trojakat
print('program sprawdza czy z odcinkow o podanej dlugosci da sie zrobic trojkat')
a=int(input('podaj dlugosc boku a'))
b=int(input('podaj dlugosc boku b'))
c=int(input('podaj dlugosc boku c'))

if a+b>c and a+c>b and c+b>a:
    print('z podanych dlugosci da sie zbudowac trojkat')

else:
    print('z podanej dlugosci nie da sie zbudowac trojkata')