import abjad


# self.score_template = organi.ScoreTemplate()
def post_process_voice_one(voice_one, score):
    # delete something
    del voice_one[-5:]
    #
    # # change last note duration
    # voice_one[-3].written_duration = (1, 2)
    # voice_one[-1].written_duration = (3, 4)
    # abjad.mutate(voice_one[-2:-1]).split([(1, 4)], cyclic=True)
    # voice_one.append("g4")
    # abjad.attach(abjad.Tie(), voice_one[-2])
    insert_chord = abjad.Chord("g' c'' e''", (3, 4))
    voice_one.insert(-2, insert_chord)
    

    voice_one[-1].written_duration = (3, 8)
    # voice_one.append(final_chord)
    abjad.attach(abjad.Tie(), voice_one[-3])

    # registers
    abjad.attach(abjad.LilyPondLiteral(r"\override TextScript.outside-staff-priority = #'1100"), voice_one[0])
    register_one = abjad.Markup(
        r"""\scale #'(0.5 . 0.5)
          \column{

            \line{
          \draw-circle #1.1 #0.3 ##f
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
    abjad.attach(register_one, voice_one[0])

    # metronome mark I
    abjad.attach(
        abjad.MetronomeMark(None, None, "Statico"), voice_one[0])
    # metronome mark II
    abjad.attach(
        abjad.MetronomeMark((1, 8), (32, 36), "Quasi Statico"), voice_one[1])
    # text script (timbres) priority
    # priority = abjad.LilyPondLiteral(
    #     r"\once \override Staff.TextScript.outside-staff-priority = #1100" +
    #     " " + r"\once \override Staff.TextScript.padding = #12")
    # abjad.attach(priority, voice_one[0])


    # markup = abjad.Markup(r"Rohrflöte 4'")
    # markup = markup.box()
    # markup = markup.override(("box-padding", 0.5))
    # abjad.tweak(markup).padding = 20
    # mark = abjad.RehearsalMark(markup=markup)
    # abjad.attach(mark, voice_one[0])

    # accelerando mark
    accel_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "accelerando poco a poco"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_accel = abjad.LilyPondLiteral(r"\startTextSpan")
    abjad.attach(accel_text_span, voice_one[4])
    abjad.attach(start_accel, voice_one[4])
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
    abjad.attach(stop_accel_text_span, voice_one[9])

    # metronome mark III
    abjad.attach(
        abjad.MetronomeMark((1, 8), (64, 72), "Lento"), voice_one[10])

    # ritardando mark
    rit_text_span = abjad.LilyPondLiteral(
        r'\once \override TextSpanner.bound-details.left.text = "ritardando poco a poco"' + " " +
        r"\once \override TextSpanner.style = #'dashed-line"
        )
    start_rit = abjad.LilyPondLiteral(r"\startTextSpan")
    abjad.attach(rit_text_span, voice_one[14])
    abjad.attach(start_rit, voice_one[14])
    stop_accel_text_span = abjad.StopTextSpan(command=r"\stopTextSpan")
    abjad.attach(stop_accel_text_span, voice_one[-3])

    # metronome mark IV
    abjad.attach(
        abjad.MetronomeMark((1, 8), (32, 36), "Quasi Statico"), voice_one[-2])


    # fermata
    abjad.attach(abjad.Fermata(), voice_one[-1])

    # REGISTER TRANSPOSITION
    abjad.mutate(voice_one).transpose(-12)
    return voice_one


def post_process_voice_four(voice_four, score):
    # print(score['LH_Voice_Four'][-3:])
    del voice_four[-6:]
    voice_four[-2] = abjad.Chord("cs' fs'", (1, 4))
    voice_four[-1] = abjad.Chord("cs' fs'", (3, 4))
    abjad.attach(abjad.Tie(), voice_four[-3])
    abjad.attach(abjad.Tie(), voice_four[-2])
    abjad.attach(abjad.Tie(), voice_four[-1])
    voice_four.extend("<cs'~ fs'>8 cs'4 ~ cs'4.")



    # voice_four[-5].written_duration = (1, 2)
    # del voice_four[-5].note_heads[0]
    # del voice_four[-4].note_heads[0]
    # del voice_four[-3].note_heads[0]
    # del voice_four[-2].note_heads[0]
    # voice_four[-3].written_duration = (1, 8)
    # voice_four[-2].written_duration = (2, 4)
    # del voice_four[-1]
    # voice_four[-2].written_duration = (1, 4)
    # voice_four[-1].written_duration = (3, 8)

    clef_bass = abjad.Clef("bass")
    abjad.attach(clef_bass, voice_four[19])
    # final_chord = abjad.Chord("c e", (3, 4))
    # final_chord.written_pitches = voice_four[-1].written_pitches
    # voice_four.append(final_chord)
    # abjad.attach(abjad.Fermata(), voice_four[-1])

    # REGISTER TRANSPOSITION
    abjad.mutate(voice_four).transpose(-12)
    return voice_four


def post_process_electronics(electronics):
    # CHORD ZERO ELECTRONICS
    chord_zero_electronics = ("cqs'32 f' gs' c'' e'' ftqs'' gqs'' gs'' b''"
                              "cs''' ctqs''' f''' fs''' ftqs''' gs''' s32 s2")

    # laisses vibrer
    # laissez_vibrer = abjad.LaissezVibrer()
    # abjad.attach(laissez_vibrer, chord_zero_electronics)

    # fermata
    # abjad.attach(abjad.Fermata("verylongfermata"), chord_zero_electronics)

    # ELECTRONICS
    elec_literal = r"s2.*6 s4 s4 s4 s4 s4 s4"

    # overrides
    # abjad.override(electronics).laissez_vibrer_tie.head_direction = 1
    # electronics.append(abjad.Chord(chord_zero_electronics))
    electronics.extend(chord_zero_electronics)
    electronics.extend(elec_literal)
    # markup = abjad.Markup(r"initial chord")
    # abjad.attach(markup, electronics[0])
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
        electronics[15])
    abjad.attach(abjad.LilyPondLiteral(
        r'\musicBoxerEnd'),
        electronics[15])
    # electronics.append(abjad.Chord(chord_zero_electronics))
    # laissez_vibrer = abjad.LaissezVibrer()
    # abjad.attach(laissez_vibrer, electronics[-1])

    # abjad.attach(abjad.Tie(), electronics[-1])
    # abjad.attach(abjad.StartHairpin(">"), electronics[-5])
    # another_chord = abjad.Chord(chord_zero_electronics)
    # another_chord.written_duration = (3, 4)
    # electronics.append(another_chord)
    # abjad.attach(abjad.StartHairpin("<"), electronics[-3])
    # laisses vibrer
    # laissez_vibrer = abjad.LaissezVibrer()
    # abjad.attach(laissez_vibrer, electronics[-1])

    # electronics.extend(r's2.')
    # abjad.attach(abjad.StopHairpin(), electronics[-1])

    # abjad.glissando(
    #     electronics[15:],
    #     left_broken=True,
    #     right_broken=True,
    #     hide_middle_note_heads=True,)

    return electronics
