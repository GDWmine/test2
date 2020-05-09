import pymysql


def chaxun(sql):
    """
    数据库的查询
    """
    # pymysql.connect(host="",user="",password="",db="")
    # db = pymysql.connect(host="106.52.239.168",user="root",password="1qaz!QAZ",db="ljtestdbb")
    db = pymysql.connect (host="192.144.148.91",user="ljtest",password="123456",db="ljtestdb")
    # 游标
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return res

# chaxun("select * from t_user limit 2;")