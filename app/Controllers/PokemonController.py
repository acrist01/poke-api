from Services.PokemonService import PokemonService

class PokemonController():

    def __init__(self, pokemon_service: object) -> None:
        self._pokemon_service = pokemon_service
    
    def get(self, name):
        return self._pokemon_service.get_pokemon_details(name)

