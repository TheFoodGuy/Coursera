if (FALSE){ 
    " All of these programs are for quiz 1. "
}

# 1. find  how many properties are worth a certain amount + 
property <- function(worth){
    readFile <- read.csv("quiz1.csv")
    property_value <- table(na.omit(readFile$VAL))
    result <- property_value[names(property_value) == worth]
    result
}

# 3. can't do it because I don't know how to read xlsx files 
# 4. 