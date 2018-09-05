library(devtools)
install_github("genomicsclass/maPooling")

# this is the set up for the work 
library(Biobase)
library(maPooling)
data(maPooling)
pd=pData(maPooling)
pooled=which(rowSums(pd)==12)
individuals=which(rowSums(pd)==1)
##remove replicates
individuals=individuals[-grep("tr",names(individuals))]
pool = exprs(maPooling)[,pooled] 
indiv = exprs(maPooling)[,individuals]
strain = ifelse(grepl("a",rownames(pData(maPooling))),0,1)

g_pool = strain[pooled]
g_indiv = strain[individuals]
