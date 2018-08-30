library(BiocInstaller)
biocLite("BSgenome.Hsapiens.UCSC.hg19")
library(BSgenome.Hsapiens.UCSC.hg19)

chr11seq <- BSgenome.Hsapiens.UCSC.hg19[["chr11"]]
subseq(chr11seq,start=10^6,width=25)

# countPattern(c("ATG", "TGA", "TAA", "TAG"), chr11seq)
countingPat <- function(d){
  return ( countPattern(d, chr11seq))
}

sort(sapply(c("ATG", "TGA", "TAA", "TAG"), countingPat))

# 2 create a function alphabetFrequency and determine the percentage of chr 7 
# is T,C, B, and A 
# what is the proportion are Cs
chr7seq <- BSgenome.Hsapiens.UCSC.hg19[["chr7"]]
alphabetFrequencyFunc <- function(){
  alpha <- alphabetFrequency(chr7seq, as.prob=FALSE)
  alpha
}

result <- alphabetFrequencyFunc()
result['C'] / sum(result)


#3 locations of SNPs in humans
if (!("SNPlocs.Hsapiens.dbSNP144.GRCh37" %in% rownames(installed.packages()))) {
  library(BiocInstaller)
  biocLite("SNPlocs.Hsapiens.dbSNP144.GRCh37")
}
library(SNPlocs.Hsapiens.dbSNP144.GRCh37)
snps144 = SNPlocs.Hsapiens.dbSNP144.GRCh37
s17 = snpsBySeqname(snps144, "17")
head(s17)
s17[s17$RefSNP_id == 'rs73971683']$pos
s17[which(s17$RefSNP_id=="rs73971683")]

#4 linking SNP genotypes to disease risk 

library(gwascat)
data(ebicat37)
ebicat37

# to find the chrm with largest number of verified hits
sort(table(ebicat37$CHR_ID),decreasing=TRUE)

sort(table(mcols(ebicat37)[,"DISEASE/TRAIT"]), decreasing=TRUE)[1:10] 

