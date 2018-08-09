
# didn't see the second part of week 3 so this is the second part here
# conditional expectation exercises here
n = 1000
y = rbinom(n,1,0.25)
##proportion of ones Pr(Y)
sum(y==1)/length(y)
##expectaion of Y
mean(y)

#1 exercise
n = 10000
set.seed(1)
men = rnorm(n,176,7) #height in centimeters
women = rnorm(n,162,7) #height in centimeters
y = c(rep(0,n),rep(1,n))
x = round(c(men,women))
##mix it up
ind = sample(seq(along=y))
y = y[ind]
x = x[ind]

mean(y[x==176])
#2 
xs = seq(160,178)
pr = sapply(xs, function(x0) mean(y[x==x0]))
plot(xs, pr)
abline(h = 0.5)
abline(v = 168)

# smoothing 
#1 
n = 10000
set.seed(1)
men = rnorm(n,176,7) #height in centimeters
women = rnorm(n,162,7) #height in centimeters
y = c(rep(0,n),rep(1,n))
x = round(c(men,women))
##mix it up
ind = sample(seq(along=y))
y = y[ind]
x = x[ind]

set.seed(5)
N = 250
ind = sample(length(y),N)
Y = y[ind]
X = x[ind]
predict(loess(Y~X), newdata=data.frame(X=168))

#2 
set.seed(5)
value <- replicate(1000, {
  N = 250
  ind = sample(length(y),N)
  Y = y[ind]
  X = x[ind]
  predict(loess(Y~X), newdata=data.frame(X=168))
})
library(rafalib)
popsd(value) 

#kNN and Cross Validation 
#1 

load("/home/david/Downloads/GSE5859Subset.rda")
y = factor(sampleInfo$group)
X = t(geneExpression)
out = which(geneAnnotation$CHR%in%c("chrX","chrY"))
X = X[,-out]
library(caret)

set.seed(1) 
idx = createFolds(y,k=10 )
idx[[3]][2] 