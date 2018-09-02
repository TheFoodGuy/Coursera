# week 1 of linear algebra course 2

install.packages("UsingR")
  library(UsingR)
data("father.son", package="UsingR")
# find son's mean height
mean(father.son$sheight)
sonsHeight <- vector("numeric", length(father.son$sheight))
# finding the son's mean height based if father's height is 71
mean(father.son$sheight[which( round(father.son$fheight) == 71)])

# introduction to matrix algebra 
# matrix notation
c(1,5,3,4)
rnorm(10) # creating 10 values
X <- matrix(1:1000, 100, 10)
X[25,3]

# creating a 10 x 5 matrix, first column x = 1:10, then 2*x ... n * x for the next 4
X <- cbind(1:10, 2*1:10, 3*1:10, 4*1:10, 5*1:10)
sum(X[7,])

# solving 4 equations using R for C or [3]  
a <- rbind(c(3, 4, -5, 1),
           c(2,2,2,-1),
           c(1,-1,5,-5),
           c(5,0,0,1))
b <- c(10, 5, 7, 4)
solve(a,b)[3]

# what is the value in the 3rd row and the 2nd column of the matrix product? 
a <- matrix(1:12, nrow = 4)
b <- matrix(1:15, nrow = 3) 

(a %*% b)[3,2]
sum(a[3,] * b[,2])

