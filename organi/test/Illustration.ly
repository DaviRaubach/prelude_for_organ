\version "2.21.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\include "../../stylesheets/segment_i_stylesheet.ily" %! abjad.LilyPondFile._get_formatted_includes()

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
                    \time 6/8 %! scaling time signatures
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
                    \tempo Estatic 4=22-45
                    af'''4.
                    ^ \markup { "Open Flutes 8'" }
                    ~
                    <g''' af'''>4
                    ~
                    <fs''' g''' af'''>8
                    ~
                    \override TextSpanner.bound-details.left.text = 'accelerando poco a poco'\override TextSpanner.style = #'dashed-line\startTextSpan
                    <fs''' g'''>4.
                    ~
                    fs'''4
                    f'''8
                    ~
                    f'''4
                    ~
                    <d''' f'''>8
                    ~
                    <d''' f'''>8
                    \stopTextSpan
                    <cs''' d''' f'''>8
                    ~
                    <cs''' d'''>8
                    ~
                    <cs''' d'''>4
                    ~
                    cs'''8
                    ~
                    cs'''8
                    b''4
                    ~
                    b''8
                    ~
                    <af'' b''>4
                    ~
                    <g'' af'' b''>8
                    ~
                    <g'' af''>4
                    ~
                    <g'' af''>8
                    ~
                    g''4
                    e''4.
                    ~
                    <c'' e''>4
                    ~
                    <g' c'' e''>2
                    \fermata
                    ~
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
                    r2
                    f'''4
                    ~
                    f'''8
                    ~
                    <d''' f'''>8
                    ~
                    <cs''' d''' f'''>8
                    ~
                    <cs''' d''' f'''>8
                    <cs''' d'''>4
                    ~
                    <cs''' d'''>8
                    ~
                    cs'''8
                    b''8
                    ~
                    b''4
                    <af'' b''>8
                    ~
                    <g'' af'' b''>4
                    ~
                    <g'' af''>8
                    ~
                    <g'' af''>4
                    g''8
                    e''4.
                    ~
                    <c'' e''>8
                    ~
                    <g' c'' e''>4
                    ~
                    <g' c''>4.
                    ~
                    g'8
                    fs'4
                    ~
                    fs'8
                    ~
                    <cs' fs'>8
                    ~
                    <gs cs' fs'>8
                    ~
                    <gs cs' fs'>2
                    \fermata
                }
                \context Voice = "LH_Voice_Five"
                {
                }
            >>
        >>
        \context Staff = "Electronics_Staff"
        {
            \set Staff.instrumentName = \markup{Electronics}
        }
    >>
    \layout {}
    \midi {}
} %! abjad.LilyPondFile._get_formatted_blocks()