library(devtools)
install_github("genomicsclass/tissuesGeneExpression")

library(tissuesGeneExpression)
data(tissuesGeneExpression)
head(e[,1:5])
table(tissue)

library(SummarizedExperiment)
tissSE = SummarizedExperiment(list(rma=e))
colData(tissSE) = DataFrame(tab)

#1 Localization of expression to tissues
assay(tissSE)
mean(assay(tissSE["209169_at",]))
boxplot(assay(tissSE)["209169_at",]~tissSE$Tissue, las=2, mar=c(6,4,2,2))

#2 which of the IDs are connected to the placenta 
boxplotList <- function(d){
  boxplot(assay(tissSE)[d,]~tissSE$Tissue, las=2, mar=c(6,4,2,2))
}
IDs = c("201884_at", "209169_at", "206269_at", "207437_at", "219832_s_at", "212827_at")
sapply(IDs, boxplotList)

#3 Oligo sequences on affymetrix arrays
library(BiocInstaller)
biocLite("hgu133aprobe")
library(hgu133aprobe)
head(hgu133aprobe)

sum(hgu133aprobe$Probe.Set.Name=="206269_at")

library(hgu133a.db)
sym = mapIds(hgu133a.db, keys=rownames(tissSE), column="SYMBOL", keytype="PROBEID")
nm = mapIds(hgu133a.db, keys=rownames(tissSE), column="GENENAME", keytype="PROBEID")
rowData(tissSE) = DataFrame(symbol=sym, genename=nm)
tissSE[ grep("kinase", rowData(tissSE)$genename), ]
nrow(tissSE[ grep("kinase", rowData(tissSE)$genename), ]) 
