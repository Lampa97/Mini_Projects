# Mini_Projects
This is a repository for practicing in deep Python knowledge and mini projects


## Project 2: Description
The starting point for this project is the Polygon class and the Polygons sequence type we created in the previous project.

The code for these classes along with the unit tests for the Polygon class are below if you want to use those as your starting point. But use whatever you came up with in the last project.

We have two goals:

Goal 1
Refactor the Polygon class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our Polygon class "immutable").

Goal 2
Refactor the Polygons (sequence) type, into an iterable. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable, and an iterator.


## Project 3: Description

For this project you are given a file that contains some parking ticket violations for NYC.

(It's just a tiny extract!)

If you're wondering where I get these data sets, Kaggle is an excellent source of data sets in a whole variety of topics: https://www.kaggle.com/

You have to sign up, but it's free.

If you want the full data set, it's available here: https://www.kaggle.com/new-york-city/nyc-parking-tickets/version/2#

For this sample data set, the file is named:

nyc_parking_tickets_extract.csv
Your goals are as follows:

Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

Goal 2
Calculate the number of violations by car make.

Note:
Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.