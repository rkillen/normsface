######## - after round 2 faces alabaster

label faceala:

##Hide images in cont***

    show bg gray
    with Dissolve(0.5)

## Reset items to pre-path state

    show pathala zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.75
        ypos 0.0
    with Dissolve(0.5)

    show feetani1 zorder 2:
        xalign 0.5
        yalign 1.3
    with Dissolve(1.5)

#### Final Choice

    menu:

        "His bare feet sank just a little into the warm, wet sand as he considers the final path remaining before him."

        "The white path felt cool and clear-headed, like the bright smile of a monk, unclouded by worry or strife.":

            hide pathgra
            hide pathmar
            with Dissolve(0.5)

            show pathala:
                ease 2.0 xpos 0.65 ypos 0.01 zoom 3.0

            jump alabaster

######## - alabaster coda

label codaala:

    show seaani1 zorder 1
    show sunani1 zorder 2:
        xalign 0.15
        yalign 0.1
    show gulani1 zorder 3:
        zoom 0.9
        xalign 0.35
        yalign 0.60
    with Dissolve(0.5)

    "The sand feels warm on Norm's feet as he, once again looks out across a calm sea. The gulls have returned, though they still eye him with suspicion."

    "Norm feels lighter, having let go of some things he doesn't need. But he was also relieved to step away when he did. \"I don't think I'm ready for a full dose of enlightment. I'm happy with small doses over a cup of tea.\""

    "As he stood there the sun got brighter, until he had to look down."

    stop piano fadeout 2.0

    hide seaani1
    hide sunani1
    hide gulani1
    show whiteover zorder 9
    with Dissolve(2.0)

    jump end