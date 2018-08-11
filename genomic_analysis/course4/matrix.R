library(devtools)
# this doesn't work on my computer for some reasons
install_github("genomicsclass/tissuesGeneExpression")
library(tissuesGeneExpression)
data(tissuesGeneExpression)

# work around down here
url <- "https://github.com/genomicsclass/tissuesGeneExpression/tree/master/data/tissuesGeneExpression.rda"
download.file(url, "~/Downloads")
load("/home/david/Downloads/tissuesGeneExpression.rda")
head(e)
head(tissue)
# finding the number of biological replicates 
table(tissue)

# distance betwen samples 3 and 45
#sqrt(crossprod(t(tissue[e[,3]] - tissue[e[,45]])))
x <- e[,3]
y <- e[,45] 
sqrt(sum((x-y)^2))
# or 
sqrt( crossprod(x-y))
# or but it takes a while tho so it does all of the distance formula
d <- dist(t(e))
as.matrix(d)[3,45]

# distance between 210486_at and 200805_at 
x <- e["210486_at",] # we're trying to get all of the row with this value
y <- e["200805_at",] 
sqrt( crossprod(x - y) )

# how many cells would this crazy command have? 
# d = as.matrix(dist( e))
dim(e)[1] ^2

# compute the distance between all pairs of samples
d = dist(t(e))
?dist 
length(d) 

# why not ncol(e) ^ 2
# because we don't want to run dim(e)[1] columns ^ 2 when we could get the
# same results using the lower form

