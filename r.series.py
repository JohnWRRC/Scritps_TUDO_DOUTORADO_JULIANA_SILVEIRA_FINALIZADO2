import os
import fnmatch
import sys


os.getcwd()



os.chdir("f:\\data\\Juliana_inpe")
lista=[]
lista=os.listdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals")
arquivo = open('sum.bat', 'w')
for i in lista:
    temp=i
   
    linha= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\\"+temp+"\""
    linha2="\n" "list=`g.mlist pattern=\"*af_tif\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_series method=maximum" "\n"
    arquivo.write(linha)
    arquivo.write(linha2)
    arquivo.close() 
    get=os.getcwd()
    
   
    
    
  
    
    
    

