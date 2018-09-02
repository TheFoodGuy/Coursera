library(IRanges)

# 1 define an integer range starting at 101 and ending at 200
ir1 <- IRanges(101, 200) * 2 

# 2 define an integer range starting at 101 and ending at 200
# using the operation narrow(x, start = 20) what is the new 
# starting point? 

ir2 <- IRanges(101, 200) 
narrow(ir2, start = 20) 

# 3 same start and end, use operation +25, what is the width of the 
# resulting range? 
ir3 <- IRanges(101, 200) 
ir3 + 25

# 4 define start = 1,11,21 and ends at 3,15,27
# what is the sum of the widths of all the ranges
ir4 <- IRanges(start = c(1,11,21), end = c(3,15,27))
sum(width(ir4))

# 5 what is the total width from 101 to 510 which is not covered by ranges 
# in x? 
start = c(101,106,201,211,221,301,306,311,351,361,401,411,501)
end = c( 150,160,210,270,225,310,310,330,390,380,415,470,510)
ir5 <- IRanges(start=start, end=end) 
# downloading the plotting ranges 
devtools::install_github("genomicsclass/ph525x")
library(ph525x)
plotRanges(ir5)
sum(width(ir5)) # not the answer 
sum(width(gaps(ir5)))


#6 how many disjoin ranges are contained within the ranges in 'x'
# from the previous question 
length(disjoin(ir5))
disjoin(ir5)

#7 
par(mfrow=c(2,1))
plotRanges(ir5)
plotRanges(resize(ir5, 1))
