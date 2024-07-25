# Objective is to automate Regression Testing of DP Works Portal and validate end to end workflows.

## Pre - requisites:
- Miniconda or Anaconda needs to be installed
- Recommended to use Visual Studio Code as IDE

### Steps to be followed:
1. Clone the git repository in your local system
2. Create a conda environment using the command:
    - conda create -p venv python==3.9 -y in the projects folder path
3. Activate the conda environment using the command:
    - activate ./venv
4. Install the libraries in the requirements.txt file using the command:
    - pip install -r requirements.txt
5. Create a general project folder structure by running the command:
    - python template.py
6. Run test cases:
   - Sample Syntax:
        - pytest -v --html=./reports/DPWorkLoginPageTestReport.html DPWork_2.O_AutomationTesting/testcases/test_dpwork_login_functionality.py
        - Where DPWorkLoginPageTestReport.html is the report to be generated for the test case run and
        test_dpwork_login_functionality.py is the test case file

Example:
pytest -v -s DPWork_2.O_AutomationTesting/testcases/test_updateSerialNumber_functionality_2_O.py --html=updateSerialNumber.html --alluredir=allure_reports 
