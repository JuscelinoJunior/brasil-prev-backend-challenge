# Brasil Prev Backend Challenge
HTTP API desenvolvida para desafio de desenvolvimento da Brasil Prev. Simula um jogo simplificado de Banco Imobiliário.

## Tecnologias utilizadas
- Python 3.11
- FastAPI
- Pytest

## Funcionalidades
A API consiste em um único endpoint GET /jogo/simular

Bônus: Para além da resposta da API sugerida no desafio, a API retorna também uma lista de "rodadas", sendo cada
item da lista um objeto com todos os jogadores que jogaram aquela rodada, em ordem, com o resultado que cada um obteve
com a sua jogada naquela rodada.

A API retorna as seguintes propriedades:
- "vencedor": nome do vencedor da partida
- "jogadores": lista em ordem pelo saldo final dos jogadores, sendo sempre estes os jogadores: ["aleatorio", "cauteloso", "impulsivo", "exigente"]
- "quantidade-rodadas": a quantidade de rodadas que foram jogadas
- "rodadas": lista com as ações e resultados de cada jogador em cada rodada.

Exemplo de resposta da API:
<details>
<summary>Exemplo JSON</summary>

```json
{
  "vencedor": "aleatorio",
  "jogadores": [
    "aleatorio",
    "cauteloso",
    "impulsivo",
    "exigente"
  ],
  "quantidade-rodadas": 26,
  "rodadas": [
    {
      "impulsivo": {
        "dado": 6,
        "propriedade": 6,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 127,
        "saldos": {
          "impulsivo": 173,
          "exigente": 300,
          "cauteloso": 300,
          "aleatorio": 300
        }
      },
      "exigente": {
        "dado": 3,
        "propriedade": 3,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 82,
        "saldos": {
          "impulsivo": 173,
          "exigente": 218,
          "cauteloso": 300,
          "aleatorio": 300
        }
      },
      "cauteloso": {
        "dado": 2,
        "propriedade": 2,
        "propriedade-dono": "cauteloso",
        "acao": "buy",
        "gasto": 77,
        "saldos": {
          "impulsivo": 173,
          "exigente": 218,
          "cauteloso": 223,
          "aleatorio": 300
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 5,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 173,
          "exigente": 218,
          "cauteloso": 223,
          "aleatorio": 300
        }
      }
    },
    {
      "impulsivo": {
        "dado": 2,
        "propriedade": 8,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 73,
        "saldos": {
          "impulsivo": 100,
          "exigente": 218,
          "cauteloso": 223,
          "aleatorio": 300
        }
      },
      "exigente": {
        "dado": 2,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 106,
        "saldos": {
          "impulsivo": 100,
          "exigente": 112,
          "cauteloso": 223,
          "aleatorio": 300
        }
      },
      "cauteloso": {
        "dado": 2,
        "propriedade": 4,
        "propriedade-dono": "cauteloso",
        "acao": "buy",
        "gasto": 66,
        "saldos": {
          "impulsivo": 100,
          "exigente": 112,
          "cauteloso": 157,
          "aleatorio": 300
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 10,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 100,
          "exigente": 112,
          "cauteloso": 157,
          "aleatorio": 300
        }
      }
    },
    {
      "impulsivo": {
        "dado": 2,
        "propriedade": 10,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 100,
          "exigente": 112,
          "cauteloso": 157,
          "aleatorio": 300
        }
      },
      "exigente": {
        "dado": 4,
        "propriedade": 9,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 100,
          "exigente": 112,
          "cauteloso": 157,
          "aleatorio": 300
        }
      },
      "cauteloso": {
        "dado": 2,
        "propriedade": 6,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 40,
        "saldos": {
          "impulsivo": 140,
          "exigente": 112,
          "cauteloso": 117,
          "aleatorio": 300
        }
      },
      "aleatorio": {
        "dado": 2,
        "propriedade": 12,
        "propriedade-dono": "aleatorio",
        "acao": "buy",
        "gasto": 150,
        "saldos": {
          "impulsivo": 140,
          "exigente": 112,
          "cauteloso": 117,
          "aleatorio": 150
        }
      }
    },
    {
      "impulsivo": {
        "dado": 1,
        "propriedade": 11,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 127,
        "saldos": {
          "impulsivo": 13,
          "exigente": 112,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "exigente": {
        "dado": 5,
        "propriedade": 14,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 103,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "cauteloso": {
        "dado": 1,
        "propriedade": 7,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "aleatorio": {
        "dado": 3,
        "propriedade": 15,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      }
    },
    {
      "impulsivo": {
        "dado": 4,
        "propriedade": 15,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "exigente": {
        "dado": 1,
        "propriedade": 15,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "cauteloso": {
        "dado": 6,
        "propriedade": 13,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 150
        }
      },
      "aleatorio": {
        "dado": 4,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "buy",
        "gasto": 131,
        "saldos": {
          "impulsivo": 13,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 19
        }
      }
    },
    {
      "impulsivo": {
        "dado": 5,
        "propriedade": 0,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 19
        }
      },
      "exigente": {
        "dado": 3,
        "propriedade": 18,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 19
        }
      },
      "cauteloso": {
        "dado": 4,
        "propriedade": 17,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 19
        }
      },
      "aleatorio": {
        "dado": 2,
        "propriedade": 1,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 119
        }
      }
    },
    {
      "impulsivo": {
        "dado": 1,
        "propriedade": 1,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 9,
          "cauteloso": 117,
          "aleatorio": 119
        }
      },
      "exigente": {
        "dado": 2,
        "propriedade": 0,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 113,
          "exigente": 109,
          "cauteloso": 117,
          "aleatorio": 119
        }
      },
      "cauteloso": {
        "dado": 2,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "impulsivo": 113,
          "exigente": 109,
          "cauteloso": 19,
          "aleatorio": 217
        }
      },
      "aleatorio": {
        "dado": 4,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 93,
        "saldos": {
          "impulsivo": 113,
          "exigente": 202,
          "cauteloso": 19,
          "aleatorio": 124
        }
      }
    },
    {
      "impulsivo": {
        "dado": 6,
        "propriedade": 7,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 102,
        "saldos": {
          "impulsivo": 11,
          "exigente": 202,
          "cauteloso": 19,
          "aleatorio": 124
        }
      },
      "exigente": {
        "dado": 5,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 93,
        "saldos": {
          "impulsivo": 11,
          "exigente": 202,
          "cauteloso": 19,
          "aleatorio": 124
        }
      },
      "cauteloso": {
        "dado": 4,
        "propriedade": 3,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 79,
        "saldos": {
          "impulsivo": 11,
          "exigente": 281,
          "cauteloso": 40,
          "aleatorio": 124
        }
      },
      "aleatorio": {
        "dado": 2,
        "propriedade": 7,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 78,
        "saldos": {
          "impulsivo": 89,
          "exigente": 281,
          "cauteloso": 40,
          "aleatorio": 46
        }
      }
    },
    {
      "impulsivo": {
        "dado": 2,
        "propriedade": 9,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 89,
          "exigente": 281,
          "cauteloso": 40,
          "aleatorio": 46
        }
      },
      "exigente": {
        "dado": 1,
        "propriedade": 6,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 40,
        "saldos": {
          "impulsivo": 129,
          "exigente": 241,
          "cauteloso": 40,
          "aleatorio": 46
        }
      },
      "cauteloso": {
        "dado": 2,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 93,
        "saldos": {
          "impulsivo": 129,
          "exigente": 334,
          "cauteloso": -53,
          "aleatorio": 46
        }
      },
      "aleatorio": {
        "dado": 6,
        "propriedade": 13,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 129,
          "exigente": 334,
          "cauteloso": -53,
          "aleatorio": 46
        }
      }
    },
    {
      "impulsivo": {
        "dado": 6,
        "propriedade": 15,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 129,
          "exigente": 334,
          "aleatorio": 46
        }
      },
      "exigente": {
        "dado": 5,
        "propriedade": 11,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 62,
        "saldos": {
          "impulsivo": 191,
          "exigente": 272,
          "aleatorio": 46
        }
      },
      "aleatorio": {
        "dado": 4,
        "propriedade": 17,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 191,
          "exigente": 272,
          "aleatorio": 46
        }
      }
    },
    {
      "impulsivo": {
        "dado": 3,
        "propriedade": 18,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 67,
        "saldos": {
          "impulsivo": 124,
          "exigente": 272,
          "aleatorio": 46
        }
      },
      "exigente": {
        "dado": 2,
        "propriedade": 13,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 127,
        "saldos": {
          "impulsivo": 124,
          "exigente": 145,
          "aleatorio": 46
        }
      },
      "aleatorio": {
        "dado": 4,
        "propriedade": 1,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 124,
          "exigente": 145,
          "aleatorio": 146
        }
      }
    },
    {
      "impulsivo": {
        "dado": 6,
        "propriedade": 4,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 66,
        "saldos": {
          "impulsivo": 158,
          "exigente": 145,
          "aleatorio": 146
        }
      },
      "exigente": {
        "dado": 4,
        "propriedade": 17,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 158,
          "exigente": 145,
          "aleatorio": 146
        }
      },
      "aleatorio": {
        "dado": 3,
        "propriedade": 4,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 82,
        "saldos": {
          "impulsivo": 240,
          "exigente": 145,
          "aleatorio": 64
        }
      }
    },
    {
      "impulsivo": {
        "dado": 5,
        "propriedade": 9,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 158,
        "saldos": {
          "impulsivo": 82,
          "exigente": 145,
          "aleatorio": 64
        }
      },
      "exigente": {
        "dado": 2,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "impulsivo": 82,
          "exigente": 47,
          "aleatorio": 162
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 9,
        "propriedade-dono": "impulsivo",
        "acao": "rent",
        "gasto": 62,
        "saldos": {
          "impulsivo": 144,
          "exigente": 47,
          "aleatorio": 100
        }
      }
    },
    {
      "impulsivo": {
        "dado": 1,
        "propriedade": 10,
        "propriedade-dono": "impulsivo",
        "acao": "buy",
        "gasto": 114,
        "saldos": {
          "impulsivo": 30,
          "exigente": 47,
          "aleatorio": 100
        }
      },
      "exigente": {
        "dado": 1,
        "propriedade": 0,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 30,
          "exigente": 147,
          "aleatorio": 100
        }
      },
      "aleatorio": {
        "dado": 6,
        "propriedade": 15,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": 30,
          "exigente": 147,
          "aleatorio": 100
        }
      }
    },
    {
      "impulsivo": {
        "dado": 2,
        "propriedade": 12,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 96,
        "saldos": {
          "impulsivo": -66,
          "exigente": 147,
          "aleatorio": 196
        }
      },
      "exigente": {
        "dado": 1,
        "propriedade": 1,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": -66,
          "exigente": 147,
          "aleatorio": 196
        }
      },
      "aleatorio": {
        "dado": 2,
        "propriedade": 17,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "impulsivo": -66,
          "exigente": 147,
          "aleatorio": 196
        }
      }
    },
    {
      "exigente": {
        "dado": 2,
        "propriedade": 3,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 79,
        "saldos": {
          "exigente": 147,
          "aleatorio": 196
        }
      },
      "aleatorio": {
        "dado": 2,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "exigente": 147,
          "aleatorio": 196
        }
      }
    },
    {
      "exigente": {
        "dado": 5,
        "propriedade": 8,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 73,
        "saldos": {
          "exigente": 74,
          "aleatorio": 196
        }
      },
      "aleatorio": {
        "dado": 6,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 93,
        "saldos": {
          "exigente": 167,
          "aleatorio": 203
        }
      }
    },
    {
      "exigente": {
        "dado": 2,
        "propriedade": 10,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 114,
        "saldos": {
          "exigente": 53,
          "aleatorio": 203
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 10,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 96,
        "saldos": {
          "exigente": 149,
          "aleatorio": 107
        }
      }
    },
    {
      "exigente": {
        "dado": 4,
        "propriedade": 14,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 88,
        "saldos": {
          "exigente": 149,
          "aleatorio": 107
        }
      },
      "aleatorio": {
        "dado": 3,
        "propriedade": 13,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 58,
        "saldos": {
          "exigente": 207,
          "aleatorio": 49
        }
      }
    },
    {
      "exigente": {
        "dado": 5,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "exigente": 109,
          "aleatorio": 147
        }
      },
      "aleatorio": {
        "dado": 6,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "exigente": 109,
          "aleatorio": 147
        }
      }
    },
    {
      "exigente": {
        "dado": 3,
        "propriedade": 2,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 77,
        "saldos": {
          "exigente": 132,
          "aleatorio": 147
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 4,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "exigente": 132,
          "aleatorio": 247
        }
      }
    },
    {
      "exigente": {
        "dado": 1,
        "propriedade": 3,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 79,
        "saldos": {
          "exigente": 132,
          "aleatorio": 247
        }
      },
      "aleatorio": {
        "dado": 3,
        "propriedade": 7,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "exigente": 132,
          "aleatorio": 247
        }
      }
    },
    {
      "exigente": {
        "dado": 2,
        "propriedade": 5,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 93,
        "saldos": {
          "exigente": 132,
          "aleatorio": 247
        }
      },
      "aleatorio": {
        "dado": 4,
        "propriedade": 11,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "exigente": 132,
          "aleatorio": 247
        }
      }
    },
    {
      "exigente": {
        "dado": 6,
        "propriedade": 11,
        "propriedade-dono": "exigente",
        "acao": "buy",
        "gasto": 127,
        "saldos": {
          "exigente": 5,
          "aleatorio": 247
        }
      },
      "aleatorio": {
        "dado": 5,
        "propriedade": 16,
        "propriedade-dono": null,
        "acao": null,
        "gasto": null,
        "saldos": {
          "exigente": 5,
          "aleatorio": 247
        }
      }
    },
    {
      "exigente": {
        "dado": 2,
        "propriedade": 13,
        "propriedade-dono": "exigente",
        "acao": "rent",
        "gasto": 58,
        "saldos": {
          "exigente": 5,
          "aleatorio": 247
        }
      },
      "aleatorio": {
        "dado": 3,
        "propriedade": 19,
        "propriedade-dono": "aleatorio",
        "acao": "rent",
        "gasto": 98,
        "saldos": {
          "exigente": 5,
          "aleatorio": 247
        }
      }
    }
  ]
}
```

</details>

## Execução remota
A API pode ser acessada com esse endereço: https://brasil-prev-backend-challenge.onrender.com/jogo/simular

## Execução local
### Docker
Para execução da API via docker rodar os comandos:
- `docker compose build`
- `docker compose up -d`

Acessar endereço http://127.0.0.1:8000/jogo/simular

### Uvicorn
- Criar venv: `python -m venv venv`
- Ativar venv: `source venv/bin/activate` (Linux/MacOS, checar equivalente para Windows)
- Instalar pacotes: `pip install -r requirements.txt`
- Executar via uvicorn: `uvicorn main:app --reload`
- Acessar endereço http://127.0.0.1:8000/jogo/simular
- Para executar testes unitários: `pytest tests.py`
