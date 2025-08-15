# qb-ptmap
Automatic port mapper for qBittorrent with the Proton WireGuard configuration

Documentation work in progress

## Prerequisites
### qbittorrent
Install qbittorrent and make sure the webui is active and with working credentials.
### Wireguard configuration
Generate a [Wireguard configuration](https://account.protonvpn.com/downloads#wireguard-configuration) for Linux and be sure to enable "NAT-PMP (Port Forwarding)".

### Install **natpmpc**
Debian:
```bash
apt install natpmpc
```

Arch Linux:
```bash
pacman -Sy libnatpmp
```
### Install wireguard
Debian:
```bash
apt install wireguard
```

Arch Linux:
```bash
pacman -Sy wireguard-tools
```


### Not mandatory but recommended
Install `uv` from the [official source](https://docs.astral.sh/uv/getting-started/installation/).

## Installation
Clone the repository:
```bash
git clone https://github.com/SimoneFelici/qb-ptmap.git
```
Generate the environment:
```bash
cd qb-ptmap && uv sync
```
## Usage
Move your wireguard configuration in `/etc/wireguard/` \
Start wireguard with your proton config:
```bash
sudo wg-quick up proton
```
Enter the environment and run the script:
```bash
source .venv/bin/activate
```
```bash
python3 main.py
```
