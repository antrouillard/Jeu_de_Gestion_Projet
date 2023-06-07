# coding: utf-8
from flask import Flask, render_template,request,session, redirect, jsonify
from .. import app
from .tools import execute_sql

def sql_select_login(token: str) -> (str,dict):
    sql: str = "SELECT login FROM Utilisateur WHERE token = %(token)s;"
    fdata: dict = {
        "token": token,
    }
    return sql,fdata    
 
def sql_select_nbHabitants(login : str) -> (str,dict):
    sql: str = "SELECT Village.nbHabitants FROM Village, Utilisateur WHERE Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata
    
def sql_select_nbMaisons(login : str) -> (str,dict):
    sql: str = "SELECT Village.nbMaisons FROM Village, Utilisateur WHERE Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata    

def sql_select_nbFer(login : str) -> (str,dict):
    sql: str = "SELECT Stock.qteContenu FROM Stock, Ressource, Entrepôt,Village, Utilisateur WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage AND Stock.idRessource = 4 AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata

def sql_select_nbNouritture(login : str) -> (str,dict):
    sql: str = "SELECT Stock.qteContenu FROM Stock, Ressource, Entrepôt,Village, Utilisateur WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage AND Stock.idRessource = 1 AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata    

def sql_select_nbBois(login : str) -> (str,dict):
    sql: str = "SELECT Stock.qteContenu FROM Stock, Ressource, Entrepôt,Village, Utilisateur WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage AND Stock.idRessource = 2 AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata  
    
def sql_select_nbPierre(login : str) -> (str,dict):
    sql: str = "SELECT Stock.qteContenu FROM Stock, Ressource, Entrepôt,Village, Utilisateur WHERE Stock.idEntrepot = Entrepôt.idEntrepot AND Entrepôt.idVillage = Village.idVillage AND Stock.idRessource = 3 AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata      
  
def sql_select_nbFermes(login : str) -> (str,dict):
    sql: str = "SELECT Production.nbFerme FROM Batiment, Village, Production, Utilisateur WHERE Batiment.idVillage = Village.idVillage AND Production.idVillage = Village.idVillage AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata 
    
def sql_select_nbScieries(login : str) -> (str,dict):
    sql: str = "SELECT Production.nbScierie FROM Batiment, Village, Production, Utilisateur WHERE Batiment.idVillage = Village.idVillage AND Production.idVillage = Village.idVillage AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata 
    
def sql_select_nbCarrieres(login : str) -> (str,dict):
    sql: str = "SELECT Production.nbCarrière FROM Batiment, Village, Production, Utilisateur WHERE Batiment.idVillage = Village.idVillage AND Production.idVillage = Village.idVillage AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata
    
def sql_select_nbMines(login : str) -> (str,dict):
    sql: str = "SELECT Production.nbMine FROM Batiment, Village, Production, Utilisateur WHERE Batiment.idVillage = Village.idVillage AND Production.idVillage = Village.idVillage AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata
    
def sql_select_nivEntrepot(login : str) -> (str,dict):
    sql: str = "SELECT Entrepôt.NiveauAmelioration FROM Entrepôt, Village,Utilisateur WHERE Entrepôt.idVillage = Village.idVillage AND Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata
    
def sql_select_nomVillage(login : str) -> (str,dict):
    sql: str = "SELECT Village.nomVillage FROM Village,Utilisateur WHERE Utilisateur.login = %(login)s AND Utilisateur.idUser = Village.idUser;"
    fdata: dict = {
        "login": login,
    }
    return sql,fdata
  
@app.route("/affiche_hab", methods=["GET"])
def affiche_hab():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbHabitants(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_maisons", methods=["GET"])
def affiche_maisons():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbMaisons(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbFer", methods=["GET"])
def affiche_nbFer():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbFer(log)
    res = execute_sql(sql, fdata)
    res = res[0]
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbNouritture", methods=["GET"])
def affiche_nbNouritture():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbNouritture(log)
    res = execute_sql(sql, fdata)
    res = res[0]
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbBois", methods=["GET"])
def affiche_nbBois():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbBois(log)
    res = execute_sql(sql, fdata)
    res = res[0]
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbPierre", methods=["GET"])
def affiche_nbPierre():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbPierre(log)
    res = execute_sql(sql, fdata)
    res = res[0]
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbFermes", methods=["GET"])
def affiche_nbFermes():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbFermes(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbScieries", methods=["GET"])
def affiche_nbScieries():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbScieries(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbCarrieres", methods=["GET"])
def affiche_nbCarrieres():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbCarrieres(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nbMines", methods=["GET"])
def affiche_nbMines():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nbMines(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_nivEntrepot", methods=["GET"])
def affiche_nivEntrepot():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nivEntrepot(log)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)
    
@app.route("/affiche_login", methods=["GET"])
def affiche_login():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    return jsonify(log)

@app.route("/affiche_nomVillage", methods=["GET"])
def affiche_nomVillage():
    token = session["token"]
    sql, fdata = sql_select_login(token)
    login = execute_sql(sql, fdata)
    log = login[0]
    log = '{}'.format(*log)
    sql, fdata = sql_select_nomVillage(token)
    res = execute_sql(sql, fdata)
    if not res:
        res = "0"
    return jsonify(res)