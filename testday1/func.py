import pymysql



def jiafa (i,j):
    """
    这个方法是实现输入任意两个数值，输出他们的和
    """
    print(i+j)

def chaxun(sql):
    """
    数据库的查询
    """
    # pymysql.connect(host="",user="",password="",db="")
    db = pymysql.connect(host="106.52.239.168",user="root",password="1qaz!QAZ",db="ljtestdbb")
    # 游标
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    print(res)

# chaxun("select * from t_user limit 2;")