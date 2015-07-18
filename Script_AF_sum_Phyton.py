import os
import fnmatch
import sys



os.chdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Abertas/Abertas_habitat_matrix")
os.getcwd()
lista=[]
lista=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Abertas/Abertas_habitat_matrix")

os.getcwd()


arquivo = open('soma_aberta_HM.bat', 'w')
for i in lista:
    temp=i
   
    linha= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Abertas\Abertas_habitat_matrix\\"+temp+"\grass\""
    linha2="\n" "list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas_HM method=sum" "\n"
    arquivo.write(linha)
    arquivo.write(linha2)
    
    
    
    
    arquivo.close() 
