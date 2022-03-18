import abjad


class ScoreTemplate(abjad.ScoreTemplate):
    """
    Score template.
    """

    def __call__(self) -> abjad.Score:
        """
        Calls score template.
        """
        # GLOBAL CONTEXT
        global_context = abjad.Voice(name="Global_Context")
        global_context_ii = abjad.Voice(name="Global_Context_II")
        global_context_iii = abjad.Voice(name="Global_Context_III")


        # RH STAFF
        rh_voice_one = abjad.Voice(name="RH_Voice_One")
        # command = abjad.LilyPondLiteral(r"\voiceOne")
        # abjad.attach(command, rh_voice_one)
        # abjad.override(rh_voice_one).stem.direction = abjad.Up
        # abjad.override(rh_voice_one).tie.direction = abjad.Up
        rh_voice_two = abjad.Voice(name="RH_Voice_Two")
        # command = abjad.LilyPondLiteral(r"\voiceTwo")
        # abjad.attach(command, rh_voice_two)
        # abjad.override(rh_voice_two).stem.direction = abjad.Down
        # abjad.override(rh_voice_two).tie.direction = abjad.Down
        rh_voice_three = abjad.Voice(name="RH_Voice_Three")
        # command = abjad.LilyPondLiteral(r"\voiceThree")
        # abjad.attach(command, rh_voice_three)
        # abjad.override(rh_voice_three).stem.direction = abjad.Down
        # abjad.override(rh_voice_three).tie.direction = abjad.Down
        rh_staff = abjad.Staff(
            [global_context,
                rh_voice_one,
                rh_voice_two,
                rh_voice_three],
            name="RH_Staff"
            )
        rh_staff.simultaneous = True

        # LH STAFF
        lh_voice_one = abjad.Voice(name="LH_Voice_Four")
        lh_voice_two = abjad.Voice(name="LH_Voice_Five")
        lh_staff = abjad.Staff([global_context_ii, lh_voice_one, lh_voice_two], name="LH_Staff")
        lh_staff.simultaneous = True

        # ORGAN STAFF
        piano_group = abjad.StaffGroup(
            [rh_staff, lh_staff],
            lilypond_type="PianoStaff",
            name="Piano_Staff",
        )
        abjad.annotate(piano_group, "default_instrument", abjad.Piano())
        instrumentName_piano = abjad.LilyPondLiteral(
             r"\set PianoStaff.instrumentName = \markup{Organ}")
        abjad.attach(instrumentName_piano, piano_group)

        # ELECTRONICS
        # ELECTRONICS RH STAFF
        voice_one_elec = abjad.Voice(name="RH_Voice_One_Electronics")
        electronics = abjad.Staff([global_context_iii, voice_one_elec], name="Electronics_Staff")
        electronics.simultaneous = True

        abjad.annotate(electronics, "default_instrument", abjad.Piano())
        instrumentName_electronics = abjad.LilyPondLiteral(
             r"\set Staff.instrumentName = \markup{Electronics}")
        abjad.attach(instrumentName_electronics, electronics)

        # SCORE
        score = abjad.Score(
            [piano_group, electronics],
            name="Score",
            )
        # abjad.override(score).script.padding = 1.1
        # abjad.override(score).spacing_spanner.strict_grace_spacing = True
        # abjad.override(score).spacing_spanner.strict_note_spacing = True
        # abjad.override(score).spacing_spanner.uniform_stretching = True
        # abjad.override(score).stem.length = 8
        # abjad.override(score).text_script.outside_staff_padding = 1
        # abjad.override(score).tuplet_bracket.bracket_visibility = True
        # abjad.override(score).tuplet_bracket.minimum_length = 3
        # abjad.override(score).tuplet_bracket.outside_staff_padding = 1.5
        # abjad.override(score).tuplet_bracket.padding = 1.5
        # abjad.override(score).tuplet_bracket.springs_and_rods = \
        #     abjad.scheme.Scheme('ly:spanner::set-spacing-rods', verbatim=True)
        # abjad.override(score).tuplet_bracket.staff_padding = 2.25
        # abjad.override(score).tuplet_number.text = \
        #     abjad.scheme.Scheme(
        #         'tuplet-number::calc-fraction-text', verbatim=True)
        # abjad.setting(score).proportional_notation_duration = \
        #     abjad.scheme.SchemeMoment((1, 24))
        # abjad.setting(score).tuplet_full_length = True

        return score
