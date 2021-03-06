%%!PS-Adobe-3.0 EPSF-3.0
%%%BoundingBox: 0 0 184 230

%% Business Card : 0 0 252.283405 144.566895
%% A6            : 0 0 297.637725 420.9447825
%% A5            : 0 0 420.9447825 595.27545
%% A4            : 0 0 595.27545 841.889565
%% A3            : 0 0 841.889565 1190.5509
%% A2            : 0 0 1190.5509 1683.77913
%% A1            : 0 0 1683.77913 2381.1018

%%% Defines more easy to deal with units 
/cm { 28.34645 mul } def
/mm {  2.83465 mul } def

/linethickness {{thickness}} mm def
/period {{period}} mm def
/drawwidth 33 mm def
/drawheight 33 mm def
/fontsize 18 mm def

%%% Sets color to black
0 setgray
{{red}} {{green}} {{blue}} setrgbcolor

drawheight drawwidth gt {drawheight} {drawwidth} ifelse

2 exp 2 mul sqrt ceiling cvi

/width exch def
/height width def

/lines height period div ceiling cvi def
/pi 3.14159 def

/unrealrand {
    {(%Calendar%) currentdevparams dup} stopped
    {
            0
    }
    {
            /Second get exch dup
            /Minute get exch 
            /Hour get
            60 mul add
            60 mul add
        } ifelse
        
        realtime add srand
} def

/shrinkto {
    /max exch def
    {
        dup max gt {-1 bitshift} {exit} ifelse
    } loop

} def

/todec {
    {
        dup 1 ge {.1 mul} {exit} ifelse
    } loop
} def

unrealrand %% add our new seed

/decrand { rand todec } def
/smallrand { rand 2147483647 div 2 mul 1 sub abs } def
/randrotate { smallrand 360 mul smallrand 6 mul mul } def
/randpattern { patterns smallrand patterns length 1 sub mul round cvi get } def

/rot randrotate def

/box {
    0 0 moveto
    exch dup 0 rlineto
    exch 0 exch rlineto
    neg 0 rlineto
} bind def

/drawpattern {
    linethickness setlinewidth 

    gsave
        randrotate rotate
        %%0 rotate        
        width 2 div neg lines period mul 2 div neg translate
        patterns randpattern exec

        %%patterns patterns 7 get exec
    grestore
    
} bind def

/patterns [
    %% 0: Simply lines
    {
        lines {
            0 0 moveto
            0 period translate
            width 0 rlineto
            stroke
        } repeat
    }
    
    %% 5: 3 Sinus waves
    { 3 sinuswave exec }
    
    %% 5: 3 Sinus waves
    { 2 sinuswave exec }

    %% 6: 1 Sinus wave
    { 1 sinuswave exec }

    %% 7: Big curve
    { 20 curve exec }

    %% 8: Medium curve
    { 15 curve exec }

    %% 9: Small curve
    { 10 curve exec }

    %% 10: Inv big curve
    { 20 neg curve exec }

    %% 11: Inv medium curve
    { 15 neg curve exec }

    %% 12: Inv small curve
    { 10 neg curve exec }
    
    %%% 15: 4 Sharkteeth
    %%{ 4 11 sharkteeth exec }

    %%% 16: 3 Sharkteeth
    %%{ 3 14 sharkteeth exec }

    %%% 17: 2 Sharkteeth
    %%{ 2 17 sharkteeth exec }

    %%% 19: 1 Sharkteeth
    %%{ 1 20 sharkteeth exec }
] def %% end patterns

/basepatterns [
    %% begin sinus wave
    { 
        %% How many curves do we need to draw
        /curves exch def
        %% Figure out how wide they need to be
        /cw width curves div ceiling def
        %% Define the half of that width
        /cwh cw 2 div def
        
        %% If we only draw a small amount of curves a
        %% big part of the drawing is not covered.
        %% Therefor we're going to draw extra lines
        %% And need extra translation.
        
        %% gap is curvewidth / (2pi) = .5 curvewidth / pi = cwh pi div
        %% fill lines is gap period div ceiling cvi
        %% filllinestop = filllinesbottom = gap period div 2 div ceiling cvi

        /gap cw pi div def
        /extralines gap period div ceiling cvi def

        %% And perform extra translation
        0 gap 2 div neg translate 

        lines extralines add{
            gsave
                curves {
                    0 0 moveto
                    cwh cwh cwh cwh neg cw 0 curveto
                    cw 0 translate
                } repeat
                
                stroke
            grestore

            0 period translate
        } repeat
    }
       
    %% Draws a curve width given height,
    %% height defined as a percentage of the width
    {
        /h exch 100 div width mul def %% Height of the curve
        /c width 2 div def %% Define center of curve
 
        /gap h def
        /extralines gap abs period div ceiling cvi def

        0 gap neg translate

        lines extralines add {
            0 0 moveto
            c h c h width 0 curveto stroke
            0 period translate
        } repeat
    }
    
    %% Draws sharkteeth. As defined by
    %% points and height
    {
        /h exch 100 div height mul ceiling cvi def %% Height of the points
        /p exch def %% Amount of points
        /pw width p div ceiling cvi def
        /pwh pw 2 div def
       
        /extralines h period div ceiling cvi def
    
        0 h neg translate

        lines extralines add{          
            gsave
                0 0 moveto
                p {
                    pwh h rlineto 
                    pwh h neg rlineto 
                    pw 0 translate                 
                } repeat
                stroke
            grestore
            0 period translate
        } repeat
    }
] def %% end base patterns

/sinuswave  basepatterns 0 get def
/curve      basepatterns 1 get def
/sharkteeth basepatterns 2 get def

%%% Font support {{{
12 dict begin
  /FontName /PropCourierSans def
  /FontType 42 def
  /FontMatrix [1 0 0 1 0 0] def
  /PaintType 0 def
  /FontBBox {0.062 -0.016 0.56 0.576 }readonly def
/FontInfo 10 dict dup begin
 /version (1.2) readonly def
 /Notice (PropCourier was designed by Manufactura Independente \050Ana Carvalho & Ricardo Lafuente\051, in October 2010. It is a friendly fork of OSP's NotCourier. \012NotCourier was designed by OSP \050Ludivine Loiseau\051, in July 2008. It is based on Nimbus Mono, copyright \050URW\051++,Copyright 1999 by \050URW\051++ Design & Development; Cyrillic glyphs added by Valek Filippov \050C\051 2001-2005) readonly def
%% PropCourier was designed by Manufactura Independente (Ana Carvalho & Ricardo Lafuente), in October 2010. It is a friendly fork of OSP's NotCourier. 
%% NotCourier was designed by OSP (Ludivine Loiseau), in July 2008. It is based on Nimbus Mono, copyright (URW)++,Copyright 1999 by (URW)++ Design & Development; Cyrillic glyphs added by Valek Filippov (C) 2001-2005
 /FullName (PropCourier) readonly def
 /FamilyName (PropCourierSans) readonly def
 /Weight (Book) readonly def
 /FSType 0 def
 /ItalicAngle 0 def
 /isFixedPitch false def
 /UnderlinePosition -0.1 def
 /UnderlineThickness 0.05 def
end readonly def
  /Encoding 256 array
   0 1 255 { 1 index exch /.notdef put} for
    dup 67/C put
    dup 73/I put
    dup 79/O put
    dup 83/S put
  readonly def
  /sfnts [
 <
  0001000000080080000300004646544D5B31775F000002940000001C637674
  20002102790000012400000004676C796663165D74000001380000015C6865
  6164FAAE95BA0000008C0000003668686561064B02DD000000C40000002468
  6D74780F85011F000001080000001C6C6F636100A200F40000012800000010
  6D617870004B0032000000E800000020
  00
 >
 <
  0001000000013333EDC6668F5F0F3CF5000B03E800000000CC908FB9000000
  00CC908FB9003EFFF002300240000000080002000000000000
  00
 >
 <
  0001000003BFFEED005A03E800000000023000010000000000000000000000
  0000000007
  00
 >
 <
  000100000007002F0002000000000002000000010001000000400000000000
  00
  00
 >
 <
  03E800000000000003E800000240004000E5005D026E003E02220044
  00
 >
 <
  00210279
  00
 >
 <
  000000000000000000380046006A00AE
  00
 >
 <
  00010040FFF0021702400025000001142322272E012322061D011416333236
  37363332151407062322263D013436373633321E0102081513010367435376
  8258345228090914264C62669D2720456627515201A81B182E447F59475A85
  2A300A131023479D65532E61224A17490000000001005D0000008602330003
  0000133311235D29290233FDCD0000000002003EFFF002300240000A001500
  000132161514062322263436172206141633323635342601376A8F92676891
  9168567A7A56557B790240AD7F79ABACF8AC2996D29695676C9600010044FF
  F001E40240002E000037343332171E01333236353427262726272635343633
  321615142322272E0123220614171617161716151406232226441513010262
  44465D2D1D57602834694F576414140103523A3E5127224F62253E745A5280
  8B1B1831444937391B130F101E24444259602F1B182D3C42621B160D111726
  50495E61000000
  00
 >
 <
  0000000100000000CC3DA2CF00000000C26344FA00000000CC908F95
  00
 >
  ] def
  /CharStrings 5 dict dup begin
    /.notdef 0 def
    /C 3 def
    /I 4 def
    /O 5 def
    /S 6 def
  end readonly def


FontName currentdict end definefont pop
%%% easy access to our font
/headerfont     /PropCourierSans findfont fontsize scalefont def
headerfont setfont
%%% }}}

%%% Performs the logo {{{
gsave
    drawwidth 1 mul drawheight 1.5 mul translate
    newpath
        drawwidth 1 mul 2 div neg drawwidth 1 mul 2 div neg moveto
        0 drawwidth rlineto
        drawheight 0 rlineto
        0 drawwidth neg rlineto
        drawheight neg 0 rlineto 
    closepath
    clip
    newpath
        unrealrand
        drawpattern
    closepath
grestore

gsave
    drawwidth 1.2 mul drawheight 1.6 mul translate
    rot neg rotate
    newpath
        drawwidth 1 mul 2 div neg drawwidth 1 mul 2 div neg moveto
        0 drawwidth 1 mul rlineto
        drawheight 1 mul 0 rlineto
        0 drawwidth 1 mul neg rlineto
        drawheight 1 mul neg 0 rlineto 
    closepath
    clip
    newpath
        unrealrand
        drawpattern
    closepath
grestore

15 mm 15 mm moveto
(COSIC) show
%%% }}}

%%% vim: set foldmethod=marker :
