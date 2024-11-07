from bancointer.bancointer import BancoInter
from bancointer.baixa import Baixa
from decouple import config


dir_base_ssl = config("SSL_DIR_BASE")

bi = BancoInter(
    config("API_URL_COBRA_V2"),
    config("API_URL_TOKEN_V2"),
    config("CLIENT_ID"),
    config("CLIENT_SECRET"),
    (
        dir_base_ssl + config("PUBLIC_KEY_V2"),
        dir_base_ssl + config("PRIVATE_KEY_V2")
    )
)

reponse = bi.baixa(nosso_numero="00814081057", motivo=Baixa.ACERTOS)

print(reponse)
