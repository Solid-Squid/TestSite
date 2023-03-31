# Should read in the times (in minutes)
# For  swimming, cycling, and running
# Qualifying time for awards is 100 minutes
# calculate and display the total time taken to complete the triathlon
# Award a participant receives is based on the total time
# Display the award

# With 100 =                                Provincial Colours
# Within 5 minutes of qualifying time. =    Provincial Half Colours
# Within 10 minutes of qualifying time. =   Provincial Scroll
# More than 10 minutes of qualifying time. =No award

# How i planned it in my head



swim = input (
    "Please enter your Swimming event time in minutes: ")
cycle = input (
    "Please enter your Cyclying event time in minutes: ")
run = input (
    "Please enter your Running event time in minutes : ")

total = int(swim) + int(cycle) + int(run) 


# Fairly simple approach to the problem


if total >= 111 :               # checks to see if the input is too high
       print(
           "You do not qualify for an award, your time was " , int(total) , " minutes")     
elif total > 105 <= 110 :       # checks to see if the input is inbetween 105 -110
       print(
           "You have been awarded Provincial Scroll, your time was " , int(total) , " minutes" )     
elif total > 100 <= 105 :       # checks to see if the input is inbetween 100 -105
       print(
           "You have been awarded Provincial Half Colours, your time was " , int(total) , " minutes")  
elif total <= 100  :            # checks to see if the input is under 100
       print(
           "You have been awarded Provincial Colours, your time was " , int(total) , " minutes")
       
print ("Thank you")