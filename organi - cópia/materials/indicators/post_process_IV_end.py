import abjad
    
        
def post_process_staffgroup(score):
    return score


def post_process_voice_one(voice_one, score):
    print("post processing voice one")
    voice_one.extend("s2. s2. s2. s2 s8 g'''8~")
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_one[-2])
    
    
    return voice_one


def post_process_voice_two(voice_two, score):
    # REGISTER TRANSPOSITION
    abjad.mutate(voice_two).transpose(-12)
    
    # literals
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_two[0])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_two[4])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_two[6])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_two[7])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_two[8])

    # metronome mark I
    # abjad.attach(
#         abjad.MetronomeMark((1, 8), (100), ), voice_two[0])
#
    # numbered leaves
    selection = abjad.select(voice_two).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)
        pass

    # slurs
    start_slur = abjad.StartSlur()
    start_slur_up = abjad.StartSlur(direction=abjad.Up)
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    # attach slurs
    start_stop_slur = [(3, 4), (8, 9), (10, 11), (12, 14)]
    for tuples in start_stop_slur:
        abjad.attach(start_slur, voice_two[tuples[0]])
        abjad.attach(stop_slur, voice_two[tuples[1]])
    # shapes come first
    abjad.attach(abjad.LilyPondLiteral(
            r"""
            \shape #'((1 . 0) (0 . 0) (-3 . 0) (-3 . 0)) Slur
            """), voice_two[7])
    abjad.attach(start_slur_up, voice_two[7])
    abjad.attach(stop_slur, voice_two[8])
    
    # delete
    del voice_two[-1]
    
    # accelerando mark
    accel_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "accelerando"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_accel = abjad.LilyPondLiteral(r"\startTextSpan")
    abjad.attach(accel_text_span, voice_two[0])
    abjad.attach(start_accel, voice_two[0])
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
    abjad.attach(stop_accel_text_span, voice_two[-1])
    
    return voice_two


def post_process_voice_three(voice_three):
    # literals
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_three[0])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_three[6])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_three[8])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceOne"), voice_three[9])
    abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_three[10])
    
    abjad.attach(abjad.LilyPondLiteral(r" \tieUp"), voice_three[5])
    abjad.attach(abjad.LilyPondLiteral(r" \tieNeutral"), voice_three[7])
    abjad.attach(abjad.LilyPondLiteral(r" \tieUp"), voice_three[8])
    
    
    
    # numbered leaves
    selection = abjad.select(voice_three).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)
        pass
    

    del voice_three[-2:]
   
    
    
    # respells
    abjad.Accidental.respell_with_flats(voice_three[1])
    abjad.Accidental.respell_with_sharps(voice_three[8:10])
    voice_three[11].written_pitch = "e''"
    abjad.Accidental.respell_with_flats(voice_three[12])
    
    # slurs
    start_slur = abjad.StartSlur()
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    #shapes come first
    # abjad.attach(abjad.LilyPondLiteral(
#         r"""
#         \shape #'((0 . 0) (1 . 0) (3 . 0) (7 . 0)) Slur
#         """), voice_four[20])

    # attach slurs
    start_stop_slur = [(0, 1), (2, 3), (10, 11), (12, 13), (14, 15)]
    for tuples in start_stop_slur:
        abjad.attach(start_slur, voice_three[tuples[0]])
        abjad.attach(stop_slur, voice_three[tuples[1]])
    
    voice_three[-1].written_duration = abjad.Duration(1, 4)
    voice_three.extend("r8")
    
    return voice_three


def post_process_voice_four(voice_four, score):
    print("post processing voice four")
    
    # del voice_four[-4:]
    voice_four[-1].written_duration = (3, 8)
    clef = abjad.Clef("treble")
    abjad.attach(clef, voice_four[1])
    # numbered leaves
    selection = abjad.select(voice_four).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)
        pass
    
    del voice_four[-2:]
    voice_four.extend("r4.")
    
    
    # add tenuto
    # tenuto_notes = [11, 17, 29, 32, 52]
    # for i, leaf in enumerate(selection):
    #     if i in tenuto_notes:
    #         # abjad.attach(abjad.Articulation("tenuto"), voice_four[i])
    #         pass

    # respells
    
# 
#     abjad.Accidental.respell_with_sharps(selection[52])

    
    
    # voice_four[22] = "s4."
    # voice_four[24] = "d4"
#     voice_four[25] = "d4."
    # abjad.attach(abjad.LilyPondLiteral(r"\rest"), voice_four[25])
    # abjad.attach(abjad.LilyPondLiteral(r"\rest"), voice_four[26])

    # slurs
    # start_slur = abjad.StartSlur()
#     start_slur_down = abjad.StartSlur(direction=abjad.Down)
#     stop_slur = abjad.StopSlur()

    

    # attach slurs
    # start_slur_notes = [13, 35, 39, 49, 54]
#     start_slur_down_notes = [5, 20, 27, 31, 43]
#     stop_slur_notes = [8, 14, 22, 28, 32, 37, 40, 47, 50, 55]
    # for i, leaf in enumerate(selection):
#         if i in start_slur_notes:
#             abjad.attach(start_slur, voice_four[i])
#         if i in start_slur_down_notes:
#             abjad.attach(start_slur_down, voice_four[i])
#         if i in stop_slur_notes:
#             abjad.attach(stop_slur, voice_four[i])

    # del voice_four[-3:]

    # abjad.attach(abjad.Clef("treble2"), voice_four[0])

    # voice_four.append(abjad.Container(
#         r"""b8
#             \clef "treble"
#             ds'4
#             ~
#             ds'8
#             fs'8
#             )
#             r8
#             as'4.
#             (
#             d''8
#             )
#             r8
#             f''8
#         """
#         ))
    return voice_four


def post_process_voice_five(voice_five):
    # abjad.attach(abjad.LilyPondLiteral(r" \voiceTwo"), voice_five[11])

    return voice_five


def post_process_electronics(electronics, score):
    del score[1]
    return electronics
