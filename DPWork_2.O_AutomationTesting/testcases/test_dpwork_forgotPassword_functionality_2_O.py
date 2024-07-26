import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.forgot_password_2_O import ForgotPassword
from pageObjects.signup_page_2_O import SignupPage
from utilities.readProperties import readConfig
from exception import CustomException
from logger import LogGen
from dotenv import load_dotenv
from utilities import XLUtils
from utilities import docsutil
from utilities import emailUtil
from configurations.constants import projectName,dot_env_file
import time
import os
from configurations.constants import *

#hi=priyam.baidya.rs@gmail.com
#nvpzchqmzngpcxpc
class Test_ForgotPassword:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)


    #sender=readConfig.getEmailSender()

    forgetPassword_Screenshot_folderName=dpwork_forgetPassword_Screenshot_folder
    forgetPassword_documentation_fileName=dpwork_forgetPassword_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work Forgot Password Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(forgetPassword_Screenshot_folderName)


    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()

    login_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    forgetPassword_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+forgetPassword_testData_file
    @pytest.mark.test_phase1
    def test_forgotPassword(self,setup):
        try:
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            time.sleep(2)
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpfp=ForgotPassword(self.driver)
            self.dpsu=SignupPage(self.driver)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.forgetPassword_testData_FilePath,sheetName=forgetPasswordSheetName1)
            forgetPasswordTestDataDict,forgetPasswordfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)
            self.logging.info("Read Data from test data file")

            for index in range(forgetPasswordfieldValues_length):

                self.driver.get(self.dpwork_url)
                self.logging.info("Surfing to DpWork login page")

                ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','00',self.driver)
                docsutil.addMediumHeading(self.document,"Test Case - Forgot Password Functionality")
                docsutil.appendContentWithBlueColor(self.document,"DP Work Fogot Password: Test Case - Begins:")
                docsutil.insertImageInDocx(self.document,ss00_location)
                self.logging.info("Iterate Over the Test Driven Test Cases")

                filenamePrefix=list(forgetPasswordTestDataDict[fp_testCaseName])[index]
                self.logging.info("Test Case Name: {}".format(str(filenamePrefix)))

                self.dpfp.clickOnForgotPassword()
                self.logging.info("User clicks on forgot password")
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','01',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on forgot password")
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dpfp.enterEmailAddressForPasswordReset(list(forgetPasswordTestDataDict[fp_emailAddressForPasswordReset])[index])
                self.logging.info("User enters email address for password reset")
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','02',self.driver)
                docsutil.addSmallHeading(self.document,"User enters email address for password reset")
                docsutil.insertImageInDocx(self.document,ss02_location)

                if self.dpfp.clickOnResetPasswordButton():
                    self.logging.info("User verifies all the prerequisite for Passowrd Reset and clicks on Reset Password Button")
                    ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','02',self.driver)
                    docsutil.addSmallHeading(self.document,"User verifies all the prerequisite for Passowrd Reset and clicks on Reset Password Button")
                    docsutil.insertImageInDocx(self.document,ss02_location)

                    self.dpfp.enterEmailOTPForPasswordReset(input("Enter OTP Received in registered email address: "))
                    self.logging.info("User enters the otp sent to email address")
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','03',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters the otp sent to email address")
                    docsutil.insertImageInDocx(self.document,ss03_location)

                    if self.dpfp.clickVerifyIdentityButtonOnAddingEmailOTP():
                        self.logging.info("User verifies all the prerequisite and clicks on Verify")
                        ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','04',self.driver)
                        docsutil.addSmallHeading(self.document,"User verifies all the prerequisite and clicks on Verify")
                        docsutil.insertImageInDocx(self.document,ss04_location)

                        self.dpfp.enterNewPassword(list(forgetPasswordTestDataDict[fp_newPassword])[index])
                        self.logging.info("User enters new password")
                        ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','05',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters new password")
                        docsutil.insertImageInDocx(self.document,ss05_location)

                        self.dpfp.enterConfirmPassword(list(forgetPasswordTestDataDict[fp_confirmPassword])[index])
                        self.logging.info("User confirms the entered password")
                        ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','06',self.driver)
                        docsutil.addSmallHeading(self.document,"User confirms the entered password")
                        docsutil.insertImageInDocx(self.document,ss06_location)

                        if self.dpfp.clickActivateAccountButton(list(forgetPasswordTestDataDict[fp_newPassword])[index],list(forgetPasswordTestDataDict[fp_confirmPassword])[index])=="ActivateButtonTrue":
                            self.logging.info("User verifies all the prerequisite and clicks on Activate Account button")
                            ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','07',self.driver)
                            docsutil.addSmallHeading(self.document,"User verifies all the prerequisite and clicks on Activate Account button")
                            docsutil.insertImageInDocx(self.document,ss07_location)

                            if self.dpfp.clickLoginNowButtonAfterGettingSuccessPasswordChangeMessage(self.driver):
                                self.logging.info("User clicks on Login Now button, after getting the success message")
                                ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','08',self.driver)
                                docsutil.addSmallHeading(self.document,"User clicks on Login Now button, after getting the success message")
                                docsutil.insertImageInDocx(self.document,ss08_location)

                                self.dplp.waitForLoginPage()
                                self.logging.info("User waits for the login page to load")
                                ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','09',self.driver)
                                docsutil.addSmallHeading(self.document,"User waits for the login page to load")
                                docsutil.insertImageInDocx(self.document,ss09_location)

                                self.dplp.setDpWorkUserName(list(forgetPasswordTestDataDict[fp_emailAddressForPasswordReset])[index])
                                self.logging.info("User enters username {}".format(str(list(forgetPasswordTestDataDict[fp_emailAddressForPasswordReset])[index])))
                                ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','10',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters username {}".format(str(list(forgetPasswordTestDataDict[fp_emailAddressForPasswordReset])[index])))
                                docsutil.insertImageInDocx(self.document,ss10_location)

                                self.dplp.setDpWorkPassword(list(forgetPasswordTestDataDict[fp_newPassword])[index])
                                self.logging.info("User enters corresponding password ***********")
                                ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','11',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters corresponding password ***********")
                                docsutil.insertImageInDocx(self.document,ss11_location)

                                self.dplp.clickLoginButton()
                                self.logging.info("User clicks on login button")
                                ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','12',self.driver)
                                docsutil.addSmallHeading(self.document,"User clicks on login button")
                                docsutil.insertImageInDocx(self.document,ss11_location)

                                Name, Status=self.dpsu.checkAndReturnUserDetailsOnSuccessfulLogin()
                                self.logging.info("Name and Status of the User: {} - {}".format(Name, Status))
                                ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','13',self.driver)
                                docsutil.addSmallHeading(self.document,"User gets inside dp works portal: Name and Status of the User: {} - {}".format(Name, Status))
                                docsutil.insertImageInDocx(self.document,ss13_location)
                                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                                self.driver.refresh()

                            else:
                                ss0A_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0A',self.driver)
                                docsutil.addSmallHeading(self.document,"User faces problem while clicking login now button")
                                docsutil.insertImageInDocx(self.document,ss0A_location)
                                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                                self.driver.quit()
                                assert False, "User faces problem while clicking login now button"

                        elif self.dpfp.clickActivateAccountButton()=="ActivateButtonFalse":
                            ss0B_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0B',self.driver)
                            docsutil.addSmallHeading(self.document,"Passwords are not matching")
                            docsutil.insertImageInDocx(self.document,ss0B_location)
                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                            self.driver.quit()
                            assert False, "Passwords are not matching"
                        else:
                            ss0C_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0C',self.driver)
                            docsutil.addSmallHeading(self.document,"User faced problem on activating the account by clicking activate button")
                            docsutil.insertImageInDocx(self.document,ss0C_location)
                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                            self.driver.quit()
                            assert False, "User faced problem on activating the account by clicking activate button"
                    else:
                        ss0D_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0D',self.driver)
                        docsutil.addSmallHeading(self.document,"User faced problem on clicking verify button")
                        docsutil.insertImageInDocx(self.document,ss0D_location)
                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                        self.driver.quit()
                        assert False, "User faced problem on clicking verify button"
                else:
                    ss0E_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0E',self.driver)
                    docsutil.addSmallHeading(self.document,"User not able to click reset password button")
                    docsutil.insertImageInDocx(self.document,ss0E_location)
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
                    self.driver.quit()
                    assert False, "User not able to click reset password button"
            self.driver.quit()
        except Exception as e:
            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0F',self.driver)
            docsutil.addSmallHeading(self.document,"User while resetting password exception occurred")
            docsutil.insertImageInDocx(self.document,ss0F_location)
            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.forgetPassword_documentation_fileName))
            self.driver.quit()
            raise CustomException(e,sys)
