import sys
from flask import Flask, request, jsonify
from system import System
from config import Config
from convolver import Convolver
from api import API
app = Flask(__name__)

DEV = True

if DEV:
    from flask_cors import CORS
    CORS(app)


system = System()
config = Config(system)
convolver = Convolver(config)
api = API(config)


@app.route('/api', methods=['get'])
def get():
    resp = jsonify({
        'config': dict(config.config),
        'network': api.get_network_status(),
        'convolver': {
            'choices': convolver.get_filter_choices()
        }
    })
    return resp


@app.route('/api', methods=['put'])
def put():
    data = request.get_json()
    with system.card:
        config.save(data['config'])
    resp = jsonify({
        'config': dict(config.config)
    })
    return resp


def main(args):
    app.run(debug=True)


if __name__ == "__main__":
    main(sys.argv[1:])