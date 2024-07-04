import mysql.connector
from CreateTable import *
def choiceDataBase(i):
    # Wybór bazy danych przez numer
    while True:
        try:
            z = int(input("\nWybierz baze daych (podaj numer):"))
            if z>0 and z<i+1:
                break
            else:
                print("nie ma takiej bazy o takim numerze")
        except:
            print("podaj liczbę, aby wybrać baze danych ")
    return z-1
def howManyTables(tables):
    # wybór użytkownika z ilu tabel Chce korzystać
    while True:
        try:
            a = int(input("\nZ ilu tabel chesz korzystac podczas zapytania? (podaj Liczbę): "))
            if a > 0 and a < len(tables) + 1:
                break
            elif a == 0:
                print("Nie podajesz rzadej tabeli to wyłącz program!")
            else:
                print("Nie ma tyle tabel w bazie")
        except:
            print("Proszę o liczbę a nie o \"wyraz\"! ")
    return a
def choiceTables(tables,a):
    # wybór użytkownika z jakich tabel Chce korzystać
    tablesForSelect = []
    while len(tablesForSelect) < a:
        print()
        i = 0
        for rekord in tables:
            i += 1
            helpStr = str(i) + " - " + rekord
            helpStr += " " * (35 - len(helpStr))
            if i % 2 == 0:
                print(helpStr)
            else:
                print(helpStr, end="")
        if i % 2 != 0:
            print()
        print()
        while True:
            try:
                q = int(input("Podaj, którą tabele chesz urzyć do zapytania "))
                if q <= len(tables) and q > 0:
                    print("Do zapytania dodano tabele:",tables[q-1])
                    tablesForSelect.append(tables[q-1])
                    del tables[q-1]
                    break
                else:
                    print("Nie ma takiej tabeli")
            except:
                print("Podaj liczbę")
    return tablesForSelect
def choiceAttributeForView(tabela):
    # Wybór artybutów z danej tabeli
    kwerenda = "describe "+tabela
    kursor.execute(kwerenda)
    help = [] # do wyboru i do późniejszch operacji
    help2 = [] # do wyświetlania
    for rekord in kursor.fetchall():
        help.append(tabela+"."+rekord[0])
        helpStr = " - " + rekord[0]
        helpStr += " " * (40 - len(helpStr))
        help2.append(helpStr)
    print("\n\t -> Podaj jakie atrybuty chesz wyświetlić z tabeli: "+tabela+" <-\n")
    i = 0
    for rekord in help2:
        i += 1
        if i % 2 == 0:
            print(str(i) + rekord)
        else:
            print(str(i) + rekord, end="")
    print(str(i+1) + " - Wyszystkie z podanych")
    while True:
        attribute = []
        try:
            s = input("Podaj atrybut/atrybuty po przecinku: ")
            s = s.replace(" ","")
            sH = s.split(",")
            if len(sH) == 1:
                if int(sH[0]) < 0 and int(sH[0]) > len(help2) + 1:
                    print("Nie ma takiego atrybutu")
                elif int(sH[0]) == len(help2) + 1:
                    attribute.append(tabela + ".*")
                    return attribute
                else:
                    attribute.append(help[int(sH[0]) - 1])
                    return attribute
            else:
                for z in sH:
                    z = int(z)
                    if z < 0 and z > len(help2)+1:
                        print("Nie ma takiego atrybutu")
                    else:
                        if help[z-1] in attribute:
                            print("Nie można podać 2 razy tej samej tabeli")
                        else:
                            attribute.append(help[z-1])
                            break
        except:
            print("Podaj poprawnie")
    return attribute
def comparisonOperator():
    # wybór operatora porównania
    print("\nPodaj ",end="")
    while True:
        z = input("operator porównania\n (wprowadź: >, <, <>, >=, <=, =  LIKE).")
        z = z.strip()
        if z == "<" or z == ">" or z == "<>" or z == "<=" or z == ">=" or z == "=":
            return " "+z+" "
        if z.upper() =="LIKE":
            return " "+z.upper()+" "
        else:
            print("Podaj ponownie ")
def valuesToCompare():
    x = input("\nPodaj warośc do porówania ")
    print()
    return "\""+x+"\""
def ComparisonCriterion(attributeForView):
    # --- Kryterum porówania ---
    print("\n\nWybierz pole, którego warośi będą kryterium wyszukiwania\n (wpisz numer",end="")
    print(")\t Możliwe pola do wyboru:")
    i = 0
    for rekord in attributeForView:
        i += 1
        helpStr = str(i) + " - " + rekord
        helpStr += " " * (35 - len(helpStr))
        if i % 2 == 0:
            print(helpStr)
        else:
            print(helpStr, end="")
    if i % 2 != 0:
        print()
    while True:
        try:
            c = input()  # Dziwne, nie działa int(input())
            c = int(c)
            if c <= 0 or c > len(attributeForView):
                print("Nie ma takiego Pola, Podaj ponownie")
            else:
                return c
        except:
            print("Podaj liczbę danego pola")
def ifLevel(level):
    """
        Level - TRUE => Poziom w dół
        Level - FALLSE => Poziom do góry
    """
    if level:
        levelStr = "zmniejszyć"
        levelStr2 = "zmniejszeniem"
    else:
        levelStr = "zwiększyć"
        levelStr2 = "zwiększeniem"
    print("Czy chesz ",levelStr," poziom logiczny? (podaj tak lub yes aby ",levelStr," poziom\n"
          " co kolwiek innego będzie powodowało nie ",levelStr2," poziomu")
    f = input()
    if f.lower() == "tak" or f.lower() == "yes":
        return True
    else:
        return False
def LevelLower(poziom):
    if(poziom == 1):
        return 1
    else:
        while True:
            try:
                print("O ile zmniejszyć poziom ligiczny?(obecny poziom: ",poziom," podaj liczbę)", end=" ")
                c = int(input(""))
                if c<=0 or c>poziom:
                    print("Nie możesz odjąć poziomu tak aby był na poziomie ujemnym")
                else:
                    return c

            except:
                print("podaj liczbę")
def logicalOperators():
    while True:
        f = input("\nPodaj operator logiczny AND lub OR ")
        if f.upper() == "OR" or f.upper() == "AND":
            print()
            return " "+f.upper()+" "
def WhereEnd():
    i  = input("Czy zakończyć działanie Selecta?\n\t(wpisz tak lub yes aby zakończyć, wszystko inne będzie traktowane jako kontynuacja) ")
    if i.lower() == "tak" or i.lower() == "yes":
        return True
    else:
        return False
def WhereMain(tablesForSelect5):
    attribute = []
    attributeForView = []
    for table in tablesForSelect5:
        kwerenda = "DESCRIBE "+table
        kursor.execute(kwerenda)
        for rekord in kursor.fetchall():
            attributeForView.append(rekord[0])
            attribute.append(table+"."+rekord[0])
    if len(tablesForSelect5) != 1:
        attributeForView = attribute
    help1 = WhereEnd()
    if help1:
        return ""
    else:
        if len(tablesForSelect5) == 1:
            Select = "WHERE "
        else:
            Select = " AND "
        poziom = 0  # "poziom logiczny "
        print("\n\t => POZIOM LOGICZNY PRZYKŁAD <=")
        print(" SELECT * FROM Tabela WHERE Warunek_1 OR/AND (Warunek_2 OR/AND (Warunek_3 OR/AND Warunek_4))")
        print("\t Warunek_1 - poziom logiczny 0")
        print("\t Warunek_2 - poziom logiczny 1")
        print("\t Warunek_3 i Warunek_4 - poziom logiczny 2")
        while True:
            c = ComparisonCriterion(attributeForView)
            Select += attribute[c-1]
            Select += comparisonOperator()
            Select += valuesToCompare()
            if poziom == 0:
                if poziom !=0:
                    Select += logicalOperators()
                    help2 = ifLevel(False) #ifLevelHigher()
                    if help2:
                        poziom+=1
                        Select += " ("
                else:
                    help1 = WhereEnd()
                    if help1:
                        return Select
                    else:
                        Select += logicalOperators()
                        help2 = ifLevel(False) #ifLevelHigher()
                        if help2:
                            poziom+=1
                            Select+=" ("

            else:
                help = ifLevel(True) #ifLevelLower()
                if help:
                    f = LevelLower(poziom)
                    Select += ")"*f
                    poziom -= f
                    if poziom == 0:
                        help1 = WhereEnd()
                        if help1:
                            return Select
                        else:
                            Select += logicalOperators()

                else:
                    Select += logicalOperators()
                    help2 = ifLevel(False)  # ifLevelHigher()
                    if help2:
                        poziom += 1
                        Select += " ("
            print(Select)
def primaryKeySelection(tabela, ifAlien):
    # wybór klucza głównego / obcego
    if ifAlien == True:
        helpStrName = "Klucz obcy"
    else:
        helpStrName = "Klucz główny"
    kwerenda = "describe " + tabela
    kursor.execute(kwerenda)
    help = []  # do wyboru i do późniejszch operacji
    help2 = []  # do wyświetlania
    print("\n\tOpis tabeli "+tabela)
    for rekord in kursor.fetchall():
        help.append(tabela + "." + rekord[0])
        helpStr = " - " + rekord[0]
        helpStr += " " * (40 - len(helpStr))
        help2.append(helpStr)
    i = 0
    for rekord in help2:
        i += 1
        if i % 2 == 0:
            print(str(i) + rekord)
        else:
            print(str(i) + rekord, end="")
    while True:
        try:
            print("\n\nWybierz klucz ",helpStrName," dla tabeli ",tabela,": ",end=" ")
            x = int(input())
            if x>0 and x<i+1:
                return help[x-1]
            else:
                print("nie ma takiego atrybutu")
        except:
            print("podaj liczbę, aby wybrać ",helpStrName)
def ifConect():
    while True:
        f = input("\nCzy podany klucz główny łaczy się z jakąś tabelą wpisz \"tak\"\t\n jeżeli tak, wszystko inne będzie traktowane jako zapszeczenie.")
        f = f.strip()
        if f.lower() == "tak" or f.lower() == "yes":
            return True
        else:
            return False
def choiceTable(tablesForSelect3,table):
    # wybór tabeli do połączenia z danym kluczem obcym w tabeli
    if len(tablesForSelect3)-1 == 1:
        for rekord in tablesForSelect3:
            if rekord != table:
                return rekord
    else:
        i=0
        helpTable = []
        for rekord in tablesForSelect3:
            if rekord != table:
                i += 1
                helpTable.append(rekord)
                helpStr = str(i) + " - " + rekord
                helpStr += " " * 18
                if i % 2 ==0:
                    print(helpStr)
                else:
                    print(helpStr,end="")
        if i % 2 != 0:
            print()
        while True:
            try:
                print("\nWybierz tabelę z którą łączy się z, tabelą ",table,", przy urzyciu jej klucza głównego", end=" ")
                d = int(input())
                if d > 0 and d < i + 1:
                    print(helpTable[d - 1])
                    return helpTable[d - 1]
                else:
                    print("nie ma takiej tabeli")
            except:
                print("podaj liczbę, aby wybrać tabele")
def connectTableMain(tablesForSelect):
    print("\t\t ==> ŁĄCZENIE TABEL <== ")
    print("\tZakładam że, liczba połączeń tabel jest o 1 mniejsza od jej ilości")
    expectedActivity = len(tablesForSelect)-1
    connect = 0
    connectStr = ""
    tableIND = 0
    while connect < expectedActivity:
        if tableIND > expectedActivity+1:
            print("Coś popsułeś i nie dziąła")
            return False
        else:
            tabela = tablesForSelect[tableIND]
            primaryKey = primaryKeySelection(tabela,False) # klucz główny
            g = ifConect()
            if g:
                alienTable = choiceTable(tablesForSelect, tabela)
                alienKey = primaryKeySelection(alienTable,True)
                if connect == 0:
                    connectStr = primaryKey + " = " + alienKey
                else:
                    connectStr+=" AND "+primaryKey + " = " + alienKey
                print(connectStr)
                connect += 1
            tableIND +=1
    return connectStr

try:
    #----- Wybór bazy -----
    baza = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='')
    kwerenda = "SHOW databases;"
    kursor = baza.cursor()
    try:
        kursor.execute(kwerenda)
        i = 0
        bazyDanych = []
        for rekord in kursor.fetchall():
            i += 1
            bazyDanych.append(rekord[0])
            helpStr = str(i) +" - "+ rekord[0]
            helpStr += " "*(40-len(helpStr))
            if i % 2 ==0:
                print(helpStr)
            else:
                print(helpStr,end="")
        z = choiceDataBase(i)
        print("\nKorzystasz z bazy:  =>"+bazyDanych[z]+"<=. ",end="")
    except:
        print("Kwerenda niepoprawna składniowo.")
    # ----- Wybór bazy KONIEC -----
    # ----- Urzycie bazy i pokazanie Tabel -----
    helpStr = ""
    kwerenda = "USE "+bazyDanych[z]+";"
    kursor.execute(kwerenda)
    kwerenda = "SHOW TABLES;"
    kursor.execute(kwerenda)
    tables = [] #Do wyświetlania
    for rekord in kursor.fetchall():
        tables.append(rekord[0])
    if len(tables) == 0:
        print("Baza ta nie posiada tabel.")
    else:
        i = 0
        print("Baza ta posiada tabele:")
        for rekord in tables:
            i += 1
            helpStr = str(i) + " - " + rekord
            helpStr += " " * (35 - len(helpStr))
            if i % 2 == 0:
                print(helpStr)
            else:
                print(helpStr, end="")
    # ----- Urzycie bazy i pokazanie Tabel KONIEC -----
    # ----- Wybór tabel do zapytania -----
    if len(tables) != 0:
        if i % 2 != 0:
            print()
        i = 0
        print("\n"+" "*16+"==> START SMART SELECT <==")
        a = howManyTables(tables)
        print("\n -> Wybierz tabele, na których chesz dokonać operacji <- ")
        tablesForSelect = choiceTables(tables,a)
    # ----- Wybór tabel do zapytania  KONIEC -----
    # ----- Zapytanie dla jednej tabeli  -----

    if len(tablesForSelect) == 1:
        helpTab = choiceAttributeForView(tablesForSelect[0])
        Select = "SELECT "+", ".join(helpTab)+" FROM "+", ".join(tablesForSelect)
        print("\nObecna forma zapytania:\n\t"+Select+"\n")
        Select += " "+WhereMain(tablesForSelect)
        print(Select)
        connect = True
    # ----- Zapytanie dla jednej tabeli KONIEC -----
    # ----- Zapytanie dla wielu tabel -----
    else:
        helpTab = []
        for help in tablesForSelect:
            helpTab += choiceAttributeForView(help)
        Select = "SELECT " + ", ".join(helpTab) + " FROM " + ", ".join(tablesForSelect)
        print("\nObecna forma zapytania:\n\t" + Select + "\n")
        connect = connectTableMain(tablesForSelect)
        if connect != False:
            Select += " WHERE "
            Select += connect
            print("\nObecna forma zapytania:\n\t" + Select + "\n")
            Select += WhereMain(tablesForSelect)
            print(Select)
    # ----- Zapytanie dla wielu tabel KONIEC -----
    # ----- Smart select zapytanie i wyświetlanie -----
    if connect != False:
        kursor.execute(Select)
        tab2 = kursor.fetchall()
        tab = [kursor.column_names]
        for i in range(len(tab2)):
            tab.append(tab2[i])
        CreateTable(tab, True)

    # ----- Smart select zapytanie i wyświetlanie KONIEC-----
except:
    print("Wystąpił błąd połączenia.")