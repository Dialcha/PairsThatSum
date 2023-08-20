# PAIRS THAT SUM

This program finds pairs of integers from a list that sum to a given value. The function take as input the list of numbers as well as the target sum.

The program reads line by line a file located in the data folder, each line has the following format **1,9,5,0,20,-4,12,16,7 12** where the first numbers are separated only by a comma, these are represented in a list. The number after the space is the target value.

The output of the program is given in the following format : *"For array [1, 9, 5, 0, 20, -4, 12, 16, 7] and target value 12, pairs are: [(12, 0), (16, -4), (7, 5)]"*

## Project structure

- In the "src" folder there is a file called _app.py_ which reads a .txt file with the program input and executes the pairs_that_sum function. In this same folder is a folder called pairs, which contains a file called _pairs.py_, this contains the logic of the problem domain that solves the problem posed.
- In the "data" folder is the file *pairs.txt* which is read by app.py and contains the program inputs. Feel free to modify this file with the desired inputs to test the program.
- In the "tests" folder is the file _test_pairs.py_ which contains the unit tests for the _pairs_that_sum_ function.

## Steps to run the program

The software is written in **python** and uses pytest for unit testing.

1. Clone this repo
2. Create a virtual environment to manage dependencies. You can use *virtualenv* for this, first make sure you have Python and virtualenv installed on your computer and then you can run the following command:
   `python -m virtualenv venv`
3. Activate the virtual environment, in linux you can use the following command: `source venv/bin/activate`
   and on windows the following: `.\venv\Scripts\activate`
4. Install requirements with `pip install -r requirements.txt`
5. You can run the program with the following command: `python3 src/app.py`
6. You can run the unit tests with the following command: `pytest`