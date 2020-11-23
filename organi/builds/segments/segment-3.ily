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
                }
                \context Voice = "RH_Voice_One"
                {
                    \tempo Lento
                    \mark #3
                    c''4
                    ~
                    <g' c''>8
                    ~
                    <fs' g' c''>4.
                    ~
                    <fs' g'>4
                    ~
                    fs'8
                    {
                        r4.
                    }
                    {
                        \change Staff = LH_Staff
                        r4.
                        r4
                    }
                    cs'8
                    ~
                    \tempo "Quasi Statico"
                    \clef "bass"
                    cs'8
                    ~
                    <b cs'>8
                    ~
                    <ds b cs'>8
                    ~
                    <ds b cs'>4
                    ~
                    <ds b>8
                    ~
                    <ds b>8
                    ~
                    ds8
                    {
                        \tempo Lento
                        r2
                    }
                    {
                        r2
                    }
                    cs4
                    ~
                    \tempo "subito Quasi Statico"
                    <c cs>8
                    ~
                    <b, c cs>4
                    ~
                    <b, c cs>8
                    ~
                    <b, c>4
                    ~
                    \tempo Lento
                    b,8
                    {
                        r4
                        r4.
                    }
                    {
                        r4.
                    }
                    \tempo "più mosso"
                    a,4
                    ~
                    <gs, a,>8
                    ~
                    <e, gs, a,>4.
                    ~
                    <e, gs,>4
                    ~
                    e,8
                    s2.
                    s2.
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
                }
                \context Voice = "LH_Voice_Four"
                {
                    r4.
                    r4
                    \clef "bass"
                    ef8
                    ~
                    \clef "bass"
                    ef4.
                    r4.
                    \change Staff = RH_Staff
                    r8
                    \clef "treble"
                    f''4
                    ~
                    (
                    \clef "treble"
                    f''4
                    \clef "bass"
                    af,8
                    \clef "treble"
                    d''2
                    )
                    r4
                    r4
                    \clef "bass"
                    a,2
                    (
                    \clef "treble"
                    \once \override TextSpanner.bound-details.left.text = "accelerando" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    fs'8
                    \clef "bass"
                    c,4
                    ~
                    \clef "bass"
                    c,4
                    \clef "treble"
                    ef'8
                    )
                    \stopTextSpan
                    r4.
                    \clef "treble"
                    g'''4.
                    ~
                    (
                    \clef "treble"
                    g'''8
                    [
                    \clef "bass"
                    cs8
                    ]
                    \clef "treble"
                    fs'''2
                    )
                    r4.
                    \clef "bass"
                    e,4.
                    ~
                    (
                    \clef "bass"
                    e,8
                    [
                    \clef "treble"
                    ef'''8
                    ]
                    \clef "bass"
                    b2
                    \clef "treble"
                    cs'''8
                    )
                    \change Staff = LH_Staff
                    r4
                    \tempo "Quasi Statico"
                    \clef "bass"
                    b,4.
                    ~
                    (
                    \clef "bass"
                    b,8
                    [
                    \change Staff = RH_Staff
                    \clef "treble"
                    a''8
                    )
                    ]
                    \change Staff = LH_Staff
                    \clef "bass"
                    ef2
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
        \context Staff = "Electronics_Staff"
        <<
            \set Staff.instrumentName = \markup{Electronics}
            \context Voice = "Global_Context_III"
            {
            }
            \context Voice = "RH_Voice_One_Electronics"
            {
            }
        >>
    >>