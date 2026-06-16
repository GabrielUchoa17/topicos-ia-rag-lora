
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="API - RAG + LoRA - O Alienista")

class ChatRequest(BaseModel):
    modelo: str
    pergunta: str

MODELS = {
    "tiny_gpt2": "sshleifer/tiny-gpt2 + LoRA",
    "tiny_random_gpt2": "hf-internal-testing/tiny-random-GPT2LMHeadModel + LoRA",
    "tiny_random_t5": "hf-internal-testing/tiny-random-t5 + LoRA",
    "flan_t5_small": "google/flan-t5-small + LoRA"
}

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/modelos")
def modelos():
    return {"modelos": MODELS}

@app.post("/chat")
def chat(req: ChatRequest):
    if req.modelo not in MODELS:
        return {
            "erro": "Modelo inválido",
            "modelos_disponiveis": list(MODELS.keys())
        }

    resposta = (
        "Resposta de demonstração da API. "
        "O pipeline treinou adaptadores LoRA e salvou os artefatos em models/. "
        "Pergunta recebida: " + req.pergunta
    )

    return {
        "modelo": req.modelo,
        "pergunta": req.pergunta,
        "resposta": resposta
    }
