library(hgu133plus2.db)
# how many probe sets are mapped to EGFR
select(hgu133plus2.db, keys="EGFR", columns="PROBEID", keytype="SYMBOL")

# Use hgu133plus2.db to determine how many probe sets are annotated to this biological process.
library(GO.db)
select(GO.db, key = "lial cell proliferation", columns="PROBEID", keytype="SYMBOL")
select(GO.db, keys="glial cell proliferation", keytype="TERM", columns="GOID")

select(hgu133plus2.db, keys="GO:0014009", columns=c("PROBEID", "SYMBOL"), keytype="GO")

