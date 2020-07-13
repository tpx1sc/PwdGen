# PWDGEN é un programma che genera passwords con tre gradi di difficoltà
# Fin dall'inizio si puo' decidere se salvarle in un file oppure eliminarle
# i tre tipi di difficoltà sono, facile, media ed Ardua
### FUNZIONI DA AGGIUNGERE: Scegliere i noma da un database, Eliminare il file all'interno del programma,
### Criptare il file con le passwords e decriptarlo all'interno del programma E creare una versione con GUI


__autore__ = 'Abdelmounaim Omri aka tpx1sc'

# Tutti i moduli usati dal programma

import random # Modulo random, che serve a generare caratteri random, usato per creare passwords
import string # Modulo stringa, usato per creare stringhe complesse coi caratteri random
import time # Modulo tempo, usato per impostare un delay tra un comando ed un altro
import os # Moduli riguardanti il sistema, il modulo os serve per eseguire i programmi
import pyperclip # Modulo che permette di copiere testi su clipboard



# Le variabili e liste usate dal programma
pwd = 0
nome_del_file = 'passwords.txt' # Nome del file nel quale verrano salvate tutte le password generate

welcoming = """
Benvenuto nel generatore di passwords !

1) Genera una password


Per uscire, digita '0'
""" # Variabile welcoming, che accoglierà l'utilizzatore nel programma e lo guiderà per la creazione di una Password

name = ('''
================================================================
.______  ___    __    ___ _______   _______  _______ .__   __.
|   _  \ \  \  /  \  /  /|       \ /  _____||   ____||  \ |  |
|  |_)  | \  \/    \/  / |  .--.  |  |  __  |  |__   |   \|  |
|   ___/   \          /  |  |  |  |  | |_ | |   __|  |  . `  |
|  |        \   /\   /   |  '--'  |  |__| | |  |____ |  |\   |
|__|         \_/  \_/    |_______/ \______| |_______||__| \__|
================================================================
Creato da {}
'''.format(__autore__)) # Variabile name, che sarebbe il nome del prgramma in ascii ed anche il nome dell'autore, cioé
# il sommo Hassan

# Le funzioni usate dal programma



def psswdgen(lenght, chars=string.ascii_letters + string.digits + string.punctuation): # 1 - lettere maisc o min, 2 - cifre, 3 - simboli
    global pwd
    pwd = ''.join(random.choice(chars) for _ in range(lenght)) # i caratteri per la password sono stati forniti come parametri
    print("--------------------------------------")
    print("La password che hai generato é: {}".format(pwd)) # Comando che manderà in input la password completa
    print("--------------------------------------")

def save(): # Funzione che, dopo la creazione di passwords, le  salva nel file 'nome_del_file.txt' se il file non esiste lo crea ma non in questa funzione
        global nome_del_file
        f= open(nome_del_file,"a") # Python apre il file 'nome_del_file.txt' in modalità append (aggiunta)
        f.write('\n{}\n'.format(pwd)) # Python aggiunge tutte le passwords genera
        print("Password salvata nel file "+ nome_del_file)
        
def copy_to_clipboard():
    global pwd # Richiama la variabile 'pwd' cioé la password
    pyperclip.copy(pwd) # Copia la variabile pwd nella clipboard
    pyperclip.paste() # Permette alla variabile pwd di essere incollata

# Loop principale del programma

while True:
    time.sleep(0.1)
    print(name)
    time.sleep(0.2)
    if os.path.exists(nome_del_file): # Se il file é già stato creato in precedenza, il programma continua il suo loop
        pass
    else: # se il file risulta inesistente
        Print("Desideri creare un file nel quale salvare le passwords generate ? (si/no)")
        y = input("--> ")
        if y == 'si':
            f = open(nome_del_file,"x") # il programma entrerà in file mode x (vuol dire che crea il file, e se il file esiste, fallisce)
            print("\nFile salvato nella directory {}".format(os.path.dirname(os.path.realpath(nome_del_file)))) # manda in output la dyrectory del file
        if y == 'no': # Se l'user non desidera creare un file per conservare le passwords, il loop prosegue
            pass
    time.sleep(0.2)
    print(welcoming)
    scelta2 = input("--> ")
    if scelta2 == '1':
        try: # Il programma chiedere all'user la lunghezza della password
            print("Quanto desideri sia lunga la password ?")
            lunghezza = int(input("-->"))
            psswdgen(lunghezza) # usa la lunghezza scelta dal user per creare la password
            time.sleep(0.2)
            copy_to_clipboard()
            print("\nPassword copiata nella clipboard\n")
            time.sleep(0.2)
            if os.path.exists(nome_del_file):
                save()
            time.sleep(2)
            os.system('cls') # comando che resetta la console
        except ValueError: # Se la lunghezza non é una cifra, il programma manda in output l'errore seguente
            print("[!] Lunghezza invalida [!]")
            
    elif scelta2 == '0':
        exit() # esce dal programma
    else:
        print("\n[!] Comando invalido [!]")
        time.sleep(1)
        os.system('cls')

        
