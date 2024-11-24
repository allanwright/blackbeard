# Blackbeard
## Introduction
The purpose of this repository is to provide automation of the configuration of a new home NAS I am building to replace an existing Synology NAS. This is part learning experience and part wanting to ensure that if I had to rebuild the entire server, I could do so with ease.

## Server Overview
### Hardware
| Part | Details |
|----------|----------|
| CPU | Intel Core i3 12100 |
| Motherboard | CWWK Q670 |
| RAM | Coming soon |
| Power Supply | HDPLEX 250w |
| Case | Athena Power RM-1UC138 1U rackmount chassis |
| Drive Bays | Icy Dock ToughArmor MB699VP-B |
| SSD (OS) | Coming soon |
| Storage Drives | Coming soon |

### Software
* [Debian (headless)](https://www.debian.org/)
* [Mergerfs](https://github.com/trapexit/mergerfs)
* [Snapraid](https://www.snapraid.it/)
* [Docker](https://www.docker.com/)
* [Glances](https://github.com/nicolargo/glances)
* [Powertop](https://github.com/fenrus75/powertop)
* [Homepage](https://gethomepage.dev/)
* [Nginx Proxy Manager](https://nginxproxymanager.com/)
* [Certbot](https://certbot.eff.org/)
* [Immich](https://immich.app/)
* [Nextcloud](https://nextcloud.com/)

### Other Software
I totally don't have any of the following software installed because I always pay for the media I consume, but I think they are really cool projects.

* [Qbittorrent](https://www.qbittorrent.org/)
* [Prowlarr](https://prowlarr.com/)
* [Radarr](https://radarr.video/)
* [Sonarr](https://sonarr.tv/)
* [Jellyfin](https://jellyfin.org/)
* [Jellyseerr](https://github.com/Fallenbagel/jellyseerr)

## In Progress
The following items are still yet to be completed.

* Configure snapraid runner.
* Add support for automated offsite backups.
* Document all of the configuration options and how to execute the Ansible playbook.