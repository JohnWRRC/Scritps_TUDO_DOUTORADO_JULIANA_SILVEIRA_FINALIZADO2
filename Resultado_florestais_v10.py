import os
import fnmatch
import sys

os.chdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Florestais")
os.getcwd()

lista1=[]
lista2=[]
lista3=[]
listaGeral=[]
lista=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Florestais/Florestais_habitat_matriz")
lista2=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Florestais/Florestais_aberta_fechada")
lista3=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Florestais/Florestais_heterogenea")
listaGeral=lista+lista2+lista3



arquivo = open('Resultados_finais_florestais.bat', 'w')
listaRaiz=os.listdir("C:/Users/juliana/Documents/RESULTADOS_DOUTORADO/Paisagens_Modelos_Smmal_Mammals/Florestais")
HM=listaRaiz[1]
AF=listaRaiz[0]
HE=listaRaiz[2]
cont2=0
for i in listaGeral:
    temp=i
   
    if temp[0:2]=="HM":
        linha1= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\\"+HM+ "\\"+temp+ "\grass" "\""  "\n"
        linha2="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_florestais_"+temp+" method=sum --o""\n" 
        linha3="list=`g.mlist pattern=\"*soma_florestais_"+temp+"\" sep=\"comma\"`" "\n" "g.region rast=$list" "\n" "r.grow.distance in=$list distance=distance_florestais_"+temp+" -m --o" "\n"
        
        linha4="\n" "cd \"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\""
        linha5="\n" "listaex=`g.mlist pattern=\"distance_florestais*\"`" "\n" "for i in $listaex" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\""+temp+"\",\""+temp+".tif""\");print}'`" "\n" "r.out.gdal in=$i out=$out format=GTiff nodata=-9999 --v " "\n" "done" "\n"        
        linhaaux="#..................................................................................................................................................................""\n"
        arquivo.write(linha1)
        arquivo.write(linha2)
        arquivo.write(linha3)
        arquivo.write(linha4)
        arquivo.write(linha5)
        arquivo.write(linhaaux) 
      
    if temp[0:2]=="AF":
        linha6= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\\"+AF+"\\"+temp+ "\grass\" " "\n"
        linha7="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_florestais_"+temp+" method=sum --o" "\n"
        linha8= "list=`g.mlist pattern=\"soma*\"`" "\n" "r.mapcalc \"$list\"_Bin\"=if($list<1,null(),1)\" " "\n"
        linhaaux="#..................................................................................................................................................................""\n"
        linha9="\n" "cd \"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\""
        linha10="\n""listaex=`g.mlist pattern=\"*_Bin\"`" "\n" "for i in $listaex" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin\""",""\"_Bin.tif\");print}'`" "\n" "r.out.gdal in=$i out=$out format=GTiff  --v" "\n" "done" "\n"         
        arquivo.write(linha6)
        arquivo.write(linha7)
        arquivo.write(linha8)
        arquivo.write( "\n")
        arquivo.write(linha9)
        arquivo.write(linha10)
        arquivo.write( linhaaux)
        
    if  temp[0:2]=="HE":
        linha6= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\\"+HE+"\\"+temp+ "\grass\"" "\n"
        linha7="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_florestais_"+temp+" method=sum --o" "\n"
        linha8= "list=`g.mlist pattern=\"soma*\"`" "\n" "r.mapcalc \"$list\"_Bin\"=if($list<1,null(),1)\" " "\n"
        linhaaux="#..................................................................................................................................................................""\n"
        linha9="\n" "cd \"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\""
        linha10="\n""listaex=`g.mlist pattern=\"*_Bin\"`" "\n" "for i in $listaex" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin\""",""\"_Bin.tif\");print}'`" "\n" "r.out.gdal in=$i out=$out format=GTiff  --v" "\n" "done" "\n"          
        arquivo.write(linha6)
        arquivo.write(linha7)
        arquivo.write(linha8)
        arquivo.write( "\n")
        arquivo.write(linha9)
        arquivo.write(linha10)
        arquivo.write( linhaaux)        
cont2=cont2+1        
linha11= "\n""g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\" ""\n"
linha12="cd \"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\""
linha13="\n" "files=*.tif" "\n" "for i in $files" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\".tif\",\".tif\");print}'`" "\n" "r.in.gdal in=$i out=$out -o --o" "\n" "done" "\n"
arquivo.write(linha11) 
arquivo.write(linha12)  
arquivo.write(linha13) 
arquivo.write( linhaaux)

arquivo.close() 


#########################################################################################################################
#############################RODAR SEPARADO##############################################################################
geral=os.listdir("C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas")
arquivo = open('rmapcal_florestais.bat', 'w')
sub='AF_ST' 
sub2='HE_ST'
sub3='distance' ###distance


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

for fname in af:
    ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
    mapdist=dista[con]
    linha14="g.region rast="+ fname +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+fname + "*" +mapdist+ "\n" 
    con=con+1  
    arquivo.write(linha14) 
    linha14=""
        

arquivo.write( linhaaux)
con=0 
for fname in het:
    ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
        
    mapdist=dista[con]
    linha15="g.region rast="+ fname +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+fname + "*" +mapdist+ "\n" 
    con=con+1  
    arquivo.write(linha15) 
    linha15=""
arquivo.write( linhaaux)
arquivo.write( linhaaux)
linha16="\n" "cd " "\"C:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\saidas\saidas\""
linha17="\n""listaex=`g.mlist pattern=\"*_final\"`" "\n" "for i in $listaex" "\n" "do" "\n" "g.region rast=$i" "\n" "out=`echo $i|awk '{gsub(\"_final\""",""\"_final.tif\");print}'`" "\n" "r.out.gdal in=$i out=$out format=GTiff nodata=-9999  --v" "\n" "done" "\n"      
arquivo.write(linha16) 
arquivo.write(linha17) 




arquivo.close()