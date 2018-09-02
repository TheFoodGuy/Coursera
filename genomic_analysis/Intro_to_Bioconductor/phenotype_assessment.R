# Phenotypes Assessment 

#` Install and attach COPDSexualDimorphism.data package using biocLite 
library(COPDSexualDimorphism.data)
data(lgrc.expr.meta)

#1 counting the number of females in the study
sum(expr.meta$GENDER == '2-Female')

#2 the median of the distribution of pack years smoked in this cohort 
median(expr.meta$pkyrs)
# or 
summary(expr.meta$pkyrs)

#3 is pkyrs well-approximated by a normal probability distribution
qqnorm(expr.meta$pkyrs)

# 4 MC or multiple choice question here
boxplot(pkyrs~gender, data=expr.meta)

# 5 
expr.meta$pyp1 = expr.meta$pkyrs+1