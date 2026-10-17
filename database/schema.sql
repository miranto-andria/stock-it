CREATE DATABASE IF NOT EXISTS stock_it
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE Produit (
    NumProduit   VARCHAR(50)  NOT NULL,
    Design       VARCHAR(255) NOT NULL,
    Stock        INT          NOT NULL DEFAULT 0,
    PRIMARY KEY (NumProduit)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE BondeEntree (
    NumBon     VARCHAR(50) NOT NULL,
    NumProduit VARCHAR(50) NOT NULL,
    QteEntree  INT         NOT NULL,
    DateEntree DATE        NOT NULL,
    PRIMARY KEY (NumBon, NumProduit),
    FOREIGN KEY (NumProduit) REFERENCES Produit(NumProduit) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE BondeSortie (
    NumBon     VARCHAR(50) NOT NULL,
    NumProduit VARCHAR(50) NOT NULL,
    QteSortie  INT         NOT NULL,
    DateSortie DATE        NOT NULL,
    PRIMARY KEY (NumBon, NumProduit),
    FOREIGN KEY (NumProduit) REFERENCES Produit(NumProduit) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;