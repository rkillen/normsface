######## - after round 2 faces marble

label facemar:

##Hide images in cont***

    show bg gray
    with Dissolve(0.5)

## Reset items to pre-path state
    show pathmar zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.25
        ypos 0.0
    with Dissolve(0.5)

    show feetani1 zorder 2:
        xalign 0.5
        yalign 1.3
    with Dissolve(1.5)

#### Final Choice

    menu:

        "His bare feet sank just a little into the warm, wet sand as he considered the final path."

        "The black stone was warm and inviting—an Irish coffee, smooth jazz, a friendly kiss on the cheek that lingers just a little bit longer than necessary.":

            hide pathala
            hide pathgra
            with Dissolve(0.5)

            show pathmar:
                ease 2.0 xpos 0.35 ypos 0.01 zoom 3.0

            jump marble


######## - marble coda

label codamar:

    show seaani1 zorder 1
    show sunani1 zorder 2:
        xalign 0.15
        yalign 0.1
    show gulani1 zorder 3:
        zoom 0.9
        xalign 0.35
        yalign 0.60
    with Dissolve(0.5)

    "Norm chuckled and tossed a pebble toward the gulls, which had come back to their spot and were now bathing. \"I'm not going to feel bad for putting 'me' first from time to time. But maybe with limits.\""

    "The sky got brighter and brighter until Norm was forced to look down."

    stop piano fadeout 2.0

    hide seaani1
    hide sunani1
    hide gulani1
    show whiteover zorder 9
    with Dissolve(2.0)

    jump end