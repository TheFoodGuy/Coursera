# Harvard PH525 Course 2 - Throughput
# This is the 1st assignment of week 1

# R refresher
library(devtools)
library(dplyr)
# since github install package toolkit is a bit wack i did it manually
load(file = "~/Documents/stats/GSE5859Subset.rda")
sum(sampleInfo$date=="2005-06-27")
sum(geneAnnotation$CHR=="chrY",na.rm=TRUE)
i = which(geneAnnotation$SYMBOL=="ARPC1A")
j = which(sampleInfo$date=="2005-06-10")
geneExpression[i,j]
median(apply(geneExpression, 2, median))

# exercise 5, this is a use apply to create a function 
# e is the vector value or data frame
# group is i guess the groups inside of the data frame 
ttestgenerator <- function(e, group){ 
  t.test(e[group==1], e[group==0])$p.value
}
g <- factor(sampleInfo$group)
min(apply(geneExpression, 1, ttestgenerator, group = g ))

# inference in practice on why p-values are random 
set.seed(1)
library(downloader)
url = "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleControlsPopulation.csv"
filename = "femaleControlsPopulation.csv"
if (!file.exists(filename)) download(url,destfile=filename)
population = read.csv(filename)
pvals <- replicate(8,{
  control = sample(population[,1],12)
  treatment = sample(population[,1],12)
  t.test(treatment,control)$p.val
})
head(pvals)
hist(pvals)

mean(pvals <= 0.05)
mean(pvals <= 0.01)

cases = rnorm(10,30,2)
controls = rnorm(10,30,2)
t.test(cases,controls)
set.seed(100)
