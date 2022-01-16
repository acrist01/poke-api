from Services.PokemonService import PokemonService

class PokemonController(object):

    def __init__(self, pokemon_service: object) -> None:
        self._pokemon_service = pokemon_service
    
    def get(self, name: str) -> dict:
        return self._pokemon_service.get_pokemon_details(name, False)

    def get_translated(self, name : str) -> dict:
        return self._pokemon_service.get_pokemon_details(name, True)
