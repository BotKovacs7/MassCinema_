CREATE DATABASE masscinema DEFAULT CHARACTER SET utf8 COLLATE utf8_hungarian_ci;
USE masscinema;
CREATE TABLE Termek (
    Terem_szam INT PRIMARY KEY,
    Film_cime VARCHAR(255),
    Ev INT,
    Mufaj VARCHAR(100),
    Jatekido VARCHAR(50),
    Kapacitas INT
);

CREATE TABLE Foglalasok (
    Foglalas_sorszam INT PRIMARY KEY,
    Keresztnev VARCHAR(100),
    Vezeteknev VARCHAR(100),
    Teremszam INT,
    Szekszam INT,
    FOREIGN KEY (Teremszam) REFERENCES Termek(Terem_szam)
);
INSERT INTO Termek (Terem_szam, Film_cime, Ev, Mufaj, Jatekido, Kapacitas) VALUES
(1, 'A galaxis őrzői', 2014, 'Sci-Fi', '121 min', 150),
(2, 'Joker', 2019, 'Dráma', '122 min', 120),
(3, 'Harry Potter', 2001, 'Fantasy', '152 min', 180),
(4, 'Tenet', 2020, 'Akció', '150 min', 100),
(5, 'The Matrix', 1999, 'Sci-Fi', '136 min', 200);
(6, 'Inception', 2010, 'Akció', '148 min', 130),
(7, 'The Dark Knight', 2008, 'Akció', '152 min', 180);

INSERT INTO Foglalasok (Foglalas_sorszam, Keresztnev, Vezeteknev, Teremszam, Szekszam) VALUES
(1, 'Anna', 'Kovács', 1, 23),
(2, 'Béla', 'Szabó', 3, 45),
(3, 'Csaba', 'Tóth', 2, 10),
(4, 'Dóra', 'Kiss', 4, 30),
(5, 'László', 'Horváth', 5, 15);
(6, 'Zoltán', 'Nagy', 6, 25),
(7, 'Eszter', 'Molnár', 7, 40);
