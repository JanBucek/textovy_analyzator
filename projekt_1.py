#   projekt_1.py:   První projekt do Engeto Online Python Akademie

#   autor:          Jan Buček
#   email:          honzabuci@seznam.cz
#   discord:        Honza#1407


texts = [''' ''','''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
registrovani_uzivatele = dict()
pomocny_atribut = True
pomocny_atribut2 = True
vycistena_slova = list()
velka_pismena = list()
mala_pismena = list()
cisla = list()
titlecase_words = list()
cisla_hodnota = list()
oddelovac = '----------------------------------------'

#   naplním dictionary
registrovani_uzivatele['bob']   = '123'
registrovani_uzivatele['ann']   = 'pass123'
registrovani_uzivatele['mike']  = 'password123'
registrovani_uzivatele['liz']   = 'pass123'

#   print(registrovani_uzivatele)

#   smyčka, která zajistí naplnění přihlašovacích údajů (proměnných od uživatele)
while pomocny_atribut:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username in registrovani_uzivatele.keys() and password in registrovani_uzivatele.values():
        print (f'Welcome to app, {username}' + '\n' + 'We have 3 texts to be analyzed.')
        pomocny_atribut = False
    else:
        print('unregistered user, terminating the program..')

#   6. Pro vybraný text spočítá následující statistiky:
#      -    počet slov,
#      -    počet slov začínajících velkým písmenem,
#      -    počet slov psaných velkými písmeny,
#      -    počet slov psaných malými písmeny,
#      -    počet čísel (ne cifer),
#      -    sumu všech čísel (ne cifer) v textu.

while pomocny_atribut2:
    cislo_textu = input('Enter a number btw. 1 and 3 to select:')
    if cislo_textu is None or cislo_textu not in ('1','2','3'):
        print('Chybně zadaný údaj')
    else:
        for slovo in texts[int(cislo_textu)].split():
            ciste_slovo = slovo.strip(',.:;')
            vycistena_slova.append(ciste_slovo)
            if ciste_slovo.isupper() and ciste_slovo.isalpha(): 
                # naplní se list pro slova začínající velkým písmenem 
                velka_pismena.append(ciste_slovo)
            elif ciste_slovo.istitle():
                # naplní se list pro slova psaná velkými písmeny
                titlecase_words.append(ciste_slovo)
            elif ciste_slovo.islower() and ciste_slovo.isalpha():
                # naplní se list pro slova psaná malými písmeny
                mala_pismena.append(ciste_slovo)
            elif ciste_slovo.isdigit():
                # naplní se list pro čísla v textu
                cisla.append(ciste_slovo)
                cisla_hodnota.append(int(ciste_slovo))

        print(f'There are {len(vycistena_slova)} words in the selected text.')
        print(f'There are {str(len(titlecase_words))} titlecase words.')
        print(f'There are {str(len(velka_pismena))} uppercase words.')
        print(f'There are {str(len(mala_pismena))} lowercase words.')
        print(f'There are {str(len(cisla))} numeric strings.')
        print(f'The sum of all the numbers {str(sum(cisla_hodnota))}')
        pomocny_atribut2 = False

#   7. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto: 

#   Tento kód vytváří seznam délek slov (word_lengths), což znamená, že pro každé slovo v seznamu vycistena_slova je jeho délka přidána do seznamu word_lengths.
word_lengths = [len(word) for word in vycistena_slova]
#   Následně se vytvoří slovník frequency, kde klíčem jsou délky slov a hodnotou počet výskytů této délky v seznamu word_lengths.
frequency = {length: word_lengths.count(length) for length in set(word_lengths)}
print(oddelovac)
print('LEN|  OCCURENCES  |NR.')
print(oddelovac)
for length, count in sorted(frequency.items()):
    print("{:3d}|{:15}|{:2d}".format(length, "*"*count, count))

#   "{:3d}" znamená, že první sloupec (délka slova) má šířku 3 znaky. 
#   "{:15}" znamená, že druhý sloupec (hvězdičky) má délků 15 znaků. 
#   "{:2d}" znamená, že třetí sloupec (počet slov) má také šířku 2 znaků.
