class PokemonService(object):

    def __init__(self, http_client: object, translation_service: object, endpoint: str) -> None:
        self._http_client = http_client
        self._translation_service = translation_service
        self._endpoint = endpoint
    
    def get_pokemon_details(self, name: str, needs_translation: bool) -> dict:
        try:
            r = self._http_client.get(self._endpoint + name)
            description = self.get_description(r['flavor_text_entries'])
            habitat = r['habitat']['name']
            is_legendary = r['is_legendary']

            if needs_translation:
                description = self.get_translation(description, habitat, is_legendary)
            return {
                'name': r['name'],
                'description': description,
                'habitat': habitat,
                'isLegendary': is_legendary
            }
        except Exception as e:
            return {'status': 404, 'message':'Pokemon not found'}
    
    def get_description(self, flavor_text_entries: list) -> str:
        descriptions = ''
        for flavor_text in flavor_text_entries:
            if flavor_text['language']['name'] == 'en':
                description = flavor_text['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                return description.strip()

    def get_translation(self, description: str, habitat: str, is_legendary: bool) -> str:
        if habitat == 'cave' or is_legendary:
            return self._translation_service.translate(description, 'yoda')
        return self._translation_service.translate(description, 'shakespeare')

   