SELECT e.`NumBonEntree` , e.`QteEntrer` , s.`QteSortie` FROM produit p
JOIN bondeentree e ON e.`NumProduit` = p.`NumProduit`
JOIN bondesortie s ON s.`NumProduit` = p.`NumProduit`