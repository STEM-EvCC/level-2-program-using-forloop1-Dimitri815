mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
mission_before_2000 = [] #Initializes a empty list for ALL of the missions conducted BEFORE the YEAR 2000.

#Initializes IMPORTANT VALUES for the rest of the program
year_threshold = 2000
index = 0
total_num_of_missions = 0
successful_num_of_missions = 0

for names in mission_names: #Cycles through the data in mission_names
    total_num_of_missions += 1 #Every cycle adds 1 to the total counter of missions

#This checks if the Indexed Value in the mission_years list to see if it's < 2000 (year_threshold)
    if mission_years[index] < year_threshold: mission_before_2000.append(names) #If True, appends the name of the mission to the mission_before_2000 list

#This checks if the Indexed Value in the mission_success list to see if it's True
    if mission_success[index] is True: successful_num_of_missions += 1 #If True, increments successful_num_of_missions by 1

    index += 1
    #End of the For Loop, increment index by 1

#The only reason why this is Initialized here is due to the fact it'll do the calculation (It'd do this: (0 / 0) * 100; NOT GOOD), when the program hasn't calculated the values.
success_rate = (successful_num_of_missions / total_num_of_missions) * 100

#Prints the stats EXACTLY how the Assignment is telling me to
print(f"Total number of Missions: {total_num_of_missions}")
print(f"Number of Successful Missions: {successful_num_of_missions}")
print(f"Success Rate: {success_rate:.2f}%")
print(f"Missions before the year {year_threshold}")

for name in mission_before_2000:
    print(f"- {name}")