from argparse import ArgumentParser
from configparser import ConfigParser
import socket
from uuid import uuid4

from requests import get


def _local_ip():
    """Your local IP address."""
    return socket.gethostbyname(socket.gethostname())


def _public_ip():
    """Your public IP address."""
    response = get('http://jsonip.com')
    return response.json()['ip']


def _read_config_file():
    """Read values from config file."""
    config = ConfigParser()
    config.read('config.cfg')
    return config['USER']


URL = 'http://autoremotejoaomgcd.appspot.com/'

KEY = _read_config_file()['key']


def register_device():
    """Register your computer with auto remote."""
    register_params = {
        'key': KEY,
        'name': 'LINUX_PC',
        'id': str(uuid4()),
        'type': 'linux',
        'publicip': _public_ip(),
        'localip': _local_ip()
    }
    response = get('{}/registerpc'.format(URL), params=register_params)
    if response.status_code == 200:
        print('{} registered with auto remote'.format(register_params['name']))
    else:
        print('Error registering device with auto remote')


def send_message(message: str):
    """Send a message to auto remote."""
    _message = '{}{}'.format(_read_config_file()['message_prefix'], message)
    response = get('{}/sendmessage'.format(URL),
                   params={'key': KEY,
                           'message': _message})
    if response.status_code != 200:
        print('Error sending message {msg}\n{error}'.format
              (msg=_message, error=response.text))
    else:
        print('Message sent')


def script_arguments():
    parser = ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('--message')
    return vars(parser.parse_args())


if __name__ == '__main__':
    args = script_arguments()
    if args['command'] == 'register':
        register_device()
    elif args['command'] == 'send':
        send_message(message=args['message'])
