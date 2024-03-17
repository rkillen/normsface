####Credits

##Continue music while showing the beach scene w/o paths.

label credits:

    hide cupfaceani
    hide normani1
    hide cuptopani
    with Dissolve(1.0)

    show seaani1 zorder 1
    show sunani1 zorder 2:
        xalign 0.15
        yalign 0.1
    show gulani1 zorder 3:
        zoom 0.9
        xalign 0.35
        yalign 0.60
    with Dissolve(1.0)

    "Music, Art & Story by Robert Killen, 2024"

    "Thank you to the Acerola Game Jam 0 for the inspiration!"

    stop mar5 fadeout 4.0

    hide seaani1
    hide sunani1
    hide gulani1
    with Dissolve(3.0)

    pause 2.0

return