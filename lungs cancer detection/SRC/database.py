import pymysql
def iud(qry,values):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="", db='lungs_cancer_detection')
    cmd = con.cursor()
    cmd.execute(qry,values)
    id=cmd.lastrowid
    con.commit()
    return id

def selectall(qry):
    con=pymysql.connect(host="localhost",port=3306,user="root",password="",db='lungs_cancer_detection')
    cmd=con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    con.close()
    return res

def select(qry,values):
    con=pymysql.connect(host="localhost",port=3306,user="root",password="",db='lungs_cancer_detection')
    cmd=con.cursor()
    cmd.execute(qry,values)
    res=cmd.fetchone()
    con.close()
    return res

def selecte(qry,values):
    con=pymysql.connect(host="localhost",port=3306,user="root",password="",db='lungs_cancer_detection')
    cmd=con.cursor()
    cmd.execute(qry,values)
    res=cmd.fetchall()
    con.close()
    return res