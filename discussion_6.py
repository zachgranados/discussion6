import os
import unittest


class FireReader():
    """
    A class for reading data about fires.
    """
    def __init__(self, filename): # You should not need to modify this method.
        """
        The constructor. Opens up the specified file, reads in the data,
        closes the file handler, and sets up the data dictionary that will be
        populated with build_data_dict().

        We have implemented this for you. You should not need to modify it.
        """

        # this is used to get the base path that this Python file is in in an
        # OS agnostic way since Windows and Mac/Linux use different formats
        # for file paths, the os library allows us to write code that works
        # well on any operating system
        self.base_path = os.path.abspath(os.path.dirname(__file__))

        # join the base path with the passed filename
        self.full_path = os.path.join(self.base_path, filename)

        # open up the file handler
        self.file_obj = open(self.full_path, 'r')

        # read in each line of the file to a list
        self.raw_data = self.file_obj.readlines()

        # close the file handler
        self.file_obj.close()

        # set up the data dict that we will fill in later
        self.data_dict = {
            'month': [],
            'day': [],
            'temp': [],
            'RH': [],
            'area': []
        }

    def build_data_dict(self):
        """
        Reads all of the raw data from the CSV and builds a dictionary where
        each key is the name of a column in the CSV, and each value is a list
        containing the data for each row under that column heading.

        There may be a couple bugs in this that you will need to fix.
        Remember that the first row of a CSV contains all of the column names,
        and each value in a CSV is seperated by a comma.
        """

        # iterate through each row of the data

        
        for i in self.raw_data:
            
            # breaks the loop for the header
            if i.startswith('month'):
                continue

            # split up the row by comma
            seperated = i.split(',')

            # map each part of the row to the correct column
            self.data_dict['month'].append(seperated[0])
            self.data_dict['day'].append(seperated[1])
            self.data_dict['temp'].append(float(seperated[2]))
            self.data_dict['RH'].append(int(seperated[3]))
            self.data_dict['area'].append(float(seperated[4]))

    def smallest_fire(self):
        """
        This method should iterate through the area column and return
        the smallest value.

        """
        min = self.data_dict['area'][0]

        for areas in self.data_dict['area']:
            if areas < min:
                min = areas
        return min


       


    def most_fires_month(self):
        """
        This method should iterate through the month column, keep count of
        how many fires occured in each month (HINT: use a dictionary), and
        finally return a string in the following format:

        'The month with the most fires was dec.'

        You should replace 'dec' with the correct month.
        """

        pass

    def temp_of_smallest(self):
        """
        This method should find the smallest fire (smallest value in the
        area column), and return the temperature (temp column) for that same
        fire (same row in the csv).

        HINT: If you want to get the index for a specific value in a list, you
        can call list.index(value). In the real world, this will only return
        the FIRST index that matches your requested value, but for our purposes
        this is ok.
        """

        pass


class TestFireReader(unittest.TestCase): # You should not need to modify this class.
    """
    In the following class, we have provided several test cases to allow you
    to easily check your work. If you've done the assignment correctly, you do
    NOT need to modify the test cases.

    Hardcoding values from the test cases into your functions is NOT how you
    should complete this assignment.
    """
    def setUp(self):
        self.fire_reader = FireReader('forestfires.csv')
        self.fire_reader.build_data_dict()

    def test_build_data_dict(self):
        self.assertEqual(self.fire_reader.data_dict['RH'][0], 42)
        self.assertEqual(self.fire_reader.data_dict['area'][0], 0.36)
        self.assertEqual(self.fire_reader.data_dict['day'][0], 'tue')
        self.assertEqual(self.fire_reader.data_dict['month'][0], 'jul')
        self.assertEqual(self.fire_reader.data_dict['temp'][0], 18.0)

    def test_smallest_fire(self):
        self.assertEqual(self.fire_reader.smallest_fire(), 0.09)

    def test_most_fires_month(self):
        self.assertEqual(
            self.fire_reader.most_fires_month(),
            'The month with the most fires was aug.'
            )

    def test_temp_of_smallest(self):
        self.assertEqual(self.fire_reader.temp_of_smallest(), 25.7)


# standard main function to run the test cases
def main():
    unittest.main(verbosity=2)


# name guard to prevent main() from running if this script is imported
if __name__ == '__main__':
    main()
