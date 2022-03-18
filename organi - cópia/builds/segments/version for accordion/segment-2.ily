 \version "2.23"
 \language "english"

 \context Score = "Score"
        \with
        {
            markFormatter = #format-mark-box-alphabet
        }
        <<
            \context StaffGroup = "Piano_Staff"
            \with
            {   
            systemStartDelimiter = #'SystemStartBrace
            midiInstrument = #"Flute"
            }
            <<
                \context StaffGroup = "RH"  \with 
                {
                systemStartDelimiter = #'SystemStartSquare
                }
                <<
                \set StaffGroup.instrumentName = \markup{R.H.}

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
                    \clef "treble^8"
                    g'''4.
                    ~
                    <fs''' g'''>4
                    ~
                    <f''' fs''' g'''>8
                    ~
                    <f''' fs'''>4.
                    ~
                    f'''4
                    {
                        r8
                    }
                    {
                        \tempo Lento
                        r4.
                    }
                    d'''4.
                    ~
                    <cs''' d'''>4
                    ~
                    <b'' cs''' d'''>8
                    ~
                    <b'' cs'''>4.
                    ~
                    b''4
                    {
                        r2
                    }
                    \tempo "Quasi Statico"
                    af''4.
                    ~
                    <g'' af''>4
                    ~
                    <e'' g'' af''>8
                    ~
                    <e'' g''>8
                    
                    {
                      r4
                      r4.
                    }
                    {
                        r4.
                    }
                    \clef "treble"
                    c''4.
                    ~
                    \tempo Lento
                    c''4.
                    r4.
                    R2.
                    % \discant "110"
                     % \once \override Staff.TextScript.outside-staff-priority = #1100 \once \override Staff.TextScript.padding = #4
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
            \context Staff = "RH_Staff_2"
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
                \context Voice = "RH_Voice_Four"
                {
                    r2.
                    r4
                    \clef "treble^8"
                    fs''''2
                    r2.
                    r8
                    \clef "treble^8"
                    bf'''4
                    ~
                    bf'''4
                    (
                    \change Staff = "LH_Staff"
                    \clef "bass"
                    e8
                    \change Staff = "RH_Staff_2"
                    \clef "treble^8"
                    gs'''2
                    )
                    r4
                    r4.
                    \change Staff = "LH_Staff"
                    \clef "bass"
                    b4.
                    ~
                    \clef "bass"
                    b8 _ 
                    [
                    
                    \change Staff = "RH_Staff_2"
                    \clef "treble^8"
                    cs''''8 (
                    ]
                    c'''8
                    ~
                    <e'' c'''>4. 
                    \change Staff = "LH_Staff"
                    \clef "bass"
                    b8
                    
                    )
                    \change Staff = "RH_Staff_2"
                    r4
                    r4.
                    \clef "treble^8"
                    a'''2 (
                    \change Staff = "LH_Staff"
                    
                    \clef "bass"
                    ds8
                    [
                    \change Staff = "RH_Staff_2"
                    \clef "treble^8"
                    gs'''8
                    ~
                    ]
                    gs'''4.
                    )
                    r4.
                    \change Staff = RH_Staff
                    r4
                    \tempo "meno mosso"
                    \clef "treble"
                    g''2
                    _ (
                    \clef "treble^8"
                    f''''8
                    
                    \change Staff = LH_Staff
                    \clef "bass"
                    af4)
                    ~
                    \clef "bass"
                    af4.
                    \fermata
                }
                \context Voice = "RH_Voice_Five"
                {
                }
            >>
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
                \context Voice = "LH_Voice_Four" {
                  s2.*7
                  
                R2.
                g'4
                ~
                <fs' g'>8
                ~
                <fs' g'>4.
                ~
                fs'4

                
                    
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
          >>
