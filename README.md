# SatelliteDataProcessing
This is a python program which makes use of satellite utility to refine the data gathered at centre and perform required action as given in the file.

attached: python file for program and text flat file for data.


In this project, we have to write a utility for people at INDIAN SPACE RESEARCH ORGANISATION (ISRO)

They have a ton of data received from different India satellites moving in orbit. Each satellite sends a large number of observations about various sensors periodically. A received at the ISRO stations, located not much far from our campus, receives these observations and stores them in a flat-file. Due to the large data volume, all data stored in a single file.

Unfortunately, due to a bug in the receiving utility, all irrelevant data is also stored. Now, they are looking for a utility to achieve two goals:

1. to separate data for each satellite,

2: to store only relevant data

The team has a large number of files for which utility should work. Due to this, the utility should be simple and

optimized

Presently, utility is storing the data in the following format:

SAD

Each row in the file contains three values separated by a space: S, A, and D. Sis the satellite number for which data received, and A identifies the action. There are two kinds of actions that can be performed on the data:: Insert and D: delete. D is the actual data that should be stored or deleted for a specific satellite.

For example, the following data shows that we have two satellites: 1 and 2. In the first line, we have to insert/store 5 for satellite 1, and in the second line, we have to insert/store 4 for satellite 2. The last line is asking to delete data for satellite 1. For delete the value can be 0 or 1:0 to remove the oldest value received for the satellite and 1 to remove the latest value received for the satellite. In this example, we have to delete the oldest value received for satellite 1. In the next line, we have to delete the latest value received for satellite 2

1 1 5
2 1 4
1 1 10
I D O 
2 D 1

The architecture of the utility decided to use List ADT to store this data. The utility will create a separate instance of List for each satellite. The SUPARCO has five satellites, but we don't have prior information about the number of observations store in the file for each satellite. Therefore, the utility should create a new instance whenever new satellite data appears in the file.

