import abjad


def post_process_staffgroup(score):
    return score


def post_process_voice_one(voice_one, score):
    print("post processing voice one")
    
    return voice_one


def post_process_voice_two(voice_two, score):
    # REGISTER TRANSPOSITION
    abjad.mutate(voice_two).transpose(-12)

    # registers
    abjad.attach(abjad.LilyPondLiteral(r"\override TextScript.outside-staff-priority = #'1100"), voice_two[0])
    register_one = abjad.Markup(
        r"""\scale #'(0.5 . 0.5)
          \column{

            \line{
          \draw-circle #1.1 #0.3 ##t
          \draw-circle #1.1 #0.3 ##f
            }
           \line{
          \draw-circle #1.1 #0.3 ##t
          \draw-circle #1.1 #0.3 ##t
            }
           \line{
          \draw-circle #1.1 #0.3 ##f
          \draw-circle #1.1 #0.3 ##t
            }
           \line{
          \draw-circle #1.1 #0.3 ##f
          \draw-circle #1.1 #0.3 ##f
            }
          }""", direction=abjad.Up)
    abjad.attach(register_one, voice_two[0])

    # metronome mark I
    abjad.attach(
        abjad.MetronomeMark((1, 8), (64, 72), "Lento"), voice_two[0])


    # rehearsal mark
    markI = abjad.RehearsalMark(number=4)
    abjad.attach(markI, voice_two[0])
    scheme = abjad.Scheme("format-mark-box-alphabet")
    abjad.setting(score).markFormatter = scheme
    
    # numbered leaves
    selection = abjad.select(voice_two).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)
        pass

     # slurs
    start_slur = abjad.StartSlur()
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    abjad.attach(start_slur, voice_two[6])
    abjad.attach(stop_slur, voice_two[8])

    abjad.attach(abjad.LilyPondLiteral(
        r"""
        \shape #'((0 . 0) (0 . 0) (-1.5 . -3) (0 . -8)) Slur
        """), voice_two[16])
    abjad.attach(start_slur, voice_two[16])
    abjad.attach(stop_slur, voice_two[17])

    abjad.attach(start_slur, voice_two[23])
    abjad.attach(stop_slur, voice_two[25])

    abjad.attach(start_slur, voice_two[26])
    abjad.attach(stop_slur, voice_two[27])

    abjad.attach(start_slur, voice_two[34])
    abjad.attach(stop_slur, voice_two[37])

    abjad.attach(start_slur, voice_two[39])
    abjad.attach(stop_slur, voice_two[40])

    abjad.attach(start_slur, voice_two[43])
    abjad.attach(stop_slur, voice_two[45])

    abjad.attach(abjad.Clef("treble"), voice_two[0])

    # accelerando mark
    accel_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "accelerando poco a poco"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_accel = abjad.LilyPondLiteral(r"\startTextSpan")
    abjad.attach(accel_text_span, voice_two[-20])
    abjad.attach(start_accel, voice_two[-20])
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
    abjad.attach(stop_accel_text_span, voice_two[-1])

    # voice_two.append(abjad.Container(
    #     r"""cs'''2
    #         (
    #         g''8
    #         )
    #         r8
    #         r8
    #         fs'''4
    #         ~
    #         (
    #         fs'''4
    #         g'''8
    #         )
    #     """
    #     ))
    
    voice_two[-1].written_pitch = "af''"
    abjad.attach(abjad.Tie(), voice_two[-1])

    return voice_two


def post_process_voice_three(voice_three):

    return voice_three


def post_process_voice_four(voice_four, score):
    print("post processing voice four")

    voice_four[0] = "s2."
    voice_four[1] = "s4"
    voice_four[2] = "s8"
    voice_four[3] = "s4"
    voice_four[4] = "s8"
    voice_four[5] = "s4."

    # numbered leaves
    selection = abjad.select(voice_four).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)
        pass

    # add tenuto
    tenuto_notes = [11, 17, 29, 32, 52]
    for i, leaf in enumerate(selection):
        if i in tenuto_notes:
            abjad.attach(abjad.Articulation("tenuto"), voice_four[i])

    # respells
    abjad.Accidental.respell_with_sharps(selection[27])
    abjad.Accidental.respell_with_sharps(selection[37])
    abjad.Accidental.respell_with_sharps(selection[52])

    
    # literals
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_four[22])
    voice_four[22] = "s4."
    voice_four[24] = "d4"
    voice_four[25] = "d4."
    abjad.attach(abjad.LilyPondLiteral(r"\rest"), voice_four[25])
    abjad.attach(abjad.LilyPondLiteral(r"\rest"), voice_four[26])

    # slurs
    start_slur = abjad.StartSlur()
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    # shapes come first
    abjad.attach(abjad.LilyPondLiteral(
        r"""
        \shape #'((0 . 0) (1 . 0) (3 . 0) (7 . 0)) Slur
        """), voice_four[20])

    # attach slurs
    start_slur_notes = [13, 35, 39, 49, 54]
    start_slur_down_notes = [5, 20, 27, 31, 43]
    stop_slur_notes = [8, 14, 22, 28, 32, 37, 40, 47, 50, 55]
    for i, leaf in enumerate(selection):
        if i in start_slur_notes:
            abjad.attach(start_slur, voice_four[i])
        if i in start_slur_down_notes:
            abjad.attach(start_slur_down, voice_four[i])
        if i in stop_slur_notes:
            abjad.attach(stop_slur, voice_four[i])

    del voice_four[-3:]

    abjad.attach(abjad.Clef("bass"), voice_four[0])

    voice_four[-1] = "r8"
    return voice_four


def post_process_voice_five(voice_five):
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_five[11])

    return voice_five


def post_process_electronics(electronics, score):
    del score[1]
    return electronics
