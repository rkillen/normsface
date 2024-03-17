######## - MARBLE / LIBERTINE PATH

label marble:


    "Approaching the polished black stone, Norm saw a reflection racing out to sea. Thinking it might be his face, he leapt in pursuit."

    hide feetani1
    hide pathmar
    with Dissolve(0.5)

#### Marble Table

    $ renpy.music.set_volume(0.40, delay=1.0, channel='marimba')

    show bg gray-dk
    with Dissolve(1.0)

    show tabani zorder 5:
        xalign 0.5
        yalign 1.05
    with Dissolve(0.5)

    "The moment his feet touched the stone, Norm found himself at a black marble table. Sitting on top was his book of joy, its pages teeming with food, music, books, presents, sunsets, lovers, and mountain streams bursting with fat trout."

    show friends zorder 1:
        yanchor -0.1
        alpha 1.0
    with Dissolve(0.5)

    "Surrounding him were 1,000 past, or future, friends. He wasn’t quite sure."

    "Remembering his purpose, he looked intently at the book. \“Maybe you’re in here.\” His breath caught as it opened."

    show bookani zorder 5:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 0.75
    with Dissolve(0.5)

#### LIBERTINE CHALLENGE

### Choice mar1

    menu:

        "The book offers Norm a Table for One at the finest restaurant in town.What do you recommend?\n\nKnow that Norm may not agree with you. Don't let it get you down."

## Yes

        "Enjoy a great meal!":

## Roll for agreement
            $ m1y = renpy.random.randint(1,10)

## mar1yes Up
            if m1y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show forkani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.7
                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar1')

                "Norm sits in a dark corner of a gourmet restaurant, basking in the solo freedom to devour whatever delights his tongue."

                "Fully sated, he drifts off for a moment, only to wake back at the book."

                hide thumbup
                hide forkani
                with Dissolve(1.0)

## mar1yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm ignores your recommendation. He isn't very hungry. After all, he brought some biscuits."

                hide thumbdown
                with Dissolve(1.0)

                jump levelcheckmar

## No

        "Close the Book":

## Roll for agreement
            $ m1n = renpy.random.randint(1,10)

## mar1no Up
            if m1n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm isn't interested in a meal right now. Upon closing the book he is surprised to find himself back at the beach."

                hide thumbup
                with Dissolve(1.0)

                jump levelcheckmar

            else:

## mar1no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show forkani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.7

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar1')

                "While Norm appreciates your recommendation, he can't resist the temptation of flavors. He sits in a dark corner of a gourmet restaurant, basking in the solo freedom to devour whatever delights his tongue."

                "Fully sated, he drifts off for a moment, only to wake back at the open book."

                hide thumbup
                hide forkani
                with Dissolve(1.0)


### Choice mar2

    menu:

        "This time the book tempts Norm with his favorite video game. What do you recommend?"

## Yes

        "Dig. Build. Adventure!":

## Roll for agreement
            $ m2y = renpy.random.randint(1,10)

## mar2yes Up
            if m2y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show creepani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.5

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar2')

                "Norm loses track of days (and at least one important meeting) as he digs for diamonds, builds grand fortresses, and battles a multitude of evil things."

                "After accidentally backing into a creeper he finds himself once again seated at the black table."

                hide thumbup
                hide creepani
                with Dissolve(1.0)

## mar2yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Although tempted, Norm decides to forgo the game for now."

                hide thumbdown
                with Dissolve(1.0)

                jump levelcheckmar

## No

        "Close the Book":

## Roll for agreement
            $ m2n = renpy.random.randint(1,10)

## mar2no Up
            if m2n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm doesn't feel like gaming right now. Upon closing the book he finds himself back at the beach."

                hide thumbup
                with Dissolve(1.0)

                jump levelcheckmar

            else:

## mar2no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show creepani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.5

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar2')

                "At your recommendation, Norm briefly considers a more productive use of his time, but the joy and simplicity of block life is too great. He loses track of days and meals (and at least one meeting) as he digs for diamonds, builds grand fortresses, and battles a multitude of evil things."

                "After accidentally backing into a creeper he finds himself once again seated at the black table."

                hide thumbup
                hide creepani
                with Dissolve(1.0)


### Choice mar3

    menu:

        "A chance for sun and sea and world class fly fishing all to himself awaits. But Norm will miss his class reunion if he goes.\n\nAny recommendation on this?"

## Yes

        "Fish on!":

## Roll for agreement
            $ m3y = renpy.random.randint(1,10)

## mar3yes Up
            if m3y >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show fishani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.3

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar3')

                "Thigh deep on the salt flats, Norm lands a powerful bonefish, justifying his decision to skip the class reunion. \”They’d all rather be me.\” he chuckles to himself."

                "He turns the page to the next delight."

                hide thumbup
                hide fishani
                with Dissolve(1.0)

## mar3yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm weighs his options and decides to pause on the trip, choosing to reconnect with old friends instead. But he still ends up back at a beach."

                hide thumbdown
                with Dissolve(1.0)

                jump levelcheckmar

## No

        "Close the Book":

## Roll for agreement
            $ m3n = renpy.random.randint(1,10)

## mar3no Up
            if m3n >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm weighs his options and decides to pause on the trip, choosing to reconnect with old friends instead."

                "He closes the book."

                hide thumbup
                with Dissolve(1.0)

                jump contmar

            else:

## mar3no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show fishani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.3

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar3')

                "Though feeling a little guilty about it, Norm stands thigh deep on the salt flats, landing a powerful bonefish, justifying his decision to skip the reunion. \”They’d all rather be me.\” he chuckles to himself."

                "He turns the page to the next delight."

                hide thumbdown
                hide fishani
                with Dissolve(1.0)


### Choice mar4

    menu:

        "Some pleasure are more guilty than others. And Norm's $300 bottle of whisky is one of them. This page transports Norm to his secret stash for a quiet glass.\n\nWhat do you think?"

## Yes

        "It's the good stuff. Cheers!":

## Roll for agreement
            $ m4y = renpy.random.randint(1,10)

## mar4yes Up
            if m4y >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show botani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.2

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar4')

                "Norm slides his bottle of $300 Macallan from its hiding place. \“Too delicious to share,\” he whispers to himself."

                hide thumbup
                hide botani
                with Dissolve(1.0)

## mar4yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm wonders if he shouldn't have a friend over instead, to share his treasured bottle. \"Probably,\" he says to himself."

                "Closing the book, he steps back from the table."

                hide thumbdown
                with Dissolve(1.0)

                jump contmar

## No

        "Close the Book":

## Roll for agreement
            $ m4n = renpy.random.randint(1,10)

## mar4no Up
            if m4n >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Suddenly things don't feel as satifying. Norm closes the book and steps back."

                hide thumbup
                with Dissolve(1.0)

                jump contmar

            else:

## mar4no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show botani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.2

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar4')

                "Norm tries to ignore the flavor already tingling on his tongue, but eventually gives in."

                "He slides his bottle of $300 Macallan from its hiding place. \“Too delicious to share,\” he whispers to himself."

                hide thumbdown
                hide botani
                with Dissolve(1.0)

### Choice mar5

    menu:

        "The pinnacle of indulgence, a casino awaits for Norm, and only Norm.\n\nWhat should he do?"

## Yes

        "All in!":

## Roll for agreement
            $ m5y = renpy.random.randint(1,10)

## mar5yes Up
            if m5y >= 1:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show chipsani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.1

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar5')

                "Norm stalks the casino, voraciously hunting his next thrill. Each streak, flush and blackjack is electrifying!"

                "Norm enjoys his time, but as groups of friends wade through the crowd, he can't help but look on with a touch of jealousy."

                hide thumbup
                hide chipsani
                with Dissolve(1.0)

                jump endmar

## mar5yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Overcoming the pull of lights and liquor and cards, Norm closes the book and steps back."

                hide thumbdown
                with Dissolve(1.0)

                jump contmar

## No

        "Close the Book":

## Roll for agreement
            $ m5n = renpy.random.randint(1,10)

## mar5no Up
            if m5n == 10:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Overcoming the pull of lights and liquor and cards, Norm closes the book and steps away."

                hide thumbup
                with Dissolve(1.0)

                jump contmar

            else:

## mar5no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show chipsani zorder 5:
                    xanchor 0.5
                    yanchor 0.5
                    xpos 0.5
                    ypos 0.4
                with Dissolve(0.5)

                show friends:
                    alpha 0.1

                $ renpy.music.set_volume(0.40, delay=1.0, channel='mar5')

                "Norm tries to close the book, but nonetheless ends up outside a casino, bathed in pink neon. His appetites had grown stronger than his will. \”Well, since I’m already here…\”"
                "He stalks the casino, voraciously hunting his next thrill."

                hide thumbdown
                hide chipsani
                with Dissolve(1.0)

                jump endmar



#### Continue

label contmar:

    $ mlevel += 1
    $ levelsum += 1

    hide bookani
    with Dissolve(0.5)

    "Norm closed the book. He had an uneasy feeling. Looking around the room, he noticed that some of his friends were becoming distant. \"I have been kind of ignoring them.\" he thought."

    "\"Maybe I should follow up my me time with some us time.\""

    "Stepping away from the table, the book opened up by itself, showing a bright sun over a calm sea..."

## Check that all channel volumes are 0, with piano at 1.0
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar5')


######## Check level for correct jump:

label levelcheckmar:

##Hide images

    show bg gray
    with Dissolve(1.0)

    hide bookani
    hide tabani
    hide friends
    with Dissolve(1.0)

    if levelsum == 3:
        jump codamar
    elif levelsum == 0:
        jump redomar
    elif levelsum == 2:
        if mlevel == 0:
            jump facemar
        elif glevel == 1:
            jump faceala
        elif alevel == 1:
            jump facegra
    elif levelsum == 1:
        if glevel == 1:
            jump mar_or_ala
        elif alevel == 1:
            jump mar_or_gra
    jump gra_or_ala


######## - losing after "winning' the libertine challenge

label endmar:

    hide bookani
    with Dissolve(1.0)

    "Norm’s whole body buzzes in the afterglow of his indulgences. Pushing away from the table, he leans back, bloated with satisfaction. \"This is the best, right? This is what life is all about.\""

    hide friends
    with Dissolve(1.0)

    "He smile up at his friends, only then realizing that they have all left."

    "\"Maybe I indulged a bit too much?\" he wonders to himself, still missing his face."

## Check that all channel volmes are 0, with piano at 1.0
    $ renpy.music.set_volume(0.0, delay=2.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='mar1')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='mar2')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='mar3')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='mar4')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='mar5')

##Hide images
    show bg gray
    with Dissolve(2.0)

    hide bookani
    hide tabani
    hide friends
    with Dissolve(2.0)

return


######## Redo from First Choice

label redomar:

## Check that all channel volmes are 0, with piano at 1.0
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='mar5')

##Hide images
    show bg gray
    with Dissolve(1.0)

    hide bookani
    hide tabani
    hide friends
    with Dissolve(1.0)

## Reset items to pre-path state
    show pathmar zorder 2:
        zoom 2.0
        xalign 0.26
        yalign 0.04
    show pathala zorder 2:
        zoom 2.0
        xalign 0.76
        yalign 0.04
    show pathgra zorder 2:
        zoom 2.0
        xalign 0.5
        yalign 0.04
    with Dissolve(0.5)

    jump choicer1