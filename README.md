# perccli-status
Nagios/Opsview plugin to check status of PowerEdge RAID Controller

Mimics `megaclisas-status` and `megaclisas-status --nagios`, uses `perccli2`.

## Tested with

* Debian 12 Bookworm, PERC H965i, perccli2 8.4.0.22


## Install

```
git clone
```

## Development

```
git clone git@github.com:bodik/perccli-status.git /opt/perccli-status
cd /opt/perccli-status
make install-dev
. venv/bin/activate
make coverage
make lint

make build-deb
```
