import sqlite3

# 1. 拨通内存数据库的电话
conn = sqlite3.connect(":memory:")
# 2. 雇佣一个传话员
cursor = conn.cursor()

# 3. 建表塞数据
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, '张三')")

# 4. 正常查询
print("正常查：", cursor.execute("SELECT * FROM users").fetchall())

# 5. 黑客注入！
payload = "1' UNION SELECT 2, '黑客窃取的密码'--"
sql = f"SELECT * FROM users WHERE id = '{payload}'"
print("注入查：", cursor.execute(sql).fetchall())

conn.close()