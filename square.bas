main: 
  high B.4    ; start left motor
  pause 700   ; keep turning left motor
  low B.4     ; stop left motor
  forward A   ; start right
  forward B
  pause 1000
  halt A
  halt B
  goto main