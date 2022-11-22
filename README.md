# Table of content
* [General info](#general-info)
* [How to run the tests](#how-to-run-the-tests)
* [Structure of the Framework](#structure-of-the-framework)
* [Before commit](#before-commit)

# General info
This is test framework created during Talent Engine 2.0

# How to run the tests
Install required packages with command:
'''
pip install -r requirements.txt
'''
Run the test from the root folder with the command:
'''
pytest
'''

# Structure of the Framework
src/config - contains configuration of the framework
src/data - contains data of the framework
src/models - contains framework's models
src/providers - contains providers for the framework
tests/ - localization of the tests to run

# Before commit
Please do commands below before commit
run isort .
run black .
