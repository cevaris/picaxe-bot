main: 

  forward A;
  forward B;

  if pinC.1 = 1 then
    halt A
    halt B
    backward A
    backward B
    wait 1
    forward A
    wait 1
    forward A;
    forward B;
    tune 2, 5,($6C,$00,$45,$44,$42,$40,$29,$40,$45,$44,$42,$43,$04,$44,$44,$40,$42,$40,$44,$40,$42,$69,$40,$67,$6A,$69,$65)

  else if pinC.3 = 1 then
    halt A
    halt B
    backward A
    backward B
    wait 1
    halt A
    halt B
    forward B
    wait 1
    forward A;
    forward B;
    tune 2, 4,($4B,$4A,$4B,$4C,$6B,$4C,$6B,$4C,$46,$44,$43,$46,$4B,$4A,$4B,$4C,$51,$50,$51,$4C,$41,$4C,$41,$4C,$48,$46,$45,$48,$51,$50,$51,$4C,$53,$54,$56,$54,$53,$51,$54,$53,$51,$4B,$53,$51,$4B,$49,$51,$4B,$49,$48,$4B,$49,$48,$46,$49,$48,$46,$44,$43,$42,$41,$40,$6B,$4C,$6B,$41,$44,$4C,$44,$4C,$44,$46,$48,$49,$4B,$4C,$4B,$4C,$4B,$4C,$51,$53,$54,$56,$54,$51,$4B,$51,$4B,$48,$46,$44,$41,$44,$46,$4C,$6B,$41,$44,$46)

  else
    forward A;
    forward B;
  end if

  goto main


  
