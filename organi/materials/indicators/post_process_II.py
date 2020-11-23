import abjad


def post_process_staffgroup(score):
    print("post processing staff group")
    # rh_staff = score['Piano_Staff'][0]
    # lh_staff = score['Piano_Staff'][1]
    # voice_four = score['LH_Voice_Four']
    #
    # staff_change1 = abjad.StaffChange(lh_staff)
    # staff_change2 = abjad.StaffChange(rh_staff)
    # abjad.attach(staff_change2, voice_four[-3])
    # abjad.attach(staff_change1, voice_four[-2])

    # rehearsal mark box
    scheme = abjad.Scheme("format-mark-box-alphabet")
    abjad.setting(score).markFormatter = scheme
    return score


def post_process_voice_one(voice_one, score):
    # rehearsal mark
    markI = abjad.RehearsalMark(number=2)
    abjad.attach(markI, voice_one[0])

    # metronome mark I
    abjad.attach(
        abjad.MetronomeMark(None, None, "Quasi Statico"), voice_one[0])
    
    # metronome mark II
    abjad.attach(
        abjad.MetronomeMark(None, None, "Lento"), voice_one[6][0])

    # metronome mark III
    abjad.attach(
        abjad.MetronomeMark(None, None, "Quasi Statico"), voice_one[13])

    # metronome mark IV
    abjad.attach(
        abjad.MetronomeMark(None, None, "Lento"), voice_one[21])


    # REGISTER TRANSPOSITION
    abjad.mutate(voice_one).transpose(-12)

    voice_one.append(abjad.Skip((3, 4)))
    voice_one.append(abjad.Skip((3, 4)))
    # text script (timbres) priority
    priority = abjad.LilyPondLiteral(
        r" \once \override Staff.TextScript.outside-staff-priority = #1100" +
        " " + r"\once \override Staff.TextScript.padding = #4")
    abjad.attach(priority, voice_one[-2])

    # registers
    register_two = abjad.Markup(
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
          \draw-circle #1.1 #0.3 ##f
            }
           \line{
          \draw-circle #1.1 #0.3 ##f
          \draw-circle #1.1 #0.3 ##f
            }
          }""", direction=abjad.Up)
    abjad.attach(register_two, voice_one[-2])
    abjad.attach(abjad.Clef("bass"), voice_one[-8])
    return voice_one


def post_process_voice_two(voice_two):

    return voice_two


def post_process_voice_three(voice_three):

    return voice_three


def post_process_voice_four(voice_four, score):
    print("post processing voice four")
    # delete and change durations
    voice_four[-2].written_duration = (1, 4)
    del voice_four[-1]
    voice_four[-1].written_duration = (3, 8)
    abjad.mutate(voice_four[17]).transpose(-12)


    # change staff
    rh_staff = score['Piano_Staff'][0]
    lh_staff = score['Piano_Staff'][1]
    voice_four = score['LH_Voice_Four']

    staff_change1 = abjad.StaffChange(lh_staff)
    staff_change2 = abjad.StaffChange(rh_staff)
    abjad.attach(staff_change2, voice_four[-3])
    abjad.attach(staff_change1, voice_four[-2])

    abjad.attach(abjad.Fermata(), voice_four[-1])

    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.pitch.PitchRange("[C6, +inf]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.pitch.PitchRange("[D4, +inf]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.pitch.PitchRange("[C1, C#4]")
    selection = abjad.select(voice_four).leaves()
    for i, leaf in enumerate(selection):
        # test3 = leaf in clef3_range
        test2 = leaf in clef2_range
        test1 = leaf in clef1_range
        test_note = not isinstance(leaf, abjad.Rest)
        # if test_note is True and test3 is True:
            # abjad.attach(clef3, voice_four[i])
        if test_note is True and test2 is True:
            abjad.attach(clef2, voice_four[i])
        if test_note is True and test1 is True:
            abjad.attach(clef1, voice_four[i])

    abjad.Accidental.respell_with_sharps(voice_four[5:7])
    # REGISTER TRANSPOSITION
    abjad.mutate(voice_four[:-7]).transpose(-12)

    # slurs
    start_slur = abjad.StartSlur()
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    abjad.attach(start_slur, voice_four[6])
    abjad.attach(stop_slur, voice_four[8])

    abjad.attach(start_slur, voice_four[12])
    abjad.attach(stop_slur, voice_four[15])

    abjad.attach(start_slur_down, voice_four[18])
    abjad.attach(stop_slur, voice_four[21])

    abjad.attach(start_slur_down, voice_four[-4])
    abjad.attach(stop_slur, voice_four[-3])

    # metronome mark IV
    abjad.attach(
        abjad.MetronomeMark(None, None, "meno mosso"), voice_four[-4])

    return voice_four


def post_process_electronics(electronics):
    # elec_literal = r"b4 s4 s4 s4 b4"
    # electronics.extend(elec_literal)
    # abjad.attach(abjad.LilyPondLiteral(
    #     r'\hide Stem'
    #     r' \set fontSize = -3'
    #     r' \override Staff.StaffSymbol.staff-space = #(magstep -3)'
    #     r' \override Staff.StaffSymbol.thickness = #(magstep -3)'
    #     r' \override Staff.Clef.font-size = -3'
    #     r' \override Staff.TimeSignature.font-size = -3'),
    #     electronics[0])
    # abjad.attach(abjad.LilyPondLiteral(
    #     r'\stopStaff'
    #     r' \hide Staff.BarLine'
    #     r' \hide Staff.Clef'
    #     r' \hide Staff.TimeSignature'),
    #     electronics[0])
    #
    # abjad.glissando(
    #     electronics[:],
    #     abjad.tweak("zigzag").style,
    #     # left_broken=True,
    #     right_broken=True,
    #     hide_middle_note_heads=True,
    #     )

    return electronics
