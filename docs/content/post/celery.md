---
title: "Celery"
author: "Nick Hildebrant"
date: 2021-12-15T12:20:08Z
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

Celery and RabbitMQ Server are installed by the CI script.

A set of test tasks will generate a thorough test to excersise the system on each startup

This should give a good target for baseline utilization. Redis is still on the table as a broker and store. amqp and rpc are used now as recommended in the celery docs.

currently add task is working from demo
need to [deploy a systemd script](https://docs.celeryproject.org/en/stable/userguide/daemonizing.html#daemon-systemd-generic) to start celery and rabbitmq server.

[Flower](https://flower.readthedocs.io/en/latest/install.html) is recommended but check what resources it would take
- [Running Flower under own Daemon](https://stackoverflow.com/questions/13579047/celery-flower-as-daemon)