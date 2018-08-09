y = e - rowMeans(e)
s = svd(y)
z = s$d * t(s$v)

library(rafalib)
ftissue = factor(tissue)
mypar(1,1)
plot(z[1,],z[2,],col=as.numeric(ftissue))
legend("topleft",levels(ftissue),col=seq_along(ftissue),pch=1)

d = dist(t(e))
mds = cmdscale(d)
cor(z[1,], mds[,1])
