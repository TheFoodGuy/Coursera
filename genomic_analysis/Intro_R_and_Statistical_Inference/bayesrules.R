# this is bayes rules in practice
tmpfile <- tempfile()
tmpdir <- tempdir()
download.file("http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip",tmpfile)
##this shows us files
filenames <- unzip(tmpfile,list=TRUE)
players <- read.csv(unzip(tmpfile,files="Batting.csv",exdir=tmpdir),as.is=TRUE)
unlink(tmpdir)
file.remove(tmpfile)

library(dplyr)
a <- filter(players,yearID==2012) %>% mutate(AVG=H/AB) %>% filter(AB>=500) %>% select(AVG) %>% na.omit()   
b <- filter(players,yearID==2011) %>% mutate(AVG=H/AB) %>% filter(AB>=500) %>% select(AVG) %>% na.omit()   
c <- filter(players,yearID==2010) %>% mutate(AVG=H/AB) %>% filter(AB>=500) %>% select(AVG) %>% na.omit()   
mean(c(a$AVG, b$AVG, c$AVG))

dat <- filter(players,yearID>=2010, yearID <=2012) %>% mutate(AVG=H/AB) %>% filter(AB>500) %>% select(AVG)

mean(dat$AVG)  
sd(dat$AVG)
hist(dat$AVG,nc=100,freq=FALSE)

mypar(1,1)
#check
qqnorm(dat$AVG)
qqline(dat$AVG)


library(rafalib)
install_bioc("SpikeInSubset")
library(Biobase)
library(SpikeInSubset)
data(rma95)
y <- exprs(rma95)
g <- factor(rep(0:1,each=3))
spike <- rownames(y) %in% colnames(pData(rma95))


library(limma)
fit = lmFit(y, design=model.matrix(~ g))
fit = eBayes(fit)
##second coefficient relates to diffences between group
pvals = fit$p.value[,2] 

