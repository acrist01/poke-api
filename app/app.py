from flask import Flask
from os import environ
from dotenv import load_dotenv

from Wrappers.HttpClient import HttpClient

from Services.PokemonService import PokemonService

from Controllers.VersionController import VersionController
from Controllers.PokemonController import PokemonController

load_dotenv()
app = Flask(__name__)

poke_species_endpoint = environ.get("POKEMON_ENDPOINT")

http_client = HttpClient()
pokemon_service = PokemonService(http_client, poke_species_endpoint)
pokemon_controller = PokemonController(pokemon_service)


@app.route('/')
def version():
    version = VersionController()
    return version.get()

@app.route('/pokemon/<name>')
def get_pokemon(name):
    return pokemon_controller.get(name)