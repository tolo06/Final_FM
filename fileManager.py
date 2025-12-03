import os
import matplotlib.pyplot as plt
import numpy as np
import platform
from PIL import Image

def elimina_file(nome_file="prova", tipo=".txt", percorso=""):
    try:
        os.remove(percorso + nome_file + tipo)
    except Exception as err:
        print(f"Errore durante l'eliminazione del file: {err}")
        return False
    else:
        print("Operazione completata con successo.")
        return True

def rinomina_file(nome_file="prova",  tipo=".txt", percorso="", nome_nuovo="copia"):
    try:
        nuovo_file = open(percorso + nome_nuovo + tipo, 'w')
        orinale = open(percorso + nome_file + tipo, 'r')
        contenuto = orinale.read()
        nuovo_file.write(contenuto)
        orinale.close()
        nuovo_file.close()
    except Exception as err:
        print(f"Errore durante la rinomina del file: {err}")
        return False
    else:
        elimina_file(percorso + nome_file)
        return True

def leggi_file(nome_file="prova", tipo=".txt", percorso=""):
    try:
        file = open(percorso + nome_file + tipo, 'r')
        contenuto = file.read()
        print(f"\n\n{nome_file}\n\n{contenuto}\n\n")
        file.close()
    except Exception as err:
        print(f"Errore durante la lettura del file: {err}") 
        return False
    else:
        return True

def crea_file(nome_file="prova", tipo=".txt", percorso=""):
    try:
        file = open(percorso + nome_file + tipo, 'w')
        file.close()
    except Exception as err:
        print(f"Errore durante la creazione del file: {err}")
        return False
    else:
        print("Operazione completata con successo.")
        return True

def copia_file(nome_file="prova", tipo=".txt", percorso=""):
    try:
        fopen = open(percorso + nome_file + tipo, 'r')
        contenuto = fopen.read()
        fcopy = open(percorso + nome_file + "_copia" + tipo, "w")
        fcopy.write(contenuto)
        fopen.close()
        fcopy.close()
    except Exception as err:
        print(f"Errore durante la copia del file: {err}")
        return False
    else:
        print("Operazione completata con successo.")
        return True

def converti_tipo(nome_file = "prova", tipo = ".txt", percorso = "", tipo_nuovo = ".bin"):
    try:
        originale = open(percorso+nome_file+tipo, "r")
        nuovo = open(percorso+nome_file+tipo_nuovo, "w")
        contenuto = originale.read()
        nuovo.write(contenuto)
        originale.close()
        nuovo.close()


    except Exception as err:
        print(f"Errore: {err}")
        return False
    else:
        elimina_file(percorso + nome_file + tipo)
        return True

def sposta_file(nome_file="prova", tipo=".txt", percorso="", percorso_nuovo=""):
    try:
        fopen = open(percorso + nome_file + tipo, 'r')
        contenuto = fopen.read()
        fnew = open(percorso_nuovo + nome_file + tipo, "w")
        fnew.write(contenuto)
        fopen.close()
        fnew.close()
    except Exception as err:
        print(f"Errore durante lo spostamento del file: {err}")
        return False
    else:
        elimina_file(nome_file, tipo, percorso)
        return True
        
def conta_caratteri(nome_file="prova", tipo=".txt", percorso=""):
    try:
        if tipo == ".txt":
            fopen = open(percorso + nome_file + tipo, 'r')
            contenuto = fopen.read()
            numero_char = 0
            for i in contenuto:
                numero_char += 1
            fopen.close()
            if numero_char > 0:
                print(f"\n{nome_file} contiene {numero_char}\n")
            else:
                print("Il file è vuoto")
        else:
            print("Tipo di file inalido (non '.txt')")
            return False
    except Exception as err:
        print(f"Errore durante il conteggio dei caratteri: {err}")
        return False
    else:
        return True

def apri_immagine(nome_file="prova", tipo=".png", percorso=""):
    try:
        if tipo == ".png":
            img = np.asarray(Image.open(percorso + nome_file + tipo))
            plt.imshow(img)
            plt.axis('off')
            plt.show()
        else:
            print("Tipo di file invalido (non '.png')\n")
            return False
    except Exception as err:
        print(f"Errore durante l'apertura dell'immagine: {err}")
        return False
    else:
        return True

def apri_file(nome_file="prova", tipo=".txt", percorso=""):
    try:
        sistema = platform.system()
        if sistema == "Windows":
            os.startfile(percorso + nome_file + tipo)
        elif sistema == "Darwin":
            os.system(f"open {percorso + nome_file + tipo}")
        else: os.system(f"xdg-open {percorso + nome_file + tipo}")
    except Exception as err:
        print(f"Errore durante l'apertura del file: {err}")
        return False
    else:
        print("Operazione completata con successo.")
        return True

def getInput():
    usrInput = input("Inserisci l'operazione da eseguire:  (-h per aiuto, -e per uscire): ").split(' ')
    usrParam = len(usrInput)
    if usrParam < 5:
        for i in range(usrParam, 5):
            usrInput.append("")
    return usrInput

def main():
    print("\n\n\t--------------- -----        -----\n"
          "\t|             | |    \\      /    |\n"
          "\t|   ----------  |     \\    /     |\n"
          "\t|   |           |      \\  /      |\n"
          "\t|   ----------  |   \\   \\/   /   |\n"
          "\t|             | |   |\\      /|   |\n"
          "\t|   ----------  |   | \\    / |   |\n"
          "\t|   |           |   |  \\  /  |   |\n"
          "\t|   |           |   |   \\/   |   |\n"
          "\t-----           -----        -----\n\n"
          "\t-----------------------------------\n"
          "\t    FILE MANAGER - PYTHON EDITION\n"
          "\t-----------------------------------\n\n")
    
    usrInput = getInput()              

    while usrInput[0] != "-e":
        if usrInput[0] == "-h":
            print("Lista dei comandi:\n"
                   "\tcrea <nome_file> <tipo_file> <percorso>\n"
                   "\tleggi <nome_file> <tipo_file> <percorso>\n"
                   "\tcopia <nome_file> <tipo_file> <percorso>\n"
                   "\telimina <nome_file> <tipo_file> <percorso>\n"
                   "\trinonima <nome_file> <tipo_file> <percorso> <nome_nuovo>\n"
                   "\tconverti <nome_file> <tipo_file> <percorso> <tipo_nuovo>\n"
                   "\tsposta <nome_file> <tipo_file> <percorso> <percorso_nuovo>\n"
                   "\tconta_char <nome_file> <tipo_file> <percorso>\n"
                   "\tapri <nome_file> <tipo_file> <percorso>\n"
                   "\tapri_img <nome_file> <percorso>\n")
        elif usrInput[0] == "crea":
            crea_file(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "leggi":
            leggi_file(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "copia":
            copia_file(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "elimina":
            elimina_file(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "rinomina":
            rinomina_file(usrInput[1], usrInput[2], usrInput[3], usrInput[4])
        elif usrInput[0] == "converti":
            converti_tipo(usrInput[1], usrInput[2], usrInput[3], usrInput[4])
        elif usrInput[0] == "sposta":
            sposta_file(usrInput[1], usrInput[2], usrInput[3], usrInput[4])
        elif usrInput[0] == "conta_char":
            conta_caratteri(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "apri_img":
            apri_immagine(usrInput[1], usrInput[2])
        elif usrInput[0] == "apri":
            apri_file(usrInput[1], usrInput[2], usrInput[3])
        elif usrInput[0] == "-e":
            break
        else:
            print("Comando non riconosciuto. Riprova.")
        usrInput = usrInput = getInput()
        
if __name__ == "__main__":
    main()  
