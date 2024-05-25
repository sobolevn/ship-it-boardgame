# Ship IT!

[![Telegram chat](https://img.shields.io/badge/chat-join-blue?logo=telegram)](https://t.me/ship_it_boardgame)

![logo](https://raw.githubusercontent.com/sobolevn/ship-it-boardgame/master/ru/graphics/name.png)

Boardgame for people who love IT.
It is built for fun, social interactions, memes, and a little bit of strategy.

No real IT skills are required to play this game :)

## Play

- Order a physical copy: [mail@sobolevn.me](mailto:mail@sobolevn.me)
- [Online via Table Top Simulator](https://steamcommunity.com/sharedfiles/filedetails/?id=3172213526) or create your own [Table Top Simulator](https://github.com/sobolevn/ship-it-boardgame/blob/master/table-top-simulator.md) version

## Rules and languages

- [Russian](https://github.com/sobolevn/ship-it-boardgame/blob/master/ru/rules.md) 🇷🇺

## TODO

This is the earliest release of the game.

What I still have to do:
- [x] Understand how to easily print it
- [x] Play it myself, make others play it
- [ ] Collect feedback (please create GitHub [issues](https://github.com/sobolevn/ship-it-boardgame/issues) or [discussions](https://github.com/sobolevn/ship-it-boardgame/discussions) for any feedback)
- [ ] Improve the game: the wording, balance, some mechanics
- [x] Work on branding: logo, card design, etc
- [x] Create tooling to be able to use [Table Top Simulator]() for playtests
- [ ] Translate the better version of it into english
- [ ] Maybe even publish it officially

All possible income of this game will support my other OpenSource projects!

## Inspirations

What this game is like?

I once played https://www.deployordie.com/ game,
which motivated me to invent my own game in a similar setting.

It is also quite similar to https://www.explodingkittens.com in some aspects.

## Attributions

Thanks a lot to my friends, who helped me with ideas, testing, and rules.

Please, add yourself to `AUTHORS` if you contributed in any way :)

## Render Schemas Locally

To render the schemas locally you just need a working [Docker](https://www.docker.com) installation:
```shell
# Run required services to render
docker compose up -d

# Tells our renderer service to render everything
docker exec -it ship-it-boardgame-renderer-1 python render.py

# Teardown the renderer environment
docker compose down --remove-orphans
```

## LICENSE

[CC BY-NC-SA 4.0](https://github.com/sobolevn/ship-it-boardgame/blob/master/LICENSE)

TLDR:
- You can print it and play with your friends for free!
- You can fork and change it (attribution and same license required)
- You cannot sell it, it would not be fair
