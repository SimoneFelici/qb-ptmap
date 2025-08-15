import subprocess
import re
import sys
from qbittorrentapi import Client, exceptions
from qb_ptmap import config

current_qbit_port = 0

def set_qbittorrent_port(port_number):
    global current_qbit_port
    if port_number == current_qbit_port:
        return

    print(f"Found port: {port_number}.")
    try:
        client = Client(host=config.QBIT_HOST, username=config.QBIT_USER, password=config.QBIT_PASS)
        client.auth_log_in()
        client.app.set_preferences(prefs={'listen_port': port_number})
        print(f"qBittorrent is now listening on the port: {port_number}.")
        current_qbit_port = port_number

    except exceptions.LoginFailed as e:
        print(f"\n[ERROR] Login failed. Please check your credentials in config.toml.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred while connecting to qBittorrent.")
        sys.exit(1)

def run_and_monitor():
    port_pattern = re.compile(r"Mapped public port (\d+) protocol (UDP|TCP)")
    process = subprocess.Popen(config.NATPMP_COMMAND, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)
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
        raise subprocess.CalledProcessError(return_code, config.NATPMP_COMMAND)

def main():
    try:
        run_and_monitor()
    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"\nScript Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
