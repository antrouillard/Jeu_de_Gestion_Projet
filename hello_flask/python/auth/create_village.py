#coding : utf-8
from .. import con
from .tools import execute_insert_sql, execute_ID_sql


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


def create_village(user_id : int, name : str):
    sql, fdata = sql_create_village(user_id,name)
    village_id = execute_ID_sql(sql,fdata)
    sql, fdata = sql_create_ressource()
    res = execute_insert_sql(sql, fdata)
    sql, fdata = sql_create_production(village_id)
    res = execute_insert_sql(sql, fdata)
    sql, fdata = sql_create_entrepot(village_id)
    entrepot_id = execute_ID_sql(sql,fdata)
    sql, fdata = sql_create_stock(entrepot_id)
    res = execute_insert_sql(sql, fdata)
    for i in range(1,3):
        sql, fdata = sql_create_maison(2,village_id)
        maison_id = execute_ID_sql(sql,fdata)
        sql, fdata = sql_create_habitant(maison_id)
        res = execute_insert_sql(sql, fdata)
        sql, fdata = sql_create_habitant(maison_id)
        res = execute_insert_sql(sql, fdata)
    for i in range(1,3):
        sql, fdata = sql_create_maison(0,village_id)
        maison_id = execute_ID_sql(sql,fdata)
    con.commit()