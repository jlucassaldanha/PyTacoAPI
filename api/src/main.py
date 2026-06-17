from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PyTACOAPI")

# 2. Definição de Contratos (Pydantic)
class UsuarioExemplo(BaseModel):
    id: int
    nome: str
    ativo: bool

# 3. Rota HTTP GET (Leitura)
@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    # O FastAPI automaticamente extrai o 'usuario_id' da URL,
    # converte para inteiro e valida.
    return {"mensagem": f"Buscando usuário {usuario_id}"}

# 4. Rota HTTP POST (Criação)
@app.post("/usuarios", response_model=UsuarioExemplo)
def criar_usuario(usuario: UsuarioExemplo):
    # O payload JSON do corpo da requisição é automaticamente 
    # convertido para o objeto 'UsuarioExemplo'.
    return usuario