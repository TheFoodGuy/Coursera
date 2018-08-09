library(tissuesGeneExpression)
data(tissuesGeneExpression)

# what is the correlation between first u of svd and m? 
load("/home/david/Downloads/tissuesGeneExpression.rda")
s = svd(e) 
signflips = sample(c(-1,1), ncol(e), replace=TRUE)
signflips

newu= sweep(s$u,2,signflips,FUN="*")
newv= sweep(s$v,2,signflips,FUN="*" )
all.equal( s$u %*% diag(s$d) %*% t(s$v), newu %*% diag(s$d) %*% t(newv))
s = svd(e) 
m = rowMeans(e)
cor(s$u[,1], m)

#diag(s$d)%*%t(s$v) is the same as what? 
newmeans = rnorm(nrow(e)) ##random values we will add to create new means
newe = e+newmeans ##we change the means
sqrt(crossprod(e[,3]-e[,45]))
sqrt(crossprod(newe[,3]-newe[,45])) 
y = e - rowMeans(e)
s = svd(y)
resid = y - s$u %*% diag(s$d) %*% t(s$v)
max(abs(resid))

x=matrix(rep(c(1,2),each=5),5,2)
x

x*c(1:5)

# apprx distance using the two distances 1 3D and 1 2D 
z = s$d * t(s$v)

sqrt(crossprod(e[,3]-e[,45]))
sqrt(crossprod(y[,3]-y[,45]))
sqrt(crossprod(z[,3]-z[,45]))

realdistance = sqrt(crossprod(e[,3]-e[,45]))
approxdistance = sqrt(crossprod(z[1:2,3]-z[1:2,45]))
abs(realdistance - approxdistance)

# finding the min number of dim to get 10% SVG 
ks = 1:189
realdistance = sqrt(crossprod(e[,3]-e[,45]))
approxdistances = sapply(ks,function(k){
  sqrt(crossprod(z[1:k,3,drop=FALSE]-z[1:k,45,drop=FALSE] )) 
})
percentdiff = 100*abs(approxdistances - realdistance)/realdistance
plot(ks,percentdiff) ##take a look
min(ks[which(percentdiff < 10)])

approxdistances = sqrt(apply(z[1:2,-3]-z[1:2,3],2,crossprod))
plot(distances,approxdistances) ##take a look
cor(distances,approxdistances,method="spearman")
