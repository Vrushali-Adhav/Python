import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='8805291205',port='3306')
if conn.is_connected():
    
    print("you are succeffull connected to "+str(conn.get_server_info()))

    handle=conn.cursor()
   ''' handle.execute("CREATE DATABASE PYTHON;")'''
'''else:
    print("not connected")'''

