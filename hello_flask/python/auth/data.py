# coding : utf-8

from flask import session

from .. import con
from .create_village import create_village
from .tools import execute_sql, execute_insert_sql


def sql_select_login_psswrd(login : str,hashed_password: str) -> (str,dict):
    sql: str = "SELECT idUser, login FROM Utilisateur WHERE login = %(login)s AND password = %(hashed_password)s;"
    fdata: dict = {
        "login": login,
        "hashed_password": hashed_password,
    }
    return sql,fdata

def is_credential_correct(login:str, hashed_password: str) -> bool :
    sql, fdata = sql_select_login_psswrd(login,hashed_password)
    res = execute_sql(sql, fdata)
    if res == [] :
        return False
    else :
        return True

def sql_update_token(login : str,token: str) -> (str,dict):
    sql: str = "UPDATE Utilisateur SET token =%(token)s WHERE login = %(login)s"
    fdata: dict = {
        "login": login,
        "token": token,
    }
    return sql,fdata
    
def set_token(login: str, token: str):
    sql,fdata = sql_update_token(login,token)
    execute_insert_sql(sql, fdata)
    con.commit()
    
def sql_select_token(token: str) -> (str,dict):
    sql: str = "SELECT token FROM Utilisateur WHERE token = %(token)s;"
    fdata: dict = {
        "token": token,
    }
    return sql,fdata   
    
def check_token_validity(token : str):
    sql, fdata = sql_select_token(token)
    res = execute_sql(sql, fdata)
    if res == [] :
        return False
    else :
        return True
    
def sql_insert_login_psswrd(login : str,password: str,token : str) -> (str,dict):
    sql: str = "INSERT INTO Utilisateur(login,password,token) VALUES (%(login)s,%(password)s,%(token)s);"
    fdata: dict = {
        "login": login,
        "password": password,
        "token": token,
    }
    return sql,fdata

def sql_select_user_id(token: str) -> (str,dict):
    sql: str = "SELECT idUser FROM Utilisateur WHERE token = %(token)s;"
    fdata: dict = {
        "token": token,
    }
    return sql,fdata  

def create_user(login : str, password : str, token : str,nomVillage : str):
    sql,fdata = sql_insert_login_psswrd(login,password,token)
    execute_insert_sql(sql, fdata)
    sql,fdata = sql_select_user_id(token)
    user_id = execute_sql(sql, fdata)
    user_id = user_id[0]
    create_village(user_id,nomVillage)
    con.commit()
    
def logged_in() -> bool:
    token: str = session.get("token", None)
    if token:
        token_valid: bool = check_token_validity(token)
        if token_valid:
            return True
    return False