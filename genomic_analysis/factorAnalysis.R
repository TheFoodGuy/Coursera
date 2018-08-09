library(RColorBrewer)
library(rafalib)
mypar(1,2)
n=ncol(y)
cors=cor(y)
cols=colorRampPalette(rev(brewer.pal(11,"RdBu")))(100)
image(1:n,1:n,cors,xaxt="n",yaxt="n",col=cols,xlab="",ylab="",zlim=c(-1,1))

o <- order(sampleInfo$date)
yo<-y[,o]
cors=cor(yo)
cols=colorRampPalette(rev(brewer.pal(11,"RdBu")))(100)
image(1:n,1:n,cors,xaxt="n",yaxt="n",col=cols,xlab="",ylab="",zlim=c(-1,1))
