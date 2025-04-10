from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

app = FastAPI()

# Login simples (exemplo)
@app.post("/login")
def login(usuario: str = Form(...), senha: str = Form(...)):
    if usuario == "admin" and senha == "123":
        return {"status": "ok", "usuario": "admin", "foto": "https://via.placeholder.com/150"}
    return JSONResponse(status_code=401, content={"erro": "Usuário ou senha inválidos"})
