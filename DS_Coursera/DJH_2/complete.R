# PART 2 
# this checks and returns the number of completed cases with the id name as wellsss
complete <- function(directory, id = 1:332){
  dir <- list.files(directory, full.names=TRUE)
  
  # reading each file in the dir()
  f_counter <- 1
  for(index in id){
    current_data <- read.csv(dir[index])
    counter <- 0
    for(pos in 2:length(current_data)){
      a <- is.na(current_data$Date[pos])
      b <- is.na(current_data$sulfate[pos])
      c <- is.na(current_data$nitrate[pos])
      d <- is.na(current_data$ID[pos])
      
      if(a == TRUE || b == TRUE || c == TRUE || d == TRUE){
        
      }else{
        counter = counter + 1
      }
    }
    print(paste(f_counter, index, counter, collapse = " "))
  }
}