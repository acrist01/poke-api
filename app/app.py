from flask import Flask
from os import environ
from dotenv import load_dotenv

from Controllers.VersionController import VersionController
from Controllers.PokemonController import PokemonController

from Services.PokemonService import PokemonService
from Services.TranslationService import TranslationService

from Wrappers.HttpClient import HttpClient

load_dotenv()
app = Flask(__name__)



poke_species_endpoint = environ.get('POKEMON_ENDPOINT')
translation_api_endpoint = environ.get('TRANSLATION_API_ENDPOINT')
translation_api_key = environ.get('FUN_TRANSLATION_API_KEY')

http_client = HttpClient()
translation_service = TranslationService(translation_api_endpoint, translation_api_key, http_client)
pokemon_service = PokemonService(http_client, translation_service, poke_species_endpoint)
pokemon_controller = PokemonController(pokemon_service)


@app.route('/')
def version():
    version = VersionController()
    return version.get()

@app.route('/pokemon/<name>')
def get_pokemon(name):
    return pokemon_controller.get(name)

@app.route('/pokemon/translated/<name>')
def get_translated_pokemon(name):
    return pokemon_controller.get_translated(name)

