######## - ALABASTER / ASCETIC PATH

label alabaster:

    "Norm steps onto the pristine white path."

## Set initial section volumes

    $ renpy.music.set_volume(0.40, delay=1.0, channel='marimba')
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')

    hide pathala
    hide feetani1
    with Dissolve(0.5)

    show alaroadani zorder 1:
        xalign 0.5
        yalign 1.0
        xpos 0.5
        ypos 1.0
    with Dissolve(1.0)

    show normani1 zorder 5:
        xanchor 0.5
        yanchor 1.0
        xpos 0.5
        ypos 1.1
    with Dissolve(0.5)
    pause 0.3

    "As he'd imagined, the white stone was cool on Norm’s feet. He walked slowly, imagining his reflection a few paces ahead enjoying the waves gently lapping at the stones."

    "I'm sure you're up here somewhere."

## Set initial section volumes

    $ renpy.music.set_volume(0.40, delay=1.0, channel='marimba')
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')

## Hide previous images

    hide feetani1
    hide pathala
    with Dissolve(0.5)

#flying gulls image

    show gullfloat zorder 3:
        xalign 0.5
        yalign 0.5
        xpos 0.15
        ypos 0.17
    with Dissolve(1.0)

    "The same two seagulls, now gliding on a light breeze, eyed him suspiciously."

#snow image

    show snowani zorder 2:
        xalign 0.5
        yalign 0.5
        xpos 0.25
        ypos 0.45
    with Dissolve(1.0)

    "As they did, the sea changed to snow..."

#desert image

    show cactani zorder 3:
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.3
    with Dissolve(1.0)

    "then desert..."

# cafe

    show cafeani zorder 4:
        xalign 0.5
        yalign 0.5
        xpos 0.75
        ypos 0.42
    with Dissolve(1.0)

    "then a lovely little cafe in Tuscany,"

# mountain lake

    hide snowani
    hide cactani
    hide cafeani
    hide alaroadani
    show lakeani zorder 1:
        xalign 0.5
        yalign 1.0
        xpos 0.5
        ypos 1.0
    with Dissolve(1.0)

    "then a small mountain lake from Norm's past."


## Flying gulls

    hide gullfloat
    with Dissolve(0.2)

    show gullfly1 zorder 3:
        xalign 0.35
        yalign 0.17
    with Dissolve(0.2)

    hide gullfly1
    with Dissolve(0.2)

    show gullfly2 zorder 3:
        xalign 0.55
        yalign 0.17
    with Dissolve(0.2)

    hide gullfly2
    with Dissolve(0.2)

    show gullfly1 zorder 3:
        xalign 0.75
        yalign 0.17
    with Dissolve(0.2)

    hide gullfly1
    with Dissolve(0.2)

    show gullfly2 zorder 3:
        xalign 0.95
        yalign 0.17
    with Dissolve(0.2)

    hide gullfly2
    with Dissolve(0.2)

    "The gulls squawked their disapproval and flew off, probably to find that cafe."

# gulls fly off

    "Norm paused. The last time he'd been here he was going through a rough patch. He's spent a whole day sitting on that rock trying to let go of things."

    "\"Maybe I need some more of that,\" he thought."

    "\"Maybe if I forget everything else I'll remember where my face is.\""

    hide normani1
    with Dissolve(0.5)

    show bg white
    show nirvani zorder 4:
        zoom 0.9
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.41
    show loopani zorder 4:
        zoom 0.9
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.39
    with Dissolve(1.0)

    "He climbed up the large boulder overlooking the lake and peered into the still water below him. \"That’s what I need, right?\" \nHe still couldn't see his reflection. But he imagined it down there, deep in meditation."

## Alabaster Challenge

### Choice ala1

    menu:

        "\nGive Norm a nudge. He might ignore you, but don't take it personally. He's having a rough day.\n\nWhat do you recommend?"

## Yes

        "Release your cravings.":

## Roll for agreement
            $ a1y = renpy.random.randint(1,10)

## ala1yes Up
            if a1y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.85

                $ renpy.music.set_volume(0.40, delay=1.0, channel='ala1')
                $ renpy.music.set_volume(0.36, delay=1.0, channel='piano')

                "Norm agrees! He lets go of his earthly desires and feels free! ...as if John Lennon wrote 'Imagine' just for him."

                "No possessions."

                "No desires."

                "No need for greed."

                "He smiles."

                hide thumbup
                with Dissolve(0.5)

## ala1yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm is a little frightened of letting go of things. \"I like things.\" he said to himself."

                "He climbs down."

                hide thumbdown
                with Dissolve(0.5)

                jump levelcheckala

## No

        "Get off the rock.":

## Roll for agreement
            $ a1n = renpy.random.randint(1,10)

## ala1no Up
            if a1n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm is a little frightened of letting go of things. \"I like things.\" he said to himself."

                "He climbs down."

                hide thumbup
                with Dissolve(0.5)

                jump levelcheckala

            else:

## ala1no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.85

                $ renpy.music.set_volume(0.40, delay=1.0, channel='ala1')
                $ renpy.music.set_volume(0.36, delay=1.0, channel='piano')

                "Norm ignores your recommendation and commits to the work. The resulting freedom causes him to wonder if John Lennon wrote Imagine just for him."

                "No possessions."

                "No desires."

                "No need for greed."

                "He chuckles."

                hide thumbdown
                with Dissolve(0.5)


### Choice ala2

    menu:

## Yes

        "What do you suggest?"

        "Release your baggage.":

## Roll for agreement
            $ a2y = renpy.random.randint(1,10)

## ala2yes Up
            if a2y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.7

                $ renpy.music.set_volume(0.35, delay=1.0, channel='ala2')
                $ renpy.music.set_volume(0.27, delay=1.0, channel='piano')

                "Norm nods in agreement."

                "He thinks about the dark times and how memories of them have taken root deep in his mind.\n\nAs he brings them to light, they wither."

                "He speaks the unspoken lies of his own shame.\n\nOnce spoken, they dissipate in the mountain breeze."

                "Norm feels an enormous weight lift. A weight he didn't even realize he'd been carrying."

                hide thumbup
                with Dissolve(0.5)

## ala2yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "The secrets hidden within Norm's baggage are too much for him to face."

                "He jumps down from the boulder."

                hide thumbdown
                with Dissolve(0.5)

                jump levelcheckala

## No

        "Get off the rock.":

## Roll for agreement
            $ a2n = renpy.random.randint(1,10)

## ala2no Up
            if a2n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "The secrets hidden within Norm's baggage are too much for him to face."

                "He jumps down from the boulder."

                hide thumbup
                with Dissolve(0.5)

                jump levelcheckala

            else:

## ala2no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.6

                $ renpy.music.set_volume(0.35, delay=1.0, channel='ala2')
                $ renpy.music.set_volume(0.27, delay=1.0, channel='piano')

                "Now committed to this undertaking, Norm considers the offences against him that have taken root in the dark parts of his mind. As he brings them to light, they wither."

                "He speaks the unspoken lies of his own shame. Once spoken, they dissipate in the mountain breeze."

                "A huge weight lifts."

                hide thumbdown
                with Dissolve(0.5)


### Choice ala3

    menu:

## Yes

        "Give Norm a nudge."

        "Release your ego.":

## Roll for agreement
            $ a3y = renpy.random.randint(1,10)

## ala3yes Up
            if a3y >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.55

                $ renpy.music.set_volume(0.30, delay=1.0, channel='ala3')
                $ renpy.music.set_volume(0.18, delay=1.0, channel='piano')

                "Okay. Norm struggled with this one, but eventually..."

                "Comparisons, conflicts, and jealousies unravel."

                "As he contemplates the threads of his ego piled around him, he is surprised by how clear his thoughts are.\nAs if he'd been walking around with shroud over him this whole time."

                "Norm ponders this."

                hide thumbup
                with Dissolve(0.5)

## ala3yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "\"I'm stiff,\" Norm says. Though that might not be the reason he got down."

                hide thumbdown
                with Dissolve(0.5)

                jump levelcheckala

## No

        "Get off the rock.":

## Roll for agreement
            $ a3n = renpy.random.randint(1,10)

## ala3no Up
            if a3n >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm wonders how much he can let go and still be himself. He decides to quit before the question loses its meaning."

                hide thumbup
                with Dissolve(0.5)

                jump contala

            else:

## ala3no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.55

                $ renpy.music.set_volume(0.30, delay=1.0, channel='ala3')
                $ renpy.music.set_volume(0.18, delay=1.0, channel='piano')

                "Although the work is difficult, eventually Norm's comparisons, conflicts, and jealousies unravel."

                "As Norm contemplates the threads of his ego piled around him, he is struck by utter lack of noise interfering with his thoughts."

                "Connection. Creativity. \"Truth maybe,\" he ponders."

                hide thumbdown
                with Dissolve(0.5)

### Choice ala4

    menu:

## Yes

        "What selection should he make?"

        "Release your attachments.":

## Roll for agreement
            $ a4y = renpy.random.randint(1,10)

## ala4yes Up
            if a4y >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.4

                $ renpy.music.set_volume(0.25, delay=1.0, channel='ala4')
                $ renpy.music.set_volume(0.09, delay=1.0, channel='piano')

                "Norm smiles in relief, is if rising from some psychological pool of anxiety, dependency, and stress."

                "\"Pretty liberating.\" Norm says loudly enough for the lake to echo it back to him. "

                hide thumbup
                with Dissolve(0.5)

## ala4yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm wonders how much he can let go and still be himself. He decides to quit before the question loses its meaning."

                hide thumbdown
                with Dissolve(0.5)

                jump contala

## No

        "Get off the rock.":

## Roll for agreement
            $ a4n = renpy.random.randint(1,10)

## ala4no Up
            if a4n >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm wonders how much he can let go and still be himself. He decides to quit before the question loses its meaning."

                hide thumbup
                with Dissolve(0.5)

                jump contala

            else:

## ala4no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.4

                $ renpy.music.set_volume(0.25, delay=1.0, channel='ala4')
                $ renpy.music.set_volume(0.09, delay=1.0, channel='piano')

                "Norm briefly imagines standing up, but his clarity is growing."

                "He wades out of his psychological pool of anxiety, dependency, possessiveness, and stress."

                "Attachments run off. "

                "He weighs his newfound inner peace against a sense of growing indifference. \"Huh,\" he thinks."

                hide thumbdown
                with Dissolve(0.5)


### Choice ala5

    menu:

## Yes

        "What would you advise?"

        "Release your ambitions.":

## Roll for agreement
            $ a5y = renpy.random.randint(1,10)

## ala5yes Up
            if a5y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.25

                $ renpy.music.set_volume(0.20, delay=1.0, channel='ala5')
                $ renpy.music.set_volume(0.0, delay=5.0, channel='piano')

                "With your nudge, Norm releases his dreams."

                "He watches them drift away without regret or concern."

                "\"I always wondered what \"nirvana\" meant.\" He tried smiling..."

                "...but it no longer seemed to matter."

                hide thumbup
                with Dissolve(0.5)

                jump endala

## ala5yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm could feel himself losing touch. He slides off the boulder, thinking about what he's learned."

                hide thumbdown
                with Dissolve(0.5)

                jump contala

## No

        "Get off the rock.":

## Roll for agreement
            $ a5n = renpy.random.randint(1,10)

## ala5no Up
            if a5n == 10:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm could feel himself losing touch. He slides off the boulder, thinking about what he's learned."

                hide thumbup
                with Dissolve(0.5)

                jump contala

            else:

## ala5no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                show nirvani:
                    alpha 0.25

                $ renpy.music.set_volume(0.20, delay=1.0, channel='ala5')
                $ renpy.music.set_volume(0.0, delay=5.0, channel='piano')

                "Norm can't stop. He releases his dreams."

                "As they drift away, he watches without regret or concern."

                "\"I always wondered what \"nirvana\" meant.\" He tried smiling..."

                "...but it no longer seemed to matter."

                hide thumbdown
                with Dissolve(0.5)

                jump endala

## End Alabaster Challenge


####Continue

label contala:

    $ alevel += 1
    $ levelsum += 1

    "Norm battled with his growing contentment. “How could this be wrong?” he asked no one in particular."

    "He felt so lighter. But he was also beginning to feel untethered"

    "—a small boat"
    "knot undone"
    "un-anchored"
    "oarless"
    "drifting slowly away from shore."

    "He glanced down at the lake and imagined a refreshing swim. Norm thought about jumping in but..."


## Check that all channel volmes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala5')


######## Check level for correct jump:

label levelcheckala:

##Hide images

    show bg gray
    with Dissolve(0.5)

    hide lakeani
    hide loopani
    hide nirvani
    with Dissolve(0.5)

## level check

    if levelsum == 3:
        jump codaala
    elif levelsum == 0:
        jump redoala
    elif levelsum == 2:
        if alevel == 0:
            jump faceala
        elif mlevel == 1:
            jump facegra
        elif glevel == 1:
            jump facemar
    elif levelsum == 1:
        if mlevel == 1:
            jump gra_or_ala
        elif glevel == 1:
            jump mar_or_ala
    jump mar_or_gra


#### Alabaster Fail

label endala:

    "Norm peers over the edge of the stone into the water. Still no reflection. Although it didn't worry him anymore.\nNothing did."

    "He had released too much of himself. His burdens and desires, attachments and ego all fade to nothingness."

    "Along with his grand passions and his simple joys"

    "and eventually... Norm."

    hide nirvani
    with Dissolve(1.0)

    "\"Huh,\" he thought."

## Check that all channel volumes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala5')

    show bg gray
    with Dissolve(1.0)

    hide lakeani
    hide loopani
    with Dissolve(1.0)

return


######## Redo from First Choice

label redoala:

## Check that all channel volmes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='ala5')

##Hide images

    show bg gray
    with Dissolve(0.5)

    hide loopani
    hide nirvani
    with Dissolve(0.5)

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