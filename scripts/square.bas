main: 
  high B.4    ; start B motor
  pause 700   ; keep turning B motor
  low B.4     ; stop B motor
  forward A   ; start A motor
  forward B   ; start B motor
  pause 1000  ; keep robot straight
  halt A      ; stop A motor
  halt B      ; stop B motor
  goto main   ; loop main