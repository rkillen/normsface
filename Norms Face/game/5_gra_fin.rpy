######## - after round 2 faces granite

label facegra:

##Hide images in cont***

    show bg gray
    with Dissolve(1.0)

## Reset items to pre-path state w/o marble

    show pathgra zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.5
        ypos 0.0
    with Dissolve(0.5)

    show feetani1 zorder 2:
        xalign 0.5
        yalign 1.3
    with Dissolve(1.5)

#### Final Choice

    menu:

        "His bare feet sank just a little into the warm, wet sand as he considers the last remaining path before him."

        "Granite formed a sturdy road built for heroes and martyrs.":

            hide pathmar
            hide pathala
            with Dissolve(0.5)

            show pathgra:
                ease 2.0 xpos 0.5 ypos 0.01 zoom 3.0

            jump granite


######## - granite coda

label codagra:

    "Sitting in the sand, back on the beach, Norm was deep in thought. \"Can helping others become an addiction?\""

    "\"Maybe.\" he said to no one, except the gulls which had returned to their preening."

    "The sun grew brighter, until Norm had to look down."

    stop piano fadeout 2.0

    hide seaani1
    hide sunani1
    hide gulani1
    show whiteover zorder 9
    with Dissolve(2.0)

    jump end