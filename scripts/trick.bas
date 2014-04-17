main: 
  high B.4    ; start B motor
  pause 1300   ; keep turning B motor
  low B.4     ; stop B motor

  forward A   ; start A motor
  forward B   ; start B motor
  pause 3000  ; keep robot straight
  halt A      ; stop A motor
  halt B      ; stop B motor

  high B.6   ; start B motor
  pause 1300   ; keep turning B motor
  low B.6    ; stop B motor


  forward A   ; start A motor
  forward B   ; start B motor
  pause 3000  ; keep robot straight
  halt A      ; stop A motor
  halt B      ; stop B motor

  goto main   ; loop main