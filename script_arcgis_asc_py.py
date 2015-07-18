#import arcpy
#from arcpy import env
import os
import fnmatch
import os
import string
import glob
import re
import fnmatch
listaraster=[]
lista_arquivos=[]
            
#rodar isso no arcpy
c=0
pasta=os.listdir('J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_aberta_fechada') #raiz

caminho='J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_aberta_fechada\\'
caminho=caminho.replace('\\','\\')
#caminho_saida='J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Medim_Big_Mammals\Generalistas\Generalistas_Heterogeneas\ascii\''

for i in pasta:
    caminho2='J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_aberta_fechada\\'+pasta[c]
    caminho2=caminho2+'\\'
    #print caminho2
    #env.workspace=(r'J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_habitat_matriz')
    env.workspace =caminho2
    rasterList = arcpy.ListRasters()
    
    print rasterList
   
    for rt in rasterList:
 
        if 'Flo_AF.tif' in rt: 
            inp=rt
            ofile2=unicode(""+os.path.splitext(inp)[0]+".asc")
            arcpy.RasterToASCII_conversion(inp, ofile2) 
            
    c=c+1
            
            
            
            
# rodar isso aqui    
move=[]
lista_arquivos=[] ## criando lista vazia para armazenar as imagens encontradas, caso aja mais de uma com o mesmo nome
for root, dirs, files in os.walk("J:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Medim_Big_Mammals/Florestais/Florestais_Heterogeneas"):
    for file in files:
        if file.endswith('.asc'):
            print os.path.join(root, file)
            lista_arquivos.append(os.path.join(root, file))## a
            move.append(file)

                
d=0
import shutil

for f in lista_arquivos:
    os.remove(f)
    


