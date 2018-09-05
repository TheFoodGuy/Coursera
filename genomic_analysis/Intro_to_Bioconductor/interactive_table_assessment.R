library(Homo.sapiens)
g = genes(Homo.sapiens)
library(ERBS)
data(HepG2)

# interpret the following computation
kp = g[resize(g,1) %over% HepG2]
kp

# how many entries mention apoptosis 
nn = names(kp)
m = select(Homo.sapiens, keys=nn, keytype="ENTREZID",
           columns=c("SYMBOL", "GENENAME", "TERM", "GO"))
library(DT)
datatable(m)

### ASSESSMENT ON KEGG
# how many pathways are listed 
keggGet("hsa", "pathway")

# what is the name of the pathway displayed 
# when used a PNG viewer to examine the file im.png
oo = keggGet("hsa00790", "image")
writePNG(oo, "im.png")

###Ontology lookup assessment 
source("https://bioconductor.org/biocLite.R")
biocLite("rols")
library(rols)
diab = OlsSearch("diabetes")
olsRows(allRows(diab))

# how many entries does it contribute on the term diabetes 
fulld = olsSearch(allRows(diab))
adf = as(fulld, "data.frame")
sort(table(adf$ontology_name), decreasing=TRUE)[1:10]

# how many entries are found in the table 
library(DT)
datatable(adf)

###GSEABase assessment 
library(GSEABase)
glioG = getGmt(system.file("gmt/glioSets.gmt", package="ph525x"))
tt = table(unlist(lapply(1:47, function(x) geneIds(glioG [[ x ]] ))))
tt[which.max(tt)]