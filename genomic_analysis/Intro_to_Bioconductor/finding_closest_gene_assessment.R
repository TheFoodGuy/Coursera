# week 3 part 4 of the first content 

# what can we tell about erbs and erbs2?
res = findOverlaps(HepG2,GM12878)
erbs = HepG2[queryHits(res)]
erbs = granges(erbs)
erbs2= intersect(HepG2,GM12878)

# what is the TSS of the gene ID: 100113402
library(Homo.sapiens)
ghs = genes(Homo.sapiens)
tssgr = resize(ghs,1)
start(tssgr["100113402"])

# what is the GENEID of the gene with TSS closest to the 4th region of erbs
library(ERBS)
data(HepG2)
data(GM12878)
res = findOverlaps(HepG2,GM12878)
erbs = HepG2[queryHits(res)]
erbs = granges(erbs)
res = findOverlaps(erbs[4],tssgr)
res = tssgr[subjectHits(res)]
res

# using select function
key = as.character(mcols(tssgr)$GENEID[i])
# columns(Homo.sapiens) would give us the list of names of columns in the Homo.sapiens
select(Homo.sapiens, keys = key, columns = c("SYMBOL", "GENENAME"), keytype = "GENEID")

