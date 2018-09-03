# week 3 part 2 of the first contente

library(ERBS) 
data(GM12878)
data(HepG2)

# what is the median of the signalValue column for the HepG2 data 
median(mcols(HepG2$signalValue)) # wrong but the other two are right
median(HepG2$signalValue)
median( mcols(HepG2)$signalValue )

# in what chromosome is the region with the highest signalValue? 
max(mcols(HepG2)$signalValue)
HepG2[mcols(HepG2)$signalValue == 91.779]
seqnames(HepG2)
as.character(seqnames(HepG2))
table(seqnames(HepG2))
# 31


# make sa historgram of the width of the rgions 
hist(width(HepG2))
median(width(HepG2))
