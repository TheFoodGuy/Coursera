# week 1 materials
# this part is the start up section of downloading and setting 
# up rstudio to be used in course 5

library(BSgenome.Hsapiens.UCSC.hg19)
nchar(Hsapiens$chr16)

library(BiocInstaller)
biocLite("genefu")

#1 using is.na to search for ways of describing the genes in the signature
library(genefu)
data(sig.gene70)
dim(sig.gene70)
head(sig.gene70)[,1:6]

sum(is.na(sig.gene70[,1:6]$NCBI.gene.symbol))

#2 kinases in the 70 gene signature 
# find the number of kinases in sig.gene70 using Description
library(dplyr)
#kinaseInd <- sig.gene70$Description %>%
#  grep("kinase") %>%
#  sum()

grep("kinase", sig.gene70$Description)