-- Active: 1790159136923@@127.0.0.1@3306@stock
DROP TABLE IF EXISTS bondeentree;
DROP TABLE IF EXISTS bondesortie;
DROP TABLE IF EXISTS produit;



CREATE TABLE produit(
    NumProduit VARCHAR(10) PRIMARY KEY,
    Design VARCHAR(20),
    Stock INT
)

CREATE TABLE BonDeEntree(
    NumBonEntree VARCHAR(10) PRIMARY KEY,
    NumProduit VARCHAR(10),
    QteEntrer INT,
    DateEntree VARCHAR(10),
    FOREIGN KEY (NumProduit) REFERENCES produit (NumProduit) ON DELETE CASCADE
)


CREATE TABLE BonDeSortie(
    NumBonSortie VARCHAR(10) PRIMARY KEY,
    NumProduit VARCHAR(10),
    QteSortie INT,
    DateSortie VARCHAR(10),
    FOREIGN KEY (NumProduit) REFERENCES produit (NumProduit) ON DELETE CASCADE
)

