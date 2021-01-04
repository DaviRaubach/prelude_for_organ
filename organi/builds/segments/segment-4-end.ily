    \context Score = "Score"
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
                }
                \context Voice = "RH_Voice_One"
                {
                    s2.
                    s2.
                    s2.
                    s2
                     \voiceOne
                    s8
                    g'''8
                    ~
                }
                \context Voice = "RH_Voice_Two"
                {
                     \voiceOne
                    \once \override TextSpanner.bound-details.left.text = "accelerando" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    af''2
                    a''4
                    ~
                    a''8
                    c'''8
                    (
                     \voiceTwo
                    cs''8
                    )
                    ~
                    cs''4
                     \voiceOne
                    cs'''8
                     \voiceTwo

                                \shape #'((1 . 0) (0 . 0) (-3 . 0) (-3 . 0)) Slur

                    cs''4.
                    ^ (
                     \voiceOne
                    ef'''8
                    )
                    (
                    f''4
                    )
                    f'''8
                    (
                    fs''4
                    )
                    fs'''8
                    (
                    fs''8
                    \stopTextSpan
                }
                \context Voice = "RH_Voice_Three"
                {
                     \voiceTwo
                    ef''8
                    (
                    gf''4
                    )
                    bf''8
                    (
                    c''4
                    )
                    e''8
                     \tieUp
                    fs''4
                    ~
                     \voiceOne
                    fs''8
                     \tieNeutral
                    g''8
                     \voiceTwo
                     \tieUp
                    gs''8
                    ~
                     \voiceOne
                    gs''4
                     \voiceTwo
                    b''8
                    (
                    e''4
                    )
                    gf''8
                    (
                    bf''4
                    )
                    c''8
                    (
                    e''4
                    )
                    r8
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
                }
                \context Voice = "LH_Voice_Four"
                {
                    f4
                    \clef "treble"
                    c'8
                    ~
                    c'4
                    ef'8
                    ~
                    ef'4.
                    e'8
                    c''4
                    ~
                    c''8
                    bf'8
                    b'8
                    ~
                    b'8
                    c''8
                    ef''8
                    ~
                    ef''8
                    e''8
                    bf''8
                    r4.
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
    >>