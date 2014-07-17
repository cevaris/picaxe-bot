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
    tune 2, 5,($6C,$00,$45,$44,$42,$40,$29,$40,$45,$44,$42,$43)

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
    tune 2, 4,($4B,$4A,$4B,$4C,$6B,$4C,$6B,$4C,$46,$44,$43,$46)

  else
    forward A;
    forward B;
  end if

  goto main