library(rtracklayer)
data(targets)
class(targets)


# what is the reference build of the chromosome? 
# cannot be determined 

# how can metadata about the data origin and 
# reference build be encoded in the bed export 
library(GenomicRanges)
mtar = with(targets,
            GRanges(chrom, IRanges(start,end), strand=strand,
                    targets=target, mirname=name))
cat(export(mtar[1:5], format="bed"), sep="\n")
cat("\n")
cat(export(mtar[1:5], format="gff3"), sep="\n")

# how many entries address CTCF binding in HepG2 
library(AnnotationHub)
ah = AnnotationHub()
mah = mcols(ah)
names(mah)
sort(table(mah$species), decreasing=TRUE)[1:10]


names(query(query(ah, "HepG2"), "CTCF"))

