import MySQLdb

def connect(hostname, username, pw, dbname):
    conn = MySQLdb.connect(
        host=hostname,
        user=username,
        passwd=pw,
        db=dbname,
        charset='utf-8'
    )
    return conn