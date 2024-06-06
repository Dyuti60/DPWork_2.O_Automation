import pytest
from selenium import webdriver
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(browser):
    #Chromepath="F:\\DpWorkProject\\DpWorkPrivate\\utilities\\chromedriver.exe"
    
    #EdgePath="C://Users//DYUTI SUNDER DUTTA//Downloads//edgedriver_win64//msedgedriver.exe"
    #edgePath=os.getcwd()+"//msedgedriver.exe"
    #FirefoxDriver=""
    if browser=='chrome':
        #driver=webdriver.Chrome(Chromepath)
        driver=webdriver.Chrome(ChromeDriverManager().install())
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Edge()
        print("Launching Edge browser.........")
    return driver

#1. this function will get the value from the command line
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

#2. this function will return the browser value to the setup method
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Tester": "Amar",
        "Project Name": "Hybrid Framework Practice",
        }


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    
