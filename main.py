import mysql.connector

# Connessione al database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="py_sql"
)

cursor = db.cursor()

# Creare il database se non esiste
#cursor.execute("CREATE DATABASE py_sql")

# Creazione delle tabelle
cursor.execute("""
CREATE TABLE IF NOT EXISTS Compagnia (
    ID_compagnia VARCHAR(10) PRIMARY KEY,
    nome_compagnia VARCHAR(100),
    Capienza INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Aereo (
    ID_aereo VARCHAR(10) PRIMARY KEY,
    ID_compagnia VARCHAR(10),
    partenza VARCHAR(50),
    arrivo VARCHAR(50),
    FOREIGN KEY (ID_compagnia) REFERENCES Compagnia(ID_compagnia)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Personale_di_Volo (
    ID_personale INT PRIMARY KEY,
    ID_compagnia VARCHAR(10),
    nome VARCHAR(50),
    cognome VARCHAR(50),
    data_nascita DATE,
    stipendio DECIMAL(10, 2),
    ruolo VARCHAR(50),
    FOREIGN KEY (ID_compagnia) REFERENCES Compagnia(ID_compagnia)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Passeggero (
    ID_passeggero VARCHAR(10) PRIMARY KEY,
    nome VARCHAR(50),
    cognome VARCHAR(50),
    data_nascita DATE,
    nazionalità VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Bagaglio (
    ID_bagaglio VARCHAR(10) PRIMARY KEY,
    ID_biglietto VARCHAR(10),
    Dimensione VARCHAR(10),
    Peso DECIMAL(10, 2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Biglietto (
    ID_biglietto VARCHAR(10) PRIMARY KEY,
    ID_volo VARCHAR(10),
    ID_passeggero VARCHAR(10),
    ID_bagaglio VARCHAR(10),
    prezzo DECIMAL(10, 2),
    N_posto VARCHAR(10),
    FOREIGN KEY (ID_passeggero) REFERENCES Passeggero(ID_passeggero),
    FOREIGN KEY (ID_bagaglio) REFERENCES Bagaglio(ID_bagaglio)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Volo (
    ID_volo VARCHAR(10) PRIMARY KEY,
    ID_aereo VARCHAR(10),
    ID_gate VARCHAR(10),
    ID_terminal VARCHAR(10),
    ID_aeroporto VARCHAR(10),
    orario_part TIME,
    orario_arr TIME,
    FOREIGN KEY (ID_aereo) REFERENCES Aereo(ID_aereo)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Gate (
    ID_gate VARCHAR(10) PRIMARY KEY,
    ID_terminal VARCHAR(10),
    orario_apertura TIME,
    orario_chiusura TIME
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Terminal (
    ID_terminal VARCHAR(10) PRIMARY KEY,
    ID_aeroporto VARCHAR(10)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Aeroporto (
    città VARCHAR(50),
    ID_aeroporto VARCHAR(10) PRIMARY KEY,
    nome_Aeroporto VARCHAR(100)
)
""")

db.commit()

# Inserimento dei dati nelle tabelle
compagnie = [
    ("ALI123", "Alitalia", 189),
    ("RYA123", "Ryanair", 197),
    ("AIR123", "AirArabia", 189),
    ("LUF123", "Luftansa", 189),
    ("VOL123", "Volotea", 197),
    ("VUE123", "Vueling", 197)
]

cursor.executemany("INSERT INTO Compagnia (ID_compagnia, nome_compagnia, Capienza) VALUES (%s, %s, %s)", compagnie)

aerei = [
    ("8451ALI", "ALI123", "Roma", "Torino"),
    ("1774RYA", "RYA123", "Roma", "Parigi"),
    ("2462AIR", "AIR123", "Roma", "Berlino"),
    ("5565LUF", "LUF123", "Roma", "Milano"),
    ("1574VOL", "VOL123", "Milano", "Istanbul"),
    ("9562VUE", "VUE123", "Milano", "Catania")
]

cursor.executemany("INSERT INTO Aereo (ID_aereo, ID_compagnia, partenza, arrivo) VALUES (%s, %s, %s, %s)", aerei)

personale = [
    (1, "ALI123", "Luca", "Rossi", "1987-02-15", 1523.00, "hostess"),
    (2, "ALI124", "Marco", "Verdi", "1992-07-19", 1718.00, "hostess"),
    (3, "RYA123", "Giulia", "Bianchi", "1990-08-02", 2062.00, "pilota"),
    (4, "AIR123", "Anna", "Russo", "1998-05-04", 1307.00, "hostess"),
    (5, "RYA123", "Giuseppe", "Canto", "1989-10-12", 2875.00, "pilota"),
    (6, "RYA124", "Fabrizio", "Abate", "2003-03-30", 1459.00, "hostess"),
    (7, "AIR124", "Federica", "Fede", "1999-12-14", 1675.00, "hostess"),
    (8, "RYA124", "Jessica", "Fortuna", "1995-11-26", 1546.00, "hostess"),
    (9, "VOL123", "Luigi", "Esposito", "2001-01-24", 1652.00, "hostess"),
    (10, "LUF123", "Andrea", "Marini", "2000-09-17", 1726.00, "hostess")
]

cursor.executemany("INSERT INTO Personale_di_Volo (ID_personale, ID_compagnia, nome, cognome, data_nascita, stipendio, ruolo) VALUES (%s, %s, %s, %s, %s, %s, %s)", personale)

# Commit delle operazioni di inserimento
db.commit()

# Chiudere la connessione
cursor.close()
db.close()
