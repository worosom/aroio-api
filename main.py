import sys
from flask import Flask, request, jsonify, send_from_directory
from system import System
from config import Config
from convolver import Convolver
from api import API
app = Flask(__name__, static_url_path='/', static_folder='dist')

DEV = False

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


@app.route('/api/system/update', methods=['GET'])
def search_update():
    return jsonify({'remote_local_versions': api.search_update()})


@app.route('/api/logs/<log>', methods=['GET'])
def get_log(log):
    return jsonify({log: api.get_log(log)})


@app.route('/api', methods=['put'])
def put():
    data = request.get_json()
    with system.card:
        config.save(data['config'])
    resp = jsonify({
        'config': dict(config.config)
    })
    return resp


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/<path>')
def catch_all(path):
    if path.lower().endswith(('js', 'css')):
        return send_from_directory('dist', f'{path}')
    if path.startswith('de'):
        return index()
    return send_from_directory('dist', f'{path}/index.html')


def main(args):
    app.run(debug=True, host='0.0.0.0', port=81)


if __name__ == "__main__":
    main(sys.argv[1:])
