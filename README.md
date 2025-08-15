# qb-ptmap
Automatic port mapper for qBittorrent with ProtonVPN

Documentation work in progress

## Prerequisites
- qBittorrent/qBittorrent-nox;
- Enabled qBittorrent webui;
- natpmpc ([debian](https://packages.debian.org/sid/natpmpc), [arch](https://archlinux.org/packages/extra/x86_64/libnatpmp/));
- Wireguard or protonvpn installed.

### Wireguard configuration
If you are using the proton vpn GUI you can skip this step.

Generate a [Wireguard configuration](https://account.protonvpn.com/downloads#wireguard-configuration) for Linux and be sure to enable "NAT-PMP (Port Forwarding)".

### Not mandatory but recommended
Install `uv` from the [official source](https://docs.astral.sh/uv/getting-started/installation/).

## Installation
### Install tool (recommended)
```bash
uv tool install  qb-ptmap
```
### From source
Clone the repository:
```bash
git clone https://github.com/SimoneFelici/qb-ptmap.git
```
Generate the environment:
```bash
cd qb-ptmap && uv sync
```
```bash
source .venv/bin/activate
```

## Usage
### Wireguard
Move your wireguard configuration in `/etc/wireguard/` \
Start wireguard with your proton config:
```bash
sudo wg-quick up proton
```
If you installed the recommended way:
```bash
qb-ptmap
```
Else: \
Enter the environment and run the script:
```bash
source .venv/bin/activate
```
```bash
uv run src/qb_ptmap/qb_ptmap.py
```
### ProtonVPN GUI
Connect to a server with port forwarding. \
If you installed the recommended way:
```bash
qb-ptmap
```
Else: \
Enter the environment and run the script:
```bash
source .venv/bin/activate
```
## Configuration
At the first run the tool will generate the configuration file at `~/.local/share/qb-ptmap/config.toml`
You can then edit:
- Webui url;
- User;
- Password.
