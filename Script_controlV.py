import os
import fnmatch
import sys

os.chdir("F:/data/Juliana_inpe")
os.getcwd()

i=0
arquivo = open('R.txt', 'w')
while i < 100:
    linha1= "while(i<10000)" "\n" "{print(i)" "\n" " temp = dados[sample(nrow(dados),30, replace=TRUE),];" "\n" " aleat<-runif(n=nrow(temp))" "\n" " x<-temp$Perm_Final" "\n" \
        " y<-temp$Conec_AF" "\n" " cut1.perm<- mean(x)" "\n" " modelo.lm<-try(glm(y~x, data=temp))" "\n" " modelo.segmented<-try(segmented(modelo.lm,seg.Z=~x,psi=list(x=c(cut1.perm)),"\
        "\n" "                                 control=seg.control(display=F)))" "\n"  " modelo.nulo<-try(glm(temp$Conec_AF~temp$aleatorio))" "\n" " if (all(class(modelo.segmented)!=\"try-error\", class(modelo.nulo)!=\"try-error\", class(modelo.lm)!=\"try-error\")){"\
        "\n"  "  ICtab_fora= ICtab(modelo.segmented, modelo.lm, modelo.nulo,type=\"AICc\", weights=T, base=T, nobs=nrow(temp))" "\n" "  out = attributes(ICtab_fora)" "\n" "  win_list = out$row.names" "\n"\
        "  win = win_list[1] " "\n" "  output[[i]] = win" "\n" "  i=i+1" "\n" " }" "\n" "}" "\n"
        
    linhaaux="#..................................................................................................................................................................""\n"
    
    
    
    
    
    
    
    
    
    arquivo.write(linha1) 
    arquivo.write(linhaaux)
    i=i+1
    
    arquivo.close() 