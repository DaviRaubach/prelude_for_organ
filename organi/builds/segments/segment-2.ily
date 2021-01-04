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
                    \tempo "Quasi Statico"
                    \mark #2
                    g''4.
                    ~
                    <fs'' g''>4
                    ~
                    <f'' fs'' g''>8
                    ~
                    <f'' fs''>4.
                    ~
                    f''4
                    {
                        r8
                    }
                    {
                        \tempo Lento
                        r4.
                    }
                    d''4.
                    ~
                    <cs'' d''>4
                    ~
                    <b' cs'' d''>8
                    ~
                    <b' cs''>4.
                    ~
                    b'4
                    {
                        r2
                    }
                    \tempo "Quasi Statico"
                    af'4.
                    ~
                    <g' af'>4
                    ~
                    <e' g' af'>8
                    ~
                    <e' g'>4.
                    ~
                    e'4
                    {
                        r8
                    }
                    {
                        r4.
                    }
                    \clef "bass"
                    c'4.
                    ~
                    \tempo Lento
                    <g c'>4
                    ~
                    <fs g c'>8
                    ~
                    <fs g>4.
                    ~
                    fs4
                    {
                        r2
                    }
                     \once \override Staff.TextScript.outside-staff-priority = #1100 \once \override Staff.TextScript.padding = #4
                    s2.
                    ^ \markup {
                        \scale
                            #'(0.5 . 0.5)
                            \column
                                {
                                    \line
                                        {
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##t
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##f
                                        }
                                    \line
                                        {
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##t
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##t
                                        }
                                    \line
                                        {
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##f
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##f
                                        }
                                    \line
                                        {
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##f
                                            \draw-circle
                                                #1.1
                                                #0.3
                                                ##f
                                        }
                                }
                        }
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
                    r2.
                    r4
                    \clef "treble"
                    fs'''2
                    r2.
                    r8
                    \clef "treble"
                    f'''4
                    ~
                    \clef "treble"
                    f'''4
                    (
                    \clef "bass"
                    e,8
                    \clef "treble"
                    ds'''2
                    )
                    r4
                    r4.
                    \clef "bass"
                    b,4.
                    ~
                    \clef "bass"
                    b,8
                    [
                    (
                    \clef "treble"
                    cs'''8
                    ]
                    \clef "treble"
                    c''2
                    \clef "bass"
                    b,8
                    )
                    r4
                    r4.
                    \clef "treble"
                    a''2
                    _ (
                    \clef "bass"
                    ds,8
                    [
                    \clef "treble"
                    gs''8
                    ~
                    ]
                    \clef "treble"
                    gs''4.
                    )
                    r4.
                    \change Staff = RH_Staff
                    r4
                    \tempo "meno mosso"
                    \clef "treble"
                    g'2
                    _ (
                    \clef "treble"
                    f'''8
                    )
                    \change Staff = LH_Staff
                    \clef "bass"
                    af,4
                    ~
                    \clef "bass"
                    af,4.
                    \fermata
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
    >>