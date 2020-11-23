\version "2.21.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\include "../../stylesheets/stylesheet.ily" %! abjad.LilyPondFile._get_formatted_includes()

\header { %! abjad.LilyPondFile._get_formatted_blocks()
    tagline = ##f
} %! abjad.LilyPondFile._get_formatted_blocks()

\layout {}

\paper {}

\score { %! abjad.LilyPondFile._get_formatted_blocks()
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
                }
                \context Voice = "RH_Voice_One"
                {
                    r1
                    \verylongfermata
                }
                \context Voice = "RH_Voice_Two"
                {
                    \voiceTwo
                }
                \context Voice = "RH_Voice_Three"
                {
                    \voiceThree
                }
            >>
            \context Staff = "LH_Staff"
            <<
                \context Voice = "LH_Voice_Four"
                {
                    r1
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
        \context Staff = "Electronics_Staff"
        {
            \set Staff.instrumentName = \markup{Electronics}
            \tempo Statico
            <cqs' f' gs' c'' e'' ftqs'' gqs'' gs'' b'' cs''' ctqs''' f''' fs''' ftqs''' gs'''>1
            \verylongfermata
            \laissezVibrer
        }
    >>
} %! abjad.LilyPondFile._get_formatted_blocks()