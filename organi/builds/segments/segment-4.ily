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
                }
                \context Voice = "RH_Voice_One"
                {
                }
                \context Voice = "RH_Voice_Two"
                {
                    \tempo Lento 8=64-72
                    \mark #4
                    \clef "treble"
                    \override TextScript.outside-staff-priority = #'1100
                    r4.
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
                                }
                        }
                    r4
                    cs'''8
                    ~
                    cs'''4.
                    r4.
                    r8
                    bf'4
                    ~
                    (
                    bf'4
                    d''8
                    )
                    r2
                    c'''4
                    ~
                    c'''4
                    r8
                    r4
                    ef'8
                    ~
                    ef'4.

                            \shape #'((0 . 0) (0 . 0) (-1.5 . -3) (0 . -8)) Slur

                    fs'''8
                    (
                    r4
                    )
                    r8
                    fs'4
                    ~
                    fs'4
                    r8
                    r8
                    g''4
                    ~
                    (
                    g''4
                    f'''8
                    )
                    \once \override TextSpanner.bound-details.left.text = "accelerando poco a poco" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    bf'2
                    (
                    d''8
                    )
                    r8
                    r8
                    f''4
                    ~
                    f''4
                    r8
                    r8
                    af''4
                    ~
                    (
                    af''4
                    g'''8
                    fs'2
                    )
                    r4
                    cs'''2
                    (
                    g''8
                    )
                    r8
                    r8
                    d''4
                    ~
                    (
                    d''4
                    a''8
                    )
                    \stopTextSpan
                    {
                        cs'''2
                        (
                        g''8
                        )
                        r8
                        r8
                        fs'''4
                        ~
                        (
                        fs'''4
                        g'''8
                        )
                    }
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
                }
                \context Voice = "LH_Voice_Four"
                {
                    \clef "bass"
                    s2.
                    s4
                    s8
                    s4
                    s8
                    s4.
                    _ (
                    ef8
                    b,4
                    ~
                    b,8
                    )
                    r4
                    r4
                    ef,8
                    - \tenuto
                    r4.
                    a,4.
                    (
                    af,8
                    )
                    r4
                    r8
                    e,8
                    - \tenuto
                    r8
                    r8

                            \shape #'((0 . 0) (1 . 0) (3 . 0) (7 . 0)) Slur

                    ef,8
                    _ (
                    c,8
                    s4.
                    )
                    af,8
                    d4
                    \rest
                    d4.
                    \rest
                    r4
                    cs8
                    _ (
                    ef,4.
                    )
                    c,8
                    - \tenuto
                    r4
                    af,8
                    _ (
                    ef8
                    - \tenuto
                    )
                    r8
                    r8
                    e,4
                    ~
                    (
                    e,8
                    cs8
                    )
                    r8
                    c,8
                    (
                    a,4
                    )
                    ~
                    a,8
                    r8
                    ef8
                    _ (
                    b,8
                    e,4
                    ~
                    e,8
                    cs8
                    )
                    r8
                    c,4.
                    (
                    a,8
                    )
                    r8
                    ds8
                    - \tenuto
                    {
                        b8
                        \clef "treble"
                        ds'4
                        ~
                        ds'8
                        fs'8
                        )
                        r8
                        as'4.
                        (
                        d''8
                        )
                        r8
                        f''8
                    }
                }
                \context Voice = "LH_Voice_Five"
                {
                    r2.
                    b,4
                    ~
                    <a, b,>8
                    ~
                    <gs, a, b,>4.
                    ~
                    <gs, a,>4
                    ~
                    gs,8
                    {
                        s1 * 3/8
                    }
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/8
                    }
                     \voiceTwo
                    e,4
                    ~
                    <ds, e,>8
                    ~
                    <c, ds, e,>4.
                    ~
                    <c, ds,>4
                    ~
                    c,8
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/4
                    }
                    {
                        s1 * 3/4
                    }
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