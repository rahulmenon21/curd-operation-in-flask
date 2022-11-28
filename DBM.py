import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='flaskbackendproject',port=3306)
    
def addAuthor(t):
    db=getConnection()
    sql='insert into author values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def addUser(t):
    db=getConnection()
    sql='insert into user values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def selectAllPost():
    db=getConnection()
    cr=db.cursor()
    sql='select * from Author_Post'
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

    
def deleteEmp(email):
    db=getConnection()
    cr=db.cursor()
    sql='delete from  user where email=%s'
    cr.execute(sql,email)
    db.commit()
    db.close()

def selectEmpById(email):
    db=getConnection()
    sql='select * from user where email=%s'
    cr=db.cursor()
    cr.execute(sql,email)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateEmp(t):
    db=getConnection()
    sql='update user set name=%s,email=%s,Password=%s,city=%s where email=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def checkalg(t):
    db=getConnection()
    sql='select email,password from author where email=%s'
    cr=db.cursor()
    cr.execute(sql,t[0])
    data=cr.fetchall()
    db.commit()
    db.close()
    return data


def checkulg(t):
    db=getConnection()
    cr=db.cursor()
    sql='select email,password from user where email=%s'
    cr.execute(sql,t[0])
    data1=cr.fetchall()
    db.commit()
    db.close()
    return data1

def blogcheck2(t):
    db=getConnection()
    cr=db.cursor()
    sql='insert into Author_Post values(%s,%s,%s)'
    cr.execute(sql,t)
    db.commit()
    db.close()


#def addblog(t):
#    db=getConnection()
#    cr=db.cursor()
#    sql='insert into Author_Post values(%s,%s,%s)'
#    cr.execute(sql,t)
#    db.commit()
#    db.close()