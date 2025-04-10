from fastapi import FastAPI
import pymysql
import os

app = FastAPI()

@app.get("/")
def conectar_mysql():
    try:
        conn = pymysql.connect(
            host=os.getenv("190.89.249.24"),
            user=os.getenv("db_user_racepro"),
            password=os.getenv("hfbga@h764Hg"),
            database=os.getenv("racepro_db"),
            port=int(os.getenv("3306")),
            connect_timeout=5
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW();")
            result = cursor.fetchone()
        conn.close()
        return {"status": "Conectado com sucesso!", "hora": result}
    except Exception as e:
        return {"erro": str(e)}
