    \context Score = "Score"
    \with
    {
        markFormatter = #format-mark-box-alphabet
    }
    <<
        \context PianoStaff = "Piano_Staff"
        \with
        {
            midiInstrument = #"Flute"
        }
        <<
            \set PianoStaff.instrumentName = \markup{Organ}
            \context Staff = "RH_Staff"
            <<
                \context Voice = "Global_Context"
                {
                    \time 6/8 %! scaling time signatures
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                }
                \context Voice = "RH_Voice_One"
                \with
                {
                    \override TupletBracket.direction = #up
                }
                {
                    \tempo "Andante, molto liberamente" 8=128-144
                    \mark #5
                    \clef "treble^8"
                    <g'''>4
                    ~
                    \clef "treble^8"
                    <f''' g'''>8
                    ~
                    \clef "treble^8"
                    <f'''>8
                    ~
                    \clef "treble^8"
                    <f''' gf'''>4
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <ef'''>4
                        ~
                        <ef''' f'''>8
                        ~
                        <ef''' f'''>8
                        ~
                        <cs''' ef'''>4
                        ~
                        <cs''' ef'''>8
                        ~
                    }
                    <ef'''>8
                    ~
                    <c''' ef'''>4
                    ~
                    <c''' df'''>4
                    ~
                    <a'' c'''>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \tempo "più mosso"
                        <a''>8
                        ~
                        <a'' c'''>4
                        ~
                        <gs'' a''>4
                        ~
                        <gs'' a''>8
                        ~
                        <gs'' a''>8
                    }
                    <g''>4
                    ~
                    <g'' af''>8
                    ~
                    <g'' af''>8
                    ~
                    <fs'' g''>4
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <g''>4
                        ~
                        <fs'' g''>8
                        ~
                        <fs''>8
                        ~
                        <fs''>4
                        ~
                        <f'' fs''>8
                        ~
                    }
                    <f''>8
                    ~
                    <f'' gf''>4
                    ~
                    <f''>4
                    ~
                    <f''>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <f''>8
                        ~
                        <d'' f''>4
                        ~
                        <d'' f''>4
                        ~
                        \clef "treble"
                        <cs'' d''>8
                        ~
                        \clef "treble"
                        <cs''>8
                    }
                    \clef "treble"
                    <d''>4
                    ~
                    \clef "treble"
                    <cs'' d''>8
                    ~
                    \clef "treble"
                    <cs''>8
                    ~
                    \clef "treble"
                    <cs''>4
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        \once \override TextSpanner.bound-details.left.text = "ritardando" \once \override TextSpanner.style = #'dashed-line
                        \startTextSpan
                        <b'>4
                        ~
                        \clef "treble"
                        <b' cs''>8
                        ~
                        \clef "treble"
                        <b' cs''>8
                        ~
                        \clef "treble"
                        <as' b'>4
                        ~
                        \clef "treble"
                        <as' b'>8
                        \stopTextSpan
                        ~
                    }
                    \tempo Lento 8=64-72
                    \clef "treble"
                    <b'>8
                    ~
                    \clef "treble"
                    <af' b'>4
                    ~
                    \clef "treble"
                    <af' bf'>4
                    ~
                    \clef "treble"
                    <g' af'>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        <g'>8
                        ~
                        \clef "treble"
                        <g' af'>4
                        ~
                        \clef "treble"
                        <fs' g'>4
                        ~
                        \clef "treble"
                        <fs' g'>8
                        ~
                        \clef "treble"
                        <fs' g'>8
                        ~
                    }
                    \clef "treble"
                    <fs'>4
                    ~
                    \clef "treble"
                    <fs'>8
                    ~
                    \clef "treble"
                    <fs'>8
                    ~
                    \clef "treble"
                    <e' fs'>4
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        <fs'>4
                        ~
                        <ds' fs'>8
                        ~
                        <ds'>8
                        ~
                        <ds' e'>4
                        ~
                        <c' ds'>8
                        ~
                    }
                    <c'>8
                    ~
                    <c' ef'>4
                    ~
                    <af c'>4
                    ~
                    <af c'>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <c'>8
                        ~
                        <f c'>4
                        ~
                        \clef "bass"
                        <f af>4
                        ~
                        \clef "bass"
                        <f c'>8
                        ~
                        \clef "bass"
                        <c'>8
                    }
                    \clef "bass"
                    \once \override TextSpanner.bound-details.left.text = "ritardando" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    <f>4
                    ~
                    <b>8
                    ~
                    <b>8
                    ~
                    <b c'>4
                    \stopTextSpan
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \tempo "Quasi Statico" 8=32-36
                        \clef "bass"
                        <ef>4
                        ~
                        <ef b>8
                        ~
                        <ef b>8
                        ~
                        \clef "bass"
                        <cs ef>4
                        ~
                        \clef "bass"
                        <cs ef>8
                        ~
                    }
                    \clef "bass"
                    <ef>8
                    ~
                    \clef "bass"
                    <cs ef>4
                    ~
                    \clef "bass"
                    <cs>4
                    ~
                    \clef "bass"
                    <b, cs>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "bass"
                        <b,>8
                        ~
                        \clef "bass"
                        <b, cs>4
                        ~
                        \clef "bass"
                        <a, b,>4
                        ~
                        \clef "bass"
                        <a, b,>8
                        ~
                        \clef "bass"
                        <a, b,>8
                        ~
                    }
                    <gs, a, b,>2.
                    r2.
                    \fermata
                }
                \context Voice = "RH_Voice_Two"
                {
                }
                \context Voice = "RH_Voice_Three"
                {
                }
            >>
            \context Staff = "LH_Staff"
            <<
                \context Voice = "Global_Context_II"
                {
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                    s1 * 3/4
                }
                \context Voice = "LH_Voice_Four"
                {
                    r8
                    <cs'''>4
                    ~
                    <a'' cs'''>4
                    ~
                    <a'' c'''>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <c'''>8
                        ~
                        <af'' c'''>4
                        ~
                        <af'' a''>4
                        ~
                        <g'' af''>8
                        ~
                        <g''>8
                    }
                    <af''>4
                    ~
                    <fs'' af''>8
                    ~
                    <fs''>8
                    ~
                    <fs'' g''>4
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <fs''>4
                        ~
                        <fs''>8
                        ~
                        <fs''>8
                        ~
                        <f'' fs''>4
                        ~
                        <f'' fs''>8
                        ~
                    }
                    <fs''>8
                    ~
                    <f'' fs''>4
                    ~
                    <f''>4
                    ~
                    <d'' f''>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        <d''>8
                        ~
                        <d'' f''>4
                        ~
                        \clef "treble"
                        <cs'' d''>4
                        ~
                        \clef "treble"
                        <cs'' d''>8
                        ~
                        \clef "treble"
                        <cs'' d''>8
                        ~
                    }
                    \clef "treble"
                    <cs''>4
                    ~
                    \clef "treble"
                    <cs''>8
                    ~
                    \clef "treble"
                    <cs''>8
                    ~
                    \clef "treble"
                    <b' cs''>4
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        <cs''>4
                        ~
                        \clef "treble"
                        <bf' cs''>8
                        ~
                        \clef "treble"
                        <bf'>8
                        ~
                        \clef "treble"
                        <bf' b'>4
                        ~
                        \clef "treble"
                        <af' bf'>8
                        ~
                    }
                    \clef "treble"
                    <af'>8
                    ~
                    \clef "treble"
                    <af' bf'>4
                    ~
                    \clef "treble"
                    <g' af'>4
                    ~
                    \clef "treble"
                    <g' af'>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "treble"
                        <af'>8
                        ~
                        \clef "treble"
                        <fs' af'>4
                        ~
                        \clef "treble"
                        <fs' g'>4
                        ~
                        \clef "treble"
                        <fs'>8
                        ~
                        \clef "treble"
                        <fs'>8
                        ~
                    }
                    \clef "treble"
                    <fs'>4
                    ~
                    \clef "treble"
                    <e' fs'>8
                    ~
                    \clef "treble"
                    <e'>8
                    ~
                    \clef "treble"
                    <e' fs'>4
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <ef'>4
                        ~
                        <ef' e'>8
                        ~
                        <ef' e'>8
                        ~
                        <c' ef'>4
                        ~
                        <c' ef'>8
                        ~
                    }
                    <ef'>8
                    ~
                    <af ef'>4
                    ~
                    <af c'>4
                    ~
                    \clef "bass"
                    <f af>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "bass"
                        <f>8
                        ~
                        \clef "bass"
                        <f af>4
                        ~
                        \clef "bass"
                        <c f>4
                        ~
                        \clef "bass"
                        <c f>8
                        ~
                        \clef "bass"
                        <c f>8
                    }
                    <b,>4
                    ~
                    <b, c>8
                    ~
                    <b, c>8
                    ~
                    <b, ef>4
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        <b,>4
                        ~
                        <b, cs>8
                        ~
                        \clef "bass"
                        <cs>8
                        ~
                        \clef "bass"
                        <cs ef>4
                        ~
                        \clef "bass"
                        <cs>8
                        ~
                    }
                    \clef "bass"
                    <cs>8
                    ~
                    \clef "bass"
                    <cs>4
                    ~
                    \clef "bass"
                    <b, cs>4
                    ~
                    \clef "bass"
                    <b, cs>8
                    ~
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "bass"
                        <cs>8
                        ~
                        \clef "bass"
                        <a, cs>4
                        ~
                        \clef "bass"
                        <a, b,>4
                        ~
                        \clef "bass"
                        <af, a,>8
                        ~
                        \clef "bass"
                        <af,>8
                    }
                    \clef "bass"
                    <a,>4
                    ~
                    \clef "bass"
                    <e, a,>8
                    ~
                    \clef "bass"
                    <e,>8
                    ~
                    \clef "bass"
                    <e, af,>4
                    \tweak text #tuplet-number::calc-fraction-text
                    \times 6/7 {
                        \clef "bass"
                        <ef,>4
                        ~
                        \clef "bass"
                        <ef, e,>8
                        ~
                        \clef "bass"
                        <ef, e,>8
                        ~
                        \clef "bass"
                        <c, ef,>4
                        ~
                        \clef "bass"
                        <c, ef,>8
                        ~
                    }
                    <c, ds,>2.
                    \once \override TextScript.extra-offset = #'(14.5 . -2)
                    r2.
                    \fermata
                    _ \markup {                            %! SCORE_2
                        \italic                            %! SCORE_2
                            \right-column                  %! SCORE_2
                                {                          %! SCORE_2
                                    "Pelotas - RS."        %! SCORE_2
                                    "May - December 2020." %! SCORE_2
                                }                          %! SCORE_2
                        }                                  %! SCORE_2
                    \bar "|." %! SCORE_1
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
    >>