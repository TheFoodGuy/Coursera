# this is for week 2 of course 2 from harvard stats or biostats

# find the fitted values of each rownames
X <- matrix(c(1,1,1,1,0,0,1,1), nrow=4)
rownames(X) <- c("a", "a", "b", "b")
beta <- c(5,2)

fitted <- X %*% beta
fitted[1:2,]
fitted[3:4,]

X <- matrix(c(1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,0,1,1),nrow=6)
rownames(X) <- c("a","a","b","b","c","c")
beta <- c(10, 3, -3)

fitted <- X %*% beta 
fitted[1:2, ]
fitted[3:4, ]
fitted[5:6, ]

# Inference Reviews
set.seed(1)
g <- 9.8 ## meters per second
h0 <- 56.67
v0 <- 0
n <- 25
tt <- seq(0,3.4,len=n) ##time in secs, t is a base function
X <- cbind(1, tt, tt^2)
A <- solve(crossprod(X), t(X))
random <- replicate(100000, {  
  y <- h0 + v0*tt - 0.5*g*tt^2 + rnorm(n,sd=1)
  beta <- -2 * (A %*% y)
  return(beta[3])
})
# using monte carlo simulations 
sd(random)

#3 monte carlo simultaions
library(UsingR)
x = father.son$fheight
y = father.son$sheight
n = length(y)

betahat <- replicate(10000, {
  index <- sample(n, 50)
  sampledat <- father.son[index,]
  x <- sampledat$fheight
  y <- sampledat$sheight
  return(lm(y ~ x)$coef[2])
})
sd(betahat)
mean( (y - mean(y))*(x-mean(x) ) )

# standard error exercises 
library(UsingR)

x = father.son$fheight
y = father.son$sheight
n = length(y)
N = 50
set.seed(1)
index = sample(n,N)

sampledat = father.son[index,]
x = sampledat$fheight
y = sampledat$sheight

betahat = lm(y~x)$coef

fit = lm(y ~ x)
fit$fitted.values
r <- vector("numeric", length(fit$fitted.values))
for (i in 1:length(fit$fitted.values) ){
  r[i] <- (y[i] - mean(fit$fitted.values[i]))^2
}
sum(r)

# other correct answer 
fit = lm(y ~ x)
sum((y - fit$fitted.values)^2)

#2 calculate the inverse of X transpose times X 

X = cbind(rep(1, N), x)
solve(t(X) %*% X)[1,1]
diag(solve(t(X) %*% X)[1,1])
