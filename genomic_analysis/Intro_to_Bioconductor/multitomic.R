source("https://bioconductor.org/biocLite.R")
biocLite("MultiAssayExperiment")
biocLite("RaggedExperiment")

library(MultiAssayExperiment)  # verify 1.4.0 at least
library(RaggedExperiment)  # verify 1.2.0 at least
download.file("https://s3.amazonaws.com/bcfound-edx/tcgaLAML.rds", "tcgaLAML.rds")
laml = readRDS("tcgaLAML.rds")

# what is the length 
length(experiments(laml))

# what is the number of samples providing CNASNP, CNVSNP
# and methylation but no RNA-seq data
upsetSamples(laml)

# how many samples are separated from the bulk of the datat 
# by having high values of PC5
lnorna = log(exprs(experiments(laml)[["RNASeq2GeneNorm"]])+1)
pca = prcomp(t(lnorna))
pairs(pca$x[,1:5])
