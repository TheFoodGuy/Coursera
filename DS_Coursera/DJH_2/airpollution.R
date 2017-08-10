# this is the first programming assignment in R

# "directory" is a character vector of length 1 indicating the location
# of the CSV file
# "pollutant" is a character vector of length 1 of either sulfate or nitrate 
# "id" is an integer vector indicating the monitor ID numbers to be used
# RETURNS the mean of the pollutant across all monitors list in the id vector

pollutantmean <- function(directory, pollutant, id){
  filenames <- list.files("specdata", full.names=TRUE)[id]
  mean_value <- 0
  accum_dom <- 0
  accum_value <- 0
  # looping through the directory and all of csv files.
  for(index in filenames){
    current_data <- read.csv(index) # getting each file here
    current_value <- mean(current_data[[pollutant]], na.rm = TRUE) # 3.880701
    accum_dom <- accum_dom + sum(!is.na(current_data[[pollutant]])) # sum(117, 1041, 243)
    accum_value <- accum_value + (current_value * sum(!is.na(current_data[[pollutant]]))) # 3.880701 * 117
  }
  mean_value <- accum_value / accum_dom
  return(mean_value)
}
