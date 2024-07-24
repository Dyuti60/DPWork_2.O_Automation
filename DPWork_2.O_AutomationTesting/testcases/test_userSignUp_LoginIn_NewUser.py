import pytest
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.signup_page_2_O import SignupPage
from utilities.readProperties import readConfig
from exception import CustomException
from logger import LogGen
from dotenv import load_dotenv
from utilities import XLUtils
from utilities import docsutil
from utilities import emailUtil
from configurations.constants import projectName,dot_env_file
import os
import time
from datetime import datetime
from configurations.constants import *


class Test_SignUpAndLoginUser:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    #field_worker_username = os.getenv('new_field_worker_username')
    #field_worker_password = os.getenv('new_field_worker_password')

    #sender=readConfig.getEmailSender()
    firstTimeSignUpLoginOTPTwice_Screenshot_folderName=dpwork_firstTimeSignUpLogin_Screenshot_folder1
    firstTimeSignUpLoginOTPOnce_Screenshot_folderName=dpwork_firstTimeSignUpLogin_Screenshot_folder2
    firstTimeSignUpLogin_documentation_fileName=dpwork_firstTimeSignUpLogin_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work - New User Sign Up Resend OTP and Login Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(firstTimeSignUpLoginOTPTwice_Screenshot_folderName)
    screenshot_location1=docsutil.createDedicatedSSFolder(firstTimeSignUpLoginOTPOnce_Screenshot_folderName)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()


    firstTimeSignUpLogin_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    firstTimeSignUpLogin_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+firstTimeSignUpLogin_testDataFile


    def test_DpWorkNewUserSignUpAndLoginResendOTP(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.logging.info("Browser will Maximize")
            self.driver.maximize_window()
            self.logging.info("Surfing to DpWork login page")
            self.driver.get(self.dpwork_url)
            time.sleep(2)
            self.logging.info("Data will be taken from Test Data file")
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.firstTimeSignUpLogin_testData_FilePath,sheetName=newUserSignUpLoginSheetName1)
            newUserSignUpLoginTestDataDict,newUserSignUpLoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.dplp=DpWorkLoginPage(self.driver)
            self.dpsu=SignupPage(self.driver)
            self.logging.info("Waiting for the login page to load...")
            self.dplp.waitForLoginPage()
            

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - SignUp:")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Sign Up Page: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)
            index=0
            registrationFlag=self.dpsu.clickRegisterNowButton()
            self.logging.info("User clicks on Register Now button")
            filenamePrefix=list(newUserSignUpLoginTestDataDict[newSignUp_testCaseName])[index]
            if registrationFlag:
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','01',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on Register Now Button to start with sign up process")
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dpsu.clickRegisterButtonAfterFillingRegisterPage()
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','02',self.driver)
                docsutil.addSmallHeading(self.document,"User Clicks on Register Button to check if error messages comes on entering nothin")
                docsutil.insertImageInDocx(self.document,ss02_location)
                self.logging.info("User Clicks on Register Button to check if error messages comes on entering nothing")
                
                if(self.dpsu.checkSignUpErrorMessage(list(newUserSignUpLoginTestDataDict[newSignUp_FirstName])[index],list(newUserSignUpLoginTestDataDict[newSignUp_LastName])[index],list(newUserSignUpLoginTestDataDict[newSignUp_ContactNumber])[index],list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index],list(newUserSignUpLoginTestDataDict[newSignUp_ConfirmPassword])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Address])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Pincode])[index])):
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','03',self.driver)
                    docsutil.addSmallHeading(self.document,"User Validates the error message displayed on entering nothing and clicking Register Button")
                    docsutil.insertImageInDocx(self.document,ss03_location)

                    self.dpsu.enterFirstName(list(newUserSignUpLoginTestDataDict[newSignUp_FirstName])[index])
                    ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','04',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters First Name")
                    docsutil.insertImageInDocx(self.document,ss04_location)
                    self.logging.info("User Enter First Name")

                    self.dpsu.enterLastName(list(newUserSignUpLoginTestDataDict[newSignUp_LastName])[index])
                    ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','05',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Last Name")
                    docsutil.insertImageInDocx(self.document,ss05_location)
                    self.logging.info("User Enter Last Name")

                    self.dpsu.enterContactNumber(list(newUserSignUpLoginTestDataDict[newSignUp_ContactNumber])[index])
                    ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','06',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Contact Name")
                    docsutil.insertImageInDocx(self.document,ss06_location)
                    self.logging.info("User Enter Contact Number")

                    self.dpsu.enterEmailAddress(list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index])
                    ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','07',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Email Address")
                    docsutil.insertImageInDocx(self.document,ss07_location)
                    self.logging.info("User Enter Email Address")

                    self.dpsu.enterPassword(list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index])
                    ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','08',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Password")
                    docsutil.insertImageInDocx(self.document,ss08_location)
                    self.logging.info("User Enter Password")

                    self.dpsu.enterConfirmPassword(list(newUserSignUpLoginTestDataDict[newSignUp_ConfirmPassword])[index])
                    ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','09',self.driver)
                    docsutil.addSmallHeading(self.document,"User Confirms Password")
                    docsutil.insertImageInDocx(self.document,ss09_location)
                    self.logging.info("User confirms entered Password")

                    self.dpsu.enterAddress(list(newUserSignUpLoginTestDataDict[newSignUp_Address])[index])
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','10',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Address")
                    docsutil.insertImageInDocx(self.document,ss10_location)
                    self.logging.info("User Enter Address")

                    self.dpsu.enterPincode(list(newUserSignUpLoginTestDataDict[newSignUp_Pincode])[index])
                    time.sleep(2)
                    ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','11',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Pincode")
                    docsutil.insertImageInDocx(self.document,ss11_location)
                    self.logging.info("User Enter Pincode")

                    self.dpsu.clickRegisterButtonAfterFillingRegisterPage()
                    ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','12',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on Registration button on filling in the registration page")
                    docsutil.insertImageInDocx(self.document,ss12_location)
                    self.logging.info("User clicks on Register Button after filling in all the information")

                    self.dpsu.waitFor3MinutesAsOtpAlreadySent()
                    ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','13',self.driver)
                    docsutil.addSmallHeading(self.document,"User waits for 3 minutes if user sends otp to the mobile or email within 3 minutes")
                    docsutil.insertImageInDocx(self.document,ss13_location)
                    self.logging.info("User waits for 3 minutes if user sends otp to the mobile or email within 3 minutes")
                    time_then=datetime.now()
                    #self.dpsu.clickLoginNowButtonAtTheBottomOfRegistrationPage()

                    if self.dpsu.checkPresenceofResetTimer():
                        ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','14',self.driver)
                        docsutil.addSmallHeading(self.document,"User checks the presence of Reset Timer")
                        docsutil.insertImageInDocx(self.document,ss14_location)
                        self.logging.info("User checks the presence of Reset Timer")

                        self.dpsu.enterPhoneOTP(phoneOTP=input("Enter phone OTP: "))
                        ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','15',self.driver)
                        docsutil.addSmallHeading(self.document,"User asked to enter phone OTP")
                        docsutil.insertImageInDocx(self.document,ss15_location)
                        self.logging.info("User asked to enter phone OTP")

                        self.dpsu.enterEmailOTP(emailOTP=input("Enter email OTP: "))
                        ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','16',self.driver)
                        docsutil.addSmallHeading(self.document,"User asked to enter email OTP")
                        docsutil.insertImageInDocx(self.document,ss16_location)
                        self.logging.info("User asked to enter email OTP")

                        time_now=datetime.now()
                        delta=time_now-time_then
                        print(delta)
                        time.sleep(int(200-(delta.total_seconds())))
                        ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','17',self.driver)
                        docsutil.addSmallHeading(self.document,"User waits for {} seconds".format(str(int(200-(delta.total_seconds())))))
                        docsutil.insertImageInDocx(self.document,ss17_location)
                        self.logging.info("User waits for {} seconds".format(str(int(200-(delta.total_seconds())))))

                        if self.dpsu.checkPresenceOfResendButton():
                            ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','18',self.driver)
                            docsutil.addSmallHeading(self.document,"User checks Resend button link after waiting for more than 3 minutes")
                            docsutil.insertImageInDocx(self.document,ss18_location)
                            self.logging.info("User checks Resend button link after waiting for more than 3 minutes")

                            self.dpsu.clickResenButtonToVerifyEmailPhone()
                            ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','19',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on Resend Button to verify email and phone")
                            docsutil.insertImageInDocx(self.document,ss19_location)
                            self.logging.info("User clicks on Resend Button to verify email and phone")

                            self.dpsu.enterPhoneOTP(phoneOTP=input("Enter phone OTP: "))
                            ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','20',self.driver)
                            docsutil.addSmallHeading(self.document,"User asked to enter phone OTP after resending otp")
                            docsutil.insertImageInDocx(self.document,ss20_location)
                            self.logging.info("User asked to enter phone OTP after resending otp")

                            self.dpsu.enterEmailOTP(emailOTP=input("Enter email OTP: "))  
                            ss21_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','21',self.driver)
                            docsutil.addSmallHeading(self.document,"User asked to enter email OTP after resending otp")
                            docsutil.insertImageInDocx(self.document,ss21_location)
                            self.logging.info("User asked to enter email OTP after resending otp")

                            self.dpsu.clickVerifyOnEnteringMobileAndEmailOTP()
                            time.sleep(3)
                            ss22_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','22',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on verify button after entering email and phone otps")
                            docsutil.insertImageInDocx(self.document,ss22_location)
                            self.logging.info("User clicks on verify button after entering email and phone otps")

                            self.dpsu.clickLoginNowButtonOnGettingSignUpSuccessMessage()
                            ss23_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','23',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on login now button on receiving sign up success message")
                            docsutil.insertImageInDocx(self.document,ss23_location)
                            self.logging.info("User clicks on login now button on receiving sign up success message")
                            #self.dpsu.clickCrossButtonOnGettingSignUpSuccessMessage()
                            #self.driver.get(self.dpwork_url)
                            self.dplp.waitForLoginPage()
                            ss24_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','24',self.driver)
                            docsutil.addSmallHeading(self.document,"User waits for the login page to load...")
                            docsutil.insertImageInDocx(self.document,ss24_location)
                            self.logging.info("User waits for the login page to load...")

                            self.dplp.setDpWorkUserName(list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index])
                            ss25_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','25',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the signed up email address")
                            docsutil.insertImageInDocx(self.document,ss25_location)
                            self.logging.info("User enters the signed up email address")

                            self.dplp.setDpWorkPassword(list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index])
                            ss26_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','26',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the password for the signed up email address")
                            docsutil.insertImageInDocx(self.document,ss26_location)
                            self.logging.info("User enters the password for the signed up email address")

                            self.dplp.clickLoginButton()
                            ss27_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','27',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on login now button after entering username and password")
                            docsutil.insertImageInDocx(self.document,ss27_location)
                            self.logging.info("User clicks on login now button after entering username and password")

                            time.sleep(5)
                            self.dpsu.waitForApprovalFromDA()
                            ss28_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','28',self.driver)
                            docsutil.addSmallHeading(self.document,"User waits for DA to approve his/her account")
                            docsutil.insertImageInDocx(self.document,ss28_location)
                            self.logging.info("User waits for DA to approve his/her account")

                            self.dpsu.enterFamilyCode(list(newUserSignUpLoginTestDataDict[newSignUp_FamilyCode])[index], list(newUserSignUpLoginTestDataDict[newSignUp_PhilName])[index])
                            ss29_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','29',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the family code and philanthropic name to map the account with")
                            docsutil.insertImageInDocx(self.document,ss29_location)
                            self.logging.info("User enters the family code and philanthropic name to map the account with")

                            self.dpsu.clickLoginButtonOnEnteringFC()
                            ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','30',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on login button on entering FC")
                            docsutil.insertImageInDocx(self.document,ss30_location)
                            self.logging.info("User clicks on login button on entering FC")
                            time_then=datetime.now()
                        
                            if self.dpsu.checkResendTimerForFamilyCodeAuthentication():
                                ss31_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','31',self.driver)
                                docsutil.addSmallHeading(self.document,"User checks resend timer for family code authentication")
                                docsutil.insertImageInDocx(self.document,ss31_location)
                                self.logging.info("User checks resend timer for family code authentication")

                                self.dpsu.enterAuthenticatedCodeForFamilyCode(mobileAuthenticatedCode=input("Enter otp sent to fc linked mobile number: "))
                                ss32_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','32',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters authenticated code for family code verification")
                                docsutil.insertImageInDocx(self.document,ss32_location)
                                self.logging.info("User enters authenticated code for family code verification")

                                time_now=datetime.now()
                                delta=time_now-time_then
                                print(delta)
                                time.sleep(int(200-(delta.total_seconds())))
                                if self.dpsu.checkResendLinkForFamilyCodeAuthentication():
                                    ss33_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','33',self.driver)
                                    docsutil.addSmallHeading(self.document,"User checks resend link after 3 minutes")
                                    docsutil.insertImageInDocx(self.document,ss33_location)
                                    self.logging.info("User checks resend link after 3 minutes")

                                    self.dpsu.clickResendLinkToVerifyFC()
                                    ss34_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','34',self.driver)
                                    docsutil.addSmallHeading(self.document,"User clicks on resend link after 3 minutes")
                                    docsutil.insertImageInDocx(self.document,ss34_location)
                                    self.logging.info("User clicks on resend link after 3 minutes")

                                    self.dpsu.enterAuthenticatedCodeForFamilyCode(mobileAuthenticatedCode=input("Enter otp sent to fc linked mobile number: "))
                                    ss35_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','35',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters authenticated code for family code verification")
                                    docsutil.insertImageInDocx(self.document,ss35_location)
                                    self.logging.info("User enters authenticated code for family code verification")

                                    self.dpsu.clickLoginButtonOnEnteringFC()
                                    ss36_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','36',self.driver)
                                    docsutil.addSmallHeading(self.document,"User clicks on login button on entering FC")
                                    docsutil.insertImageInDocx(self.document,ss36_location)
                                    self.logging.info("User clicks on login button on entering FC")

                                    Name0, Status1=self.dpsu.checkAndReturnUserDetailsOnSuccessfulLogin()
                                    ss37_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Sign Up Page -Register','37',self.driver)
                                    docsutil.addSmallHeading(self.document,"{} - {}".format(Name0, Status1))
                                    docsutil.insertImageInDocx(self.document,ss37_location)
                                    docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - DP Work Sign Up Page -Register ")
                                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                                    self.logging.info("{} - {}".format(Name0, Status1))

                                else:
                                    ss0A_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0A',self.driver)
                                    docsutil.addSmallHeading(self.document,"'Resend' button is not visible to resend otp to verify FC")
                                    docsutil.insertImageInDocx(self.document,ss0A_location)
                                    docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                                    assert False,"'Resend' button is not visible to resend otp to verify FC"

                            else:
                                ss0B_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0B',self.driver)
                                docsutil.addSmallHeading(self.document,"'Resend in <>' timer is not visible to verify phone")
                                docsutil.insertImageInDocx(self.document,ss0B_location)
                                docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                                assert False,"'Resend in <>' timer is not visible to verify phone"

                        else:
                            ss0C_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0C',self.driver)
                            docsutil.addSmallHeading(self.document,"'Resend' button is not visible to resend otp to verify email and phone")
                            docsutil.insertImageInDocx(self.document,ss0C_location)
                            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                            assert False,"'Resend' button is not visible to resend otp to verify email and phone"
                    else:
                        ss0D_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0D',self.driver)
                        docsutil.addSmallHeading(self.document,"'Resend in <>' timer is not visible in verify email and phone")
                        docsutil.insertImageInDocx(self.document,ss0D_location)
                        docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                        assert False,"'Resend in <>' timer is not visible in verify email and phone"
                else:
                    ss0E_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0E',self.driver)
                    docsutil.addSmallHeading(self.document,"Sign Up Error Message Not Hanlded properly, please check the artifacts")
                    docsutil.insertImageInDocx(self.document,ss0E_location)
                    docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                    assert False,"Sign Up Error Message Not Hanlded properly, please check the artifacts"


            else:
                ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0F',self.driver)
                docsutil.addSmallHeading(self.document,"Text Field related to register now is not there in the page")
                docsutil.insertImageInDocx(self.document,ss0F_location)
                docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                assert False,"Text Field related to register now is not there in the page"

        except Exception as e:
            ss0G_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'New User - SignUp','0G',self.driver)
            docsutil.addSmallHeading(self.document,"Some Exception Occurred - Snippet Attached")
            docsutil.insertImageInDocx(self.document,ss0G_location)
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
            raise CustomException(e,sys)
        

    def test_DpWorkNewUserSignUpAndLoginOnceOTPSend(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.logging.info("Browser will Maximize")
            self.driver.maximize_window()
            self.logging.info("Surfing to DpWork login page")
            self.driver.get(self.dpwork_url)
            time.sleep(2)
            self.logging.info("Data will be taken from Test Data file")
            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.firstTimeSignUpLogin_testData_FilePath,sheetName=newUserSignUpLoginSheetName2)
            newUserSignUpLoginTestDataDict,newUserSignUpLoginfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.dplp=DpWorkLoginPage(self.driver)
            self.dpsu=SignupPage(self.driver)
            self.logging.info("Waiting for the login page to load...")
            self.dplp.waitForLoginPage()
            

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'New User - SignUp','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - SignUp:")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Sign Up Page: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)
            index=0
            registrationFlag=self.dpsu.clickRegisterNowButton()
            self.logging.info("User clicks on Register Now button")
            filenamePrefix=list(newUserSignUpLoginTestDataDict[newSignUp_testCaseName])[index]
            if registrationFlag:
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','01',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on Register Now Button to start with sign up process")
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dpsu.clickRegisterButtonAfterFillingRegisterPage()
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','02',self.driver)
                docsutil.addSmallHeading(self.document,"User Clicks on Register Button to check if error messages comes on entering nothin")
                docsutil.insertImageInDocx(self.document,ss02_location)
                self.logging.info("User Clicks on Register Button to check if error messages comes on entering nothing")
                
                if(self.dpsu.checkSignUpErrorMessage(list(newUserSignUpLoginTestDataDict[newSignUp_FirstName])[index],list(newUserSignUpLoginTestDataDict[newSignUp_LastName])[index],list(newUserSignUpLoginTestDataDict[newSignUp_ContactNumber])[index],list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index],list(newUserSignUpLoginTestDataDict[newSignUp_ConfirmPassword])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Address])[index],list(newUserSignUpLoginTestDataDict[newSignUp_Pincode])[index])):
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','03',self.driver)
                    docsutil.addSmallHeading(self.document,"User Validates the error message displayed on entering nothing and clicking Register Button")
                    docsutil.insertImageInDocx(self.document,ss03_location)

                    self.dpsu.enterFirstName(list(newUserSignUpLoginTestDataDict[newSignUp_FirstName])[index])
                    ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','04',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters First Name")
                    docsutil.insertImageInDocx(self.document,ss04_location)
                    self.logging.info("User Enter First Name")

                    self.dpsu.enterLastName(list(newUserSignUpLoginTestDataDict[newSignUp_LastName])[index])
                    ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','05',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Last Name")
                    docsutil.insertImageInDocx(self.document,ss05_location)
                    self.logging.info("User Enter Last Name")

                    self.dpsu.enterContactNumber(list(newUserSignUpLoginTestDataDict[newSignUp_ContactNumber])[index])
                    ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','06',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Contact Name")
                    docsutil.insertImageInDocx(self.document,ss06_location)
                    self.logging.info("User Enter Contact Number")

                    self.dpsu.enterEmailAddress(list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index])
                    ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','07',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Email Address")
                    docsutil.insertImageInDocx(self.document,ss07_location)
                    self.logging.info("User Enter Email Address")

                    self.dpsu.enterPassword(list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index])
                    ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','08',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Password")
                    docsutil.insertImageInDocx(self.document,ss08_location)
                    self.logging.info("User Enter Password")

                    self.dpsu.enterConfirmPassword(list(newUserSignUpLoginTestDataDict[newSignUp_ConfirmPassword])[index])
                    ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','09',self.driver)
                    docsutil.addSmallHeading(self.document,"User Confirms Password")
                    docsutil.insertImageInDocx(self.document,ss09_location)
                    self.logging.info("User confirms entered Password")

                    self.dpsu.enterAddress(list(newUserSignUpLoginTestDataDict[newSignUp_Address])[index])
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','10',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Address")
                    docsutil.insertImageInDocx(self.document,ss10_location)
                    self.logging.info("User Enter Address")

                    self.dpsu.enterPincode(list(newUserSignUpLoginTestDataDict[newSignUp_Pincode])[index])
                    time.sleep(2)
                    ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','11',self.driver)
                    docsutil.addSmallHeading(self.document,"User Enters Pincode")
                    docsutil.insertImageInDocx(self.document,ss11_location)
                    self.logging.info("User Enter Pincode")

                    self.dpsu.clickRegisterButtonAfterFillingRegisterPage()
                    ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','12',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on Registration button on filling in the registration page")
                    docsutil.insertImageInDocx(self.document,ss12_location)
                    self.logging.info("User clicks on Register Button after filling in all the information")

                    self.dpsu.enterPhoneOTP(phoneOTP=input("Enter phone OTP: "))
                    ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','15',self.driver)
                    docsutil.addSmallHeading(self.document,"User asked to enter phone OTP")
                    docsutil.insertImageInDocx(self.document,ss15_location)
                    self.logging.info("User asked to enter phone OTP")

                    self.dpsu.enterEmailOTP(emailOTP=input("Enter email OTP: "))
                    ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','16',self.driver)
                    docsutil.addSmallHeading(self.document,"User asked to enter email OTP")
                    docsutil.insertImageInDocx(self.document,ss16_location)
                    self.logging.info("User asked to enter email OTP")


                    self.dpsu.clickVerifyOnEnteringMobileAndEmailOTP()
                    time.sleep(3)
                    ss22_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','22',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on verify button after entering email and phone otps")
                    docsutil.insertImageInDocx(self.document,ss22_location)
                    self.logging.info("User clicks on verify button after entering email and phone otps")

                    self.dpsu.clickLoginNowButtonOnGettingSignUpSuccessMessage()
                    ss23_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','23',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on login now button on receiving sign up success message")
                    docsutil.insertImageInDocx(self.document,ss23_location)
                    self.logging.info("User clicks on login now button on receiving sign up success message")
                    #self.dpsu.clickCrossButtonOnGettingSignUpSuccessMessage()
                    #self.driver.get(self.dpwork_url)
                    self.dplp.waitForLoginPage()
                    ss24_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','24',self.driver)
                    docsutil.addSmallHeading(self.document,"User waits for the login page to load...")
                    docsutil.insertImageInDocx(self.document,ss24_location)
                    self.logging.info("User waits for the login page to load...")

                    self.dplp.setDpWorkUserName(list(newUserSignUpLoginTestDataDict[newSignUp_EmailAddress])[index])
                    ss25_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','25',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters the signed up email address")
                    docsutil.insertImageInDocx(self.document,ss25_location)
                    self.logging.info("User enters the signed up email address")

                    self.dplp.setDpWorkPassword(list(newUserSignUpLoginTestDataDict[newSignUp_Password])[index])
                    ss26_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','26',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters the password for the signed up email address")
                    docsutil.insertImageInDocx(self.document,ss26_location)
                    self.logging.info("User enters the password for the signed up email address")

                    self.dplp.clickLoginButton()
                    ss27_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','27',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on login now button after entering username and password")
                    docsutil.insertImageInDocx(self.document,ss27_location)
                    self.logging.info("User clicks on login now button after entering username and password")

                    time.sleep(5)
                    self.dpsu.waitForApprovalFromDA()
                    ss28_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','28',self.driver)
                    docsutil.addSmallHeading(self.document,"User waits for DA to approve his/her account")
                    docsutil.insertImageInDocx(self.document,ss28_location)
                    self.logging.info("User waits for DA to approve his/her account")

                    self.dpsu.enterFamilyCode(list(newUserSignUpLoginTestDataDict[newSignUp_FamilyCode])[index], list(newUserSignUpLoginTestDataDict[newSignUp_PhilName])[index])
                    ss29_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','29',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters the family code and philanthropic name to map the account with")
                    docsutil.insertImageInDocx(self.document,ss29_location)
                    self.logging.info("User enters the family code and philanthropic name to map the account with")

                    self.dpsu.clickLoginButtonOnEnteringFC()
                    ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','30',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on login button on entering FC")
                    docsutil.insertImageInDocx(self.document,ss30_location)
                    self.logging.info("User clicks on login button on entering FC")
                        

                    self.dpsu.enterAuthenticatedCodeForFamilyCode(mobileAuthenticatedCode=input("Enter otp sent to fc linked mobile number: "))
                    ss32_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','32',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters authenticated code for family code verification")
                    docsutil.insertImageInDocx(self.document,ss32_location)
                    self.logging.info("User enters authenticated code for family code verification")



                    self.dpsu.clickLoginButtonOnEnteringFC()
                    ss36_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','36',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on login button on entering FC")
                    docsutil.insertImageInDocx(self.document,ss36_location)
                    self.logging.info("User clicks on login button on entering FC")

                    Name0, Status1=self.dpsu.checkAndReturnUserDetailsOnSuccessfulLogin()
                    ss37_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'DP Work Sign Up Page -Register','37',self.driver)
                    docsutil.addSmallHeading(self.document,"{} - {}".format(Name0, Status1))
                    docsutil.insertImageInDocx(self.document,ss37_location)
                    docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - DP Work Sign Up Page -Register ")
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                    self.logging.info("{} - {}".format(Name0, Status1))

                else:
                    ss0E_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'New User - SignUp','0E',self.driver)
                    docsutil.addSmallHeading(self.document,"Sign Up Error Message Not Hanlded properly, please check the artifacts")
                    docsutil.insertImageInDocx(self.document,ss0E_location)
                    docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                    assert False,"Sign Up Error Message Not Hanlded properly, please check the artifacts"


            else:
                ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'New User - SignUp','0F',self.driver)
                docsutil.addSmallHeading(self.document,"Text Field related to register now is not there in the page")
                docsutil.insertImageInDocx(self.document,ss0F_location)
                docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
                assert False,"Text Field related to register now is not there in the page"

        except Exception as e:
            ss0G_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location1,'New User - SignUp','0G',self.driver)
            docsutil.addSmallHeading(self.document,"Some Exception Occurred - Snippet Attached")
            docsutil.insertImageInDocx(self.document,ss0G_location)
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - New SignUp And Login")
            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.firstTimeSignUpLogin_documentation_fileName))
            raise CustomException(e,sys)