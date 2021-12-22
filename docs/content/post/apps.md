---
title: "Apps"
author: "Nick Hildebrant"
date: 2021-12-21T14:10:40Z
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
draft: true
---

# Two Kinds of Apps
Two kinds of apps with different security models

Blessed apps use the system which is provided. They come with some guarantees regarding security,
but are fairly restrictive (no js, user themed styling)

Untrusted apps provide they're own web endpoint. Someone could make an app which uses your phone 
as an attack platform using garbage like React or whatever JS nonsense they wish to subject you too

### Blessed

Blessed apps should be simple to write. Just templates rendering an email based IMAP channel. emails can be generated via templating and sent using the platform api. 
There shall be no way to control the users browser. Everything is rendered statically and served by the platform itself
It shall be impossible for any app to cause the client to request anything from the oldernet

### Untrusted
