'''
Creare un repository pubblico (con nome "3fsia_<COGNOME>_dati")

Creare un file sorgente python

Assegnare i valori 5, -3, 6.81, 5.0, "c", "ciao", -0.5, "5", "5.0" ad altrettante variabili

Assegnare i seguenti valori forniti in input ad altrettante variabili: "scuola", 
"13/11/2024", "13", "0119553131", "segreteria@iismajoranamoncalieri.edu.it"

Per ogni variabile, stampare il valore contenuto nella variabile e il tipo 
di dato contenuto nella variabile (usare la funzione type())

Convertire le stringhe di tipo numerico in interi e assegnare i valori a 
nuove variabili con lo stesso nome delle variabili precedenti, ma col suffisso "_int". Stampare valore e tipi dati di quelle variabili.

Convertire le stringhe di tipo numerico in numeri reali (float) e assegnare 
i valori a nuove variabili con lo stesso nome delle variabili precedenti, ma col suffisso "_float". Stampare valore e tipi dati di quelle variabili.
'''

numero_i = 5
numero_i2 = -3
numero_f = 6.81
numero_f2 = 5.0
lettera = "c"
parola = "ciao"
numero_f3 = -0.5
numero_i3 = "5"
numero_f4 = "5.0"
nome = "scuola"
data = "13/11/2024"
numero = "13"
telefono = "0119553131"
print(f"Primo numero: {numero_i, type(numero_i)};\nSecondo numero: {numero_i2, type(numero_i2)};\nTerzo numero: {numero_f, type(numero_f)};\nQuarto numero: {numero_f2, type(numero_f2)};\nPrima lettera: {lettera, type(lettera)};\nPrima parola: {parola, type(parola)};\nQuinto numero: {numero_f3, type(numero_f3)};\nSesto numero: {numero_i3, type(numero_i3)};\nSettimo numero: {numero_f4, type(numero_f4)};\nNome: {nome, type(nome)};\nData: {data, type(data)};\nNumero: {numero, type(numero)};\nNumero di telefono: {telefono, type(telefono)}.\n")

numero_i3_int = int(numero_i3)
numero_int = int(numero)
telefono_int = int(telefono)
print(f"Primo numero intero: {numero_i3_int, type(numero_i3_int)};\nSecondo numero intero: {numero_int, type(numero_int)};\nPrimo numero di telefono: {telefono_int, type(telefono_int)}.\n")

numero_i3_float = float(numero_i3)
numero_float = float(numero)
telefono_float = float(telefono)
numero_f4_float = float(numero_f4)
print(f"Primo numero decimale: {numero_i3_float, type(numero_i3_float)};\nSecondo numero decimale: {numero_float, type(numero_float)};\nTerzo numero decimale: {telefono_float, type(telefono_float)};\nQuarto numero decimale: {numero_f4_float, type(numero_f4_float)}.")
