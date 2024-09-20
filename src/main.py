# ---- IMPORT SECTION ---- #
from clear_console import *
from data import load_data
from handle_missing_data import handle_missing_values

# ---- IMPORT SECTION ---- #

# ---- MAIN CODE SECTION ---- #
"""Machine learning model to predict the potential purchase of a car of a person, using 
the dataset as source input.

Import and processing DataSet.
"""


def main():
    clear()
    matrix_features_independent, vector_features_dependent, has_nan = load_data.load_data()

    print("Matrix Features Independent:", end='\n')
    print(matrix_features_independent)

    print('\n')
    print("Vector Features Dependent:", end='\n')
    print(vector_features_dependent)

    if has_nan:
        print('\n')
        print("There is/are missing value", end='\n')
        matrix_features_independent = handle_missing_values(matrix_features_independent)

        print('\n')
        print("New Dataset without data missing", end='\n')
        print(matrix_features_independent)


# ---- MAIN CODE SECTION ---- #


# __name__ is a special built-in variable that exists in every module (a module is simply a Python file).
# __main__ is a string that Python assigns to the __name__ variable when the module is executed as the main program.
# It serves as an entry point for the script execution.
# The if __name__ == "__main__": condition checks whether the script is being run directly or being imported.
# Code inside this if block will only execute if the script is run directly not when it is imported.
if __name__ == '__main__':
    main()
