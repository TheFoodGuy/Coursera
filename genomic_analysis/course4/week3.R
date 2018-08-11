# week 3 because the homeworks seem to be short and imma fit them all here
# clustering exercises
set.seed(1)
m = 10000
n = 24
x = matrix(rnorm(m*n),m,n)
colnames(x)=1:n
hclust(t(x))

d <- dist(t(x))
hc <- hclust(d)
plot(hc, cex=1)

# 2 
library(rafalib)
set.seed(1)
finding_error <- replicate(100, {
  m = 10000
  n = 24
  x = matrix(rnorm(m*n),m,n)
  d <- dist(t(x)) 
  hc <- hclust(d) 
  length(unique(cutree(hc,h=143)))
})
plot(table(finding_error))
popsd(finding_error)

# kmeans exercise
load("/home/david/Downloads/GSE5859Subset.rda")
set.seed(10)
mds = cmdscale(dist(t(geneExpression)))
set.seed(10)
result=kmeans(t(geneExpression),5)
plot(mds, bg=result$cl, pch=21)

# heat map exercises
#1 Use heatmap.2 to make a heatmap showing the sampleInfo$group
# with color, the date as labels, the rows labelled with chromosome, and scaling the rows.
library(rafalib)
library(gplots)
library(matrixStats)
library(RColorBrewer)
##make colors
cols = colorRampPalette(rev(brewer.pal(11,"RdBu")))(25)
gcol=brewer.pal(3,"Dark2")
gcol=gcol[sampleInfo$g+1]

##make lables: remove 2005 since it's common to all
labcol= gsub("2005-","",sampleInfo$date)  

##pick highly variable genes:
sds =rowMads(geneExpression)
ind = order(sds,decreasing=TRUE)[1:25]

## make heatmap
heatmap.2(geneExpression[ind,],
          col=cols,
          trace="none",
          scale="row",
          labRow=geneAnnotation$CHR[ind],
          labCol=labcol,
          ColSideColors=gcol,
          key=FALSE)
