import sys
from flask import Flask, request, jsonify, send_from_directory
from system import System
from config import Config
from convolver import Convolver
from api import API
app = Flask(__name__, static_url_path='/', static_folder='dist')

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
        'system': api.get_system_status(),
        'convolver': {
            'choices': convolver.get_filter_choices()
        }
    })
    return resp


@app.route('/api/iwlist', methods=['get'])
def get_iwlist():
    resp = jsonify({
        'iwlist': api.get_iwlist()
    })
    return resp


@app.route('/api/convolver/set_active_filter', methods=['put'])
def set_active_filter():
    data = request.get_json()

    convolver.active_filter = data['active_filter']
    return jsonify({'status': 'ok'})


@app.route('/api/system', methods=['post'])
def post_system():
    data = request.get_json()
    if data['reboot']:
        system.reboot()


@app.route('/api', methods=['put'])
def put():
    data = request.get_json()
    with system.card:
        config.save(data['config'])
    resp = jsonify({
        'config': dict(config.config)
    })
    return resp


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path.lower().endswith(('js', 'css')):
        return send_from_directory('dist', f'{path}')
    return app.send_static_file('index.html')


def main(args):
    app.run(debug=True, host='0.0.0.0', port=81)


if __name__ == "__main__":
    main(sys.argv[1:])
