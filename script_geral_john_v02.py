import os
import fnmatch
import sys

os.chdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals/juliana_teste")


lista=[]
lista=os.listdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals/juliana_teste")

os.getcwd()


arquivo = open('soma_aberta_HM.bat', 'w')
for i in lista:
    temp=i
   
    
    if temp=="hm":
        linha1= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\\"+temp+ "\n"
        linha2="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas_"+temp+" method=sum""\n" 
        linha3="list=`g.mlist pattern=\"*soma_abertas_"+temp+"\" sep=\"comma\"`" "\n" "g.region rast=$list" "\n" "r.grow.distance in=$list out=distance_abertas_"+temp+" -m" "\n"
        linhaaux="#..................................................................................................................................................................""\n"
        arquivo.write(linha1)
        arquivo.write(linha2)
        arquivo.write(linha3)
        arquivo.write( linhaaux) 
      
    if temp=="AF" or temp=="Het":
        linha4= "g.mapset  mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\\"+temp+ "\n"
        linha5="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas"+temp+" method=sum" "\n"
        linha6= "llist=`g.mlist pattern=\"soma*\"`" "\n" "r.mapcalc \"$list\"_Bin\"=if($list<1,null(),1)\" " "\n"
        
        
        linhaaux="#..................................................................................................................................................................""\n"
        arquivo.write(linha4)
        arquivo.write(linha5)
        arquivo.write(linha6)
        arquivo.write( linhaaux)
    linha7="\n" "cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\""
    linha8="\n""listaex=`g.mlist pattern=\"_Bin*\"`" "\n" "for i in $" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin"",""_Bin.tif\");print}'`" "\n" "r.out.gdal in=$a out=$out format=GTiff nodata=-9999 --v" "\n" "done" "\n" 
    arquivo.write(linha7)
    arquivo.write(linha8)     
           
linha9= "\n""g.mapset -c mapset=PERMANENT location=newLocation gisdbase=\"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\" ""\n"
linha10="cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\Imagens_Binarias_Distance\bins_het\""
linha11="\n" "files=*.tif" "\n" "for i in $files" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\".tif\",\"_tif\");print}'\`" "\n" "r.in.gdal in=$i out=$out -o --o" "\n" "done"
arquivo.write(linha9) 
arquivo.write(linha10)  
arquivo.write(linha11) 



arquivo.close() 

 