import requests
class HttpClient(object):

    def get(self, endpoint: str) -> dict:
        try:
            r = requests.get(endpoint).json()
            return r
        except Exception as e:
            return {'status': 404, 'message': e}
    
    def post(self, endpoint: str, headers: dict, body: str) -> dict:
        try:
            r = requests.post(
                endpoint, 
                headers = headers,
                data = body).json()
            return r
        except Exception as e:
            return {'status': 404, 'message': e}
