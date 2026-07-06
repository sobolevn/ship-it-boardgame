# FAQ

Didn't find the answer to your question?
Write in our chat:

[![Telegram chat](https://img.shields.io/badge/chat-join-blue?logo=telegram)](https://t.me/ship_it_boardgame)

## How is a player punished for not performing a social ritual?

If a player forgot to perform a social ritual and got caught, the player who noticed pulls a card out of their hand.

Not performing a social ritual does not cancel the card's effect.

Importantly, the random card is pulled only after all the actions of the played card have been resolved. For example:
- Alice plays "Vulnerability" against Bob. Bob gives her a component
- However, Bob noticed that Alice didn't perform the social ritual of the "Vulnerability" card
- Alice discards "Vulnerability", takes the stolen component into her hand, shuffles her cards and lets Bob pull a random card

This mechanic gives an attentive player instant revenge.


## How do component cards work?

You can play only one component per turn.

In a 5-player game, the number of "Database", "Backend", and "Frontend" components in the deck always equals the number of those components required by the "Architecture" cards.

With fewer than 5 players, the number of "Database", "Backend", and "Frontend" components in the deck equals the number of players, but the number of components required by the "Architecture" cards may be a bit different. This slightly changes the value of each component in a particular game.

You can lay any component out on the table, even if your "Architecture" doesn't need it.

Some components (if the card says so) can be returned to the deck (somewhere near the middle) in exchange for new cards from the deck. This counts as playing a component too. That means you still have to perform social rituals. And you can still play only one component per turn, by either method: you can't return two components to the deck, and you can't return a component to the deck and lay one out in the same turn.

### How does the "Cloud" card work?

When you play a "Cloud" card, you choose which component it replaces (it can replace absolutely any component). Then you lay the card out at the right angle, so that neither you nor the other players forget which component you replaced.

While the "Cloud" is on the table, it can't change its type. To change the type of component a "Cloud" replaces, play "sudo" on your turn and rotate the "Cloud" card to the right side. This works on your own "Cloud" or someone else's.

If you have a "Known Legacy", you can only rotate your own "Cloud" when playing "sudo".

If a "Cloud" was returned to the hand by a "Bug" card, the one-turn block applies to the type of component the "Cloud" represented. For example:
- Alice has a "Cloud" on the table that replaces a "Frontend"
- Bob plays a "Bug", and Alice returns the "Cloud" to her hand
- On her next turn, Alice can't play "Frontend" cards, but she can play the "Cloud" as a "Backend" (or any other type except "Frontend")


## How do Draw cards work?

### How does the "RFC" card work?

Say the name of a card and choose the specific player
you want to take that card from.
The card name is printed in the center of the card: "Backend", "Hype", "RFC", etc.

You can't name a card type: "component", "draw", etc.
You can't take an Architecture card.

If that player doesn't have the requested card,
they must show you their hand to confirm that the card isn't there.

When played with "sudo", you can choose who gets the card. For example, this way you can move a "Legacy" from one player to another. You can't play this card on yourself.

Cards that were just 🚧 blocked are very easy to take, because you know exactly what you are taking.

### How does the "Man in the Middle" card work?

This card lets you take a card that another player has just drawn into their hand and put it into yours instead. If the player draws several cards, you take a random one of the cards they drew. Watch out for "Legacy"!

With the "OpenSource" card, players take cards one at a time, so snatch the right card at the right moment.

If you're unlucky enough to steal an event on someone else's turn, you resolve it on your next turn.

When played with "sudo", you take all the cards the player drew, however many there were. For example, at the start of their turn a player can draw 5 cards if they had no cards in hand. You can steal them all!

### How does the "OpenSource" card work?

Players put cards face up in the center of the table, in turn order. They take them in turn order too.

If a player put down a "Legacy" and got it back, it counts as receiving it from another player. That player follows the "Legacy" rule and discards cards.


## How do attack cards work?

- Who can you attack? On your turn: any player, including yourself.
- Who can you defend? Only yourself.
- Who can play "sudo" cards? Only the attacker and the defender.

### Example: attacking a component

Alice has a "Backend" component on the table. On his turn, Bob attacks it with a "Bug" card.

Possible outcomes:
- Alice has a defense card and plays it. Both cards go to the discard pile, and the component stays on Alice's table
- Alice has no defense card, so she has to fulfill the condition on the "Bug" card. The "Bug" card goes to the discard pile

Attacks with other kinds of bugs and vulnerabilities work the same way.
However, note that bugs and vulnerabilities may be blocked by different defense cards!

### Example: attacking a component with "sudo"

Suppose Alice played a defense card. Now Bob plays a "sudo" card to break through her regular defense.

Possible outcomes:
- Alice also plays a "sudo" card. The defense card, the attack card, and both "sudo" cards go to the discard pile, and the component stays on Alice's table
- If Alice can't or doesn't want to play a "sudo" card, her defense fails. She has to fulfill the condition on the "Bug" card. The "sudo", the attack card, and the defense card go to the discard pile

You can't play "sudo" together with defense cards unless the attacker played "sudo".
Other players can't throw in a "sudo" card during an attack or defense.

### Example: defending with "Not a Bug" and "Patch"

Alice has a "Backend" component on the table. On his turn, Bob attacks it with a "Vulnerability" card.
Alice has a "Patch" card (a "Not a Bug" card would work the same way, but against bugs).

In this case, the "sudo" card raises the stakes a lot for the attacker. If an attack with "sudo" is blocked, the attacker loses the attack card to the other player.

Possible outcomes:
- Alice doesn't play "Patch" and chooses to give up the component. Then "Vulnerability" goes to the discard pile, and "Backend" goes to Bob's hand.
- Alice plays "Patch", but Bob can't play "sudo". Then "Vulnerability" and "Patch" go to the discard pile, and "Backend" stays on Alice's table.
- Alice plays "Patch". Bob plays "sudo". Alice doesn't play "sudo" in response. Then "Vulnerability", "sudo", and "Patch" go to the discard pile, and "Backend" goes to Bob's hand.
- Alice plays "Patch". Bob plays "sudo". Alice plays "sudo" too. Then both "sudo" cards and "Patch" go to the discard pile, "Vulnerability" goes to Alice's hand, and "Backend" stays on Alice's table.

### Example: attacking yourself

In some cases, it makes sense to attack yourself. For example: you have a "Cloud" card on the table, and you want to change the type of component the "Cloud" replaces.

Note that all the attack and defense rules apply as usual.


## How do "sudo" cards work?

You can play "sudo" cards on your own cards at any moment while those cards are in play.
For example:
- "sudo" is usually played after an attack card, when the other player has defended
- "sudo" is played after a defense card, if the attacker added a "sudo" on top
- "sudo" can be played right away with "Hype", "OpenSource", "Man in the Middle", "Burnout", etc.

You can play 2 or more "sudo" cards with cards where it makes sense. For example: a "Hype" card + 2 "sudo" cards let you draw +2 cards from the deck, +1 for each "sudo".


## How do Meta cards work?

### How does the "Cancel" card work?

The "Cancel" card can completely cancel the effect of any card from the "Draw" and "Meta" categories.
Any player can play "Cancel" as a ↩️ reaction to a card played by another player, at any moment. You can also cancel your own cards.

You can only cancel the most recent card.
Cancelled cards go to the discard pile.
If more than two players are involved in an action (for example, with "Redirect" or "RFC" + "sudo"), any of the players involved can cancel the card's effect.

Example: Alice uses an "RFC" card to ask Bob to give her a card. Bob plays a "Cancel" card. The "RFC" and "Cancel" cards go to the discard pile.

A "Cancel" card can cancel other "Cancel" cards.

Example: Alice uses an "RFC" card to ask Bob to give her a card. Bob plays a "Cancel" card, and Alice then cancels Bob's "Cancel" with her own "Cancel". Bob has nothing left to defend with, so the "RFC" card resolves. The "RFC" card and both "Cancel" cards go to the discard pile.

"Cancel" cancels cards completely, including any extra "sudo" abilities.

Example: Alice plays "Garbage Collector" with "sudo". Bob plays "Cancel". Alice doesn't take a card from the discard pile. "Garbage Collector", "sudo", and "Cancel" go to the discard pile.

"Cancel" cancels other cards as if they had never been played.

Example: Alice plays "OpenSource", Bob puts down a "Legacy", and Charlie cancels "OpenSource". Bob takes the "Legacy" back into his hand. But since "OpenSource" was, in effect, never played, Bob doesn't discard cards for receiving the "Legacy". After all, it never left his hand. Learn to think across multiple space-time continuums!

### How does the "Redirect" card work?

The "Redirect" card lets you redirect any attack from yourself to any other player (including the attacker) who has components on the table.

If the "Redirect" succeeds, the player who played it no longer takes part in this attack.

An attack can be redirected several times in a row.

If the attack is redirected to the attacker, they can only play defensive reaction cards ("Not a Bug" / "Patch" / "Crutches") and "sudo" until the attack is over. That is: they can't, say, play "Draw" cards and only then go back to defending.

If a player played "Redirect" with a "sudo" card when redirecting the attack, they temporarily become the attacker. This means they can: choose the component when attacking with a "Specific Vulnerability" or a "Specific Bug"; take the card obtained through vulnerabilities; play another "sudo" of their own if the defender plays a defense card.

Once the attack is over, the turn returns to the player who originally played the attack card.

Example:
- Alice plays "Specific Bug" on Bob's component
- Bob plays "Not a Bug"
- Alice plays "sudo"
- Bob plays "Redirect" on Charlie, and Bob chooses Charlie's component to attack
- Charlie plays "Crutches" with "sudo"
- The "Specific Bug", "Not a Bug", "Redirect", and "Crutches" cards and 2 "sudo" cards go to the discard pile. The component stays on Charlie's table
- The turn returns to Alice

### How does the "Manual" card work?

This card lets you introduce new social rituals:
- Either at the start of a turn (before drawing a card)
- Or at the end of a turn
- Or when playing a component
- Or when drawing a card

Forgot to do it and someone noticed? A card gets pulled from your hand for every forgotten social ritual.
Like any other card, this card can be played several times per game (for example, when the deck runs out or via "Garbage Collector"). In that case, the social rituals stack.

Examples (it all depends on your imagination and your group):
- Before the start of your turn, you have to quack like a duck
- At the end of your turn, you have to say "I quit!"

This card can only be cancelled while it is being played, not afterwards.
The card goes to the discard pile like all the others.

### How does the "Burnout" card work?

This card can be played at any moment to force a player to end their turn.
Everything the player did before the "Burnout" stays as it was. The player can't do anything new (except "Cancel", of course).

Skipped turns don't stack. For example, if a player drew "500" and has to skip a turn, throwing a "Burnout" at them on top won't make them skip two turns. It will just waste a card.

A "Cancel" played against "Burnout" at the start of your turn doesn't count as an action (since these cards are reactions), so the player can still draw two cards and end their turn.

1 "sudo" card lets you give away 1 of your "Legacy" cards along with the "Burnout". 2 "sudo" cards let you give away 2 of your "Legacy" cards along with the "Burnout".


## How does the "Legacy" card work?

A "Legacy" card can't be played directly or discarded from your hand (for example, when you're over the hand limit).
If you drew it from the deck, it stays in your hand. While other players don't know that you have a "Legacy", it counts as unknown. Use that wisely.

If you received this card into your hand in any way other than from the deck:
- via "Handshake", "OpenSource", "Man in the Middle", or other cards
- by pulling a card out of another player's hand

Then you must fulfill its condition. Such a "Legacy" is now known to all the other players. Now everyone will know you have it! The extra gray "Known Legacy" strips on some cards now apply to you.

This card can't be discarded. At all. Not even because of the hand limit. Not even if the only card in your hand is a "Legacy" and you have to discard a card because of "Hacker's Paws" or because you received another "Legacy".

You can get rid of a "Legacy":
- By letting another player pull it out of your hand
- With card-swapping cards: "OpenSource", "Handshake"
- With "Burnout" + "sudo"
- If someone takes it from you with "RFC" + "sudo"

Card effects with a gray "Known Legacy" strip only apply when other players know that the player has a "Legacy". If a player received a "Legacy" and didn't give themselves away, the effect doesn't apply.

If a "Known Legacy" effect contains a - or a +, such effects stack. For example: discarding +1 card with "Hacker's Paws". If you have two known "Legacy" cards, you discard 2 extra cards. However, effects without a - or a +, such as skipping a turn, don't stack.


## How do event cards work?

Event cards are special. The player is expected to fulfill their condition immediately and discard the event card. In other words: an event card can never end up in a player's hand.

In some cases, the player can't carry out the event's action. For example, the player drew a "500" card but currently has no components on the table. Then the player is lucky: they don't have to do that part of the action, they just skip a turn.

While events are being resolved, you can't play new cards, except defensive reactions.

If you receive events outside of your turn (for example, from a "Man in the Middle" card), the event is resolved on your turn, as your first card. In that case, event cards still don't count as "cards in hand": they lie on the table next to the player.
