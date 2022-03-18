 \version "2.23"
 \language "english"

 \context Score = "Score"
    <<
        \context StaffGroup = "Piano_Staff"
        \with
        {   systemStartDelimiter = #'SystemStartBrace
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
                    \clef "treble^8"
                    r1 
                    \verylongfermata
                    \tempo "Quasi Statico" 8=32-36
                    \discant "100"
                    af'''4. 
                    ~
                    <g''' af'''>4
                    ~
                    <fs''' g''' af'''>8
                    ~
                    \once \override TextSpanner.bound-details.left.text = "accelerando poco a poco" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    <fs''' g'''>4.
                    ~
                    fs'''4
                    f'''8
                    ~
                    <d''' f'''>4.
                    ~
                    <cs''' d''' f'''>4
                    ~
                    <cs''' d'''>8
                    \stopTextSpan
                    ~
                    \tempo Lento 8=64-72
                    cs'''4.
                    
                    b''4
                    ~
                    <af'' b''>8
                    ~
                    <g'' af'' b''>4.
                    ~
                    \once \override TextSpanner.bound-details.left.text = "ritardando poco a poco" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    
                    <g'' af''>4
                    ~
                    g''8
                    \clef "treble"
                    e''4.
                    ~
                    <c'' e''>4
                    ~
                    <g' c'' e''>8
                    ~
                    <g' c'' e''>2.
                    \stopTextSpan
                    ~
                    \tempo "Quasi Statico" 8=32-36
                    <g' c''>4.
                    ~
                    g'4.
                    \fermata
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
                \context Voice = "RH_Voice_Four"
                {   \clef "treble^8"
                    r1
                    r2
                    d'''4
                    ~
                    d'''8
                    ~
                    <cs''' d'''>8
                    ~
                    <b'' cs''' d'''>8
                    ~
                    <b'' cs''' d'''>8
                    ~
                    <b'' cs'''>4
                    ~
                    <b'' cs'''>8
                    ~
                    b''8
                    af''8
                    ~
                    af''8
                    ~
                    <g'' af''>4
                    ~
                    <g'' af''>8
                    ~
                    <e'' g'' af''>8
                    ~
                    <e'' g''>8
                    ~
                    <e'' g''>8
                    ~
                    e''4
                    ~
                    e''8
                    \clef "treble"
                    c''8
                    ~
                    2
                    ~
                    8
                    r4 r4.
                    r2. r2.
                    
                }
                \context Voice = "RH_Voice_Five"
                {
                }
            >>
            >>
            \context Staff = "LH_Staff"
            
            <<
                \set Staff.instrumentName = \markup{L.H.}

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
                  s1
                  s2. * 4
                  r4 \freeBass "1" g'4 ~ <g' fs'>4 ~ 4 ~ fs'4 ~ <cs' fs'>4 ~ 2. ~ 8 ~ cs'4 ~ 4.
                    
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
        
    >>