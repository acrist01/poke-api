from flask import Flask

from Controllers.VersionController import VersionController

app = Flask(__name__)


@app.route('/')
def version():
    version = VersionController()
    return version.get()