rm(list=ls())
library(GenomicRanges)
library(ph525x)

# 1 this is testing out GRanges and understanding how they 
# work in comparsion to IRanges 

x = GRanges("chr1", IRanges(c(1,101), c(50,150)), strand=c("+", "-"))
ranges(x)
plotGRanges = function(x) plotRanges(ranges(x))
plotGRanges(x) 
plotGRanges(resize(x,1))

# 2 Isoforms and understanding overlapping gene and the detection
# of them 
x = GRanges("chr1", IRanges(c(101,201,401,501),c(150,250,450,550)), strand="+")
y = GRanges("chr1", IRanges(c(101,221,301,401,541),c(150,250,350,470,550)), strand="+")
GRangesList(x,y)
plotGRanges(x)
plotGRanges(y)

disjoin_x_y = disjoin(c(x,y))
overlap = disjoin_x_y %over% x & disjoin_x_y %over% y
sum(width(disjoin_x_y[overlap]))

# 3 - instead of and use or
overlap = !(disjoin_x_y %over% x & disjoin_x_y %over% y)
sum(width(disjoin_x_y[overlap]))

z = GRanges("chr1", range(ranges(x)), strand="-")
ranges(z)
sum(x %over% z)

