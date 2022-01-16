import requests

class HttpClient():

    def get(self, endpoint: str) -> dict:
        try:
            r = requests.get(endpoint).json()
            return r
        except Exception as e:
            return {'status': 404, 'message': e}

