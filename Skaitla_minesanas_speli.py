from random import randint
print('Datorspele\'Uzmini skaitli\'.')
print('Dators "iedomajas" veselo skaitli no 1 lidz 10.', end='\n\n')
print('Uzminiet skaitli')
Datora_skaitlis = randint(1,10)

neuzmineja=True
while neuzmineja:
    ievade= input('Ievadiet skaitli no 1 lidz 10, ieskaitot 10: ')
    Cilveka_skaitlis = int(ievade)
    if Datora_skaitlis < Cilveka_skaitlis:
        print('Neuzminejat. Ievadiet mazaku skaitli.')
    else:
        if Datora_skaitlis > Cilveka_skaitlis:
            print('Neuzminejat. Ievadiet lielaku skaitli.')
        else:
            neuzmineja=False

print('Uzmenejat!!!!')
