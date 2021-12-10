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
- A translator of documents
- An internet filtered of garbage
- A path out of the cloud
- Keep your own email, back it up EZ
- UX - just for you
  - ads be damned
  - Extremely opinionated to favor accessibility and UX performance
  - No JS, just enough CSS to unify browsers, there is no ad network
  - No colors, user theme-able viewer
  - Gemini with markdown and pictures
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
hidden state can be shared by receiving a list of signed item hashes and returning a signed hash of the permutation to be checked at end of game
State hidden from both players and next_item messages pop next hash from opponent
Like a deck of cards, you know WHAT is in the pile, you just don't know the order
You must ask your opponent what the next item is, but they are drawing blind
By popping all items from your opponent you can verify the shuffle hash
or make all shuffle indexes strictly monotonic increasing (the shuffle is the sorted signed hashes returned)

##### Shuffle 2p


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
- connects to an email account
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

### Synced to Existing Mail

Possible tools:
- https://github.com/imapsync/imapsync
- [alternatives](https://imapsync.lamiral.info/S/external.shtml)

### Caddy

### Direct Delivery Postfix

MUST ONLY ACCEPT:
mail for own recipients (local mailbox, NO RELAY)
mail encrypted with recipient public key
mail encrypted (signed) by verified sender -> file in mail directory
mail signed by unknown sender -> new contacts, user interaction required

offer something like: [ProtonMail's Easy Switch](https://protonmail.com/support/knowledge-base/transitioning-from-gmail-to-protonmail/)

Skip DNS Zone Replication
Provide SMTP service which sends a signed encrypted email which updates user specific MX record only
[Each app syncs own folder?](https://imapsync.lamiral.info/FAQ.d/FAQ.Folders_Selection.txt)

![alt rktpi](/rktpi/svg/rktpi.svg)

![alt drawio](/rktpi/svg/rktpi.drawio.svg)







