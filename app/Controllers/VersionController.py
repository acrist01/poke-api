
class VersionController():

    def get(self) -> dict:
        return {
            'status' : 200,
            'version': '1.0.0'
        }