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

### Project 4: Description

For this project you have 4 files containing information about persons.

The files are:

personal_info.csv - personal information such as name, gender, etc. (one row per person)
vehicles.csv - what vehicle people own (one row per person)
employment.csv - where a person is employed (one row per person)
update_status.csv - when the person's data was created and last updated
Each file contains a key, SSN, which uniquely identifies a person.

This key is present in all four files.

You are guaranteed that the same SSN value is present in every file, and that it only appears once per file.

In addition, the files are all sorted by SSN, i.e. the SSN values appear in the same order in each file.

Goal 1
Your first task is to create iterators for each of the four files that contained cleaned up data, of the correct type (e.g. string, int, date, etc), and represented by a named tuple.

For now these four iterators are just separate, independent iterators.

Goal 2
Create a single iterable that combines all the columns from all the iterators.

The iterable should yield named tuples containing all the columns. Make sure that the SSN's across the files match!

All the files are guaranteed to be in SSN sort order, and every SSN is unique, and every SSN appears in every file.

Make sure the SSN is not repeated 4 times - one time per row is enough!

Goal 3
Next, you want to identify any stale records, where stale simply means the record has not been updated since 3/1/2017 (e.g. last update date < 3/1/2017). Create an iterator that only contains current records (i.e. not stale) based on the last_updated field from the status_update file.

Goal 4
Find the largest group of car makes for each gender.

Possibly more than one such group per gender exists (equal sizes).

You will not be able to use a simple split approach here, as I explain in the video.

Instead you should use the csv module and the reader function.

Here's a simple example of how to use it - you will need to expand on this for your project goals, but this is a good starting point.

import csv

def read_file(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows

from itertools import islice

rows = read_file('personal_info.csv')
for row in islice(rows, 5):
    print(row)

['ssn', 'first_name', 'last_name', 'gender', 'language']
['100-53-9824', 'Sebastiano', 'Tester', 'Male', 'Icelandic']
['101-71-4702', 'Cayla', 'MacDonagh', 'Female', 'Lao']
['101-84-0356', 'Nomi', 'Lipprose', 'Female', 'Yiddish']
['104-22-0928', 'Justinian', 'Kunzelmann', 'Male', 'Dhivehi']


As you can see, the data is already separated into a list containing the individual fields - but of course they are all just strings.