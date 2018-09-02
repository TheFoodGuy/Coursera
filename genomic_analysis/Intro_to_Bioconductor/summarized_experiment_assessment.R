# how many samples are derived from the brain 
library(erma)
ee = makeErmaSet()
class(colData(ee))
length(names(colData(ee)))  # lots of attributes!
table(ee$ANATOMY)

# using ermaset instance, why do the last two dim() result disagree? 

mydf = colData(ee)[,1:10]
getClass("DataFrame")
mydf$demomat = matrix(0, nr=nrow(mydf), nc=5)
dim(mydf$demomat)
dim(mydf)
dim(data.frame(mydf))

# what data structure should be used to manage paths 
# to the BAM files 

