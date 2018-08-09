# week 2 
# error rates and procedures 
# website for this https://github.com/genomicsclass/labs/blob/master/advinference/multiple_testing.Rmd

alphas <- seq(0,0.25,0.01)
par(mfrow=c(2,2))
for(m in c(2,10,100,1000)){
  plot(alphas,alphas/m - (1-(1-alphas)^(1/m)),type="l")
  abline(h=0,col=2,lty=2)
}

# Bonferroni Correction Exercises 
set.seed(1) 
B=10000
cutoffs = 0.05 ##we know it has to be small
prob = sapply(cutoffs,function(cutoff){
  minpval =replicate(B, min(runif(8793,0,1))<=cutoff)
  mean(minpval>=1)
})
cutoffs[which.min(abs(prob-0.05))]

set.seed(1)
B <- 10000
m <- 8793
alpha <- 0.05
pvals <- matrix(runif(B*m,0,1),B,m)
k <- alpha/m
mistakes <- rowSums(pvals<k) 
mean(mistakes>0)


set.seed(1)
B <- 10000
m <- 8793
alpha <- 0.05
pvals <- matrix(runif(B*m,0,1),B,m)
k <- (1-(1-alpha)^(1/m))
mistakes <- rowSums(pvals<k) 
mean(mistakes>0)


library(rafalib)
library("devtools")
install_github("genomicsclass/GSE5859Subset")
install_bioc("genefilter")
install_bioc("qvalue")
library(genefilter)
library(qvalue)
library(GSE5859Subset)
data(GSE5859Subset)
load('/home/david/Documents/stats/GSE5859Subset.rda')
factors <- factor(sampleInfo)
sum(rowttests(geneExpression, g)$p.value < 0.05)

pval <- rowttests(geneExpression, g)$p.value
k <- 0.05 / length(pval)
sum(pval < k)

a <- p.adjust(pval, 'fdr')
sum(a < 0.05)

sum(qvalue(pval)$qvalues < 0.05)
qvalue(pval)$pi0

n <- 24
m <- 8793 
mat <- matrix(rnorm(n*m), m, n)

delta <- 2 
  positives <- 500
  mat[1:positives, 1:(n/2)] <- mat[1:positives, 1:(n/2)] + delta 
set.seed(1)

# statistical model exercises 
dbinom(2, size =4 , prob = .49) 
dbinom(4, size = 10, prob = .49) 
1 - pbinom(10, 20, 0.4) 

prob <- 1/175223510 # doing this on a calculator will give you the wrong prob just saying 
N <- 189000000 # the number of tickets sold
1 - pbinom(0, N, prob) # for at least one ticket that is sold that wins 
1 - pbinom(1, N, prob) # 2 or more tickets sold and won

pbinom(9,20,0.4) - pbinom(7,20,0.4) 

n <- 20 # the sample size 
p <- .40 # from both G and C
q <- 1 - p # not p == q
# http://www.statisticshowto.com/probability-and-statistics/binomial-theorem/normal-approximation-to-the-binomial/
u <- (n * p)
sd <- sqrt(u * q) 
a <- (9 - u) / sd # this is the continuity error rate 
# we want to find P(X ... n) like P(X > 35) or P(X < 45) - we want that percentage
b <- (7 - u) / sd 
pnorm(b) - pnorm(a)


1 - pbinom(10, 20, 0.4) 

exact = pbinom(450,1000,0.4)-pbinom(350,1000,0.4)
b <- (450 - 1000*.4)/sqrt(1000*.4*.6)
a <- (350 - 1000*.4)/sqrt(1000*.4*.6)
approx <- pnorm(b)-pnorm(a)
abs(exact-approx)

N <- 189000000
p <- 1/175223510
dbinom(2,N,p)

a <- (2+0.5 - N*p)/sqrt(N*p*(1-p))
b <- (2-0.5 - N*p)/sqrt(N*p*(1-p))
pnorm(a) - pnorm(b)

dpois(2,N*p)

1-ppois(1,N*p)

# maximum likelihood estimate (MLE)
library(devtools)
#install_github("genomicsclass/dagdata")
load("~/Downloads/hcmv.rda")
library(rafalib)
mypar()
plot(locations,rep(1,length(locations)),ylab="",yaxt="n")

breaks=seq(0,4000*round(max(locations)/4000),4000)
tmp=cut(locations,breaks)
counts=as.numeric(table(tmp))
hist(counts)

probs <- dpois(counts,4)
likelihood <- prod(probs)
likelihood

logprobs <- dpois(counts,4,log=TRUE)
loglikelihood <- sum(logprobs)
loglikelihood

lambdas = seq(0,15,len=300)

loglikelihood = function(lambda,x){
  sum(dpois(x,lambda,log=TRUE))
}
lambdas = seq(1,15,len=300)
l = sapply(lambdas,function(lambda) loglikelihood(lambda,counts))
plot(lambdas,l)
mle=lambdas[which.max(l)]
abline(v=mle)
print(mle)

breaks=seq(0,4000*round(max(locations)/4000),4000)
tmp=cut(locations,breaks)
counts=as.numeric(table(tmp))
binLocation=(breaks[-1]+breaks[-length(breaks)])/2
plot(binLocation,counts,type="l",xlab=)
max(counts)
binLocation[which.max(counts)]

lambda = mean(counts[ - which.max(counts) ])
pval = 1 - ppois(13,lambda)
print(pval)


0.05/57

