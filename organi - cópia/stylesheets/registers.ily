
registerI = \markup { \scale #'(0.4 . 0.4)
  \column{

    \line{
  \draw-circle #1.1 #0.3 ##f
  \draw-circle #1.1 #0.3 ##f
    }
   \line{
  \draw-circle #1.1 #0.3 ##t
  \draw-circle #1.1 #0.3 ##t
    }
   \line{
  \draw-circle #1.1 #0.3 ##f
  \draw-circle #1.1 #0.3 ##f
    }
   \line{
  \draw-circle #1.1 #0.3 ##f
  \draw-circle #1.1 #0.3 ##f
    }
  }
}

registerII = \markup { \scale #'(0.4 . 0.4)
  \column{

    \line{
  \draw-circle #1.1 #0.3 ##t
  \draw-circle #1.1 #0.3 ##f
    }
   \line{
  \draw-circle #1.1 #0.3 ##t
  \draw-circle #1.1 #0.3 ##t
    }
   \line{
  \draw-circle #1.1 #0.3 ##f
  \draw-circle #1.1 #0.3 ##f
    }
   \line{
  \draw-circle #1.1 #0.3 ##f
  \draw-circle #1.1 #0.3 ##f
    }
  }
}
