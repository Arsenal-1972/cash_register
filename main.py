#
# Kases aparāts
#
# 0.5pt pievienot jaunu preci - nosaukumu un cenu
#     0.5pt preces nosaukumam jābūt no 2 līdz 120 simboliem (jābūt validācijai, rādīt paziņojumu ja neder)
#     0.5pt preces cenai jābūt veselam skaitlim vai daļskaitlim ar vērtību no 0 līdz 9999 (jābūt validācijai, rādīt paziņojumu ja neder)
# 0.5pt dzēst preci pēc kārtas numura
# 0.5pt atcelt ievadu / iztukšot preču sarakstu
# 0.5pt piemērot atlaidi, ievadīt summu procentos
# 0.5pt samaksāt, ja iedota lielāka summa - izdrukāt atlikumu
# 0.5pt izdrukāt čeku uz ekrāna - preces nosaukumus un summas
#     0.5pt izdrukāt piemēroto atlaidi (ja ir)
#     0.5pt izdrukāt kopējo summu

# 1pt programmas stāvoklis tiek glabāts JSON faila un programmas sākumā tiek ielasīts un beigās saglabāts
# 1pt kodam ir jēdzīgi komentāri, pirms "if, for, while" koda konstrukcijam
# 1pt koda palaišanas brīdī nerādās kļūdas
# 1pt mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# 1pt izmaiņas saglabātas versiju vadības sistēmā Git, savs fork
#
# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
#
import json

products_and_prices= []
#atver products_and_prices kā mainīgo
with open('products_and_prices.json', 'r') as openfile:
    products_and_prices = json.load(openfile)

while True: #Kamēr darbosies programma varēs izpildīt zemaprakstītas darbības
    print('1. Ievadīt produkta nosaukumu un cenu')
    print('2. Dzēst preci no produkta saraksta')
    print('3. Iztukšot preču sarakstu')
    print('4. Pievienot atlaidi')
    print('5. Izdrukāt čeku')
    print('6. Iziet no programmas')
    choice = input('Izvelēties operāciju:')#operācijas izvelēšana
    
    if choice == '1':# Pievieno produktu sarakstam
        Preces_nosaukums = input('Ievadiet preces nosaukumu:')
        Preces_cena = input('Ievadiet preces cenu:')
        Atlaide = input('Ievadiet preces atlaidi:')
        saraksts = {'Preces nosaukums': Preces_nosaukums, 'Preces cena': Preces_cena, 'Preces atlaide': Atlaide}
        products_and_prices.append(saraksts)
    elif choice == '2':#Izdzēš tikai izveleto produktu
        id = int(input('Ievadiet preces indeksu:'))
        products_and_prices.pop(id)
    elif choice == '3':#Izdzēš sarakstu ar produktiem
        products_and_prices.clear()
    elif choice == '4':#nestrādā
        id = int(input('Ievadiet preces indeksu:'))
        preces_summa_ar_atlaidi = int('Preces cena'[id])*int('Preces atlaide'[id])/100
        print(preces_summa_ar_atlaidi)
    elif choice == '5':#Izprintē čeku
        print(products_and_prices)
    elif choice == '6': # Šī funkcija izslēdz programmu saglabajot ievaditus datus
        print('Exiting...')
        break
    else: # Rāda, ka ir skaitlis, kura nav operācijas izvelēšanā
        print('Invalid choice. Please try again.')

with open("products_and_prices.json", "w") as outfile:#pievieno mainīgo products_and_prices json failā
    json.dump(products_and_prices, outfile)