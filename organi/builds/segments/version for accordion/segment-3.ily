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
            midiInstrument = #"Flute"
        }
        <<
          % \set PianoStaff.instrumentName = \markup{Organ}

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
                    \tempo Lento
                    \mark #3
                    % \clef "treble"
                    c'''4
                    ~
                    <g'' c'''>8
                    ~
                    <fs'' g'' c'''>4.
                    ~
                    <fs'' g''>4
                    ~
                    fs''8
                    {
                      r4.
                    }
                    {
                        \change Staff = LH_Staff
                        r4.
                        r4
                      }
                    \stemUp
                    cs'8
                    ~
                    \stemNeutral
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
                    \stemDown
                    % \tempo "più mosso"
                    a,4
                    ~
                    <gs, a,>8
                    ~
                    <e, gs, a,>4.
                    ~
                    <e, gs,>4
                    ~
                    e,8
                    \stemNeutral
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
             \context Voice = "Global_Context_x"
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
                    % \discant "11"
                    r8
                    % \clef "treble"
                    f'''4
                    ~
                    (
                    % \clef "treble"
                    f'''4
                    \change Staff = LH_Staff
                    \clef "bass"
                    \stemDown
                    gs,8
                    \change Staff = RH_Staff
                    \clef "treble^8"
                    \stemNeutral
                    d'''2
                    )
                    r4
                    r4
                    % \clef "bass"
                    \showStaffSwitch
                    \change Staff = LH_Staff
                    a,2(
                    \hideStaffSwitch
                    
                    \change Staff = RH_Staff
                    \clef "treble"
                    \once \override TextSpanner.bound-details.left.text = "accelerando" \once \override TextSpanner.style = #'dashed-line
                    \startTextSpan
                    fs''8
                    \showStaffSwitch
                    % \clef "bass"
                    \change Staff = LH_Staff
                    \stemDown
                    c,4)
                    ~
                    % \clef "bass"
                    c,4
                    \change Staff = RH_Staff
                    \stemNeutral
                    ef''8
                    
                    \stopTextSpan
                    % \discant "110"
                    r4.
                    \hideStaffSwitch
                    \clef "treble^8"
                    g''''4.
                    ~
                    (
                    g''''8
                    [
                      \change Staff = LH_Staff
                    cs8
                    ]
                    \change Staff = RH_Staff
                    fs''''2
                    )
                    
                    r4.
                    \change Staff = LH_Staff
                    \clef "bass"
                    \stemUp
                    c'4.
                    ~
                    (
                    \tempo "più mosso"                % \clef "bass"
                    c'8
                    [
                    \change Staff = RH_Staff
                    \stemNeutral

                    % \clef "treble"
                    ef''''8
                    ]
                    \showStaffSwitch
                                % \clef "bass"
                    \change Staff = LH_Staff
                    \stemUp
                    b2
                    \change Staff = RH_Staff
                    \clef "treble^8"
                    \stemNeutral
                    cs''''8
                    )
                    \hideStaffSwitch
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
                    a'''8
                    )
                    ]
                    \change Staff = LH_Staff
                    \clef "bass"
                    ds2
                    
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
      >>



