library(GSE5859Subset)
data(GSE5859Subset)
library(qvalue)
library(genefilter)

sex = sampleInfo$group
month = factor( format(sampleInfo$date,"%m"))
table( sampleInfo$group, month)
ttxt <- rowttests(geneExpression, sex)
pval <- ttxt$p.val
qval <- qvalue(pval)

sum(qval$qvalues < 0.1)

#2 
sexchr <- geneAnnotation$CHR[qval$qvalues < 0.1]

mean(sexchr == "chrX" | sexchr == "chrY")

#3 
filter <- geneAnnotation[geneAnnotation$CHR != "chrX" & geneAnnotation$CHR != "chrY" & qval$qvalues < 0.1, ]

autosomal <- geneExpression[filter$PROBEID,]

month = factor( format(sampleInfo$date,"%m"))

ttxt2 <- rowttests(autosomal, month)

mean(ttxt2$p.val < 0.05)

#4 
pvals <- vector()
for(i in 1:nrow(geneExpression)){
  X = model.matrix( ~ sex + month)
  y = geneExpression[i,]
  fit = lm( y ~ X - 1)
  sa <- summary(fit)
  pvals[i] <- sa$coefficients[2,4]
}

qvals <- qvalue(pvals)
sum(qvals$qvalues < 0.1)

#6 
chr <- geneAnnotation$CHR[qvals$qvalues < 0.1]

mean(chr == "chrX" | chr == "chrY")

#7 

Mpvals <- vector()
for(i in 1:nrow(geneExpression)){
  X = model.matrix(~ sex + month)
  y = geneExpression[i,]
  fit = lm(y ~ X - 1 )
  sa <- summary(fit)
  Mpvals[i] <- sa$coefficients[3, 4]
  
}

Mqvals <- qvalue(Mpvals)
sum(Mqvals$qvalues < 0.1)
