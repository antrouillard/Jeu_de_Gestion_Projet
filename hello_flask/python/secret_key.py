# coding: utf-8
import hashlib
import random

def hash_sha512(value: str) -> str:
    h = hashlib.sha512()
    h.update(value.encode('utf-8'))
    return h.hexdigest()
    
def random_number() -> int :
    r=random.randint(0,1000000000)
    return r
    
def generate_secret_key() -> str:
    secret_key: str = ""
    # On génère un nombre aléatoire que l'on transforme en chaîne de caractère
    r_num = random_number()
    str_num: str = str(r_num)
    # On le hash et on le concatène à notre token
    secret_key += hash_sha512(str_num)
    return hash_sha512(secret_key)
    
