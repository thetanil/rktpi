---
title: "rktpi"
author: "Nick Hildebrant"
date: 2021-12-08T18:47:08+01:00
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


## What it is

A platform for web apps running on YOUR Pi, with YOUR Data, accessible from YOUR phone.

Your data in your home. Your safe space near the Internet.

## Features

- A guard computer for your phone
- A transformer of documents
- An internet filtered of garbage
- A path out of the cloud
- Keep your own email, back it up EZ
- UX - just for you
  - ads be damned
  - Extremely opinionated to favor accessibility and UX performance
  - No JS, just enough CSS to unify browsers, there is no ad network
  - No colors, user theme-able viewer
  - Gemini with markdown and pictures
  - Target 3G full page renders under 200ms (not including images)
- Has to may may
  - but with SVG
  - they can be big [think HighQualityGifs](https://www.reddit.com/r/HighQualityGifs/)
  - you see them when they are cached already
- comments about a content item are found in matrix via #content_id 

## The Questions

Rocket Pi is an attempt to answer the following questions:
- how can we get developers to build web apps which allow you to keep your data
- how can I legally show you your FB feed without all the garbage you didn't ever ask for
- why can't we have just email we can trust (spoiler: we can)

*many people want out of the cloud, but do not know how*

## But First...

### It's a game engine?

##### Rocket Pi Motto #1: Invent Nothing

Use well known reliable software everywhere possible.
SMTP, DNS, OpenSSH

Any turn in a card game or board game can be represented as a state, and a choice of moves

##### Shuffle 2p

hidden state can be shared by receiving a list of signed item hashes and returning a signed hash of the permutation to be checked at end of game
State hidden from both players and next_item messages pop next hash from opponent
Like a deck of cards, you know WHAT is in the pile, you just don't know the order
You must ask your opponent what the next item is, but they are drawing blind
By popping all items from your opponent you can verify the shuffle hash
or make all shuffle indexes strictly monotonic increasing (the shuffle is the sorted signed hashes returned)

##### Dice Roll 2p
- generate random[n] for n dice rolls
- send to all players for turn x
- when all players have received turn[x][random[n]] 
- sum all random[1] % 6 for 6 sided

```
t1 = P1 sequence of random numbers and/or moves
t2 = P2 sequence of random numbers and/or moves

h1 = hash(p1)
h2 = hash(p2)

P1 -> P2, h1
P2 -> P1, h2

P1(h2) -> P2, p1
P2(h1) -> P1, p2
```


- Games with repeatable starting positions, or rewind
- What about timeouts, sequenced turns, drawing in multiplayer
- Can you play werewolf?

##### Playing Rock Paper Scissors

game_id = hash(hash(P1.salt), hash(P2.salt))

Email directly self, opponent

m1p1 = game_id, turn_id, move, previous_state

m1p2 = game_id, turn_id, move, previous_state

P1 -> P2 game_id, turn_id, hash(m1p1)

P2 -> P1 game_id, turn_id, hash(m1p2)

P2 -> P1 m1p2 = hash(scissors, game_id, turn#, sig)
P1 -> 
state = apply previous state, m1

# state should be same for both players

P1 -> P2 m2p1 = state, sig(hash(paper, game_id, turn#, state))


First Cheat Free Simultaneous selection multiplayer FMAIL based game engine

### What is fmail

fmail is just an extremely restrictive and prescriptive subset of email

- pki encryption required
- signatures required
- should be formalized like an addendum RFC

##### fmail.client

- can be made by anyone
- connects to an email account (raw access to maildir)
- app notifications via IMAP notifications
- "official" is reference no-JS web app running on pi
- https://keys.openpgp.org/about/faq
- https://weberblog.net/pgp-key-distribution-via-dnssec-openpgpkey/
- https://weberblog.net/how-to-use-danetlsa/
- https://github.com/emersion/go-smtp
- https://dev.gnupg.org/T4618 (RFC is experimental 5 years)
- use a fake TLD? (rktpi) so we can't even be found by clear-net spammers
- pi generates unique ID -> request(id, IPv4/6) -> get domain.rktpi unique to that device


## MVP for GE

### Required Packages

- Postfix
- Caddy
- Custom: configure caddy to read a maildir
  - plugins registered by some service manager
  - addons register their own web services and request document access
- Custom: register postfix MX or dyndns like [DuckDNS](https://www.duckdns.org/spec.jsp)
  - User at pi prompt triggers signed email with current IP to ddns@rktpi.com
  - ddns@rktpi.com updates A and MX records


### Synced to Existing Mail

Possible tools:
- https://github.com/imapsync/imapsync
- [alternatives](https://imapsync.lamiral.info/S/external.shtml)

### Caddy

### Direct Delivery Postfix

MUST ONLY ACCEPT:
- mail for own recipients (local mailbox, NO RELAY)
- mail encrypted with recipient public key
- mail encrypted (signed) by verified sender -> file in mail directory
- mail signed by unknown sender -> new contacts, user interaction required

offer something like: [ProtonMail's Easy Switch](https://protonmail.com/support/knowledge-base/transitioning-from-gmail-to-protonmail/)

Skip DNS Zone Replication
Provide SMTP service which sends a signed encrypted email which updates user specific MX record only
[Each app syncs own folder?](https://imapsync.lamiral.info/FAQ.d/FAQ.Folders_Selection.txt)

    ![alt drawio](/rktpi/svg/rktpi.drawio.svg)

[artboards](/rktpi/post/artboard)

# 2 weeks in (vacation)

Java solutions will not be considered due to memory availability on the device.

### most reliable stack
- [nginx](/rktpi/post/web) for static assets and reverse proxy (maybe caddy later?)
- [postfix](/rktpi/post/messaging) messaging for external communications
- [postgresql](/rktpi/post/events) queue and store
- [bind](/rktpi/post/names) for name resolution
- [fastapi](/rktpi/post/apps) webapp in fastapi

### golang low resource stack
- [coreDNS](https://coredns.io/)
- caddy
- [NSQ](https://nsq.io/) [quickstart](https://nsq.io/overview/quick_start.html)
- pynsq is a mess and I didn't like it at all (cancelled)

2021.12.17 - Benchmarking NSQ. Celery is at 740MB used and < 100 msg/sec and requires extra servers.

- ansible install golang https://github.com/fubarhouse/ansible-role-golang
- [pynsq docs](https://pynsq.readthedocs.io/en/latest/reader.html)
- [ansible docs](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)

No Comparison here really, this is way better, memory usage at 500MB during 21mb/s throughput.

    PUB: [bench_writer] 2021/12/17 09:09:52 duration: 10.043130334s - 21.328mb/s - 111817.726ops/s - 8.943us/op
    SUB: [bench_reader] 2021/12/17 09:10:02 duration: 10.006693747s - 13.754mb/s - 72109.532ops/s - 13.868us/op

But for me it's essentially unusable. the pynsq wrapper is not documented well. it's barely a wrapper
since you have to handle tornado yourself.
you get half a wrapper integrated with a tornado instance where you have to integrate your own CBs
doesn't work with asyncio you have to use tornado


# The Oldernet

The lifecycle of most apps (mobile or web) is:

1. Invent something useful
1. Get popular
1. Sell ads
1. Add social media features to collect user data
1. Sell app to SEO company
1. Sell user data
1. Replace useful buttons with buttons that sell ads
1. Replace social media features with ads
1. more ads
1. app becomes unusable

This happens EVERYWHERE

- The frontpage of google is now just ads. 
- Facebook, Instagram, ...
- Your ex-favorite mobile game..

## No User is asking for this!

The idea that YOU want ads more relevant to you is rediculous. You never wanted them anyway.
Sure, people are allowed to make money, they can do it on the oldernet.

### How can you stop it?
If we allow JS, then the browser can be used as an agent of the ad network which will
inevitably grow in it.
If we allow second requests (even favicons) then users will be tracked and fingerprinted

TODO: what do I want though?!

{{< svg "test.drawio.svg" >}}

{{< svg "spinner.svg" >}}
