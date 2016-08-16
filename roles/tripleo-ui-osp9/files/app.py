from __future__ import unicode_literals

import json
import mimetypes
import os
import sys

from flask import Flask, render_template, send_from_directory
from oslo_config import cfg, types
from oslo_log import log


LOG = log.getLogger(__name__)

LOCAL_STATIC_PATH = os.path.join(os.getcwd(), 'static')

PortType = types.Integer(1, 65535)

# Service options
cfg.CONF.register_group(cfg.OptGroup(name='service',
                                     title='Service options'))
cfg.CONF.register_opts([cfg.StrOpt('bind_host',
                                   default='0.0.0.0',
                                   help='App host address'),
                        cfg.Opt('bind_port',
                                default=8888,
                                type=PortType,
                                help='App port'),
                        cfg.BoolOpt('debug',
                                    default=False)],
                       group='service')

# App options
cfg.CONF.register_group(cfg.OptGroup(name='app',
                                     title='App options'))
cfg.CONF.register_opts([cfg.StrOpt('keystone',
                                   default=None,
                                   help='Keystone API URL'),
                        cfg.StrOpt('tripleo',
                                   default=None,
                                   help='TripleO API URL'),
                        cfg.StrOpt('validations',
                                   default=None,
                                   help='Validations API URL'),
                        cfg.StrOpt('heat',
                                   default=None,
                                   help='Heat API URL'),
                        cfg.StrOpt('ironic',
                                   default=None,
                                   help='Ironic API URL'),
                        cfg.StrOpt('swift',
                                   default=None,
                                   help='Swift API URL'),
                        cfg.StrOpt('glance',
                                   default=None,
                                   help='Glance API URL'),
                        cfg.StrOpt('neutron',
                                   default=None,
                                   help='Neutron API URL'),
                        cfg.StrOpt('zaqar',
                                   default=None,
                                   help='Zaqar API URL'),
                        cfg.StrOpt('mistral',
                                   default=None,
                                   help='Mistral API URL'),
                        cfg.StrOpt('zaqar_websocket_url',
                                   default=None,
                                   help='Zaqar Websocket URL'),
                        cfg.StrOpt('zaqar_default_queue',
                                   default="tripleo",
                                   help='Zaqar Default Queue')],
                       group='app')

app = Flask(__name__, static_folder='static')


# .svg is not recognized on all systems
mimetypes.add_type('image/svg+xml', '.svg')


@app.route('/', methods=['GET'], defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def index(path):
    return render_template('index.html')


@app.route('/js/tripleo_ui_config.js')
def send_config_js():
    return send_from_directory(
        LOCAL_STATIC_PATH, 'tripleo_ui_config.js',
        mimetype=mimetypes.guess_type('tripleo_ui_config.js')[0])


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js/', path,
                               mimetype=mimetypes.guess_type(path)[0])


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css/', path,
                               mimetype=mimetypes.guess_type(path)[0])


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(app.static_folder + '/img/', path,
                               mimetype=mimetypes.guess_type(path)[0])


@app.route('/fonts/<path:path>')
def send_fonts(path):
    print mimetypes.guess_type(path)
    return send_from_directory(app.static_folder + '/fonts/', path,
                               mimetype=mimetypes.guess_type(path)[0])


def create_config_js(app_conf):
    try:
        os.stat(LOCAL_STATIC_PATH)
    except OSError:
        os.mkdir(LOCAL_STATIC_PATH)
    json_str = json.dumps({key: val for key, val in app_conf.items()
                           if val is not None})
    file_path = os.path.join(LOCAL_STATIC_PATH, 'tripleo_ui_config.js')
    with open(file_path, 'w') as js:
        # TODO(flfuchs) rename to tripleoUiConfig
        # as soon as this is done in the JS application as well.
        js.write("window.tripleOUiConfig = %s;" % json_str)


def main(args=sys.argv[1:]):
    cfg.CONF(args)
    create_config_js(cfg.CONF.app)
    app.run(host=cfg.CONF.service.bind_host,
            port=cfg.CONF.service.bind_port,
            debug=cfg.CONF.service.debug)


if __name__ == '__main__':
    main()
