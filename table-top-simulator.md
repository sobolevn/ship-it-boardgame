# How to upload your deck to Table Top Simulator

The base game has an official Table Top Simulator link: https://steamcommunity.com/sharedfiles/filedetails/?id=3172213526

So, you don't have to upload anything. Just Play!

But, if you want to have your own version
(a fork, for example) - here's how you can make it.


## Building

First of all, you would need to build your game as described in
https://github.com/sobolevn/ship-it-boardgame/tree/master/tools


## Creating a custom deck

When you have all the resources for the game,
you can double check them in your folder:

![tts-folder](https://raw.githubusercontent.com/sobolevn/ship-it-boardgame/master/assets/tts/tts-folder.png)

There should be:
- `0-front.png` with 70 cards' fronts
- `0-back.png` with 70 cards' backs
- `1-front.png` with around ~25 cards' fronts (the amount of cards can change based on the version)
- `1-back.png` with around ~25 cards' backs

Then, load Table Top Simulator and click "Create" / "Singleplayer".
Then, click: "Objects" / "Components" / "Cards". You will see this screen:

![cards](https://raw.githubusercontent.com/sobolevn/ship-it-boardgame/master/assets/tts/cards.png)

Next, the most important part, where you have to create your deck.
Click "Custom deck" and then add it to your table. You will see:

![first-deck](https://raw.githubusercontent.com/sobolevn/ship-it-boardgame/master/assets/tts/first-deck.png)

You will need to set:
- "Face" to `0-front.png` (select "cloud" / "root")
- Check "Unique backs"
- "Back" to `0-back.png` (select "cloud" / "root")
- "Width" to 10 (the amount of cards in `0-front.png` in width)
- "Height" to 7 (the amount of cards in `0-front.png` in height)
- "Number" to 70
- Check "Back is hidden"

Then, click "Import". It will upload the images
and will import the first part of the deck.
You will need to repeat this once again
for `1-front.png` and `1-back.png`,
but you will need to adjust the "Number"
to the actual number of cards in these files.

You can now play the game! ⚓️
