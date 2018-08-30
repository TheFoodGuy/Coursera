rm(list=ls())

library(ERBS)
data(HepG2)
data(GM12878)

# where does 17th HepG2 region start? 
start(HepG2[17,])

# find the closest region in GM12878 to the 17th region in HepG2
# what is the start site of this region
dtn<-distanceToNearest(HepG2[17],GM12878)
start( GM12878[subjectHits(dtn)] )

# what is the distance between the 17th region of HepG2 and its 
# closest region in GM12878
mcols(dtn)$distance

d<-distanceToNearest(HepG2,GM12878)
mean(mcols(d)$distance <2000)