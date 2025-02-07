# Homework02 Writeup

The objective of this homework was to implement the new code organization, documentation, and testing practices that were taught in class. This inculdes including typehints, docstrings, utilizing a main function, and using pytest to perform unit testing. In this folder there are two script files and two test files. It is important to follow the practices taught in class so that code can be easily understood by other developers, preventing the software application from crashing all together as a result of a minute error, and allows for smoother execution of software. 

The data used for this project is NASA meteorite landings data which includes information on all known meteorite landings and can be found here: https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/about_data. The API endpoint was found under the actions button on the top right. This link was then used in conjunction with the wget command to enable the code to access the data.

The first python file is primary.py and this file contains three functions which parse through the inputted data and print out summary statsitics. The first function indicates if the numerical data in a specific column is valid/processable. The second function outputs the years the three most meteorite landings. The last function uses a function imported from the next file and determines how far apart two meteorite landings were. 

The second python file is gcd_algorithm.py and it contains a function that finds the distance between two points on a sphere using the great circle distance algorithm. This file only contains the function and the function is imported into the primary.py file and is used in one of the functions as explained above. 

The third python file is a test_primary.py file and it uses the pytest library to aid in testing the functionality of the functions within the primary.py file. Various different inputs are tested to make sure the code still works as expected. All tests were passed. This file does not test the great circle distance function, it only tests the other two.

The fourth python file is test_gcd_algorithm.py and it uses the pytest library to test the functionality of the great circle distance function. Various different inputs are tested to make sure the code still works as expected. All tests were passed. 

To interpret the results, it is important to understand the raw data. The first function considers numerical data to be invalid if there is an emtpy string or if there is non-numerical data. The top three years function looks at the date column in the meteorite landings data sheet and mainpulates the data and presents the years with the three most meteorite landings as well as the count of how many occured in the respective year. The function outputs two lists and the respective indexes are related to each other. For example, the year with the most meteorite landings will be in the first index of the first list and the number of times a meteor landed during that year will be in the first index of the second list. The distance returned by the last function is in units of kilometers. 

  

