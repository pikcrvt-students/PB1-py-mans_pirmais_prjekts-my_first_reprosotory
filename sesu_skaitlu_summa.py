""" Sešu skaitļu summa
    Izveidoja: Artjoms Jablonskis
"""
print('Sešu skaitļu summas aprēķināšana.')
print()

sum=0
for x in range(6):
    sum+=int(input('Ievadiet' + str(x+1) + '. veselo skaitli: '))

print('\nSumma ir', sum)
