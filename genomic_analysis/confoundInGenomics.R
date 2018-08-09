rm(list=ls())
library(Biobase)
library(GSE5859)
data(GSE5859)
#1 
geneExpression = exprs(e)
sampleInfo = pData(e)
year = format(sampleInfo$date,"%y")
length(unique(year))

tab = table(year, sampleInfo$ethnicity)
tab
x =rowSums(tab!=0)
sum(x >= 2)

# 2
month.year = format(sampleInfo$date,"%m%y")
mytab=table(month.year,sampleInfo$ethnicity)
print(mytab)
myx=rowSums(mytab!=0)
mean(myx>=2)

# 3 Perform a t-test (use rowttests) comparing CEU samples processed in 2002 to those processed in 2003. Then use the qvalue package to obtain q-values for each gene. 
# 4
library(qvalue)
library(genefilter)
year = factor( format(sampleInfo$date,"%y") )
index = which(year%in% c("03","04") & sampleInfo$ethnicity=="CEU")
year = droplevels(year[index])
pval = rowttests(geneExpression[ ,index], year)$p.value
qval = qvalue(pval)
sum(qval$qvalue < 0.05)
qval$pi0

# 5 compare ASN and CEU with rowttests 
library(qvalue)
library(genefilter)
ethnicity = factor( sampleInfo$ethnicity)
index = which(ethnicity%in% c("CEU","ASN"))
ethnicity = droplevels(ethnicity[index])
pval = rowttests(geneExpression[ ,index], ethnicity)$p.value
qval = qvalue(pval)
sum(qval$qvalue < 0.05)

#6 
library(qvalue)
library(genefilter)
ethnicity = factor( sampleInfo$ethnicity)
year = factor( format(sampleInfo$date,"%y") )
index = which(ethnicity%in% c("CEU","ASN") & year=="05")
ethnicity = droplevels(ethnicity[index])
pval = rowttests(geneExpression[ ,index], ethnicity)$p.value
qval = qvalue(pval)
sum(qval$qvalue < 0.05)

#7 
library(qvalue)
library(genefilter)
ethnicity = factor( sampleInfo$ethnicity)
year = factor( format(sampleInfo$date,"%y") )
indexASN = which(ethnicity%in% c("ASN") & year=="05")
indexCEU = which(ethnicity%in% c("CEU") & year=="02")
set.seed(3)
indexCEU<-sample(indexCEU,3)
index<-c(indexASN,indexCEU)
ethnicity = droplevels(ethnicity[index])
pval = rowttests(geneExpression[ ,index], ethnicity)$p.value
qval = qvalue(pval)
sum(qval$qvalue < 0.05)

