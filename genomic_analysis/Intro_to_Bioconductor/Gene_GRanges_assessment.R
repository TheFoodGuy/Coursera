library(Homo.sapiens)
ghs = genes(Homo.sapiens)
# what genome build was used here
# how many genes are represented in ghs
hg19
23056

# what is the chromosome with the most gene 
which.max(table(seqnames(ghs)))


#what best describe the width of genes
hist(width(ghs))
# what is the median gene width
median(width(ghs))
