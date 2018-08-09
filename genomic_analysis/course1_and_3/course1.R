# this is a basic summary of how to answer the questions in course 1 and good practice on my end.
# week 2
# random variables
library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleControlsPopulation.csv"
filename <- basename(url)
download(url, destfile=filename)
x <- unlist( read.csv(filename) )

mean(x)

set.seed(1)
sampling <- sample(x, 5) 
sum(abs(mean(sampling)) - mean(x))

set.seed(5)
sampling <- sample(x, 5) 
sum(abs(mean(sampling)) - abs(mean(x)))

# null distributions
set.seed(1)
nulls <- vector('numeric', 1000)
for (i in 1:1000){
  nulls[i] <- mean(sample(x, 5))
}
mean(abs(nulls - mean(x)) > 1)

set.seed(1)
nulls <- vector('numeric', 10000)
for (i in 1:10000){
  nulls[i] <- mean(sample(x, 5))
}
mean(abs(nulls - mean(x)) > 1)


# normal distribution
library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/femaleControlsPopulation.csv"
filename <- basename(url)
download(url, destfile=filename)
x <- unlist( read.csv(filename) )

# populatino samples, and estimates exercises
library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/mice_pheno.csv"
filename <- basename(url)
download(url, destfile=filename)
dat <- read.csv(filename) 
dat <- na.omit( dat )

x <- filter(dat, Sex=="M" & Diet=="chow") %>% select(Bodyweight) %>% unlist
mean(x)

library(rafalib)
popsd(x)

set.seed(1)
X <- sample(x,25)
mean(X)

# CLT - central limit theorem 
library(downloader) 
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/mice_pheno.csv"
filename <- basename(url)
download(url, destfile=filename)
dat <- na.omit( read.csv(filename) )








