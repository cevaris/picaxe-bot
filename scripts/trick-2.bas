main: 
  let b2 = 0
  let b3 = 0
  do
    high B.4    ; start B motor
    pause 600   ; keep turning B motor
    low B.4     ; stop B motor
    forward A   ; start A motor
    forward B   ; start B motor
    pause 1000  ; keep robot straight
    halt A      ; stop A motor
    halt B      ; stop B motor
    inc b2
    inc b3
    calibfreq b3
  loop while b2 < 4