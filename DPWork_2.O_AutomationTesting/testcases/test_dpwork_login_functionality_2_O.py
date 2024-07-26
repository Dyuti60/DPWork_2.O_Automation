import pytest
import sys
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from utilities.readProperties import readConfig
from exception import CustomException
from logger import LogGen
from dotenv import load_dotenv
from utilities import XLUtils
from utilities import docsutil
from utilities import emailUtil
from configurations.constants import projectName,dot_env_file
from configurations.constants import dpwork_loginpage_Screenshot_folder,dpwork_loginpage_documentation_filename
import time
import os
from configurations.constants import *

#hi=priyam.baidya.rs@gmail.com
#nvpzchqmzngpcxpc
class Test_LoginFunationality:
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    #sender=readConfig.getEmailSender()
    loginpage_Screenshot_folderName=dpwork_loginpage_Screenshot_folder
    loginpage_documentation_fileName=dpwork_loginpage_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work Login Functionality Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(loginpage_Screenshot_folderName)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()
    #login_page_evidence_attachment_filepath=os.getcwd()+"\\documentation\\"+login_page_evidence_attachment
    #login_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    Login_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+Login_testData_File

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.test_phase1
    def test_DpWorkLoginPageValidFieldWorkerJustRegisteredSimpleLogIn(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            index=0
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.Login_testData_FilePath,sheetName=SimpleLoginExistingUser)
            LoginTestDataDict,LoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.logging.info("Data will be taken from Test Data file".format(str(list(LoginTestDataDict[login_testCaseName])[index])))
            docsutil.addMainHeading(self.document,"Test Case - Test DpWork Login Page - ".format(str(list(LoginTestDataDict[login_testCaseName])[index])))


            self.dplp=DpWorkLoginPage(self.driver)

            for index in range(LoginfieldValues_length):
                self.driver.get(self.dpwork_url)
                self.dplp.waitForLoginPage()
                time.sleep(2)
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','00',self.driver)
                docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker")
                docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dplp.setDpWorkUserName(list(LoginTestDataDict[user_emailAddress])[index])
                self.logging.info("Username Entered- {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                self.dplp.setDpWorkPassword(list(LoginTestDataDict[user_password])[index])
                self.logging.info("Corresponding Password Entered")

                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','01',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
                docsutil.appendContent(self.document,"DP worker valid username - {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                docsutil.appendContent(self.document,"DP worker valid password - **************")
                docsutil.insertImageInDocx(self.document,ss01_location)
                allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)

                self.dplp.clickLoginButton()
                time.sleep(2)
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','02',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
                docsutil.insertImageInDocx(self.document,ss02_location)
                self.logging.info("Click on login button")

                if self.dplp.checkAndReturnUserDetailsOnSuccessfulLogin(list(LoginTestDataDict[login_userRoleName])[index],list(LoginTestDataDict[login_userRole])[index]):
                    ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','05',self.driver)
                    docsutil.addSmallHeading(self.document,"User checks the userrole for the logged user and the userstatus for the logged user")
                    docsutil.insertImageInDocx(self.document,ss05_location)
                    self.logging.info("user checks the userrole for the logged user and the userstatus for the logged user")
                    self.dplp.logoutButtonDisplayed()
                    self.dplp.clickLogoutButton()

                    ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','05',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker Clicks logout link from the Navation Menu")
                    docsutil.insertImageInDocx(self.document,ss05_location)
                    self.logging.info("Field Worker clicks on the logout button")

                    
                    self.dplp.waitForLoginPageAfterLogout()
                    ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','06',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
                    docsutil.insertImageInDocx(self.document,ss06_location)
                    self.logging.info("Returns to the Initial Login Page")
                    docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid User")
                    self.logging.info("Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid User - Pass")
                    time.sleep(2)
                    docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))
                    #self.logging.info(self.login_page_evidence_attachment_filepath)
                    #self.logging.info("Email with Attachments shared via email")
                    #emailUtil.sendEmail(self.emailSender,self.emailSenderPassword,self.receiversTo,self.receiversCC,self.login_page_evidence_attachment_filepath,self.login_page_logs_attachment_filepath)
                else:
                    allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
                    docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid User")
                    docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))
                    assert False,"User role and user status not expected"

            
            self.driver.quit()
            assert True,"Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid User - Pass"  

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid User")
            docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))
            self.driver.quit()
            raise CustomException(e,sys)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_phase1
    def test_DpWorkLoginPageInValidCredentials(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()

            index=0
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.Login_testData_FilePath,sheetName=SimpleLoginExistingUserInvalidPasssword)
            LoginTestDataDict,LoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.logging.info("Data will be taken from Test Data file".format(str(list(LoginTestDataDict[login_testCaseName])[index])))
            docsutil.addMainHeading(self.document,"Test Case - Test DpWork Login Page - ".format(str(list(LoginTestDataDict[login_testCaseName])[index])))

            self.dplp=DpWorkLoginPage(self.driver)
            
            for index in range(LoginfieldValues_length):
                self.driver.get(self.dpwork_url)
                self.dplp.waitForLoginPage()
                self.logging.info("Surfing to DpWork login page")
                time.sleep(2)
                ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','06',self.driver)
                docsutil.addMediumHeading(self.document,"Test Case - 002 - Test DpWork Login Page for FieldWorker with Invalid Username")
                docsutil.appendContentWithBlueColor(self.document,"DP Work Login Page: Test Case - 002 - Begins:")
                docsutil.insertImageInDocx(self.document,ss06_location)

                self.dplp.setDpWorkUserName(list(LoginTestDataDict[user_emailAddress])[index])
                self.logging.info("Invalid Username Entered- {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                self.dplp.setDpWorkPassword(list(LoginTestDataDict[user_password])[index])
                self.logging.info("Any Password Entered")
                allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
                ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','07',self.driver)
                docsutil.addSmallHeading(self.document,"Entered InValid Usename and Password")
                docsutil.appendContent(self.document,"DP worker valid username - {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                docsutil.appendContent(self.document,"DP worker valid password - **************")
                docsutil.insertImageInDocx(self.document,ss07_location)

                self.dplp.clickLoginButton()
                self.logging.info("Click on login button")
                ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','08',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
                docsutil.insertImageInDocx(self.document,ss08_location)

                self.dplp.errorMessageInvalidCredentials()
                self.logging.info("Error Message Displayed")
                ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','09',self.driver)
                docsutil.addSmallHeading(self.document,"Error Message Displayed for invalid username")
                docsutil.insertImageInDocx(self.document,ss09_location)
                time.sleep(1)

                self.dplp.waitForLoginPage()
                self.logging.info("Returns to the Initial Login Page")
                ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','10',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker returns to Login Page")
                docsutil.insertImageInDocx(self.document,ss10_location)

                self.logging.info("Successfully Validated Test Case - 002 - Test DpWork Login Page for A user with Invalid Username - Pass")
                docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A user with Invalid Username - Pass")
                docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))

            self.driver.quit()
            assert True,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid Username - Pass"            
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
            docsutil.appendContentWithFailColor(self.document,"Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid username")
            docsutil.saveDocument(self.document,"TC-"+str(list(LoginTestDataDict[login_testCaseName])[index])+"-"+str(self.loginpage_documentation_fileName))
            self.driver.quit()
            raise CustomException(e,sys)
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.test_phase1
    def test_DpWorkLoginPageInValidEmailAddress(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()

            index=0
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.Login_testData_FilePath,sheetName=SimpleLoginExistingUserInvalidEmail)
            LoginTestDataDict,LoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.logging.info("Data will be taken from Test Data file".format(str(list(LoginTestDataDict[login_testCaseName])[index])))
            docsutil.addMainHeading(self.document,"Test Case - Test DpWork Login Page - ".format(str(list(LoginTestDataDict[login_testCaseName])[index])))

            self.dplp=DpWorkLoginPage(self.driver)
            
            for index in range(LoginfieldValues_length):
                self.driver.get(self.dpwork_url)
                self.dplp.waitForLoginPage()
                self.logging.info("Surfing to DpWork login page")
                time.sleep(2)
                ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','06',self.driver)
                docsutil.addMediumHeading(self.document,"Test Case - 002 - Test DpWork Login Page for FieldWorker with Invalid Username")
                docsutil.appendContentWithBlueColor(self.document,"DP Work Login Page: Test Case - 002 - Begins:")
                docsutil.insertImageInDocx(self.document,ss06_location)

                self.dplp.setDpWorkUserName(list(LoginTestDataDict[user_emailAddress])[index])
                self.logging.info("Invalid Username Entered- {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                self.dplp.setDpWorkPassword(list(LoginTestDataDict[user_password])[index])
                self.logging.info("Any Password Entered")
                allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
                ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','07',self.driver)
                docsutil.addSmallHeading(self.document,"Entered InValid Usename and Password")
                docsutil.appendContent(self.document,"DP worker valid username - {}".format(list(LoginTestDataDict[user_emailAddress])[index]))
                docsutil.appendContent(self.document,"DP worker valid password - **************")
                docsutil.insertImageInDocx(self.document,ss07_location)

                self.dplp.clickLoginButton()
                self.logging.info("Click on login button")
                ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','08',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
                docsutil.insertImageInDocx(self.document,ss08_location)

                self.dplp.errorMessageInvalidCredentials()
                self.logging.info("Error Message Displayed")
                ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','09',self.driver)
                docsutil.addSmallHeading(self.document,"Error Message Displayed for invalid username")
                docsutil.insertImageInDocx(self.document,ss09_location)
                time.sleep(1)

                self.dplp.waitForLoginPage()
                self.logging.info("Returns to the Initial Login Page")
                ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page Type1','10',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker returns to Login Page")
                docsutil.insertImageInDocx(self.document,ss10_location)

                self.logging.info("Successfully Validated Test Case - 002 - Test DpWork Login Page for A user with Invalid Username - Pass")
                docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A user with Invalid Username - Pass")
                docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))

            self.driver.quit()
            assert True,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid Username - Pass"            
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(),name=list(LoginTestDataDict[login_testCaseName])[index], attachment_type=AttachmentType.PNG)
            docsutil.appendContentWithFailColor(self.document,"Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid username")
            docsutil.saveDocument(self.document,"TC-"+str(str(list(LoginTestDataDict[login_testCaseName])[index]))+"-"+str(self.loginpage_documentation_fileName))
            self.driver.quit()
            raise CustomException(e,sys)

'''
    def test_DpWorkLoginPageExistingUserMemCodeVerifiedAndPrimaryAccountNotSet(self, setup):
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
            self.dplp.waitForLoginPage()
            index=0
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.Login_testData_FilePath,sheetName=LoginExistingUserPANSEmailNV_SheetName)
            LoginPANotSetEmailNotVerifiedTestDataDict,newUserSignUpLoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.dplp.setDpWorkUserName(list(LoginPANotSetEmailNotVerifiedTestDataDict[simpleLogin_user_emailAddress])[index])
            self.dplp.setDpWorkPassword(list(LoginPANotSetEmailNotVerifiedTestDataDict[simpleLogin_user_password])[index])
            self.dplp.clickLoginButton()
            

        
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker")
            self.driver.quit()
            raise CustomException(e,sys)

'''
