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
                    \time 4/4 %! scaling time signatures
                    s1 * 1
                    \time 6/8 %! scaling time signatures
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
                    \tempo Statico
                    \override TextScript.outside-staff-priority = #'1100
                    r1
                    \verylongfermata
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
                    \tempo "Quasi Statico" 8=32-36
                    af''4.
                    ~
                    <g'' af''>4
                    ~
                    <fs'' g'' af''>8
                    ~
                    \once \override TextSpanner.bound-details.left.text = "accelerando poco a poco" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    <fs'' g''>4.
                    ~
                    fs''4
                    f''8
                    ~
                    <d'' f''>4.
                    ~
                    <cs'' d'' f''>4
                    ~
                    <cs'' d''>8
                    \stopTextSpan
                    ~
                    \tempo Lento 8=64-72
                    cs''4.
                    b'4
                    ~
                    <af' b'>8
                    ~
                    <g' af' b'>4.
                    ~
                    \once \override TextSpanner.bound-details.left.text = "ritardando poco a poco" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    <g' af'>4
                    ~
                    g'8
                    e'4.
                    ~
                    <c' e'>4
                    ~
                    <g c' e'>8
                    ~
                    <g c' e'>2.
                    \stopTextSpan
                    ~
                    \tempo "Quasi Statico" 8=32-36
                    <g c'>4.
                    ~
                    g4.
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
                    s1 * 1
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
                    r1
                    r2
                    d''4
                    ~
                    d''8
                    ~
                    <cs'' d''>8
                    ~
                    <b' cs'' d''>8
                    ~
                    <b' cs'' d''>8
                    ~
                    <b' cs''>4
                    ~
                    <b' cs''>8
                    ~
                    b'8
                    af'8
                    ~
                    af'8
                    ~
                    <g' af'>4
                    ~
                    <g' af'>8
                    ~
                    <e' g' af'>8
                    ~
                    <e' g'>8
                    ~
                    <e' g'>8
                    ~
                    e'4
                    ~
                    e'8
                    \clef "bass"
                    c'8
                    ~
                    <g c'>8
                    ~
                    <g c'>8
                    ~
                    <fs g c'>4
                    ~
                    <fs g c'>8
                    ~
                    <fs g>8
                    ~
                    fs8
                    ~
                    fs8
                    ~
                    <cs fs>4
                    ~
                    <cs fs>2.
                    ~
                    <cs fs>8
                    ~
                    cs4
                    ~
                    cs4.
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