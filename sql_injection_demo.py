import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'super_secret_password')")
conn.commit()

username = input("请输入用户名: ")
password = input("请输入密码: ")

# 注意这一行必须在一行里，不能按回车断开！
sql_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print(f"\n正在执行: {sql_query}")

cursor.execute(sql_query)
result = cursor.fetchall()

if result:
    print(f"✅ 登录成功！账号: {result[0][0]}")
else:
    print("❌ 登录失败！")
conn.close()