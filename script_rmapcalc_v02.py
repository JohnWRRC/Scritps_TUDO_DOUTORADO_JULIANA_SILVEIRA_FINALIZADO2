import os
import fnmatch
import sys



os.chdir ("C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\RESULTADOS_SMMALL\Resultados")


os.getcwd()

geral=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/RESULTADOS_SMMALL/newLocation/PERMANENT/cell")

sub='af_tif'
sub2='het_tif'
sub3='distance'

het= []
af=[]
dista=[]

for i in geral:
    if sub in i:
        print i
        af.append(i)
    elif sub2 in i:
            het.append(i)
    elif sub3 in i:
        dista.append(i)


mapdist=[]
fname=[]
con=0
arquivo = open('r.mapcalc2_af.bat', 'w')
for fname in af:
        ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
        
        mapdist=dista[con]
        linha="g.region rast="+ fname +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+fname + "*" +mapdist+ "\n" 
        con=con+1  
        arquivo.write(linha)

linha=""

arquivo.close() 

