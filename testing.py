import pymysql

connection = pymysql.connect(
    host="your-rds-endpoint.amazonaws.com",
    user="admin",
    password="password",
    database="mydb",
    port=3306
)

print("Connected!")