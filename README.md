# Table of content
* [General info](#general-info)
* [How to run the tests](#how-to-run-the-tests)
* [Structure of the Framework](#structure-of-the-framework)
* [Before commit](#before-commit)

# General info
This is test framework created during Talent Engine 2.0

# How to run the tests
Install required packages with command:<br>
pip install -r requirements.txt<br>
Run the test from the root folder with the command:<br>
pytest -v -s --browser=BROWSER_NAME<br>
optional commands:<br>
-v - verbose, traces all import statements<br>
-s - prints what's in test<br>
--browser=BROWSER_NAME - browser name can be replaces with available browser, default is Chrome

# Structure of the Framework
envs_config - localization of json and secrets used in config<br>
src/applications - contains application of the framework<br>
src/config - contains configuration of the framework<br>
src/data - contains data of the framework<br>
src/models - contains framework's models<br>
src/pages - contains pages used by applications<br>
src/providers - contains providers (config and browser) for the framework<br>
tests/ - localization of the tests to run

# Before commit
Please do commands below before commit<br>
run isort .<br>
run black .
