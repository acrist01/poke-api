class TranslationService(object):

    def __init__(self, translation_api_endpoint: str, translation_api_key: str, http_client: object) -> None:
        self._translation_api_endpoint = translation_api_endpoint
        self._translation_api_key = translation_api_key
        self._http_client = http_client
        # this would be more suited for production
        # self._header_content = {'X-Funtranslations-Api-Secret':self._translation_api_key} 
        self._header_content = {}
    
    def translate(self, description: str, language: str) -> str: 
        try:
            return self._http_client.post(
            self._translation_api_endpoint + language + '.json', 
            self._header_content,
            {'text' : description}
            )['contents']['translated']
        except Exception as e:
            return description