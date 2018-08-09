load("/home/dcom/Downloads/admissions.rda")
admissions
library(GSE5859)
library(devtools)
install_github("genomicsclass/GSE5859")

#1 the number of women that were accepted or proportion
index = which(admissions$Gender==0)
accepted= sum(admissions$Number[index] * admissions$Percent[index]/100)
applied = sum(admissions$Number[index])
accepted/applied

#2 what is the pvalue if you perform an independence test
admissions
genderTable <- as.data.frame(matrix(0,2,2))
rownames(genderTable) <- c("Men", "Women")
colnames(genderTable) <- c("Accepted", "Rejected")
index = admissions$Gender==1
men = admissions[index,]
women = admissions[!index,]

genderTable[1,1] <- sum(men$Number * men$Percent / 100)
genderTable[1,2] <- sum(men$Number * (1 - men$Percent / 100))
genderTable[2,1] <- sum(women$Number * women$Percent / 100)
genderTable[2,2] <- sum(women$Number * (1 - women$Percent / 100))
genderTable
chisq.test(genderTable)$p.value
print( data.frame( major=admissions[1:6,1],men=men[,3], women=women[,3]) )

#3 what proportion gets in for the major from confounding exercise 3? 
#4 what is the letter
admissions
major = admissions[1:6,1]
men = admissions[1:6,]
women =admissions[7:12,]
H = (men$Number*men$Percent/100 + women$Number*women$Percent/100) / (men$Number+women$Number)
H
major[which.min(H)]
min(H)

#5 / #6
sum(admissions$Number)
cor(admissions$Number, H)
cor(men$Number, H)
cor(women$Number, H)
