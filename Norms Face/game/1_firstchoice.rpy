label choicer1:

## Display images

    show feetani1 zorder 2:
        xalign 0.5
        yalign 1.3
    with Dissolve(1.5)

    "His bare feet sank just a little into the warm, wet sand as he considered the three paths before him."

#### First Round Choice

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

        "The white path felt cool and clear-headed, like the bright smile of a monk, unclouded by worry or strife.":

            hide pathgra
            hide pathmar
            with Dissolve(0.5)

            show pathala:
                ease 2.0 xpos 0.65 ypos -0.03 zoom 3.0

            jump alabaster