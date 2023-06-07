--Antoine ROUILARD


INSERT INTO Utilisateur(login,password)
VALUES
('toto');

INSERT INTO Village(nomVillage,nbMaisons,nbHabitants,idUser)
VALUES
('TotoVille',6,4,1);

INSERT INTO Ressource(typeRessource)
VALUES
('Nourriture'),
('Bois'),
('Pierre'),
('Fer');

INSERT INTO Production (état,idVillage,nbMine,nbFerme,nbScierie,nbCarrière)
VALUES
(True,1,0,0,0,0);

INSERT INTO Batiment(typeBatiment,nbHabitantsNécessaire,idRessourceProduite,qteProduite,tempsProduction,état,idVillage)
VALUES
('Ferme',2,1,9,1,True,1),
('Scierie',3,2,5,1,True,1),
('Carrière',3,3,5,1,True,1),
('Mine',5,4,2.5,1,True,1);

UPDATE Production
SET nbMine = nbMine + 1,nbFerme = nbFerme + 1,nbScierie = nbScierie + 1,nbCarrière = nbCarrière + 1
WHERE idVillage = 1;

INSERT INTO Entrepôt(Capacité,NiveauAmelioration,idVillage)
VALUES
(300,1,1);

INSERT INTO Stock(qteContenu,idRessource,idEntrepot)
VALUES
(50,1,1),
(20,2,1),
(10,3,1),
(0,4,1);

INSERT INTO Maison(Capacité,idVillage)
VALUES
(2,1),
(2,1),
(0,1),
(0,1),
(0,1),
(0,1);

INSERT INTO Habitant(Nourri,idMaison)
VALUES
(True,1),
(True,1),
(True,2),
(True,2);

/*UPDATE Stock 
SET qteContenu = qteContenu + 9
WHERE idRessource = 1;

UPDATE Stock 
SET qteContenu = qteContenu + 5
WHERE idRessource = 2;

UPDATE Stock 
SET qteContenu = qteContenu + 5
WHERE idRessource = 3;

UPDATE Stock 
SET qteContenu = qteContenu + 2.5
WHERE idRessource = 4;

UPDATE Village
SET nbMaisons = nbMaisons +1;*/

INSERT INTO Maison(Capacité,idVillage)
VALUES
(0,1);

SELECT Batiment.typeBatiment,Production.nbFerme
FROM Batiment, Village, Production
WHERE Village.idVillage = Batiment.idVillage AND Production.idVillage = Village.idVillage ;

SELECT Stock.qteContenu,Ressource.typeRessource
FROM Stock, Village, Ressource, Entrepôt
WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage AND Stock.idRessource = Ressource.idRessource;

SELECT Entrepôt.Capacité, sum(Stock.qteContenu)
FROM Stock,Village, Entrepôt
WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage;

SELECT Village.nbHabitants - Production.nbHabitantsAffecté as nbHabitantsLibres FROM Village,Production WHERE Village.idVillage = Production.idVillage