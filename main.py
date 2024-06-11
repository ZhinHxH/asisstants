import os
from lolapy import LolaSDK, LolaContext, ResponseText
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **os.environ
}

# Configuracion basica que por buenas practicas no queda alamacenado dentro del codigo
lola = LolaSDK(
    lola_token=config["LOLA_TOKEN"],
    prompter_url=config["PROMPTER_URL"],
    webhook_url=config["WEBHOOK_URL"],
    host=config["HOST"]
)

lola.listen()