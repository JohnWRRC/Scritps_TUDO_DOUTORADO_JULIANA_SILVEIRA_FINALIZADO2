import os
import fnmatch
import sys

os.chdir(r'F:\data\Juliana_inpe')
c=open('teste.bat', 'w')
for i in range(30):
    linha1='LOADDATA FILE=\"D:\PASSaGE 2\pai'+`i+1`+'.txt\"' '\n' 
    linha2='FORMAT=TXT TAB=NO SPACE=YES COMMA=NO CONSECUTIVE=YES NAME=\"pai'+`i+1`+'\"' ' \n' 
    linha3='LABELS=NO MISSING=BLANK TYPE=RECT COLUMNS=ALL;' '\n'
    linha4='QUADVAR DATA=\"pai'+`i+1`+'\" MAXSCALE=25 METHOD=9TLQV WRAP=NO  SCALEFACTOR=1.0 PERMUTE=NO SAVE=YES SAVENAME=\"pai1_scale\";' '\n'
    linha5='SAVEDATA DATA=\"pai'+`i+1`+'_scale\"' '\n'
    linha6='FORMAT=TXT LABELS=NO MISSING=-9999 DECIMALS=5 FILE=\"D:\PASSaGE 2\pai'+`i+1`+'_scale.txt\";' '\n'
    linha7='DELETE #2; DELETE #2; DELETE #2; DELETE #1;' '\n'
    pula='\n'
    
    c.write(linha1)
    c.write(linha2)
    c.write(linha3)
    c.write(linha4)
    c.write(linha5)
    c.write(linha6)
    c.write(linha7)
    c.write(pula)
    
c.close()  
    
