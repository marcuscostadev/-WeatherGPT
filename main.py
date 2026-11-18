import os

from database.connection import DatabaseManager
from model.check_weather import ConsultaClima
from model.city_fav import CidadeFavorita
from dao.check_weather_dao import ConsultaClimaDAO
from dao.city_fav_dao import CidadeFavoritaDAO
from services.openweather_client import OpenWeatherClient
from services.chat_client import ChatGPTClient
from controller.weather_controller import ClimaController
from controller.fav_controller import FavoritoController
from controller.assist_controller import AssistenteController
from view.screen_weather import TelaClima


def main():
    db = DatabaseManager()
    db.criar_tabelas()
    session = db.criar_sessao()

    openweather_client = OpenWeatherClient(os.getenv("OPENWEATHER_API_KEY"))
    chatgpt_client = ChatGPTClient(os.getenv("OPENAI_API_KEY"))

    consulta_dao = ConsultaClimaDAO(session)
    favorita_dao = CidadeFavoritaDAO(session)

    clima_controller = ClimaController(openweather_client, consulta_dao)
    favorito_controller = FavoritoController(favorita_dao)
    assistente_controller = AssistenteController(clima_controller, chatgpt_client)

    tela = TelaClima(clima_controller, favorito_controller, assistente_controller)
    tela.iniciar()

if __name__ == "__main__":
    main()