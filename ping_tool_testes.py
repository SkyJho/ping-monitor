from typing import List, Dict
from fastapi import FastAPI, BackgroundTasks
import requests
import time
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from pydantic import BaseModel
import asyncio
from datetime import datetime
from fastapi import FastAPI
import httpx

# Criando a aplicação FastAPI
app = FastAPI()

# Dicionário para armazenar os status dos sites
site_status = {}

# Lista de sites a serem monitorados
sites_monitorados = ["https://www.google.com", "https://www.example.com"]  # Adicione mais sites aqui

# Permitir que o frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servindo arquivos estáticos e templates
templates = Jinja2Templates(directory="templates")

# Armazena os sites monitorados e seus status
sites: Dict[str, str] = {}

# Modelo para receber URLs
class SiteRequest(BaseModel):
    urls: List[str]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Função para verificar o status dos sites
def verificar_site(url: str):
    while True:
        try:
            response = requests.get(url, timeout=5)
            sites[url] = "Online ✅" if response.status_code == 200 else f"Offline ❌ (Código: {response.status_code})"
        except requests.RequestException:
            sites[url] = "Offline ❌ (Erro na requisição)"
        time.sleep(10)  # Aguarda 10 segundos antes da próxima verificação

# Endpoint para adicionar sites ao monitoramento
@app.post("/adicionar_site")
def adicionar_site(request: SiteRequest, background_tasks: BackgroundTasks):
    adicionados = []
    for url in request.urls:
        if url not in sites:
            sites[url] = "Verificando..."
            background_tasks.add_task(verificar_site, url)
            adicionados.append(url)
    return {"mensagem": "Sites adicionados", "sites": adicionados}

# Endpoint para listar os sites monitorados
@app.get("/sites")
def listar_sites():
    return {"sites": sites}

async def monitor_sites():
    """Função assíncrona para monitorar os sites periodicamente."""
    while True:
        for site in sites_monitorados:
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.get(site, timeout=5)
                    online = response.status_code == 200
            except Exception:
                online = False

            if site not in site_status:
                site_status[site] = {
                    "online": online,
                    "caiu_em": None,
                    "voltou_em": None
                }

            if online and not site_status[site]["online"]:
                site_status[site]["voltou_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if not online and site_status[site]["online"]:
                site_status[site]["caiu_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            site_status[site]["online"] = online
        
        await asyncio.sleep(10)  # Verifica a cada 10 segundos

@app.on_event("startup")
async def start_monitoring():
    """Inicia o monitoramento dos sites quando o servidor inicia."""
    asyncio.create_task(monitor_sites())

@app.get("/status")
async def get_status():
    """Retorna o status dos sites monitorados."""
    return site_status

app.mount("/static", StaticFiles(directory="static"), name="static")
