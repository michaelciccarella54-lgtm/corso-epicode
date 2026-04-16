import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
nome = "michael ciccarella"
eta = 27 
saldo = 5000
vip = True
destinazioni = ["parigi", "londra", "new york", "tokyo", "zanzibar"]
prezzi_medi = {"parigi": 1200, "londra": 1000, "new york": 1500, "tokyo": 1300, "zanzibar": 1100}
print("=== PARTE 1 ===")
print("nome:", nome)
print("età:", eta)
print("saldo:", saldo)
print("vip:", vip)
print("destinazioni:", destinazioni)
print("prezzi medi:", prezzi_medi)
class Cliente:
    def __init__(self, nome, eta, saldo, vip):
        self.nome = nome
        self.eta = eta
        self.saldo = saldo
        self.vip = vip
    def info(self):
        return f"Cliente: {self.nome}, Età: {self.eta}, saldo: {self.saldo}, VIP: {self.vip}"
class Viaggio:
    def __init__(self, destinazione, prezzo, durata):
        self.destinazione = destinazione
        self.prezzo = prezzo
        self.durata = durata
    def info(self):
        return f"Viaggio verso {self.destinazione}, Prezzo: {self.prezzo}€, Durata: {self.durata} giorni"
class Prenotazione:
    def __init__(self, cliente, viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
    def calcola_importo_finale(self):
        if self.cliente.vip:
            return self.viaggio.prezzo * 0.9
        return self.viaggio.prezzo
    def dettagli(self):
        return (
            f"{self.cliente.nome} ha prenotato un viaggio verso {self.viaggio.destinazione}"
            f" di  {self.viaggio.durata} giorni. Importo finale: {self.calcola_importo_finale()}€"
        )
print("=== PARTE 2 ===")
cliente1 = Cliente("michael ciccarella", 27, 5000, True)
cliente2 = Cliente("anna", 24, 3000, False)
viaggio1 = Viaggio("parigi", 1200, 7)
viaggio2 = Viaggio("londra", 1000, 5)   
prenotazione1 = Prenotazione(cliente1, viaggio1)
prenotazione2 = Prenotazione(cliente2, viaggio2)
print(prenotazione1.dettagli())
print(prenotazione2.dettagli()) 
print()
np.random.seed(42)
prenotazioni_simulate = np.random.randint(200, 2002, 100)
prezzo_medio = np.mean(prenotazioni_simulate)
prezzo_min = np.min(prenotazioni_simulate)
prezzo_max = np.max(prenotazioni_simulate)
deviazione_standard = np.std(prenotazioni_simulate)
percentuale_sopra_media = np.sum(prenotazioni_simulate > prezzo_medio) / len(prenotazioni_simulate) * 100
print("=== PARTE 3 ===")
print("Prezzo medio:", round(prezzo_medio, 2))
print("Prezzo minimo:", round(prezzo_min, 2))
print("Prezzo massimo:", round(prezzo_max, 2))
print("Deviazione standard:", round(deviazione_standard, 2))
print("Percentuale di prenotazioni sopra la media:", round(percentuale_sopra_media, 2), "%")
print()
clienti = [
    "michael", "anna", "dennis", "giovanni", "luca",
    "michael", "anna", "dennis", "giovanni", "luca",
]
destnazioni_df = [
    "parigi", "londra", "new york", "tokyo", "zanzibar",
    "parigi", "londra", "new york", "tokyo", "zanzibar" 
]
prezzi = [1200, 1000, 1500, 1300, 1100,1200, 1000, 1500, 1300, 1100]
Giorni_Partenza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
durata = [7, 5, 10, 8, 6, 7, 5, 10, 8, 6]
incassi = prezzi
df = pd.DataFrame({
    "Cliente": clienti,
    "Destinazione": destnazioni_df,
    "Prezzo": prezzi,
    "Giorni_Partenza": Giorni_Partenza,
    "Durata": durata,
    "Incasso": incassi
})
print("=== PARTE 4 ===")
print(df)
print()
incasso_totale = df["Incasso"].sum()
incasso_medio_destinazione = df.groupby("Destinazione")["Incasso"].mean()
top3_destinazioni = df["Destinazione"].value_counts().head(3)
print("Incasso totale agenzia:", incasso_totale)
print()
print("Incasso medio destinazione:")
print(incasso_medio_destinazione)
print()
print("Top 3 destinazioni più prenotate:")
print(top3_destinazioni)
print()
incasso_per_destinazione = df.groupby("Destinazione")["Incasso"].sum()
plt.figure(figsize=(10, 5))
plt.bar(incasso_per_destinazione.index, incasso_per_destinazione.values)
plt.title("Incasso totale per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso")
plt.tight_layout()
plt.bar(top3_destinazioni.index, top3_destinazioni.values)
incasso_giornaliero = df.groupby("Giorni_Partenza")["Incasso"].sum()
plt.figure(figsize=(10, 5))
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker='o')
plt.title("Andamento giornaliero degli incassi")
plt.xlabel("Giorni di partenza")
plt.ylabel("Incasso")
plt.tight_layout()
plt.show()
vendite_per_destinazione = df["Destinazione"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(vendite_per_destinazione.values, labels=vendite_per_destinazione.index, autopct='%1.1f%%')
plt.title("Distribuzione delle prenotazioni per destinazione")
plt.tight_layout()
plt.show()
categorie = {
    "Parigi" : "Europa",
    "Londra" : "Europa",
    "New York" : "America",
    "Tokyo" : "Asia",
    "Zanzibar" : "Africa"
}
df["Categoria"] = df["Destinazione"].map(categorie)
incasso_per_categoria = df.groupby("Categoria")["Incasso"].mean()
durata_media_per_categoria = df.groupby("Categoria")["Durata"].mean()
print("=== PARTE 6 ===")
print("Incasso totale per categoria:")
print(incasso_per_categoria)
print()
print("Durata media dei viaggi per categoria:")
print(durata_media_per_categoria)
print()
df.to_csv("prenotazione_analizzata.csv", index=False)
print("File CSV salvato come prenotazioni_analizzate.csv")
print()
def top_clienti(df, n=5):
    return df["Cliente"].value_counts().head(n)
categorie = {
    "parigi" : "Europa",
    "londra" : "Europa",
    "new york" : "America",
    "tokyo" : "Asia",
    "zanzibar" : "Africa"
}
df["Categoria"] = df["Destinazione"].map(categorie)
print("=== PARTE 7 ===")
print ("Top clienti con più prenotazioni:")
print(top_clienti(df, n=5))
print()
incasso_medio_categoria = df.groupby("Categoria")["Incasso"].mean()
durata_media_categoria = df.groupby("Categoria")["Durata"].mean()
fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.bar(incasso_medio_categoria.index, incasso_medio_categoria.values,)
ax1.set_xlabel("Categoria")
ax1.set_ylabel("Incasso medio")
ax2 = ax1.twinx()
ax2.plot(durata_media_categoria.index,
         durata_media_categoria.values,
         marker='o')
ax2.set_ylabel("Durata media")
plt.title("Incasso medio e durata media per categoria")
plt.tight_layout()
plt.show()
print()
print("progetto completato con successo!")