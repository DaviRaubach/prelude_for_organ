import abjad


def post_process_staffgroup(score):
    return score


def post_process_voice_one(voice_one, score):
    print("post processing voice one")

    voice_one[-2] = abjad.Skip((3, 4))
    voice_one[-1] = abjad.Skip((3, 4))

    # change staff
    voice_one = score['RH_Voice_One']
    rh_staff = score['Piano_Staff'][0]
    lh_staff = score['Piano_Staff'][1]

    staff_change1 = abjad.StaffChange(lh_staff)
    staff_change2 = abjad.StaffChange(rh_staff)
    abjad.attach(staff_change1, voice_one[6][0])

    # change clef
    clef1 = abjad.Clef("bass")
    abjad.attach(clef1, voice_one[8])

    # tempos 
    lento = abjad.MetronomeMark(None, None, "Lento")
    quasi_statico = abjad.MetronomeMark(None, None, "Quasi Statico")
    # metronome mark I
    abjad.attach(lento, voice_one[0])
    # metronome mark II
    abjad.attach(quasi_statico, voice_one[8])
    # metronome mark III
    abjad.attach(lento, voice_one[15][0])

    # metronome mark IV
    abjad.attach(abjad.MetronomeMark(None, None, "subito Quasi Statico"), voice_one[18])
    # metronome mark V
    abjad.attach(lento, voice_one[22])
    # metronome mark VI
    abjad.attach(abjad.MetronomeMark(None, None, "più mosso"), voice_one[25])

    # rehearsal mark
    markI = abjad.RehearsalMark(number=3)
    abjad.attach(markI, voice_one[0])
    scheme = abjad.Scheme("format-mark-box-alphabet")
    abjad.setting(score).markFormatter = scheme
    return voice_one


def post_process_voice_two(voice_two):
    
    return voice_two


def post_process_voice_three(voice_three):

    return voice_three


def post_process_voice_four(voice_four, score):
    print("post processing voice four")
    rh_staff = score['Piano_Staff'][0]
    lh_staff = score['Piano_Staff'][1]
    voice_four = score['LH_Voice_Four']

    staff_change1 = abjad.StaffChange(lh_staff)
    staff_change2 = abjad.StaffChange(rh_staff)
    abjad.attach(staff_change2, voice_four[5])

    abjad.attach(staff_change1, voice_four[-5])
    abjad.attach(staff_change2, voice_four[-2])
    abjad.attach(staff_change1, voice_four[-1])
    
# REGISTER TRANSPOSITION
    selection_reg = abjad.select(voice_four).leaves()
    register_range = abjad.pitch.PitchRange("[C4, +inf]")
    for leaf in selection_reg:
        test_resgister = leaf in register_range
        if test_resgister is True:
            abjad.mutate(leaf).transpose(-12)

    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.pitch.PitchRange("[A#6, +inf]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.pitch.PitchRange("[D4, G6]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.pitch.PitchRange("[C1, C#4]")
    selection = abjad.select(voice_four).leaves()
    for i, leaf in enumerate(selection):
        test3 = leaf in clef3_range
        test2 = leaf in clef2_range
        test1 = leaf in clef1_range
        test_note = not isinstance(leaf, abjad.Rest)
        
        if test_note is True and test3 is True:
            abjad.attach(clef3, voice_four[i])
        if test_note is True and test2 is True:
            abjad.attach(clef2, voice_four[i])
        if test_note is True and test1 is True:
            abjad.attach(clef1, voice_four[i])
        


    # slurs
    start_slur = abjad.StartSlur()
    start_slur_down = abjad.StartSlur(direction=abjad.Down)
    stop_slur = abjad.StopSlur()

    abjad.attach(start_slur, voice_four[6])
    abjad.attach(stop_slur, voice_four[9])

    abjad.attach(start_slur, voice_four[12])
    abjad.attach(stop_slur, voice_four[16])

    abjad.attach(start_slur, voice_four[18])
    abjad.attach(stop_slur, voice_four[21])

    abjad.attach(start_slur, voice_four[23])
    abjad.attach(stop_slur, voice_four[27])

    abjad.attach(start_slur, voice_four[-4])
    abjad.attach(stop_slur, voice_four[-2])

    # metronome mark VII
    quasi_statico = abjad.MetronomeMark(None, None, "Quasi Statico")
    abjad.attach(quasi_statico, voice_four[-4])

    # accelerando mark
    accel_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "accelerando"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_accel = abjad.LilyPondLiteral(r"\startTextSpan")
    abjad.attach(accel_text_span, voice_four[13])
    abjad.attach(start_accel, voice_four[13])
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
    abjad.attach(stop_accel_text_span, voice_four[16])

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
