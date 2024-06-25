import mysql.connector

try:
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
    compagnia = [
        ("ALI124", "Alitalia", 189),
        ("RYA124", "Ryanair", 197),
        ("AIR124", "AirArabia", 189),
        ("LUF124", "Luftansa", 189),
        ("VOL124", "Volotea", 197),
        ("VUE124", "Vueling", 197)
    ]

    cursor.executemany("INSERT INTO Compagnia (ID_compagnia, nome_compagnia, Capienza) VALUES (%s, %s, %s)", compagnia)
    db.commit()

    cursor.execute("SELECT * FROM Compagnia")
    compagnie_results = cursor.fetchall()
    print("Dati Compagnia:", compagnie_results)

    aereo = [
        ("8451ALI", "ALI124", "Roma", "Torino"),
        ("1774RYA", "RYA124", "Roma", "Parigi"),
        ("2462AIR", "AIR124", "Roma", "Berlino"),
        ("5565LUF", "LUF124", "Roma", "Milano"),
        ("1574VOL", "VOL124", "Milano", "Istanbul"),
        ("9562VUE", "VUE124", "Milano", "Catania")
    ]

    cursor.executemany("INSERT INTO Aereo (ID_aereo, ID_compagnia, partenza, arrivo) VALUES (%s, %s, %s, %s)", aereo)

    personale = [
        (1, "ALI124", "Luca", "Rossi", "1987-02-15", 1523.00, "hostess"),
        (2, "ALI124", "Marco", "Verdi", "1992-07-19", 1718.00, "hostess"),
        (3, "RYA124", "Giulia", "Bianchi", "1990-08-02", 2062.00, "pilota"),
        (4, "AIR124", "Anna", "Russo", "1998-05-04", 1307.00, "hostess"),
        (5, "RYA124", "Giuseppe", "Canto", "1989-10-12", 2875.00, "pilota"),
        (6, "RYA124", "Fabrizio", "Abate", "2003-03-30", 1459.00, "hostess"),
        (7, "AIR124", "Federica", "Fede", "1999-12-14", 1675.00, "hostess"),
        (8, "RYA124", "Jessica", "Fortuna", "1995-11-26", 1546.00, "hostess"),
        (9, "VOL124", "Luigi", "Esposito", "2001-01-24", 1652.00, "hostess"),
        (10, "LUF124", "Andrea", "Marini", "2000-09-17", 1726.00, "hostess")
    ]

    cursor.executemany("INSERT INTO Personale_di_Volo (ID_personale, ID_compagnia, nome, cognome, data_nascita, stipendio, ruolo) VALUES (%s, %s, %s, %s, %s, %s, %s)", personale)

    db.commit()
    cursor.execute("SELECT * FROM Personale_di_Volo")
    personale_results = cursor.fetchall()
    print("Dati Personale_di_Volo:", personale_results)


    aeroporti = [
        ("Roma", "FIUM456", "Fiumicino"),
        ("Milano", "MIL7512", "Malpensa")
    ]
    cursor.executemany("INSERT INTO Aeroporto (città, ID_aeroporto, nome_Aeroporto) VALUES (%s, %s, %s)", aeroporti)
    db.commit()

    terminal = [
        ("T1", "FIUM456"),
        ("T2", "MIL7512")
    ]
    cursor.executemany("INSERT INTO Terminal (ID_terminal, ID_aeroporto) VALUES (%s, %s)", terminal)
    db.commit()

    gate = [
        ("A6", "T1", "08:45", "09:05"),
        ("A2", "T1", "10:15", "10:40"),
        ("A12", "T1", "11:00", "11:20"),
        ("A7", "T1", "13:35", "13:50"),
        ("A11", "T2", "14:35", "15:00"),
        ("A9", "T2", "16:00", "16:40")
    ]
    cursor.executemany("INSERT INTO Gate (ID_gate, ID_terminal, orario_apertura, orario_chiusura) VALUES (%s, %s, %s, %s)", gate)
    db.commit()

    voli = [
        ("VOLO_ALI", "8451ALI", "A6", "T1", "FIUM456", "09:15", "10:30"),
        ("VOLO_RYA", "1774RYA", "A2", "T1", "FIUM456", "10:50", "13:05"),
        ("VOLO_AIR", "2462AIR", "A12", "T1", "FIUM456", "11:25", "13:40"),
        ("VOLO_LUF", "5565LUF", "A7", "T1", "FIUM456", "14:00", "15:10"),
        ("VOLO_VOL", "1574VOL", "A11", "T2", "MIL7512", "15:10", "19:15"),
        ("VOLO_VUE", "9562VUE", "A9", "T2", "MIL7512", "16:50", "19:05")
    ]
    cursor.executemany("INSERT INTO Volo (ID_volo, ID_aereo, ID_gate, ID_terminal, ID_aeroporto, orario_part, orario_arr) VALUES (%s, %s, %s, %s, %s, %s, %s)", voli)
    db.commit()

    passeggeri = [
        ("PAS001", "Valeria", "Rossi", "1999-12-14", "Italiana"),
        ("PAS002", "Roberto", "Aprile", "2001-08-12", "Italiana"),
        ("PAS003", "Gabriele", "Mizzi", "1984-01-19", "Italiana"),
        ("PAS004", "Ginevra", "Stella", "2000-03-27", "Italiana"),
        ("PAS005", "Bryan", "Martin", "1995-02-28", "Italiana"),
        ("PAS006", "Marco", "Ferro", "1990-01-12", "Italiana"),
        ("PAS007", "Giulia", "Bianchi", "1985-02-23", "Italiana"),
        ("PAS008", "Luca", "Verdi", "1992-03-15", "Italiana"),
        ("PAS009", "Sofia", "Neri", "1988-04-30", "Italiana"),
        ("PAS010", "Matteo", "Ferrari", "1995-05-08", "Italiana"),
        ("PAS011", "Chiara", "Romano", "1987-06-27", "Italiana"),
        ("PAS012", "Davide", "Fontana", "1991-07-14", "Italiana"),
        ("PAS013", "Alice", "Gallo", "1989-08-02", "Italiana"),
        ("PAS014", "Francesco", "Moretti", "1994-09-21", "Italiana"),
        ("PAS015", "Martina", "Esposito", "1986-10-11", "Italiana"),
        ("PAS016", "Alessandro", "Luca", "1993-11-03", "Italiana"),
        ("PAS017", "Elisa", "Conti", "1990-12-18", "Italiana"),
        ("PAS018", "Andrea", "Ricci", "1988-01-29", "Italiana"),
        ("PAS019", "Francesca", "Marino", "1991-02-05", "Italiana"),
        ("PAS020", "Giorgio", "Colombo", "1989-03-16", "Italiana"),
        ("PAS021", "Laura", "Greco", "1987-04-07", "Italiana"),
        ("PAS022", "Federico", "Rinaldi", "1992-05-25", "Italiana"),
        ("PAS023", "Valentina", "Lombardi", "1986-06-19", "Italiana"),
        ("PAS024", "Riccardo", "Barbieri", "1993-07-06", "Italiana"),
        ("PAS025", "Elena", "Sanna", "1990-08-22", "Italiana")
    ]
    cursor.executemany("INSERT INTO Passeggero (ID_passeggero, nome, cognome, data_nascita, nazionalità) VALUES (%s, %s, %s, %s, %s)", passeggeri)
    db.commit()

    bagagli = [
        ("bag123", "BIG123", "D2", 23),
        ("bag124", "BIG124", "D2", 23),
        ("bag125", "BIG125", "D3", 30),
        ("bag126", "BIG126", "D2", 23),
        ("bag138", "BIG138", "D2", 23),
        ("bag354", "BIG354", "D2", 23),
        ("bag548", "BIG548", "D3", 30),
        ("bag345", "BIG345", "D2", 23),
        ("bag346", "BIG346", "D2", 23),
        ("bag421", "BIG421", "D2", 23),
        ("bag423", "BIG423", "D3", 30),
        ("bag754", "BIG754", "D2", 23),
        ("bag865", "BIG865", "D2", 23),
        ("bag985", "BIG985", "D2", 23),
        ("bag512", "BIG512", "D3", 30),
        ("bag456", "BIG456", "D2", 23),
        ("bag632", "BIG632", "D2", 23),
        ("bag712", "BIG712", "D2", 23),
        ("bag956", "BIG956", "D2", 23),
        ("bag652", "BIG652", "D2", 23),
        ("bag741", "BIG741", "D3", 30),
        ("bag369", "BIG369", "D2", 23),
        ("bag852", "BIG852", "D2", 23),
        ("bag741", "BIG741", "D2", 23),
        ("bag482", "BIG482", "D3", 30)
    ]
    cursor.executemany("INSERT INTO Bagaglio (ID_bagaglio, ID_biglietto, Dimensione, Peso) VALUES (%s, %s, %s, %s)", bagagli)
    db.commit()

    biglietti = [
        ("BIG123", "VOLO_ALI", "PAS001", "bag123", 103.25, "12A"),
        ("BIG124", "VOLO_RYA", "PAS002", "bag124", 75.87, "5B"),
        ("BIG125", "VOLO_AIR", "PAS003", "bag125", 75.88, "23C"),
        ("BIG126", "VOLO_LUF", "PAS004", "bag126", 103.25, "16D"),
        ("BIG138", "VOLO_VOL", "PAS005", "bag138", 89.54, "8E"),
        ("BIG354", "VOLO_VUE", "PAS006", "bag354", 103.25, "19F"),
        ("BIG548", "VOLO_VOL", "PAS007", "bag548", 75.87, "3A"),
        ("BIG345", "VOLO_ALI", "PAS008", "bag345", 75.88, "14B"),
        ("BIG346", "VOLO_RYA", "PAS009", "bag346", 69.05, "20C"),
        ("BIG421", "VOLO_AIR", "PAS010", "bag421", 62.21, "7D"),
        ("BIG423", "VOLO_LUF", "PAS011", "bag423", 55.38, "11E"),
        ("BIG754", "VOLO_VOL", "PAS012", "bag754", 48.54, "22F"),
        ("BIG865", "VOLO_VUE", "PAS013", "bag865", 89.54, "4A"),
        ("BIG985", "VOLO_VOL", "PAS014", "bag985", 103.25, "18B"),
        ("BIG512", "VOLO_LUF", "PAS015", "bag512", 75.87, "9C"),
        ("BIG456", "VOLO_VUE", "PAS016", "bag456", 75.88, "1D"),
        ("BIG632", "VOLO_RYA", "PAS017", "bag632", 69.05, "17E"),
        ("BIG712", "VOLO_AIR", "PAS018", "bag712", 62.21, "13F"),
        ("BIG956", "VOLO_LUF", "PAS019", "bag956", 55.38, "2A"),
        ("BIG652", "VOLO_VOL", "PAS020", "bag652", 48.54, "15B"),
        ("BIG741", "VOLO_VUE", "PAS021", "bag741", 89.54, "6C"),
        ("BIG369", "VOLO_ALI", "PAS022", "bag369", 103.25, "10D"),
        ("BIG852", "VOLO_RYA", "PAS023", "bag852", 75.87, "21E"),
        ("BIG741", "VOLO_AIR", "PAS024", "bag741", 75.88, "5F"),
        ("BIG482", "VOLO_LUF", "PAS025", "bag482", 69.05, "12A")
    ]
    cursor.executemany("INSERT INTO Biglietto (ID_biglietto, ID_volo, ID_passeggero, ID_bagaglio, prezzo, N_posto) VALUES (%s, %s, %s, %s, %s, %s)", biglietti)
    db.commit()

except mysql.connector.Error as err:
    print(f"Errore: {err}")

finally:

    cursor.close()
    db.close()

