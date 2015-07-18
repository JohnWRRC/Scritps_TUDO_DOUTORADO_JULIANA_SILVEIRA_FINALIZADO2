import os
import fnmatch
import sys



os.chdir ("F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\Imagens_Binarias_Distance")
corr_af=os.listdir("F:/data/Juliana_inpe/RESULTADOS_Smmal_Mammals/Imagens_Binarias_Distance/bins_af")
dist=os.listdir("F:\data\Juliana_inpe\RESULTADOS_Smmal_Mammals\Imagens_Binarias_Distance\distances")
os.getcwd()



con=0
arquivo = open('r.mapcalc.bat', 'w')
for fname in corr_af:
    
        ofile2=unicode(""+os.path.splitext(fname)[0]+"_final")
        entrada1=unicode(""+os.path.splitext(fname)[0]+"_tif")
        entrada2=dist[con]
        entrada2=unicode(""+os.path.splitext(entrada2)[0]+"_tif")
        linha="g.region rast="+ entrada1 +" " "res=28.5" "\n" "r.mapcalc "+ofile2+"="+entrada1 + "*" +entrada2+ "\n" 
        con=con+1
        
        arquivo.write(linha)

arquivo.close() 
