import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.update_2_O import DpWorkUpdatePage
from pageObjects.signup_page_2_O import SignupPage
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

class Test_001_UpdateSerialNumber:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)
    field_worker_username = os.getenv('field_worker_username')
    field_worker_password = os.getenv('field_worker_password')
    #sender=readConfig.getEmailSender()

    updateSerialNumber_Screenshot_folderName=dpwork_updateSerialNumber_Screenshot_folder
    updateSerialNumber_documentation_fileName=dpwork_updateSerialNumber_documentation_filename

    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work Update Serial Number Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(updateSerialNumber_Screenshot_folderName)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()

    updateSerialNumber_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    updateSerialNumber_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+updateSerialNumber_testData_file
    
    def test_serialNumberUpdateActiveMemberByFW(self,setup):
        try:
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - Update Serial Number Functionality")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Update: Test Case - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)
            time.sleep(2)

            self.dplp=DpWorkLoginPage(self.driver)
            self.dpup=DpWorkUpdatePage(self.driver)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.dplp.clickLoginButton()
            



            

        except Exception as e:
            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0F',self.driver)
            docsutil.addSmallHeading(self.document,"User while resetting password exception occurred")
            docsutil.insertImageInDocx(self.document,ss0F_location)
            raise CustomException(e,sys)

    def test_serialNumberUpdateInActiveMember(self,setup):
        try:
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - Forgot Password Functionality")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Fogot Password: Test Case - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            time.sleep(2)
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpfp=ForgotPassword(self.driver)
            self.dpsu=SignupPage(self.driver)
            
        except Exception as e:
            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Simple -Forgot Password','0F',self.driver)
            docsutil.addSmallHeading(self.document,"User while resetting password exception occurred")
            docsutil.insertImageInDocx(self.document,ss0F_location)
            raise CustomException(e,sys)