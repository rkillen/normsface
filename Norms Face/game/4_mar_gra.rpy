######## - Second Round Choice - Marble or Granite

label mar_or_gra:

##Hide images

    show bg gray
    with Dissolve(0.5)

    hide loopani
    hide nirvani
    hide grabgani
    hide leaves
    hide tabani
    hide friends
    with Dissolve(1.0)


## Reset items to pre-path state
    show pathmar zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.25
        ypos 0.0
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

    "His bare feet sank just a little into the warm, wet sand as he considered the two paths remaining before him."

#### Second Round Choice

    menu:

        "The black stone was warm and inviting—an Irish coffee, smooth jazz, a friendly kiss on the cheek that lingers just a little bit longer than necessary.":

            hide pathala
            hide pathgra
            with Dissolve(0.5)

            show pathmar:
                ease 2.0 xpos 0.35 ypos -0.03 zoom 3.0

            jump marble

        "Granite formed a sturdy road built for heroes and martyrs.":

            hide pathmar
            hide pathala
            with Dissolve(0.5)

            show pathgra:
                ease 2.0 xpos 0.5 ypos -0.03 zoom 3.0

            jump granite