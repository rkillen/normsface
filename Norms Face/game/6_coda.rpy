########Coda

label end:

## Close out music and restart for ensemble

## Stop all channels with fade
    stop piano fadeout 5.0
    stop marimba fadeout 5.0
    stop ala1 fadeout 5.0
    stop ala2 fadeout 5.0
    stop ala3 fadeout 5.0
    stop ala4 fadeout 5.0
    stop ala5 fadeout 5.0
    stop gra1 fadeout 5.0
    stop gra2 fadeout 5.0
    stop gra3 fadeout 5.0
    stop gra4 fadeout 5.0
    stop gra5 fadeout 5.0
    stop mar1 fadeout 5.0
    stop mar2 fadeout 5.0
    stop mar3 fadeout 5.0
    stop mar4 fadeout 5.0
    stop mar5 fadeout 5.0

    hide whiteover
    with Dissolve(1.0)

    "Norm sat his kitchen table pouring a cup tea."

## Set final tracks to play.

    $ renpy.music.play("piano.ogg", channel='piano', loop=True, synchro_start=True, fadein=0.0)

    $ renpy.music.play("marimba.ogg", channel='marimba', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='marimba')

    $ renpy.music.play("alabaster.ogg", channel='ala1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala1')
    $ renpy.music.play("granite.ogg", channel='gra1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra1')
    $ renpy.music.play("marble.ogg", channel='mar1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar1')

    $ renpy.music.play("faceloop.ogg", channel='mar5', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar5')


    show normani1 zorder 9:
        zoom 1.8
        xanchor 0.5
        yanchor 0.0
        xpos 0.5
        ypos 0.5
    with Dissolve(0.5)

    show cuptopani zorder 3:
        xanchor 0.5
        yanchor 0.5
        xpos 0.54
        ypos 0.3
    with Dissolve(0.5)

    "Norm smiled at his reflection through the vapor.\"There you are! It's so nice to see you. I've had quite the time looking for you.\""

    show cupfaceani zorder 4:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(0.5)

    "His face smiled back. \"Thank you for looking. But I wasn't lost.\""

    "\"What?\""

    "\"I was hiding... and hoping.\""

    "\"Hoping for what?\""

    "Norm's face paused..."

    "\"That in searching for me you might find more of yourself.\""

    "Norm considered his journey..."

    $ renpy.music.set_volume(0.0, delay=1.0, channel='piano')
    $ renpy.music.set_volume(0.40, delay=1.0, channel='mar1')

    hide cupfaceani
    with Dissolve(0.5)

    show cupmar zorder 4:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(1.0)

    "...indulging his sweetest desires"

    "while keeping his connection to others."

    $ renpy.music.set_volume(0.0, delay=3.0, channel='mar1')

    $ renpy.music.set_volume(0.40, delay=1.0, channel='gra1')

    hide cupmar
    with Dissolve(0.5)

    show cupgra zorder 4:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(1.0)

    "...giving to others."

    "while protecting the value he sees in himself."

    $ renpy.music.set_volume(0.0, delay=3.0, channel='gra1')

    $ renpy.music.set_volume(0.40, delay=1.0, channel='ala1')
    $ renpy.music.set_volume(0.40, delay=1.0, channel='marimba')

    hide cupgra
    with Dissolve(0.5)

    show cupala zorder 4:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(1.0)

    "...letting go."

    "without losing himself in the process."

    $ renpy.music.set_volume(0.40, delay=1.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='ala1')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='marimba')

    hide cupala
    with Dissolve(0.5)

    show cupfaceani zorder 4:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(0.5)

    "Norm had found himself somewhere in the balance."

    "\"You know, I think I did.\""

    "\"Yes,\" Norm's face smiled,"

    $ renpy.music.set_volume(0.0, delay=3.0, channel='piano')
    $ renpy.music.set_volume(0.40, delay=1.0, channel='mar5')

    "\"...and it sounds lovely.\""


    "The End"

jump credits