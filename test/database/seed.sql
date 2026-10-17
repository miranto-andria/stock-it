INSERT INTO produit (`NumProduit` , `Design` , `Stock`)
VALUES
("P001" , "Riz" , 100),
("P002" , "Blé" , 200)

INSERT INTO bondeentree(`NumBonEntree` , `NumProduit` , `QteEntrer`)
VALUES
("E001" , "P001" , 10),
("E002" , "P002" , 15)


INSERT INTO bondesortie(`NumBonSortie` , `NumProduit` , `QteSortie`)
VALUES
("S001" , "P001" , 50),
("S002" , "P002" , 5)

-- SELECT p.`NumProduit` , p.`Stock` , b.`NumBonEntree` , b.`QteEntrer` , s.`NumBonSortie`, s.`QteSortie` , b.`QteEntrer` + p.`Stock` - s.`QteSortie` FROM produit p
-- JOIN bondeentree b ON b.`NumProduit` = p.`NumProduit`
-- JOIN bondesortie s ON s.`NumProduit` = p.`NumProduit`

UPDATE produit p 
JOIN bondeentree e ON p.`NumProduit` = e.`NumProduit`
JOIN bondesortie s ON p.`NumProduit` = s.`NumProduit`
SET p.`Stock` = p.`Stock` + e.`QteEntrer` - s.`QteSortie` 

SELECT * FROM produit