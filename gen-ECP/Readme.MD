Small script to generate the basis and ECP parts for a GAMESS input file.
 $BASIS 
  basnam(1)= basH, ...
 $END
 
 Then define each of the basis using
$BASH
S   3
1        19.2384000              0.0328280
2         2.8987000              0.2312040
3         0.6535000              0.8172260
S   1
1         0.1776000              1.0000000

$END

and then the ECP part
 $ECP
 H-ecp none
 ...
 
 $END
