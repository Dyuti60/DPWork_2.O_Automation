import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage import DpWorkLoginPage
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
from configurations.constants import login_page_evidence_attachment,login_page_report_attachment

#hi=priyam.baidya.rs@gmail.com
#nvpzchqmzngpcxpc
class Test_001_Login:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    field_worker_username = os.getenv('field_worker_username')
    field_worker_password = os.getenv('field_worker_password')
    field_worker_invalid_username=os.getenv('field_worker_invalid_username')
    field_worker_invalid_password=os.getenv('field_worker_invalid_password')
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
    login_page_evidence_attachment_filepath=os.getcwd()+"\\documentation\\"+login_page_evidence_attachment
    login_page_report_attachment_filepath=os.getcwd()+"\\reports\\"+login_page_report_attachment


    def test_DpWorkLoginPageValidFieldWorker(self, setup):
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

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Login Page: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)

            self.dplp.clickMenu()
            self.logging.info("Field Worker Clicks on the Navigation Menu Hamburger Icon")
            self.dplp.waitForUserRole('FIELD WORKER')
            self.logging.info("Validates the user role of the user")

            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','03',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Menu Bar and validates the user role for the user logged in")
            docsutil.insertImageInDocx(self.document,ss03_location)

            self.dplp.waitforLogoutButton()
            self.dplp.clickLogoutButton()

            ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','04',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks logout link from the Navation Menu")
            docsutil.insertImageInDocx(self.document,ss04_location)


            self.logging.info("Field Worker clicks on the logout button")
            self.dplp.waitForLoginPageAfterLogout()
            self.logging.info("Returns to the Initial Login Page")

            ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','05',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
            docsutil.insertImageInDocx(self.document,ss05_location)

            self.logging.info("Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker - Pass")
            time.sleep(2)
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker")


            assert True,"Successfully Validated Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork Login Page for A Valid FieldWorker")
            raise CustomException(e,sys)
        
    def test_DpWorkLoginPageInValidFieldWorkerType1(self, setup):
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

            ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','06',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 002 - Test DpWork Login Page for FieldWorker with Invalid Username")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Login Page: Test Case - 002 - Begins:")
            docsutil.insertImageInDocx(self.document,ss06_location)

            self.dplp.setDpWorkUserName(self.field_worker_invalid_username)
            self.logging.info("Invalid Username Entered- {}".format(self.field_worker_invalid_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Any Password Entered")

            ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','07',self.driver)
            docsutil.addSmallHeading(self.document,"Entered InValid Usename and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_invalid_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss07_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")

            ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','08',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss08_location)

            self.dplp.errorMessageType1()
            self.logging.info("Error Message Displayed")

            ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','09',self.driver)
            docsutil.addSmallHeading(self.document,"Error Message Displayed for invalid username")
            docsutil.insertImageInDocx(self.document,ss09_location)
            time.sleep(1)

            self.dplp.waitForLoginPage()
            self.logging.info("Returns to the Initial Login Page")

            ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','10',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to Login Page")
            docsutil.insertImageInDocx(self.document,ss10_location)

            self.logging.info("Successfully Validated Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid Username - Pass")
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid Username - Pass")
            assert True,"Successfully Validated Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid Username - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 002 - Test DpWork Login Page for A FieldWorker with Invalid username")
            raise CustomException(e,sys)
        
    def test_DpWorkLoginPageInValidFieldWorkerType2(self, setup):
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

            ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','06',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 003 - Test DpWork Login Page for A FieldWorker with Valid Username but Invalid Password")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Login Page: Test Case - 003 - Begins:")
            docsutil.insertImageInDocx(self.document,ss11_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Valid Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_invalid_password)
            self.logging.info("Invalid Password Entered")

            ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','12',self.driver)
            docsutil.addSmallHeading(self.document,"Entered Valid Usename but Invalid Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss12_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','13',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss13_location)
            
            self.dplp.errorMessageType2()
            self.logging.info("Error Message Displayed")


            ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','14',self.driver)
            docsutil.addSmallHeading(self.document,"Error Message Displayed for invalid password")
            docsutil.insertImageInDocx(self.document,ss14_location)

            time.sleep(1)
            self.dplp.waitForLoginPage()
            self.logging.info("Returns to the Initial Login Page")

            ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Login Page','15',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Returns to Login Page")
            docsutil.insertImageInDocx(self.document,ss15_location)

            self.driver.close()
            
            
            
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 003 - Test DpWork Login Page for A FieldWorker with Invalid Password" )
            docsutil.saveDocument(self.document,self.loginpage_documentation_fileName)
            self.logging.info("Evidence Document for Login Page Functionality Testing : {}".format(str(self.loginpage_documentation_fileName)))
            print(self.login_page_evidence_attachment_filepath)
            self.logging.info(self.login_page_evidence_attachment_filepath)
            emailUtil.sendEmail(self.emailSender,self.emailSenderPassword,self.receiversTo,self.receiversCC,self.login_page_evidence_attachment_filepath,self.login_page_report_attachment_filepath)
            self.logging.info("Email with Attachments shared via email")

            self.logging.info("Successfully Validated Test Case - 003 - Test DpWork Login Page for A FieldWorker with Invalid Password - Pass")
            assert True,"Successfully Validated Test Case - 003 - Test DpWork Login Page for A FieldWorker with Invalid Password - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 003 - Test DpWork Login Page for A FieldWorker with Invalid Password")
            raise CustomException(e,sys)
'''
        self.driver=setup
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.dplp=DpWorkLoginPage(self.driver)
        document=docsutil.createDocxFile()
        count=1
        docsutil.addMainHeading(document,"DP Work Login Functionality Testing Documentation")
        
        self.logger.info("**********************************************Test_001_DP Worker Login***************************************************")
        self.logger.info("**********************************************DP Work Login Page Testing***************************************************")
        
        self.driver.get(self.dpwork_url)
        self.logger.info("**********************************************Request DP Work QA URL***************************************************")

        filename='.//testData//DpWorkDataParameterization.xlsx'
        filename=os.getcwd()+"//testData//DpWorkDataParameterization.xlsx"
        sheetname='LoginPage'
        rowNum=XLUtils.getRowCount(filename, sheetname)
        colNum=XLUtils.getColCount(filename, sheetname)
        
        dataset=XLUtils.getDataIn2DList(filename,sheetname,rowNum, colNum)
        self.logger.info("**********************************************Get Data from Excel File***************************************************")
        
        location=self.dplp.createDedicatedSSFolder(self.dpwork_loginpage_SS_folder)

        self.dplp.waitForLoginPage()

        ss0_location=self.dplp.takeAndSaveScreenshotUnique(location,'DP Work Login Page','00')
        docsutil.addMediumHeading(document,"DP Work Login Page:")
        docsutil.insertImageInDocx(document,ss0_location)

        for data in dataset:
            userRole=data[0]
            username=data[1]
            password=data[2]
            accessStatus=data[3]
            expectedResult=data[4]
            INDEX=dataset.index(data)

            self.dplp.setDpWorkUserName(username)
            self.logger.info("**********************************************Username Entered- {}***************************************************".format(username))
            self.dplp.setDpWorkPassword(password)
            self.logger.info("**********************************************Corresponding Password Entered***************************************************")

            self.dplp.takeAndSaveScreenshotCommon(location,username,'01')

            self.dplp.clickLoginButton()
            self.logger.info("**********************************************Click on login button***************************************************")
            
            if expectedResult=='Pass':
                if(self.dplp.logoutButtonDisplayed()>0):
                    #self.dplp.onLoginHandleNotification()
                    self.dplp.clickMenu()
                    time.sleep(1)
                    if userRole ==self.userRole1 and accessStatus=="Accessible":
                        self.dplp.waitForUserRole(self.userRole1)
                    elif userRole==self.userRole2 and accessStatus=="Accessible":
                        self.dplp.waitForUserRole(self.userRole2)
                    elif userRole ==self.userRole3 and accessStatus=="Accessible":
                        self.dplp.waitForUserRole(self.userRole3)
                    elif userRole==self.userRole4 and accessStatus=="Accessible":
                        self.dplp.waitForUserRole(self.userRole4)
                    elif userRole==self.userRole5 and accessStatus=="Accessible":
                        self.dplp.waitForUserRole(self.userRole5)

                    if accessStatus=="Accessible":
                        self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                        self.dplp.clickLogoutButton()
                        self.logger.info("**********************************************Click on Logout button***************************************************")
                        time.sleep(2)
                        self.driver.get(self.dpwork_url)
                        self.dplp.waitForLoginPage()
                        XLUtils.writeData(filename,sheetname,INDEX+2,6,"Pass")
                    
                elif(accessStatus=="Access Denied" and self.dplp.accessDeniedDisplayed()>0):                
                        self.dplp.accessDeniedMessage()
                        self.logger.info("**********************************************Message displayed***************************************************")
                        self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                        self.dplp.closeErrorMessage()
                        XLUtils.writeData(filename,sheetname,INDEX+2,6,"Pass")  
                    
                elif(accessStatus=="Blocked" and self.dplp.accessBlockedDisplayed()>0):                
                        self.dplp.accessBlockedMessage()
                        self.logger.info("**********************************************Message displayed***************************************************")
                        self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                        self.dplp.closeErrorMessage()
                        XLUtils.writeData(filename,sheetname,INDEX+2,6,"Pass")    
                else:
                    self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                    self.logger.info("**********************************************Logout button not found***************************************************")
                    self.driver.get(self.dpwork_url)
                    self.dplp.waitForLoginPage()
                    XLUtils.writeData(filename,sheetname,INDEX+2,6,"Fail")

            if expectedResult=='Fail':
                if(accessStatus=="Fail" and self.dplp.errorMessageDisplayed()>0):
                    self.dplp.errorMessage()
                    self.logger.info("**********************************************Message displayed***************************************************")
                    self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                    self.dplp.closeErrorMessage()
                    XLUtils.writeData(filename,sheetname,INDEX+2,6,"Pass")
                else:
                    self.logger.info("**********************************************No Error Message displayed***************************************************")
                    self.dplp.takeAndSaveScreenshotCommon(location,username,'02')
                    XLUtils.writeData(filename,sheetname,INDEX+2,6,"Fail")

            

            #documentation:
            userloginevidences=self.dplp.collectScreenshot(self.dpwork_loginpage_SS_folder,username)
            docsutil.addMediumHeading(document,"Scenario")
            docsutil.appendContent(document,"DP worker username - {}".format(username))
            docsutil.appendContent(document,"DP worker password - {}".format(password))
            docsutil.appendContentWithBlueColor(document,"Scenario expected result - {}".format(expectedResult))
            docsutil.addMediumHeading(document,"User login into DpWork Portal")
            docsutil.insertImageInDocx(document,userloginevidences[0])
            docsutil.addMediumHeading(document,"User clicks on the login button")
            docsutil.appendContentWithBlueColor(document,"Scenario actual result:")
            docsutil.insertImageInDocx(document,userloginevidences[1])
            self.dplp.deleteScreenshots(self.dpwork_loginpage_SS_folder,username)
            self.dplp.deleteScreenshots(self.dpwork_loginpage_SS_folder,"DP Work Login Page")
            time.sleep(1)

        LoginFunctionalityStatus=XLUtils.getDataInList(filename,sheetname,XLUtils.getRowCount(filename,sheetname),6)
        if "Fail" not in LoginFunctionalityStatus:
            docsutil.appendContentWithPassColor(document,"Overall DP Work Login Functionality Testing:")
        else:
            docsutil.appendContentWithFailColor(document,"Overall DP Work Login Functionality Testing:")

        docsutil.saveDocument(document,self.dpwork_loginpage_documentation_filename)
        
        emailUtil.sendEmail(self.sender,self.receivers,self.attachment1, self.attachment2, self.attachment3)
        
        if "Fail" not in LoginFunctionalityStatus:
            self.logger.info("**********************************************Test_001_Login- Passed***************************************************")
            assert True
        else:
            self.logger.error("**********************************************Test_001_Login- Failed***************************************************")
            assert False,"Actual result doesnt matches the expected result"

        self.logger.error("**********************************************Test_001_Login- Failed***************************************************")
        assert False
'''



