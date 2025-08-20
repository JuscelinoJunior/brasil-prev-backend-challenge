from fastapi import FastAPI
from simulator import Simulator

app = FastAPI(
    title="Simulador de Banco Imobiliário simplificado",
    version="1.0.0"
)

@app.get("/jogo/simular")
def simulate_game():
    simulator = Simulator()
    return simulator.simulate()