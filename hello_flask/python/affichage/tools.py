# coding: utf-8
from .. import con

def execute_sql(sql : str, fdata : dict):
    cr = con.cursor()
    cr.execute(sql, fdata)
    res = cr.fetchall()
    return res