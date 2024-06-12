import pytest
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.master_search_2_O import DpWorkMasterSearchPage
from utilities.readProperties import readConfig
from exception import CustomException
from logger import LogGen
from dotenv import load_dotenv
from utilities import XLUtils
from utilities import docsutil
from utilities import emailUtil
from configurations.constants import projectName,dot_env_file
from configurations.constants import dpwork_masterSearch_Screenshot_folder,dpwork_masterSearch_documentation_filename,masterSearch_testDataFile,masterSearchSheetName
import time
import os
from configurations.constants import masterSearch_page_evidence_attachment, parametersFields,fieldValues,\
    GlobalSearchName,MemberFirstName,MemberMiddleName,MemberLastName,GuardianFirstName,GuardianMiddleName,\
    GuardianLastName,RitwikFirstName,RitwikMiddleName,RitwikLastName,Address,InitiationDate,PinCode,\
    StateOption,DistrictOption,AreYouUpdatedFamilyCode


class Test_002_MasterSearch:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    field_worker_username = os.getenv('field_worker_username')
    field_worker_password = os.getenv('field_worker_password')

    #sender=readConfig.getEmailSender()
    masterSearch_Screenshot_folderName=dpwork_masterSearch_Screenshot_folder
    masterSearch_documentation_fileName=dpwork_masterSearch_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work Master Search Functionality Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(masterSearch_Screenshot_folderName)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()
    masterSearch_page_evidence_attachment_filepath=os.getcwd()+"\\documentation\\"+masterSearch_page_evidence_attachment
    masterSearch_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    masterSearch_testDate_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+masterSearch_testDataFile

    # Get Data from Excel file:
    dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=masterSearch_testDate_FilePath,sheetName=masterSearchSheetName)
    masterSearchTestDataDict,masterSearchfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)


    def test_DpWorkMasterSearchGlobalSearch(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpms=DpWorkMasterSearchPage(self.driver)
            self.dplp.waitForLoginPage()

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork Master Search Page - Global Search for A FW - Happy Path")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Master Search Page - Global Search: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)

            self.dplp.clickMasterSearchFromMenu()
            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','03',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Master Search Button")
            docsutil.insertImageInDocx(self.document,ss03_location)

            self.dpms.clickGlobalSearchTab()
            ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','04',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Global SEarch Button")
            docsutil.insertImageInDocx(self.document,ss04_location)

            self.dpms.enterNameAndDoGlobalSearch(Name=list(self.masterSearchTestDataDict[MemberFirstName])[0])
            ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','05',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters Name for global search")
            docsutil.insertImageInDocx(self.document,ss05_location)

            self.dpms.clickGlobalSearchSearchButton()
            time.sleep(3)
            ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','06',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on global search Search button")
            docsutil.insertImageInDocx(self.document,ss06_location)
            time.sleep(3)

            self.dpms.clickGlobalSearchClearButton()
            ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','07',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on global search Clear button")
            docsutil.insertImageInDocx(self.document,ss07_location)

            #self.dpms.enterMemberFirstName(memberFirstName=list(self.masterSearchTestDataDict[MemberFirstName])[0])

            self.dplp.clickLogoutButton()
            self.logging.info("Field Worker clicks on the logout button")
            self.dplp.waitForLoginPageAfterLogout()
            self.logging.info("Returns to the Initial Login Page")
            ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Global Search','08',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
            docsutil.insertImageInDocx(self.document,ss08_location)

            self.logging.info("Successfully Validated Test Case - 001 - Test DpWork Master Search Page -Global Search Tab - Pass")
            time.sleep(2)
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork Master Search Page -Global Search Tab")

            assert True,"Successfully Validated Test Case - 001 - Test DpWork Master Search Page - Global Search Page - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Master Search Page - Global Search Page")
            raise CustomException(e,sys)

    def test_DpWorkMasterSearchKeywordSearch(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpms=DpWorkMasterSearchPage(self.driver)
            self.dplp.waitForLoginPage()

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 002 - Test DpWork Master Search Page  - Keyword Search for A FW - Happy Path")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Master Search  - Keyword Search : Test Case - 002 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)

            self.dplp.clickMasterSearchFromMenu()
            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','03',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Master Search Button")
            docsutil.insertImageInDocx(self.document,ss03_location)

            self.dpms.clickKeyWordSearchTab()
            ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','04',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Keyword Search Button")
            docsutil.insertImageInDocx(self.document,ss04_location)

            self.dpms.enterMemberFirstName(memberFirstName=list(self.masterSearchTestDataDict[MemberFirstName])[0])
            ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','05',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters member first name for keyword search")
            docsutil.insertImageInDocx(self.document,ss05_location)

            self.dpms.enterMemberMiddleName(memberMiddleName=list(self.masterSearchTestDataDict[MemberMiddleName])[0])
            ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','06',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters member middle name for keyword search")
            docsutil.insertImageInDocx(self.document,ss06_location)

            self.dpms.enterMemberLastName(memberLastName=list(self.masterSearchTestDataDict[MemberLastName])[0])
            ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','07',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters member middle name for keyword search")
            docsutil.insertImageInDocx(self.document,ss07_location)

            self.dpms.enterGuardianFirstName(guardianFirstName=list(self.masterSearchTestDataDict[GuardianFirstName])[0])
            ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','08',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters guardian first name for keyword search")
            docsutil.insertImageInDocx(self.document,ss08_location)

            self.dpms.enterGuardianMiddleName(guardianFirstName=list(self.masterSearchTestDataDict[GuardianMiddleName])[0])
            ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','09',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters guardian middle name for keyword search")
            docsutil.insertImageInDocx(self.document,ss09_location)

            self.dpms.enterGuardianLastName(guardianFirstName=list(self.masterSearchTestDataDict[GuardianLastName])[0])
            ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','10',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters guardian last name for keyword search")
            docsutil.insertImageInDocx(self.document,ss10_location)

            self.dpms.enterRitwikFirstName(guardianFirstName=list(self.masterSearchTestDataDict[RitwikFirstName])[0])
            ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','11',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters ritwik first name for keyword search")
            docsutil.insertImageInDocx(self.document,ss11_location)

            self.dpms.enterRitwikMiddleName(guardianFirstName=list(self.masterSearchTestDataDict[RitwikMiddleName])[0])
            ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','12',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters ritwik middle name for keyword search")
            docsutil.insertImageInDocx(self.document,ss12_location)

            self.dpms.enterRitwikLastName(guardianFirstName=list(self.masterSearchTestDataDict[RitwikLastName])[0])
            ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','13',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters ritwik last name for keyword search")
            docsutil.insertImageInDocx(self.document,ss13_location)

            self.dpms.enterInitiationDate(initiationDate=list(self.masterSearchTestDataDict[InitiationDate])[0])
            ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','14',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters initiation date for keyword search")
            docsutil.insertImageInDocx(self.document,ss14_location)

            self.dpms.enterAddress(address=list(self.masterSearchTestDataDict[Address])[0])
            ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','15',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters address for keyword search")
            docsutil.insertImageInDocx(self.document,ss15_location)

            self.dpms.enterState(state=StateOption)
            ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','16',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker selects State from dropdown for keyword search")
            docsutil.insertImageInDocx(self.document,ss16_location)

            self.dpms.enterDistrict(district=DistrictOption)
            ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','17',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker selects District from dropdown for keyword search")
            docsutil.insertImageInDocx(self.document,ss17_location)

            self.dpms.clickKeywordSearchSearchButton
            ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','18',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on search button for keyword search")
            docsutil.insertImageInDocx(self.document,ss18_location)
            time.sleep(10)


            self.dpms.clickKeywordSearchClearButton()
            ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','19',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on clear button to reset keyword search parameters")
            docsutil.insertImageInDocx(self.document,ss19_location)


            self.dplp.clickLogoutButton()
            self.logging.info("Field Worker clicks on the logout button")
            self.dplp.waitForLoginPageAfterLogout()
            self.logging.info("Returns to the Initial Login Page")
            ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','20',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
            docsutil.insertImageInDocx(self.document,ss20_location)

            self.logging.info("Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Tab - Pass")
            time.sleep(2)
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Tab")

            assert True,"Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Page")
            raise CustomException(e,sys)
        

    def test_DpWorkMasterAreYouUpdatedSearch(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpms=DpWorkMasterSearchPage(self.driver)
            self.dplp.waitForLoginPage()

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork Master Search Page -  - Are You Updated for A FW - Happy Path")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Master Search Page - Are You Updated: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)

            self.dplp.clickMasterSearchFromMenu()
            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','03',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Master Search Button")
            docsutil.insertImageInDocx(self.document,ss03_location)

            self.dpms.clickGlobalSearchTab()
            ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','04',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Global SEarch Button")
            docsutil.insertImageInDocx(self.document,ss04_location)

            self.dpms.enterNameAndDoGlobalSearch(Name=list(self.masterSearchTestDataDict[MemberFirstName])[0])
            ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','05',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker enters Name for global search")
            docsutil.insertImageInDocx(self.document,ss05_location)

            self.dpms.clickGlobalSearchSearchButton()
            time.sleep(3)
            ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','06',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on global search Search button")
            docsutil.insertImageInDocx(self.document,ss06_location)
            time.sleep(3)

            self.dpms.clickGlobalSearchClearButton()
            ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','07',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker clicks on global search Clear button")
            docsutil.insertImageInDocx(self.document,ss07_location)

            #self.dpms.enterMemberFirstName(memberFirstName=list(self.masterSearchTestDataDict[MemberFirstName])[0])

            self.dplp.clickLogoutButton()
            self.logging.info("Field Worker clicks on the logout button")
            self.dplp.waitForLoginPageAfterLogout()
            self.logging.info("Returns to the Initial Login Page")
            ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Are You Updated','08',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
            docsutil.insertImageInDocx(self.document,ss08_location)

            self.logging.info("Successfully Validated Test Case - 001 - Test DpWork Master Search Page  - Are You Updated Tab - Pass")
            time.sleep(2)
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork Master Search Page  - Are You Updated Tab")

            assert True,"Successfully Validated Test Case - 001 - Test DpWork Master Search Page  - Are You Updated Page - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Master Search Page  - Are You Updated Page")
            raise CustomException(e,sys)