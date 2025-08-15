import tomllib
import os

CONFIG_DIR = os.path.expanduser("~/.local/share/qb-ptmap")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.toml")

DEFAULT_CONFIG = {
    'qbitconf': {
        'QBIT_HOST': 'localhost:8080',
        'QBIT_USER': 'admin',
        'QBIT_PASS': 'adminadmin'
    },
    'natpmp': {
        'NATPMP_COMMAND': "while true ; do date ; natpmpc -a 1 0 udp 60 -g 10.2.0.1 && natpmpc -a 1 0 tcp 60 -g 10.2.0.1 || { echo -e 'ERROR with natpmpc command \\\\a' ; break ; } ; sleep 45 ; done"
    }
}

def load_config():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            f.write("[qbitconf]\n")
            f.write(f"QBIT_HOST = \"{DEFAULT_CONFIG['qbitconf']['QBIT_HOST']}\"\n")
            f.write(f"QBIT_USER = \"{DEFAULT_CONFIG['qbitconf']['QBIT_USER']}\"\n")
            f.write(f"QBIT_PASS = \"{DEFAULT_CONFIG['qbitconf']['QBIT_PASS']}\"\n\n")

            f.write("[natpmp]\n")
            f.write(f"NATPMP_COMMAND = \"{DEFAULT_CONFIG['natpmp']['NATPMP_COMMAND']}\"\n")
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "rb") as f:
        user_config = tomllib.load(f)
        config = DEFAULT_CONFIG.copy()
        config.update(user_config)
        return config

config = load_config()
qbit_config = config.get('qbitconf', {})
QBIT_HOST = qbit_config.get('QBIT_HOST')
QBIT_USER = qbit_config.get('QBIT_USER')
QBIT_PASS = qbit_config.get('QBIT_PASS')
natpmp_config = config.get('natpmp', {})
NATPMP_COMMAND = natpmp_config.get('NATPMP_COMMAND')
