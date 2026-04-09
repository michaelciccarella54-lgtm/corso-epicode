nome = "michael"
cognome = "ciccarella"
codice_fiscale = "CCCMHLD24A26F839B" 
eta = 26
peso = 73
analisi = ["emocromo" , "colesterolo" , "glicemia"]
nome = "dennis"
cognome = "tavola"
codice_fiscale = "TVLDNN24A26F839B" 
eta = 24
peso = 80
analisi = ["emocromo" , "colesterolo" , "glicemia"]
nome = "giovanni"
cognome = "depaoli"
codice_fiscale = "RSSGNN24A26F839B"
eta = 30
peso = 75
analisi = ["emocromo" , "colesterolo" , "glicemia"]
class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
    def scheda_personale(self):
        return f"{self.nome} {self.cognome}, CF: {self.codice_fiscale}, Età: {self.età}, Peso: {self.peso}"   
class Medico: 
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione
    def visita_paziente(self, Paziente):
        print(f"il dott.{self.cognome} visita {Paziente.nome} {Paziente.cognome} ")
class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato
    def valuta(self):
        if self.tipo == "glicemia":
            if self.risultato < 70:
                return "normale" if 70 <= self.risultato <= 100 else "fuori norma"
            elif self.tipo == "colesterolo":
                if self.risultato < 200:
                    return "normale" if self.risultato < 200 else "alto"
            else:                return "valore non definito"
import numpy as np
valori = np.array([80, 190, 90, 85, 210, 95, 75, 180, 88])
print ("media:" , np.mean(valori))
print ("max: " , np.max(valori))
print ("min: " , np.min(valori))
print ("deviazione standard: " , np.std(valori))    
class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = risultati_analisi
    def scheda_personale(self):
        return f"{self.nome} {self.cognome}, CF: {self.codice_fiscale}, Età: {self.età}, Peso: {self.peso}"
    def statistiche_analisi(self):
        return {
            "media": np.mean(self.risultati_analisi),
            "max": np.max(self.risultati_analisi),
            "min": np.min(self.risultati_analisi),
            "std": np.std(self.risultati_analisi)
        }
import numpy as np
# pazienti
paziente1 = Paziente("michael", "ciccarella", "CCCMHLD24A26F839B", 26, 73, ["emocromo" , "colesterolo" , "glicemia"], [80, 190, 90])
paziente2 = Paziente("dennis", "tavola", "TVLDNN24A26F839B", 24, 80, ["emocromo" , "colesterolo" , "glicemia"], [85, 210, 95])
paziente3 = Paziente("giovanni", "depaoli", "RSSGNN24A26F839B", 30, 75, ["emocromo" , "colesterolo" , "glicemia"], [75, 180, 88])
# medici
medico1 = Medico("Luca", "Rossi", "Cardiologia")
medico2 = Medico("Maria", "Bianchi", "Endocrinologia") 
medico3 = Medico("Giulia", "Verdi", "Medicina Generale")
# stampa schede 
for p in [paziente1, paziente2, paziente3]:
    print(p.scheda_personale())
    print("Statistiche analisi:", p.statistiche_analisi())
# visite
medico1.visita_paziente(paziente1)
medico2.visita_paziente(paziente2)
medico3.visita_paziente(paziente3)