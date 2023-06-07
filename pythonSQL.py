import psycopg2
import sys
sys.path.append(".local/lib/python3.10/site-packages")
from tabulate import tabulate
# Pensez a adapter les parametre ci-dessous à votre environnement
# Votre base de donnee doit etre creer avant de lancer ce script
con = psycopg2.connect(host='localhost', user='management_game', password='ant', dbname='bd')

def execute_sql(sql: str, fdata: dict):
    cr = con.cursor()
    res = cr.execute(sql, fdata)
    return res
    
def execute_ID_sql(sql : str, fdata : dict):
    cr = con.cursor()
    res = cr.execute(sql, fdata)
    res = cr.fetchone()[0]
    return res
    
def execute_select_sql(sql : str, fdata : dict):
    cr = con.cursor()
    cr.execute(sql, fdata)
    col_names = [desc[0] for desc in cr.description]
    res = cr.fetchall()
    return res,col_names

def sql_create_user(username: str) -> (str,dict):
    sql: str = "INSERT INTO Utilisateur(login) VALUES (%(username)s)"
    fdata : dict = {
        "username": username,
    }
    return sql,fdata

def sql_create_entrepot(village_id : int) -> (str,dict):
    sql: str = "INSERT INTO Entrepôt(Capacité,NiveauAmelioration,idVillage) VALUES (300,1,%(village_id)s) RETURNING idEntrepot"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
 
def sql_create_village(user_id : int, name : str) -> (str,dict):
    sql: str = "INSERT INTO Village(nomVillage,nbMaisons,nbHabitants,idUser) VALUES (%(name)s,6,6,%(user_id)s) RETURNING idVillage"
    fdata: dict = {
        "user_id" : user_id,
        "name" : name,
    }
    return sql,fdata

def sql_create_maison(nbHabitant : int, village_id : int) -> (str,dict):
    sql: str = "INSERT INTO Maison(Capacité,CapacitéTotale,idVillage) VALUES (%(nbHabitant)s,2,%(village_id)s) RETURNING idMaison"
    fdata: dict = {
        "nbHabitant": nbHabitant,
        "village_id": village_id,
    }
    return sql,fdata

def sql_create_habitant(maison_id : int) -> (str,dict):
    sql: str = "INSERT INTO Habitant(Nourri,idMaison) VALUES (True,%(maison_id)s)"
    fdata: dict = {
        "maison_id": maison_id,
    }
    return sql,fdata

def sql_create_ressource() -> (str,dict):
    sql: str = "INSERT INTO Ressource(typeRessource) VALUES ('Nourriture'),('Bois'),('Pierre'),('Fer');"
    fdata: dict = {
    }
    return sql,fdata

def sql_create_stock(entrepot_id : int) -> (str,dict):
    sql: str = "INSERT INTO Stock(qteContenu,idRessource,idEntrepot) VALUES (50,1,%(entrepot_id)s),(20,2,%(entrepot_id)s),(10,3,%(entrepot_id)s),(0,4,%(entrepot_id)s);"
    fdata: dict = {
        "entrepot_id": entrepot_id,
    }
    return sql,fdata

def sql_create_production(village_id : int) -> (str,dict):
    sql: str = "INSERT INTO Production(état,idVillage,nbMine,nbFerme,nbScierie,nbCarrière) VALUES (True,%(village_id)s,0,0,0,0);"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
    
def create_user(username: str) :
    sql, fdata = sql_create_user(username)
    res = execute_sql(sql, fdata)
    con.commit()

def create_village(user_id : int, name : str):
    sql, fdata = sql_create_village(user_id,name)
    village_id = execute_ID_sql(sql,fdata)
    sql, fdata = sql_create_ressource()
    res = execute_sql(sql, fdata)
    sql, fdata = sql_create_production(village_id)
    res = execute_sql(sql, fdata)
    sql, fdata = sql_create_entrepot(village_id)
    entrepot_id = execute_ID_sql(sql,fdata)
    sql, fdata = sql_create_stock(entrepot_id)
    res = execute_sql(sql, fdata)
    for i in range(1,3):
        sql, fdata = sql_create_maison(2,village_id)
        maison_id = execute_ID_sql(sql,fdata)
        sql, fdata = sql_create_habitant(maison_id)
        res = execute_sql(sql, fdata)
        sql, fdata = sql_create_habitant(maison_id)
        res = execute_sql(sql, fdata)
    for i in range(1,3):
        sql, fdata = sql_create_maison(0,village_id)
        maison_id = execute_ID_sql(sql,fdata)
    con.commit()
    
def sql_show_village_summary_village(village_id : int) -> (str,dict):
    sql: str = "SELECT Village.nomVillage, Village.nbHabitants,Village.nbMaisons FROM Village WHERE Village.idVillage = %(village_id)s"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
    
def sql_show_village_summary_stock(village_id :  int) -> (str,dict):
    sql: str = "SELECT Stock.qteContenu,Ressource.typeRessource FROM Stock, Ressource, Entrepôt WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = %(village_id)s AND Stock.idRessource = Ressource.idRessource;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
    
def sql_show_village_summary_batFerme(village_id : int) -> (str,dict):
    sql: str = "SELECT Batiment.typeBatiment,Production.nbFerme FROM Batiment, Village, Production WHERE Batiment.idVillage = %(village_id)s AND Production.idVillage = %(village_id)s ;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
def sql_show_village_summary_batMine(village_id : int) -> (str,dict):
    sql: str = "SELECT Batiment.typeBatiment,Production.nbMine FROM Batiment, Village, Production WHERE Batiment.idVillage = %(village_id)s AND Production.idVillage = %(village_id)s ;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
def sql_show_village_summary_batCarriere(village_id : int) -> (str,dict):
    sql: str = "SELECT Batiment.typeBatiment,Production.nbCarrière FROM Batiment, Village, Production WHERE Batiment.idVillage = %(village_id)s AND Production.idVillage = %(village_id)s ;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
def sql_show_village_summary_batScierie(village_id : int) -> (str,dict):
    sql: str = "SELECT Batiment.typeBatiment,Production.nbScierie FROM Batiment, Village, Production WHERE Batiment.idVillage = %(village_id)s AND Production.idVillage = %(village_id)s ;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata
    
def sql_show_village_summary_habBusy(village_id :  int) -> (str,dict):
    sql: str = "SELECT Production.nbHabitantsAffecté FROM Village,Production WHERE Village.idVillage = Production.idVillage and Village.idVillage = %(village_id)s;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata

def sql_show_village_summary_habLibres(village_id :  int) -> (str,dict):
    sql: str = "SELECT Village.nbHabitants - Production.nbHabitantsAffecté as nbHabitantsLibres FROM Village,Production WHERE Village.idVillage = %(village_id)s and Production.idVillage = Village.idVillage;"
    fdata: dict = {
        "village_id": village_id,
    }
    return sql,fdata

def show_village_summary(village_id : int):
    #Récap village
    sql, fdata = sql_show_village_summary_village(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    #Récap stock
    sql, fdata = sql_show_village_summary_stock(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    #Récap batiments
    sql, fdata = sql_show_village_summary_batFerme(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    sql, fdata = sql_show_village_summary_batScierie(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    sql, fdata = sql_show_village_summary_batCarriere(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    sql, fdata = sql_show_village_summary_batMine(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    #Récap habitants busy
    sql, fdata = sql_show_village_summary_habBusy(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    #Récap habitants libres
    sql, fdata = sql_show_village_summary_habLibres(village_id)
    res,col_names = execute_select_sql(sql, fdata)
    print(tabulate(res, headers=col_names, tablefmt="psql"))
    con.commit()

    


"""
CREATE TABLE users (
  name VARCHAR(30),
  first_name VARCHAR(30),
  login VARCHAR(30) PRIMARY KEY,
  pssword VARCHAR(30)
);
"""

print("Si ce message apparait, votre environnement postgresql + python est pret ^^)")

create_user('toto')
create_village(1,'totoVille')
show_village_summary(1)