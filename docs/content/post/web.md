---
title: "Web Service with NGINX"
author: "Nick Hildebrant"
date: 2021-12-21T11:48:01Z
description: Describe this document
tags:
- markdown
- css
- html
categories:
- themes
- syntax
series:
- World Premier
aliases:
- aliased
draft: false
---

# NGINX will be our web server

RktPi uses nginx as it's static content server and reverse proxy

rktpi will use the package distributed with raspbian

## Installation and Base Config

Part of the rktpi [ansible deployment for nginx](https://github.com/thetanil/rktpi/blob/main/ansible/roles/rktpi/tasks/nginx.yml). 

## Nginx as Static Site Server

for now, all paths are either open to the public or only for the owner of the device

every app has
- public/<appname>/<version>/
- private/<appname>/<version>/

private is a seperate server which only listens on 127


## Nginx as Reverse Proxy

every app can request to have a single port forwarded by nginx
