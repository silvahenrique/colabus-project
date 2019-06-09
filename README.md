# PROJETO NOME


## Endpoints publicados:

#### Pesquisar linhas de ônibus.

Endpoint: https://dblvku87af.execute-api.sa-east-1.amazonaws.com/dev?search_term=8622

#### Obter ônibus da linha.
Endpoint: https://3ngvwvs54h.execute-api.sa-east-1.amazonaws.com/dev?line_code=33206

#### Obter a distância dos ônibus na linha até o usuário.
Endpoint: https://ktosj3xoek.execute-api.sa-east-1.amazonaws.com/dev

PAYLOAD:
`````json
"input_origins": {
        "lat": -23.550473780636015,
        "lon": -46.641219352653806
    },
    "input_destinations": [
        {
            "lat": -23.453173,
            "lon": -46.786489
        },
        {
            "lat": -40.45823275,
            "lon": -2.78327337499999
        }
    ]
}
`````

#### Registar informações
Endpoint: https://ai6l2b1r85.execute-api.sa-east-1.amazonaws.com/dev

PAYLOAD:
`````json
{
  "data": {
    "message": "Hello world!",
    "bus_id": 11673,
    "user_id": 1
  },
  "action": "insert"
}
`````