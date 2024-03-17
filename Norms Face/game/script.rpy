######## This is the script for Norm's Face
## All art, music, text and programming authored by Robert Killen 2024
## All right reserved

####Crossfading Image code

transform LiveDissolve(spriteB, duration=0.5):
    DynamicImage(spriteB) with Dissolve(duration, alpha=True)

#### Additional Music Channels

init python:
    renpy.music.register_channel("piano", "music", True)
    renpy.music.register_channel("marimba", "music", True)
    renpy.music.register_channel("ala1", "music", True)
    renpy.music.register_channel("ala2", "music", True)
    renpy.music.register_channel("ala3", "music", True)
    renpy.music.register_channel("ala4", "music", True)
    renpy.music.register_channel("ala5", "music", True)
    renpy.music.register_channel("gra1", "music", True)
    renpy.music.register_channel("gra2", "music", True)
    renpy.music.register_channel("gra3", "music", True)
    renpy.music.register_channel("gra4", "music", True)
    renpy.music.register_channel("gra5", "music", True)
    renpy.music.register_channel("mar1", "music", True)
    renpy.music.register_channel("mar2", "music", True)
    renpy.music.register_channel("mar3", "music", True)
    renpy.music.register_channel("mar4", "music", True)
    renpy.music.register_channel("mar5", "music", True)

####Transitions

define bg_transition = {"master" : Fade(0.5, 0.0, 0.5,  color="#FFFFFF")}

####Random (maybe not needed to define here)

## $ d10 = renpy.random.randint(1,10)

######## START HERE!

## Variables needed for jumps

label start:
    $ mlevel = 0
    $ glevel = 0
    $ alevel = 0
    $ levelsum = 0

## Start the piano.

    $ renpy.music.play("piano.ogg", channel='piano', loop=True, synchro_start=True, fadein=0.0)
    $ renpy.music.set_volume(0.35, delay=0.0, channel="piano")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="marimba")

    $ renpy.music.set_volume(0.35, delay=0.0, channel="ala1")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="ala2")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="ala3")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="ala4")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="ala5")


    $ renpy.music.set_volume(0.35, delay=0.0, channel="gra1")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="gra2")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="gra3")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="gra4")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="gra5")


    $ renpy.music.set_volume(0.35, delay=0.0, channel="mar1")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="mar2")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="mar3")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="mar4")
    $ renpy.music.set_volume(0.35, delay=0.0, channel="mar5")

    $ renpy.music.play("marimba.ogg", channel='marimba', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=1.0, channel='marimba')

    $ renpy.music.play("ala1.ogg", channel='ala1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala1')
    $ renpy.music.play("ala2.ogg", channel='ala2', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala2')
    $ renpy.music.play("ala3.ogg", channel='ala3', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala3')
    $ renpy.music.play("ala4.ogg", channel='ala4', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala4')
    $ renpy.music.play("ala5.ogg", channel='ala5', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='ala5')

    $ renpy.music.play("gra1.ogg", channel='gra1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra1')
    $ renpy.music.play("gra2.ogg", channel='gra2', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra2')
    $ renpy.music.play("gra3.ogg", channel='gra3', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra3')
    $ renpy.music.play("gra4.ogg", channel='gra4', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra4')
    $ renpy.music.play("gra5.ogg", channel='gra5', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='gra5')

    $ renpy.music.play("mar1.ogg", channel='mar1', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar1')
    $ renpy.music.play("mar2.ogg", channel='mar2', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar2')
    $ renpy.music.play("mar3.ogg", channel='mar3', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar3')
    $ renpy.music.play("mar4.ogg", channel='mar4', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar4')
    $ renpy.music.play("mar5.ogg", channel='mar5', loop=True, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.0, delay=0.0, channel='mar5')


####SCENE START

    scene bg gray
    with fade

    show normani1 zorder 3:
        xalign 0.5
        yalign 1.0
    with Dissolve(0.5)
    pause 0.3

    show mirani1 zorder 2:
        xalign 0.5
        yalign 0.25
    with Dissolve(0.5)

    "Norm’s day started out pretty normal, except for the song in his head and the fact that he couldn’t find his face."

    show normani1 at Move((0.5, 0.0), (0.5, -0.15), 1.0, xanchor=0.5, yanchor=-0.5):
        ease 1.0 zoom 1.5

    show mirani1:
        ease 1.0 zoom 1.5

    "He searched the bathroom mirror, looking everywhere. In all the corners. Behind the shower curtain. He even squinted through the door behind him, thinking his face might still be in bed. But it wasn’t. It was just gone."

    hide mirani1
    with Dissolve(0.5)

    show teaani1 zorder 2:
        zoom 0.75
        xalign 0.5
        yalign 0.1
    with Dissolve(0.5)

    "Norm thought about this over a lovely cup of tea. But as lovely as the tea was, he couldn't help but feel a little worried."

    "Not about shaving or checking his hair. He didn't care about that stuff. But he was used to seeing his face in the pots and pans and windows... and in his cups of tea, for that matter."

    "He worried that without it he might forget himself."

    hide teaani1
    with Dissolve(0.5)

    show mirani1 zorder 2:
        xalign 0.5
        yalign 0.25
    with Dissolve(0.5)

    "So Norm decided to go find it."

    "He grabbed some biscuits and a pouch of tea leaves (just in case) and stumbled awkwardly through the mirror, slipping on the towel he forgot to pack."

    show normani1 at Move((0.5, -0.15), (0.5, 0.3), 5.0, xanchor=0.5, yanchor=-0.5):
        ease 5.0 zoom 0.7

    show mirani1:
        ease 5.0 zoom 4.0

    pause 2.0

    scene bg gray
    with bg_transition

    pause 1.0

    show seaani1 zorder 1
    with Dissolve(0.5)

    show sunani1 zorder 2:
        xalign 0.15
        yalign 0.1
    with Dissolve(0.5)

    show gulani1 zorder 3:
        zoom 0.9
        xalign 0.35
        yalign 0.60
    with Dissolve(0.5)

    "Straightening up on the other side, Norm blinked at a bright sun over a calm sea stretched out before him."

    show pathmar zorder 2:
        zoom 1.1
        xanchor 0.5
        yanchor 0.0
        xpos 0.26
        ypos 0.49
    show pathala zorder 2:
        zoom 1.1
        xanchor 0.5
        yanchor 0.0
        xpos 0.76
        ypos 0.49
    show pathgra zorder 2:
        zoom 1.1
        xanchor 0.5
        yanchor 0.0
        xpos 0.5
        ypos 0.49
    with Dissolve(0.5)

    "A couple of seagulls, preening in the quiet surf, were surprised by his sudden appearance, but even more surprised by the three paths of stone abruptly rising around them."

    "A chain of smooth black marble pointed a little to the left. Alabaster gleamed like a ribbon of snow on the right. And in the middle, a path of speckled, gray granite led straight to the horizon."

## Flying gulls

    hide gulani1
    with Dissolve(0.2)

    show gullfly1 zorder 3:
        xalign 0.40
        yalign 0.35
    with Dissolve(0.2)

    hide gullfly1
    with Dissolve(0.2)

    show gullfly2 zorder 3:
        xalign 0.55
        yalign 0.2
    with Dissolve(0.2)

    hide gullfly2
    with Dissolve(0.2)

    show gullfly1 zorder 3:
        xalign 0.75
        yalign 0.1
    with Dissolve(0.2)

    hide gullfly1
    with Dissolve(0.2)

    show gullfly2 zorder 3:
        xalign 0.95
        yalign 0.1
    with Dissolve(0.2)

    hide gullfly2
    with Dissolve(0.2)

    "The gulls flew off in a huff."

    "\"Huh,\" Norm thought. He might have come up with more thoughts, but at that particular moment, he was distracted by the song that was still playing in his head, apparently on loop. It was soft and simple and reminded him of a lovely, light shade of green he couldn’t quite name."

    hide seaani1
    hide sunani1
    with Dissolve(0.5)

    show pathmar:
        linear 2.0 ypos 0.0 zoom 2.0

    show pathala:
        linear 2.0 ypos 0.0 zoom 2.0

    show pathgra:
        linear 2.0 ypos 0.0 zoom 2.0

    "The song tugged him toward the stones."

    jump choicer1






