# Card reference

The physical cards are currently printed in Russian only.
This page is an English translation of every card, so you can play with the Russian deck.
Cards are listed by their English name, with the Russian name printed on the card in parentheses.

How to read the cards:
- ● – the colored dot refers to a card category, using the color of that category (for example, a red ●attack or a blue ●defense)
- 2/⚙️1 – the first number applies normally, the ⚙️ number applies if you have at least one component on the table
- 🪟 – the word before it is a [hard mode](rules.md#hard-mode) modifier: act it out when you play the card
- **sudo** – the extra effect you get when you play the card together with a "sudo" card
- **Known Legacy** – the extra effect that applies when other players know you have a "Legacy" card (see the [FAQ](faq.md#how-does-the-legacy-card-work))
- 👥 – the number of players

See the [rules](rules.md) for the card types and symbols.


## Architecture (white)

Your secret objective for the game. Each card has a "Task" number, used in [Freelance mode](rules.md#freelance-mode).

| Card | Task | Win condition | Copies | Joke |
|------|------|---------------|--------|------|
| Analytics (Аналитика) | 1 | 1 Backend, 2 Databases | 1 | Solid and clear-cut |
| Microfrontends (Микрофронтенды) | 2 | 2 Frontends, 1 Database | 1 | You're lucky if you don't know what microfrontends are |
| Microservices (Микросервисы) | 3 | 1 Frontend, 2 Backends | 1 | – |
| Monolith (Монолит) | 4, 5 | 1 Frontend, 1 Backend, 1 Database | 2 | Monolith: as old as the world (and you) |


## Components (purple)

### ⚙️ Database (База данных)

*Copies: = number of 👥 players · On your turn*

- **Effect:** Lay it out on the table. Or return it from your hand to the middle of the deck and draw 2/⚙️1 cards
- **Social ritual:** Ask the most gullible player to invest in your project
- **Joke:** Violates the CAP theorem, twice

### ⚙️ Backend (Бекенд)

*Copies: = number of 👥 players · On your turn*

- **Effect:** Lay it out on the table. Or return it from your hand to the middle of the deck and draw 2/⚙️1 cards
- **Social ritual:** Praise yourself for the release in exactly 4 words
- **Joke:** The backend was written by a junior, brace yourselves!

### ⚙️ Frontend (Фронтенд)

*Copies: = number of 👥 players · On your turn*

- **Effect:** Lay it out on the table. Or return it from your hand to the middle of the deck and draw 2/⚙️1 cards
- **Social ritual:** Point out who is winning and who everyone should gang up on
- **Joke:** `"b" + "a" + +"a" + "a" // "baNaNa"`

### ⚙️ Cloud (Облако)

*Copies: 2 · On your turn*

- **Effect:** When played, it can become any ●component. Neatly🪟 lay it out on the table with the right side up
- **sudo:** Rotate your own or someone else's Cloud on the table
- **Known Legacy:** You can't rotate someone else's Cloud
- **Joke:** — What are clouds made of? — Linux servers, mostly


## Draw (green)

### Garbage Collector (Сборщик мусора)

*Copies: 4 · On your turn*

- **Effect:** Take 1 card of your choice from the discard pile and thoroughly🪟 show it to everyone
- **sudo:** Take 2 cards from the discard pile and show them: keep 1, give 1 to another player
- **Known Legacy:** Also take the top card of the discard pile
- **Social ritual:** Make excuses: why do you have to dig through the garbage?
- **Joke:** And let the whole world wait!

### Hype (Хайп)

*Copies: 3 · On your turn*

- **Effect:** Mindlessly🪟 draw 2/⚙️3 cards from the deck
- **sudo:** Draw +1/⚙️2 cards
- **Known Legacy:** Draw -1 card
- **Social ritual:** Say or do something hype and very annoying
- **Joke:** The online version of this game will have AI

### RFC

*Copies: 4 · On your turn*

- **Effect:** Name a card and a player who has it in their hand, and take it, if they have it. If they don't, the player must show you their cards. (Card names are the ones printed in the center of the cards)
- **sudo:** Choose who gets the card instead of you
- **Social ritual:** Passive-aggressively explain why that person doesn't need this card
- **Joke:** — I need your database, your clouds, and your motorcycle

### Handshake

*Copies: 2 · On your turn*

- **Effect:** Openly swap 1 card from your hand for 2/⚙️3 cards of another player
- **sudo:** Give away the top card of the discard pile instead of your own card
- **Joke:** — Looks like I'm going to burn out from all this legacy soon...

### Man in the Middle

*Copies: 2 · ↩️ When another player draws a card*

- **Effect:** Intercept the last card they just drew and quickly🪟 take it into your hand
- **sudo:** Take all the cards they just drew
- **Social ritual:** Say a villainous line when you intercept the card
- **Joke:** Alice sends Bob her public key, but Bob is out drinking

### OpenSource

*Copies: 5 · On your turn*

- **Effect:** Everyone puts down 1 card face up. You pick 1/⚙️2, then the others take 1 each, in turn
- **sudo:** All the cards are put down from the deck instead
- **Joke:** Real open source is when you don't get paid and get insulted


## Attack (red)

### ▲ Bug (Ошибка)

*Copies: 3 · On your turn*

- **Effect:** The player returns 1 of their ●components of their choice to their hand. They can play ●components of that type again after 🚧1 turn
- **sudo:** The ●attack breaks through a ●defense without sudo
- **Joke:** As always, the bug is somewhere between the chair and the monitor

### ▲ Specific Bug (Специфическая ошибка)

*Copies: 2 · On your turn*

- **Effect:** Return 1 specific ●component of the player to their hand. They can play ●components of that type again after 🚧1 turn
- **sudo:** The ●attack breaks through a ●defense without sudo
- **Social ritual:** Explain, in a nitpicky way, what exactly broke
- **Joke:** What a nitpicker you are!

### ▲ Critical Bug (Критическая ошибка)

*Copies: 2 · On your turn*

- **Effect:** The player discards 1 of their ●components of their choice from the table
- **sudo:** The ●attack breaks through a ●defense without sudo
- **Joke:** `undefined is not a function`

### ɷ Vulnerability (Уязвимость)

*Copies: 4 · On your turn*

- **Effect:** Steal 1 of the player's ●components of their choice from their table into your hand
- **sudo:** The ●attack breaks through a ●defense without sudo
- **Social ritual:** Say your social media password
- **Joke:** `$password = base64_encode($_POST["password"]);`

### ɷ Specific Vulnerability (Специфическая уязвимость)

*Copies: 2 · On your turn*

- **Effect:** Carefully🪟 steal 1 specific ●component from the player's table into your hand
- **sudo:** The ●attack breaks through a ●defense without sudo
- **Joke:** We're not going to joke about security issues, are we?


## Defense (blue)

### ▲ Not a Bug (Отговорка)

*Copies: 2 · ↩️ When you are ●attacked*

- **Effect:** Thoroughly🪟 ●defend against 1 ▲bug
- **sudo:** ●Defend against an ●attack with sudo, then take the ●attack card into your hand
- **Social ritual:** Talk your way out: explain why this bug is actually not a bug at all
- **Joke:** Docker was invented to ship your machine to production

### ɷ Patch (Патч)

*Copies: 3 · ↩️ When you are ●attacked*

- **Effect:** ●Defend against 1 ɷvulnerability
- **sudo:** ●Defend against an ●attack with sudo, then take the ●attack card into your hand
- **Social ritual:** Must be played in silence
- **Joke:** `if user == 'admin' and password == '123': ...`

### ▲ɷ Crutches (Костыли)

*Copies: 5 · ↩️ When you are ●attacked*

- **Effect:** Shamelessly🪟 ●defend against 1 ▲bug or ɷvulnerability
- **sudo:** ●Defend against an ●attack with sudo
- **Social ritual:** Explain why you have to use crutches: for a salary like this!
- **Joke:** Good enough!

"Crutches" is Russian developer slang for hacky workarounds.


## sudo (gold)

### sudo

*Copies: 6 · ↩️ At any time, on your own cards*

- **Effect:** Powers up cards. Each card's power-up is printed in its "sudo" strip
- **Joke:** `$ make sandwich` `$ sudo make sandwich`


## Meta (brown)

### Burnout (Выгорание)

*Copies: 7 · ↩️ On another player's turn*

- **Effect:** Interrupt the player's current turn. They can't take any new actions
- **sudo:** Give the burned-out player 1 of your ●Legacy cards
- **Social ritual:** Toxically explain why the player burned out
- **Joke:** After burning out, you can, for example, start raising geese

### Manual

*Copies: 1 · On your turn*

- **Effect:** Invent a new fun🪟 social ritual for one of these: the start or end of a turn; drawing any card; playing a component. The ritual applies to all players for the rest of the game
- **Joke:** Nobody reads them anyway!

### Redirect

*Copies: 2 · ↩️ When you are ●attacked*

- **Effect:** Redirect the ●attack to any other player, if possible. After the redirect, you no longer take part in the ●attack
- **sudo:** You become the ●attacker
- **Joke:** It's not our problem!

### Cancel (Отмена)

*Copies: 7 · ↩️ At any time*

- **Effect:** Cancel the effect of any ●Draw or ●Meta card, with or without ●sudo
- **Social ritual:** Play it dramatically!
- **Joke:** — Why don't mosquitoes bite you? — They're not allowed to!


## Legacy (light gray)

### Legacy (Легаси)

*Copies: 2 · Can't be played*

- **Effect:** Can't be discarded, only given away using suitable card abilities. When you get a ●Legacy into your hand from anywhere other than the deck, discard 2/⚙️1 other cards
- **Joke:** `print u"Oh look, python2!"`


## Events (dark gray)

Play events immediately on your turn.

### 500

*Copies: 2*

- **Effect:** You have a ▲bug. You calmly🪟 skip your turn. ●Defend, or return your ●component from the table to your hand. You can play ●components of that type again after 🚧1 turn
- **Joke:** Reply that you're a teapot

### 0 Day (0 день)

*Copies: 2*

- **Effect:** You have a ɷvulnerability. You sadly🪟 skip your turn. ●Defend, or choose who gets your ●component from the table into their hand
- **Joke:** Hmm, speculative execution, what could possibly go wrong?

### Friday (Пятница)

*Copies: 2*

- **Effect:** You can't lay out ●components this turn :(
- **Known Legacy:** You skip your turn
- **Joke:** Just deploy every commit, and there will be no problems

### Hacker's Paws (Хакерские лапки)

*Copies: 2*

- **Effect:** Cats ran past and knocked everything over! Discard 2/⚙️1 cards from your hand
- **Known Legacy:** Discard +1 card
- **Joke:** This is the cutest card in the whole game!


## Boosters

Optional extra cards, not part of the base game.

### "Soft Skills" booster: NDA

*Meta · Copies: 1 · On your turn*

- **Effect:** Until your next turn, all players must play in silence
- **Joke:** We won't tell anyone, and don't you tell either

### "Streaming" booster

Event cards 🖥 for playing on a stream.

#### Root access

*Event 🖥 · Copies: 2*

- **Effect:** The ●"Manual" card has been hacked. If it is active, its social interaction is replaced with one invented by the viewers. Pick one from the chat yourselves!
- **Joke:** This is no laughing matter!

#### Naming Convention

*Event 🖥 · Copies: 2*

- **Effect:** The player whose first name or last name shows up in the chat first discards 3/⚙️2 cards
- **Joke:** Let bygones be bygones (a twist on a Russian proverb)


## Quick reference card

The back of the quick reference card that comes with the deck:

- **Card types:** ⚙️ Component, Attack, Defense, Meta, Draw, Legacy, Event, sudo
- **Symbols:** ▲ bug, ɷ vulnerability, ↩️ reaction, ⚙️ you have a ●component on the table, 🚧 block
- **Dealing:** Swap ●events for other cards. The dealer goes first
- **Turn order:** Draw 1 card, then play any cards (only 1 ●component per turn). Or draw 2 cards and skip your turn. Hand limit at the end of your turn = 8 cards. No cards in hand at the start of your turn? Draw 5 cards
- **To win:** Lay out ●components on the table matching your ●architecture
- **Social rituals:** Were you the first to notice that a player didn't perform a social ritual or didn't draw a card? Pull a card out of their hand
