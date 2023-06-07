--Antoine ROUILLARD
DROP TABLE Utilisateur CASCADE;
DROP TABLE Village CASCADE;
DROP TABLE Entrepôt CASCADE;
DROP TABLE Habitant CASCADE;
DROP TABLE Maison CASCADE;
DROP TABLE Production CASCADE;
DROP TABLE Batiment CASCADE;
DROP TABLE Ressource CASCADE;
DROP TABLE Stock CASCADE;


CREATE TABLE Utilisateur (
	idUser SERIAL PRIMARY KEY,
	login VARCHAR(30) NOT NULL,
	password VARCHAR(256) NOT NULL,
	token VARCHAR(256) NOT NULL
);

CREATE TABLE Village (
	idVillage SERIAL PRIMARY KEY,
	nomVillage VARCHAR(30) NOT NULL,
	nbHabitants int ,
	nbMaisons int,
	idUser int,
	FOREIGN KEY (idUser) references Utilisateur(idUser)
);

CREATE TABLE Entrepôt (
	idEntrepot SERIAL PRIMARY KEY,
	Capacité int,
	NiveauAmelioration int,
	idVillage int,
	FOREIGN KEY (idVillage) references  Village(idVillage)
);

CREATE TABLE Maison (
	idMaison SERIAL PRIMARY KEY,
	Capacité int,
	CapacitéTotale int,
	idVillage int,
	FOREIGN KEY (idVillage) references Village(idVillage)
);

CREATE TABLE Habitant (
	idHabitant SERIAL PRIMARY KEY,
	Nourri boolean,
	idMaison int,
	FOREIGN KEY (idMaison) references Maison(idMaison)
);

CREATE TABLE Production (
	état boolean NOT NULL PRIMARY KEY,
	nbHabitantsAffecté int,
	idVillage int,
	nbMine int,
	nbFerme int,
	nbScierie int,
	nbCarrière int,
	FOREIGN KEY (idVillage) references Village(idVillage)
);

/*CHANGER PRIMARY KEY PRODUCTION (Un boolean c'est bizarre)*/
CREATE TABLE Ressource (
	idRessource SERIAL PRIMARY KEY,
	typeRessource VARCHAR(30) NOT NULL
);

CREATE TABLE Batiment (
	idBatiment SERIAL PRIMARY KEY,
	typeBatiment VARCHAR(30) NOT NULL,
	nbHabitantsNécessaire int,
	idVillage int,
	idRessourceProduite int,
	qteProduite float,
	tempsProduction int,
	état boolean NOT NULL,
	FOREIGN KEY (idVillage) references Village(idVillage),
	FOREIGN KEY (idRessourceProduite) references Ressource(idRessource),
	FOREIGN KEY (état) references Production(état)
);



CREATE TABLE Stock (
	idStock SERIAL PRIMARY KEY,
	qteContenu float,
	idRessource int NOT NULL,
	idEntrepot int,
	FOREIGN KEY (idEntrepot) references Entrepôt(idEntrepot),
	FOREIGN KEY (idRessource) references Ressource(idRessource)
);
