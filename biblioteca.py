titolo = "harry potter e il prigioniero di azkaban"
copie = 5
prezzo = 19.99
disponibile = True
print(titolo, copie, prezzo, disponibile)
lista_libri = ["harry potter e la pietra filosofale", "harry potter e la camera dei segreti", "harry potter e il prigioniero di azkaban", "harry potter e il calice di fuoco", "harry potter e l'ordine della fenice"]
dizionario_copie = {"harry potter e la pietra filosofale": 10, "harry potter e la camera dei segreti": 8, "harry potter e il prigioniero di azkaban": 5, "harry potter e il calice di fuoco": 7, "harry potter e l'ordine della fenice": 6}
utenti_registrati = {"Michael", "Anna","dennis"}
class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.copie_disponibili = copie_disponibili
    def info(self):
        return f"{self.titolo} di {self.autore}, pubblicato nel {self.anno_pubblicazione}, disponibili: {self.copie_disponibili}"
class Utente:
    def __init__(self, nome, età, id_utente):
        self.nome = nome
        self.età = età
        self.id_utente = id_utente
    def info(self):
        return f"Utente: {self.nome}, Età: {self.età}, ID Utente: {self.id_utente}"
class Prestito:
    def __init__(self, utente, libro, giorni_prestito):       
        self.utente = utente
        self.libro = libro
        self.giorni_prestito = giorni_prestito
    def dettagli_prestito(self):
        return f"{self.utente.nome} ha preso in prestito '{self.libro.titolo}' per {self.giorni_prestito} giorni."
def presta_libro(utente, libro, giorni_prestito):
        if libro.copie_disponibili > 0:
            libro.copie_disponibili -= 1
            return Prestito(utente, libro, giorni_prestito)
        else:
            return f"Mi dispiace, '{libro.titolo}' non è disponibile al momento."
libro1 = Libro("harry potter e il prigioniero di azkaban", "J.K. Rowling", 1999, 5)
utente1 = Utente("dennis", 24, "U001")
libro2 = Libro("harry potter e la camera dei segreti", "J.K. Rowling", 1998, 8)
utente2 = Utente("Anna", 20, "U002")
libro3 = Libro("harry potter e la pietra filosofale", "J.K. Rowling", 1997, 10)
utente3 = Utente("Michael", 26, "U003")
prestiti = []
prestiti.append(presta_libro(utente1, libro1, 14))
prestiti.append(presta_libro(utente2, libro2, 7))
prestiti.append(presta_libro(utente3, libro3, 21))
print("\--- copie aggiornate ---")
print(libro1.info())
print(libro2.info())
print(libro3.info())
print("\--- dettagli prestiti ---")
for p in prestiti:
    print(p.dettagli_prestito())   