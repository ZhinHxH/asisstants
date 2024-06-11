import os
from lolapy import LolaSDK, LolaContext, ResponseText
from dotenv import dotenv_values
import requests

config = {
    **dotenv_values(".env"),
    **os.environ
}

# Configuracion basica que por buenas practicas no queda alamacenado dentro del codigo
lola = LolaSDK(
    lola_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb2NhbGhvc3QiLCJhdWQiOiJsb2NhbGhvc3QiLCJzdWIiOiI5OUwxT0JOc2xMN1dIM004Z2xsciIsImV4cCI6MTc1NDEzOTE1NDgxMiwiaWF0IjoxNzE4MTM5MTU0ODEyLCJkYXRhIjp7InRlbmFudElkIjoiOTlMMU9CTnNsTDdXSDNNOGdsbHIiLCJhc3Npc3RhbnRJZCI6ImlhcmRxekZQaXJhOUdqMVlUQTNIRVcifX0.XQw4dXxLyM3-mxKikRELtCrhKIfctI6HWSpRRm6vE3Q",
    prompter_url="https://lola-dev-v2.ue.r.appspot.com/",
    webhook_url="https://377e-181-60-112-158.ngrok-free.app"
)


@lola.on_command('get_pokemon_info')
def handle_get_cryptocurrency_price(lead, ctx: LolaContext, cmd):
    pokemon_name = cmd['data']['args']['pokemon']

    ctx.messanger.send_typing_action()
    ctx.messanger.send_text_message(f'Hola futuro entrenador')

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}')

    if response.status_code != 200:
        return {'data': f'Pokemon not found, maybe you write wrong the name, please check'}
    
    pokemon_data = response.json()
    name = pokemon_data['name'].capitalize()
    types = [pokemon_data['type']['name'].capitalize() for type_info in pokemon_data['types']]
    abilities = [pokemon_data['ability']['name'].capitalize() for ability_info in pokemon_data['abilities']]

    types_str = ', '.join(types)
    abilities_str = ', '.join(abilities)
    response_message = f'{name} is a Pokemon of type {types_str}. Its abilities include {abilities_str}.'

    ctx.messanger.send_text_message(response_message)
    return {
    'data': {
        'name': name,
        'types': types,
        'abilities': abilities
        }
    }

lola.listen()