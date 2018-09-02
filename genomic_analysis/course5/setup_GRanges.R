# this is for week 3
# setting up GRanges and checking up on it again before starting here 
# checking my version of bioconductor
library(devtools)
install_github("genomicsclass/ERBS")
library(BiocInstaller)
biocVersion # you will get it wrong if you're using the latest bioconductor since the correct ansewr is 3.6 and not 3.7 at the time 
            # of this typing

# probably needs to update/upgrade here 
source("https://bioconductor.org/biocLite.R")
biocLite("BiocUpgrade")
# what is the class of HepG2 and the package it is defined in? 
library(ERBS)
data(HepG2)
class(HepG2)

# how many regions are represented? 
# not chromosomes but I guess they are referring to the gene regions
length(HepG2)
unique(HepG2@ranges)
