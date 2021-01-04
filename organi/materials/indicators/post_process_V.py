import abjad
from organi.materials.pitches import pitches_V as pitches


def custom_ties(music):
    tuplets = abjad.select(music).tuplets()
    for tuplet in tuplets:
        leaves = abjad.select(tuplet).leaves()
        for leaf in leaves:
            if not isinstance(leaf, abjad.Rest):
                pitch = [leaf.written_pitch]
                abjad.mutate(leaf).replace(abjad.Chord(pitch, leaf.written_duration))
        
        leaves2 = abjad.select(tuplet).leaves()
        # print(leaves2)
        for leaf1, leaf2 in zip(leaves2, leaves2[1:]):
            if isinstance(leaf1, abjad.Chord):
                pitch1 = leaf1.written_pitches
                pitch2 = leaf2.written_pitches
                interval = abjad.NumberedPitch(pitch2[0]) - abjad.NumberedPitch(pitch1[0])
                interval = abs(interval.number)
                if interval <= 10 and interval != 0:
                    leaf2.written_pitches = [pitch1[0], pitch2[0]]
    # TIES
    selection = abjad.select(music).leaves().logical_ties()
    # verify next leave to apply ties correctly
    for leave, next_leave in zip(selection, selection[1:]):
        if isinstance(leave[-1], abjad.Note) and isinstance(next_leave[0], abjad.Chord):
            # verify if there are same pitches in both leaves
            for item in next_leave[0].written_pitches:
                if item == leave[-1].written_pitch:
                    # print("note-chord tie:" + str(leave[-1]))
                    abjad.attach(abjad.Tie(), leave[-1])
        if isinstance(leave[-1], abjad.Note) and isinstance(next_leave[0], abjad.Note):
            if leave[-1].written_pitch == next_leave[0].written_pitch:
                # print("note-note tie:" + str(leave[-1]))
                abjad.attach(abjad.Tie(), leave[-1])
        # if leave is chord
        if isinstance(leave[-1], abjad.Chord) and isinstance(next_leave[0], abjad.Chord):
            # verify if there are same pitches in both leaves
            if set(leave[-1].written_pitches) & set(next_leave[0].written_pitches):
                # print("chord-chord tie:" + str(leave[-1]))
                abjad.attach(abjad.Tie(), leave[-1])
        if isinstance(leave[-1], abjad.Chord) and isinstance(next_leave[0], abjad.Note):
            for item in leave[-1].written_pitches:
                # print("chord-note tie:" + str(leave[-1]))
                if item == next_leave[0].written_pitch:
                    abjad.attach(abjad.Tie(), leave[-1])
    tuplets = abjad.select(music).tuplets()
    
    for tuplet in tuplets:
        if tuplet.multiplier == 1:
            abjad.mutate(tuplet).extract()

    return music

def respell(music):
    selection = abjad.select(music).leaves()
    selection = selection.group_by_measure()
    for measure in selection:
        for leaf1 in measure:
            if isinstance(leaf1, abjad.Chord):
                pitches_leaf_1 = leaf1.written_pitches
                if len(pitches_leaf_1) == 2:
                    pitch1_str = str(pitches_leaf_1[0])
                    pitch2_str = str(pitches_leaf_1[1])
                    if pitch1_str[0] == pitch2_str[0]:
                        # print('they are')
                        if pitch1_str[1] == 'f': 
                            # print('first pitch is flat')
                            abjad.Accidental.respell_with_sharps(measure)
                        if pitch2_str[1] == 'f': 
                            # print('second pitch is flat')
                            abjad.Accidental.respell_with_sharps(measure)
                        if pitch1_str[1] == 's':
                            # print('first pitch is sharp')
                            abjad.Accidental.respell_with_flats(measure)
                        if pitch2_str[1] == 's':
                            # print('second pitch is sharp')
                            abjad.Accidental.respell_with_flats(measure)

def change_clef(music):
    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.pitch.PitchRange("[F6, +inf]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.pitch.PitchRange("[E4, E5]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.pitch.PitchRange("[-inf, A3]")
    # clef0 = abjad.Clef("bass_8")
    # clef0_range = abjad.pitch.PitchRange("[-inf, C1]")
    
    # REGISTER TRANSPOSITION
    register_range = abjad.pitch.PitchRange("[C4, +inf]")
    select_reg = abjad.select(music).leaves()
    for i, leaf in enumerate(select_reg):
        if not isinstance(leaf, abjad.Rest):
            test = leaf in register_range
            if test is True:
                abjad.mutate(leaf).transpose(-12)
            if test is False:
                # print((i, leaf))
                pass
    selection = abjad.select(music).leaves()
    # selection = selection[0::3]
    for i, leaf in enumerate(selection):
        test3 = leaf in clef3_range
        test2 = leaf in clef2_range
        test1 = leaf in clef1_range
        # test0 = leaf in clef0_range
        test_note = not isinstance(leaf, abjad.Rest)
        if test_note is True and test2 is True:
            abjad.attach(clef2, selection[i])
        if test_note is True and test3 is True:
            abjad.attach(clef3, selection[i])
        if test_note is True and test1 is True:
            abjad.attach(clef1, selection[i])
        # elif test_note is True and test0 is True:
        #     abjad.attach(clef0, selection[i])


def post_process_staffgroup(score):
    return score


def post_process_voice_one(voice_one, score):
    print("post processing voice one")
    custom_ties(voice_one)
    respell(voice_one)
    # metronome mark I
    abjad.attach(
        abjad.MetronomeMark((1, 8), (128, 144), "Andante, molto liberamente"), voice_one[0])
    # rehearsal mark
    markI = abjad.RehearsalMark(number=5)
    abjad.attach(markI, voice_one[0])
    scheme = abjad.Scheme("format-mark-box-alphabet")
    abjad.setting(score).markFormatter = scheme

    change_clef(voice_one)

    # numbered leaves
    selection = abjad.select(voice_one).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i, direction=abjad.Up), leaf)  ###################################### numerate leaves
        pass
    abjad.Accidental.respell_with_sharps(selection[22:28])
    abjad.Accidental.respell_with_flats(selection[28:32])

    del selection[70].note_heads[0]
    selection[70].note_heads.extend([0])
    abjad.mutate(selection[71]).transpose(+12)

    del selection[73].note_heads[-1]

    # ritardando mark
    rit_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "ritardando"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_rit = abjad.LilyPondLiteral(r"\startTextSpan")
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")

    abjad.attach(rit_text_span, selection[40])
    abjad.attach(start_rit, selection[40])
    abjad.attach(stop_accel_text_span, selection[44])
    abjad.attach(rit_text_span, selection[72])
    abjad.attach(start_rit, selection[72])
    abjad.attach(stop_accel_text_span, selection[75])

    abjad.override(voice_one).tuplet_bracket.direction = abjad.Up
    
    # tempos 
    lento = abjad.MetronomeMark((1, 8), (64, 72), "Lento")
    quasi_statico = abjad.MetronomeMark((1, 8), (32, 36), "Quasi Statico")
    # metronome mark I
    # abjad.attach(lento, voice_one[0])
    # metronome mark II
    abjad.attach(abjad.MetronomeMark(None, None, "più mosso"), selection[13])
    # metronome mark III
    abjad.attach(lento, selection[45])
    abjad.attach(quasi_statico, selection[76])

    del voice_one[-4:]
    abjad.attach(abjad.Tie(), selection[89])
    voice_one.append('<gs, a, b,>2.')
    voice_one.append('r2.')
    abjad.attach(abjad.Fermata(), voice_one[-1])

    return voice_one


def post_process_voice_four(voice_four, score):
    print("post processing voice four")
    respell(voice_four)
    custom_ties(voice_four)
    change_clef(voice_four)
    # numbered leaves
    selection = abjad.select(voice_four).leaves()
    for i, leaf in enumerate(selection):
        # abjad.attach(abjad.Markup(i), leaf)  ###################################### numerate leaves
        pass
    abjad.mutate(selection[63:66]).transpose(-12)
    del selection[66].note_heads[-1]
    selection[66].note_heads.extend([-13])
    
    abjad.mutate(selection[67]).transpose(-12)
    del selection[68].note_heads[-1]
    selection[68].note_heads.extend([-13])
    del voice_four[-4:]
    voice_four.append("<c, ds,>2.")
    voice_four.append('r2.')
    abjad.attach(abjad.Fermata(), voice_four[-1])
    place = abjad.Markup("Pelotas - RS.", direction=abjad.Down,)
    date = abjad.Markup("May - December 2020.")
    markup = abjad.Markup.right_column([place, date], direction=abjad.Down,)
    markup = markup.italic()
    markup = score.add_final_markup(markup, extra_offset=(14.5, -2),)
    bar_line = score.add_final_bar_line()

    return voice_four


def post_process_electronics(electronics, score):
    # CHORD ZERO ELECTRONICS
    
    # ELECTRONICS
    for pitch in pitches.electronics_pitches:
        electronics.append(abjad.Note.from_pitch_and_duration(pitch, (1, 32)))
    elec_literal = r"r32*6"

    electronics.extend(elec_literal)
    abjad.attach(abjad.LilyPondLiteral(
        r'\hide Stem'
        # r' \override MusicBoxer.fill-color = 
        r' \musicBoxerStart'
        r' \set fontSize = -3'
        r' \override Staff.StaffSymbol.staff-space = #(magstep -3)'
        r' \override Staff.StaffSymbol.thickness = #(magstep -3)'
        r' \override Staff.Clef.font-size = -3'
        r' \override Staff.TimeSignature.font-size = -3'),
        electronics[0])
    abjad.attach(abjad.LilyPondLiteral(
        r'\stopStaff'
        r' \hide Staff.BarLine'
        r' \hide Staff.Clef'
        r' \hide Staff.TimeSignature'),
        electronics[41])
    abjad.attach(abjad.LilyPondLiteral(
        r'\musicBoxerEnd'),
        electronics[41])

    # abjad.attach(abjad.Markup("  ", direction=abjad.Up), electronics[43])

    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.pitch.PitchRange("[F6, +inf]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.pitch.PitchRange("[E4, E5]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.pitch.PitchRange("[E2, A3]")
    clef0 = abjad.Clef("bass_8")
    clef0_range = abjad.pitch.PitchRange("[-inf, D#2]")
    
    selection = abjad.select(electronics).leaves()
    # selection = selection[0::3]
    for i, leaf in enumerate(selection):
        test3 = leaf in clef3_range
        test2 = leaf in clef2_range
        test1 = leaf in clef1_range
        test0 = leaf in clef0_range
        test_note = not isinstance(leaf, abjad.Rest)
        if test_note is True and test2 is True:
            abjad.attach(clef2, selection[i])
        elif test_note is True and test3 is True:
            abjad.attach(clef3, selection[i])
        elif test_note is True and test1 is True:
            abjad.attach(clef1, selection[i])
        elif test_note is True and test0 is True:
            abjad.attach(clef0, selection[i])
            
    del score[1]
    return electronics


