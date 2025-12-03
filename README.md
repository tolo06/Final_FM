# File Manager

## Obbiettivo del progetto e descrizione
File Manager che permette all'utente di 
* creare un file della tipologia richiesta al percorso richiesto con un nome richiesto
* eliminare uno specifico file
* copiare uno specifico file
* rinominare un file
* spostare un file
* convertire il tipo del file
* stampare sul terminale i contenuti del file
* stampare su termnale un'immagine se il file in questione è un png
* contare il numero di caratteri
* aprire il file

## Sintesi del setup
Avere installate le librerie os, matplotlib, numpy, platform, PIL

## Come usare il progetto
Inserire nel terminale le seguenti istruzioni:
* [-h] per aiuto
* [-e] per terminare FileManager.py
* [crea <nome_file> <tipo_file> <percorso>] per creare un file
* [elimina <nome_file> <tipo_file> <percorso>] per elimare un file
* [copia <nome_file> <tipo_file> <percorso>] per copiare un file
* [rinonima <nome_file> <tipo_file> <percorso> <nome_nuovo>] per rinominare un file
* [sposta <nome_file> <tipo_file> <percorso> <percorso_nuovo>] per spostare un file
* [converti <nome_file> <tipo_file> <percorso> <tipo_nuovo>] per convertire un file
* [leggi <nome_file> <tipo_file> <percorso>] per stampare il file sul terminale
* [apri_img <nome_file> <percorso>] per stampare l'immagine sul terminale (solo per .png)
* [conta_char <nome_file> <tipo_file> <percorso>] per contare il numero di caratteri in un file (solo per .txt)
* [apri <nome_file> <tipo_file> <percorso>] per far aprire dal sistema operativo il file


## Idee di miglioramento
* implementare l'apertura in terminale di altri tipi di file
* poter cercare e trovare il file in questione senza doverne specificare il tipo o il percorso
