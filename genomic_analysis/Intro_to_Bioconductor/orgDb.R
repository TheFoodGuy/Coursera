library(org.Hs.eg.db)
keytypes(org.Hs.eg.db)

# how many genes are present on 17q21.1 
nrow(select(org.Hs.eg.db, keys="17q21.1", keytype="MAP", columns="SYMBOL"))

# select GO tags occurring among the five most common 
# annotations for geens on 17q21.1 
m17 = select(org.Hs.eg.db, keys="17q21.1", keytype="MAP", columns=c("SYMBOL", "GO"))
sort(table(m17$GO), decreasing=TRUE)[1:5]

# how many of the GO annotations for ORMDL3 have TAS as their 
# evidence code 
m17 = select(org.Hs.eg.db, keys="17q21.1", keytype="MAP", columns=c("SYMBOL", "GO"))
m17[m17$SYMBOL=="ORMDL3",]

library(Homo.sapiens)
g = genes(Homo.sapiens)
library(ERBS)
data(HepG2)


kp = g[resize(g,1) %over% HepG2]
kp
