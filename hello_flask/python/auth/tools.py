# coding: utf-8
from .. import con
import hashlib
import random
import datetime

def execute_insert_sql(sql : str, fdata : dict):
    cr = con.cursor()
    cr.execute(sql, fdata)
    
def execute_sql(sql : str, fdata : dict):
    cr = con.cursor()
    cr.execute(sql, fdata)
    res = cr.fetchall()
    return res

def execute_ID_sql(sql : str, fdata : dict):
    cr = con.cursor()
    cr.execute(sql,fdata)
    save = cr.fetchone()[0]
    return save

def hash_sha512(value: str) -> str:
    h = hashlib.sha512()
    h.update(value.encode('utf-8'))
    return h.hexdigest()

def random_number() -> int :
    r=random.randint(0,1000000000)
    return r
    
def current_datetime() -> str:
    now = datetime.datetime.now()
    date_as_str : str = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_as_str
    

def token_for(login: str) -> str:
    token_content: str = ""
    # On génère un nombre aléatoire que l'on transforme en chaîne de caractère
    r_num = random_number()
    str_num: str = str(r_num)
    # On le hash et on le concatène à notre token
    token_content += hash_sha512(str_num)
    # On récupère la date actuel, on la hash et on la concatène
    c_date: str = current_datetime()   
    token_content += hash_sha512(c_date)
    # On hash et on ajoute le nom d'utilisateur au token
    token_content += hash_sha512(login)
    return hash_sha512(token_content)
