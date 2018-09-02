## for some reasons I couldn't get the library installed 
# so im going to take the loss for this part and move on

install.packages("devtools")
library(devtools)
install_github("Bioconductor-mirror/SummarizedExperiment")
source("https://bioconductor.org/biocLite.R")
biocLite("airway")
library(airway)
library(SummarizedExperiment)
td = tempfile()
saveHDF5SummarizedExperiment(airway, td)

X  = readRDS(dir(td, full=TRUE)[2]) 
