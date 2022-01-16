class PokemonService():

    def __init__(self, http_client: object, endpoint: str) -> None:
        self._http_client = http_client
        self._endpoint = endpoint
    
    def get_pokemon_details(self, name: str) -> dict:
        try:
            r = self._http_client.get(self._endpoint + name)
            return {
                'name': r['name'],
                'description': self.get_description(r['flavor_text_entries']),
                'habitat': r['habitat']['name'],
                'isLegendary': r['is_legendary']
            }
        except Exception as e:
            return {'status': 404, 'message':'Pokemon not found'}
    
    def get_description(self, flavor_text_entries: list) -> str:
        descriptions = ''
        for flavor_text in flavor_text_entries:
            if flavor_text['language']['name'] == 'en':
                description = flavor_text['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                return description.strip()


   