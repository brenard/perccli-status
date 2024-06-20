# perccli-status
Nagios/Opsview plugin to check status of PowerEdge RAID Controller

Mimics `megaclisas-status` and `megaclisas-status --nagios`, uses `perccli`.

## Tested with

* Ubuntu 24.04 Noble, PERC H755, perccli 7.2110.0.0


## Install

```
apt install python3 git
git clone https://github.com/brenard/perccli-status.git /usr/local/src/perccli-status
ln -s /usr/local/src/perccli-status/percli_status.py /usr/local/sbin/perccli-status
```

## Development

```
git clone https://github.com/brenard/perccli-status.git /usr/local/src/perccli-status
cd /usr/local/src/perccli-status
make install-dev
make coverage
make lint

make build-deb
```
