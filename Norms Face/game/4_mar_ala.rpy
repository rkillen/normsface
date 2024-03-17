######## - Second Round Choice - Marble or Alabaster

label mar_or_ala:

##Hide images
    show bg gray
    with Dissolve(0.5)

    hide grabgani
    hide leaves
    with Dissolve(0.5)

## Reset items to pre-path state
    show pathmar zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.25
        ypos 0.0
    show pathala zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.75
        ypos 0.0
    with Dissolve(0.5)

    "pause"

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
                ease 2.0 xpos 0.35 ypos 0.01 zoom 3.0

            jump marble

        "The white path felt cool and clear-headed, like the bright smile of a monk, unclouded by worry or strife.":

            hide pathgra
            hide pathmar
            with Dissolve(0.5)

            show pathala:
                ease 2.0 xpos 0.65 ypos 0.01 zoom 3.0

            jump alabaster