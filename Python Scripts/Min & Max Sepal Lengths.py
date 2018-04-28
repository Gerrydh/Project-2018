# Ger Hanlon, 02.04.2018
# This code returns the min and max value of the sepal lenghts, Column(0).
#https://stackoverflow.com/questions/46281738

with open("Iris data2.csv") as file: # open, then close the Iris Dataset file
    lines = file.read().split("\n")     #Read each line and split each line 

num_list = [] # only numbers
for line in lines: # reach each line by line
    try:
        item = line.split(",")[0] #Choose 1st column which is seperated by a comma
        num_list.append(float(item))    #Try to parse 
    except:
        pass  #If it can't parse, the string is not a number

print("The smallest Sepal Length is : ", min(num_list)) #Prints the minimum value
print("The tallest Sepal Length is : ", max(num_list)) # Prints the maximum value
