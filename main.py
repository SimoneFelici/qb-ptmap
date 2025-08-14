import subprocess
import re
import sys
from qbittorrentapi import Client

QBIT_HOST = 'localhost:8080'
QBIT_USER = 'admin'
QBIT_PASS = 'adminadmin'
NATPMP_COMMAND = "while true ; do date ; natpmpc -a 1 0 udp 60 -g 10.2.0.1 && natpmpc -a 1 0 tcp 60 -g 10.2.0.1 || { echo -e 'ERROR with natpmpc command \a' ; break ; } ; sleep 45 ; done"

current_qbit_port = 0

def set_qbittorrent_port(port_number):
    global current_qbit_port
    if port_number == current_qbit_port:
        return

    print(f"Found port: {port_number}.")
    try:
        client = Client(host=QBIT_HOST, username=QBIT_USER, password=QBIT_PASS)
        client.auth_log_in()
        client.app.set_preferences(prefs={'listen_port': port_number})
        
        print(f"qBittorrent is now listening on the port: {port_number}.")
        current_qbit_port = port_number
        
    except Exception as e:
        print(f"Error: {e}")

def run_and_monitor():
    port_pattern = re.compile(r"Mapped public port (\d+) protocol (UDP|TCP)")
    process = subprocess.Popen(NATPMP_COMMAND, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

    for line in iter(process.stdout.readline, ''):
        line = line.strip()
        print(line)
        match = port_pattern.search(line)
        if match:
            port = int(match.group(1))
            protocol = match.group(2)
            if protocol == "TCP":
                set_qbittorrent_port(port)
    process.stdout.close()
    return_code = process.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, NATPMP_COMMAND)

if __name__ == '__main__':
    try:
        run_and_monitor()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"\nScript Error: {e}")
        sys.exit(1)
