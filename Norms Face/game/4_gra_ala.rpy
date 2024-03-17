######## - after round 1 marble decides between b and c


label gra_or_ala:

##Hide images
    show bg gray
    with Dissolve(1.0)

    hide tabani
    hide friends
    with Dissolve(1.0)

## Reset items to pre-path state w/o marble

    show pathala zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.75
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

#### Second Round Choice - Granite or Alabaster

    menu:

        "Granite formed a sturdy road built for heroes and martyrs.":

            hide pathmar
            hide pathala
            with Dissolve(0.5)

            show pathgra:
                ease 2.0 xpos 0.5 ypos 0.01 zoom 3.0

            jump granite

        "The white path felt cool and clear-headed, like the bright smile of a monk, unclouded by worry or strife.":

            hide pathgra
            hide pathmar
            with Dissolve(0.5)

            show pathala:
                ease 2.0 xpos 0.65 ypos 0.01 zoom 3.0

            jump alabaster