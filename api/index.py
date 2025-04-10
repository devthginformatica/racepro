from fastapi import FastAPI
import pymysql
import os

app = FastAPI()

@app.get("/")
def conectar_mysql():
    try:
        conn = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            connect_timeout=5
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()
        conn.close()
        return {"status": "Conectado com sucesso!", "hora": result}
    except Exception as e:
        return {"erro": str(e)}
