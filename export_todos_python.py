import os
import fnmatch
import sys
import grass.script as grass
from grass.script import raster as grassR


os.chdir("J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_heterogenea")


lista=[]
lista=os.listdir(r"J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_heterogenea")

os.getcwd()

c=0

for i in lista:
    temp=i
    grass.run_command( 'g.mapset',  mapset='PERMANENT', location='newLocation', gisdbase='J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_heterogenea\\'+temp+'\\grass')
   
    #grass.run_command( 'g.region',flags='p')
    p=grass.mlist_grouped ('rast', pattern='Custo_Pai*') ['PERMANENT']
    os.chdir('J:\Users\juliana\Documents\RESULTADOS_DOUTORADO\Paisagens_Modelos_Smmal_Mammals\Florestais\Florestais_heterogenea\saidas_grass')
    inp=p
    outfile=''.join(p)
    grass.run_command('g.region',rast=inp)
    grass.run_command('r.out.gdal',input=inp, out=outfile+'_small_HE.tif', format='GTiff')
    c=c+1
    
    print p
                       #linha2="list=`g.mlist pattern=\"*sem0\" sep=\"comma\"`" "\n" "r.series in=$list out=soma_abertas_"+temp+" method=sum""\n" 
                       #linha3="list=`g.mlist pattern=\"*soma_abertas_"+temp+"\" sep=\"comma\"`" "\n" "g.region rast=$list" "\n" "r.grow.distance in=$list out=distance_abertas_"+temp+" -m" "\n"
                       
                       # linha4="\n" "cd \"F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\juliana_teste\saidas\""
                       # linha5="\n""listaex=`g.mlist pattern=\"*distance\"`" "\n" "for i in $" "\n" "do" "\n" "out=`echo $i|awk '{gsub(\"_Bin"",""_Bin.tif\");print}'`" "\n" "r.out.gdal in=$a out=$out format=GTiff nodata=-9999 --v" "\n" "done" "\n"        
    