
class VersionController():

    def get(self):
        return {
            'status' : 200,
            'version': '1.0.0'
        }