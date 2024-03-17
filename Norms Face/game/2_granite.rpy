######## - GRANITE / MARTYR PATH

label granite:

    "Norm stepped onto the long grey track. It reminded him somehow of the long straight road to his childhood home."

    $ renpy.music.set_volume(0.40, delay=1.0, channel='marimba')
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')

    hide feetani1
    with Dissolve(0.5)

    hide pathgra
    with Dissolve(0.5)

    show bg gray-mid
    with Dissolve(1.0)

    show grabgani:
        xalign 0.5
        yalign 0.5
    show treeani:
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.0
    with Dissolve(1.0)

    "For some reason Norm wasn't surprised to be walking down the old lane. His mind was flooded with pictures from his past, some of which he took great pride in."

    show papersani zorder 5:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.35
    with Dissolve(0.5)

    "Rescuing Michelle’s homework from the ditch, after a heartless 5th grader threw it into the wind. Michelle’s pale blue eyes welled with gratitude."

    hide papersani
    show umbani zorder 5:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.35
    with Dissolve(0.5)

    "Running all the way home and all the way back again through a relentless downpour to get Jenny an umbrella. She'd left hers at school and Norm loved being a hero.\n\nEspecially for Jenny."

    hide umbani
    show jackani zorder 5:
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.35
    with Dissolve(0.5)

    "With his brand new driver's license, Norm drove Scott and his old dog, Jack, to the vet. He stood close when the hard choice had to be made."

    hide jackani
    with Dissolve(0.5)

    "\"This is the real me,\" Norm thought. And he suspected that somewhere down this road, his face was probably helping someone else out."

    "He went looking."

    show leaves1 zorder 3:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.0
    with Dissolve(2.0)

    "As he walks, Norm sees his neighbor Bud picking up leaves."

#### Granite Challenge

### Choice gra1

    menu:

        "Bud has been sick lately, but he's still out there working away.\n\nWhat should Norm do? Bear in mind, he might not listen. But your opinion does matter."

## Yes

        "Offer to help.":

## Roll for agreement
            $ g1y = renpy.random.randint(1,10)

## gra1yes Up
            if g1y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra1')

                "Norm takes your advice and asks if he can lend a hand.\n\n\"Well yes, that would be great!\" Bud replies thankfully."

                "Norm smiles and grabs a rake. A feeling of pride rushes through him."

                hide thumbup
                hide leaves1
                with Dissolve(1.0)

## gra1yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm has other projects to attend to."

                hide thumbdown
                hide leaves1
                with Dissolve(1.0)

                jump levelcheckgra

## No

        "Walk on by.":

## Roll for agreement
            $ g1n = renpy.random.randint(1,10)

## gra1no Up
            if g1n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm has other projects to attend to."

                hide thumbup
                hide leaves1
                with Dissolve(1.0)

                jump levelcheckgra

            else:

## gra1no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra1')

                "Norm ignores your recommendation and offers to help anyway. After all, Bud's been sick! \"That would be great!\" Bud replies thankfully."

                hide thumbdown
                hide leaves1
                with Dissolve(1.0)


### Choice gra2

    show leaves2 zorder 3:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.0
    with Dissolve(2.0)

    menu:

        "Another windy night has dropped more leaves at Bud's house. He's been feeling much better lately.\n\nWhat do you recommend?"

## Yes

        "Offer to help.":

## Roll for agreement
            $ g2y = renpy.random.randint(1,10)

## gra2yes Up
            if g2y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra2')

                "\"Well sure, if you got nothing better to do.\" Bud smiles."

                "Norm grabs his wheelbarrow. This will make the job even easier.\n\nNorm looks forward to the thanks he'll get for his assistance."

                hide thumbup
                hide leaves2
                with Dissolve(1.0)

## gra2yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "\"Honestly, Bud probably enjoys the exercise.\" Norm waved as he walked by."

                hide thumbdown
                hide leaves2
                with Dissolve(1.0)

                jump levelcheckgra

## No

        "Walk on by.":

## Roll for agreement
            $ g2n = renpy.random.randint(1,10)

## gra2no Up
            if g2n >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "\"Honestly, Bud probably enjoys the exercise.\" Norm waved as he walked by."

                hide thumbup
                hide leaves2
                with Dissolve(1.0)

                jump levelcheckgra

            else:

## gra2no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra2')

                "Norm considers walking by this time, but decides to help out anyway. \"Can I help?\""
                "\"Well sure, if you got nothing better to do.\" Bud smiles."

                hide thumbdown
                hide leaves2
                with Dissolve(1.0)


### Choice gra3

    show leaves3 zorder 3:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.0
    with Dissolve(2.0)

    menu:

        "Bud and his grandchildren are picking up the newest batch leaves.\n\nWhat is Norm's best option in your opinion?"

## Yes

        "Offer to help":

## Roll for agreement
            $ g3y = renpy.random.randint(1,10)

## gra3yes Up
            if g3y >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra3')

                "\"You really don't have to, were doing fine,\" Bud says jovially."

                "\"It's not a problem at all!\" Norm replies. He's sure that Bud will appreciate being able to focus more on the kids if he's helping."

                hide thumbup
                hide leaves3
                with Dissolve(1.0)

## gra3yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm thinks better of it. It seems like \'grandkid time\'."

                "\"Great job getting the kids outside, Bud!\" He smiles and waves. The kids throw leaves at Norm as he walks by."

                hide thumbdown
                hide leaves3
                with Dissolve(1.0)

                jump levelcheckgra

## No

        "Walk on by.":

## Roll for agreement
            $ g3n = renpy.random.randint(1,10)

## gra3no Up
            if g3n >= 3:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Bud seems to be enjoying the time with his grandkids. Norm smiles and waves as he walks by."

                "Joyful, yelling children shower him with leaves as he does."

                hide thumbup
                hide leaves3
                with Dissolve(1.0)

                jump contgra

            else:

## gra3no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra3')

                "Norm loves kids too much to walk by. He grabs his tools and filled a plastic tub with cookies to share."

                hide thumbdown
                hide leaves3
                with Dissolve(1.0)

### Choice gra4

    show leaves4 zorder 3:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.0
    with Dissolve(2.0)

    menu:

        "This time, upon asking to help, Bud smiled and replied \"Oh, thank you. But I think I've got it.\" Norm is certain that if he comes back with his gloves and tools Bud will greatly appreciate the support.\n\nWhat would you advise?"

## Yes

        "Help anyway.":

## Roll for agreement
            $ g4y = renpy.random.randint(1,10)

## gra4yes Up
            if g4y >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra4')

                "Bud is quiet. Norm is quietly bursting with pride."

                hide thumbup
                hide leaves4
                with Dissolve(1.0)

## gra4yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm feels a little disappointed, but Bud was clear."

                hide thumbdown
                hide leaves4
                with Dissolve(1.0)

                jump contgra

## No

        "Walk on by.":

## Roll for agreement
            $ g4n = renpy.random.randint(1,10)

## gra4no Up
            if g4n >= 4:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "Norm feels a little hollow at not helping. But Bud was clear."

                hide thumbup
                hide leaves4
                with Dissolve(1.0)

                jump contgra

            else:

## gra4no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra4')

                "Norm dismisses your advice, and Bud's reply, and decides to help out anyway. \"Bud secretly wants the assist. I'm sure of it.\""

                hide thumbdown
                hide leaves4
                with Dissolve(1.0)


### Choice gra5

    show leaves5 zorder 3:
        xanchor 0.0
        yanchor 1.0
        xpos 0.0
        ypos 1.0
    with Dissolve(2.0)

    menu:

        "A storm dropped yet more leaves. Knowing how grateful he will be, Norm considers grabbing his tools and cleaning the yard before Bud gets home from work.\n\nWhat do you suggest?"

## Yes

        "Clean the yard.":

## Roll for agreement
            $ g5y = renpy.random.randint(1,10)

## gra5yes Up
            if g5y >= 2:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra5')

                "Bud's reaction was less appreciative than Norm had expected. \"Must be having a bad day,\" Norm thought."

                hide thumbup
                hide leaves5
                with Dissolve(1.0)

                jump endgra

## gra5yes Down
            else:
                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "After the last time, when Bud told him not to help, Norm worries that maybe Bud doesn't appreciate his help quite as much as he thought."

                "Norm walks on by."

                hide thumbdown
                hide leaves5
                with Dissolve(1.0)

                jump contgra

## No

        "Walk on by.":

## Roll for agreement
            $ g5n = renpy.random.randint(1,10)

## gra5no Up
            if g5n == 10:
                show thumbup zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                "After the last time, when Bud told him not to help, Norm worries that maybe Bud doesn't appreciate his help quite as much as he thought."

                "Norm walks on by."

                hide thumbup
                hide leaves5
                with Dissolve(1.0)

                jump contgra

            else:

## gra5no Down

                show thumbdown zorder 9:
                    xalign 1.0
                    yalign 0.0
                with Dissolve(1.0)

                $ renpy.music.set_volume(0.40, delay=1.0, channel='gra5')

                "Norm couldn't help himself. And he easily put aside Bud's reaction, which was less appreciative than Norm had expected. \"Must be having a bad day,\" Norm thought."

                hide thumbdown
                hide leaves5
                with Dissolve(1.0)

                jump endgra

## End Granite Challenge


#### Continue

label contgra:

    $ glevel += 1
    $ levelsum += 1

    "Norm still didn't know where his face went. But he did know that it wasn't on the road to martyrdom. He was more than happy to help others in need. But he could feel himself needing that acclaim a little too much. Becoming dependent on it."

    "With that realization, the road, the tree, and the newly fallen leaves all slipped away."

## Check that all channel volumes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra5')


######## Check level for correct jump:

label levelcheckgra:

##Hide images

    show bg gray
    with Dissolve(0.5)

    hide treeani
    hide grabgani
    hide leaves
    with Dissolve(0.5)

## level check

    if levelsum == 3:
        jump codagra
    elif levelsum == 0:
        jump redogra
    elif levelsum == 2:
        if glevel == 0:
            jump facegra
        elif mlevel == 1:
            jump faceala
        elif alevel == 1:
            jump facemar
    elif levelsum == 1:
        if mlevel == 1:
            jump gra_or_ala
        elif alevel == 1:
            jump mar_or_gra
    jump mar_or_ala


#### Granite Fail

label endgra:

    "Norm felt oddly desperate. He wasn't quite sure how to respond to a request to \"NOT help\" someone. In an uncomforable realization, Norm understood that he'd become dependent on the appreciation of others in order to feel of value."

    "\"That doesn't seem right,\" he complained to himself."

    "Which reminded him... He still hadn't found his face."

## Check that all channel volumes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.0, delay=2.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='gra1')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='gra2')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='gra3')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='gra4')
    $ renpy.music.set_volume(0.0, delay=2.0, channel='gra5')

##Hide images

    show bg gray
    with Dissolve(2.0)

    hide treeani
    hide grabgani
    hide leaves
    with Dissolve(2.0)

return


######## Redo from First Choice

label redogra:

## Check that all channel volumes are 0, with piano at 0.35
    $ renpy.music.set_volume(0.40, delay=5.0, channel='piano')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='marimba')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra1')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra2')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra3')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra4')
    $ renpy.music.set_volume(0.0, delay=5.0, channel='gra5')

##Hide images

    show bg gray
    with Dissolve(0.5)

    hide treeani
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
    show pathgra zorder 2:
        zoom 2.0
        xanchor 0.5
        yanchor 0.0
        xpos 0.5
        ypos 0.0
    with Dissolve(0.5)

    jump choicer1