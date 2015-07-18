import os
import fnmatch
import sys



os.chdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Abertas/Abertas_aberta_fechada")
os.getcwd()
lista=[]
lista=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Abertas/Abertas_aberta_fechada")

os.getcwd()


arquivo = open('Binario_aberta_AF.bat', 'w')
for i in lista:
    temp=i
   
    linha= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Abertas\Abertas_aberta_fechada\\"+temp+"\grass\""
    linha2="\n" "list=`g.mlist pattern=\"soma*\"`" "\n" "r.mapcalc \"$list\"_Bin\"=if($list<1,null(),1)\" " "\n"
    arquivo.write(linha)
    arquivo.write(linha2)
    
 
    
    
    
    
    arquivo.close() 
