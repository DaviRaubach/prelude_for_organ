\version "2.20.0"

discant = \markup {
  \musicglyph "accordion.discant"
}
dot = \markup {
  \musicglyph "accordion.dot"
}

% 16 voets register
accBasson = ^\markup {
  \combine
  \discant
  \translate-scaled #'(0 . 0.5) \dot
}

% een korig 8 en 16 voets register
accBandon = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \translate-scaled #'(0 . 1.5) \dot
}

accVCello = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \combine
        \translate-scaled #'(0 . 1.5) \dot
        \translate-scaled #'(1 . 1.5) \dot
}

% 4-8-16 voets register
accHarmon = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \combine
        \translate-scaled #'(0 . 1.5) \dot
        \translate-scaled #'(0 . 2.5) \dot
}

accTrombon = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \combine
        \translate-scaled #'(0 . 1.5) \dot
        \combine
          \translate-scaled #'(1 . 1.5) \dot
          \translate-scaled #'(-1 . 1.5) \dot
}

% eenkorig 4 en 16 voets register
accOrgan = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \translate-scaled #'(0 . 2.5) \dot
}

accMaster = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 0.5) \dot
      \combine
        \translate-scaled #'(0 . 1.5) \dot
        \combine
          \translate-scaled #'(1 . 1.5) \dot
          \combine
            \translate-scaled #'(-1 . 1.5) \dot
            \translate-scaled #'(0 . 2.5) \dot
}

accAccord = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 1.5) \dot
      \combine
        \translate-scaled #'(1 . 1.5) \dot
        \combine
          \translate-scaled #'(-1 . 1.5) \dot
          \translate-scaled #'(0 . 2.5) \dot
}

accMusette = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 1.5) \dot
      \combine
        \translate-scaled #'(1 . 1.5) \dot
        \translate-scaled #'(-1 . 1.5) \dot
}

accCeleste = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 1.5) \dot
      \translate-scaled #'(-1 . 1.5) \dot
}

accOboe = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 1.5) \dot
      \translate-scaled #'(0 . 2.5) \dot
}

accClarin = ^\markup {
  \combine
    \discant
    \translate-scaled #'(0 . 1.5) \dot
}

accPiccolo = ^\markup {
    \combine
       \discant
       \translate-scaled #'(0 . 2.5) \dot
}

accViolin = ^\markup {
  \combine
    \discant
    \combine
      \translate-scaled #'(0 . 1.5) \dot
      \combine
        \translate-scaled #'(1 . 1.5) \dot
        \translate-scaled #'(0 . 2.5) \dot
}