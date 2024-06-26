import pytest
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.master_search_2_O import DpWorkMasterSearchPage
from pageObjects.update_2_O import DpWorkUpdatePage
from utilities.readProperties import readConfig
from exception import CustomException
from logger import LogGen
from dotenv import load_dotenv
from utilities import XLUtils
from utilities import docsutil
from utilities import emailUtil
from configurations.constants import projectName,dot_env_file
from configurations.constants import dpwork_masterSearch_Screenshot_folder,dpwork_masterSearch_documentation_filename,masterSearch_testDataFile,dpwork_masterSearch_documentation_filename,masterSearchGlobalSheetName,masterSearchKeywordSheetName,masterSearchAreYouUpdatedSheetName
import time
import os
from configurations.constants import masterSearch_page_evidence_attachment, parametersFields,fieldValues,\
    GlobalSearchName,MemberFirstName,MemberMiddleName,MemberLastName,GuardianFirstName,GuardianMiddleName,\
    GuardianLastName,RitwikFirstName,RitwikMiddleName,RitwikLastName,Address,InitiationDate,PinCode,\
    StateOption,DistrictOption,AreYouUpdatedFamilyCode,extractGlobalSearchDataFile,extractKeywordSearchDataFile,extractAreYouUpdatedDataFile

class Test_003_MasterSearchAndUpdate:
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
    masterSearch_testDate_FilePath=os.getcwd()+"\\"+projectName+"\\testdata\\"+masterSearch_testDataFile
    keywordSearchDataExtractFilePath=os.getcwd()+"\\documentation\\"+extractKeywordSearchDataFile
    testdatakeywordSearchExcelFilePath=masterSearch_testDate_FilePath
    testdatakeywordSearchExcelSheetName=masterSearchKeywordSheetName

    def test_DpWorkKeywordSerachAndUpdate(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.masterSearch_testDate_FilePath,sheetName=masterSearchKeywordSheetName)
            masterSearchTestDataDict,masterSearchfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)

            self.dplp=DpWorkLoginPage(self.driver)
            self.dpms=DpWorkMasterSearchPage(self.driver)
            self.dpu=DpWorkUpdatePage(self.driver)
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



            for index in range(masterSearchfieldValues_length):

                self.dplp.clickMasterSearchFromMenu()
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','03',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Master Search Button")
                docsutil.insertImageInDocx(self.document,ss03_location)

                self.dpms.clickKeyWordSearchTab()
                ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','04',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Keyword Search Button")
                docsutil.insertImageInDocx(self.document,ss04_location)

                self.dpms.enterMemberFirstName(memberFirstName=list(masterSearchTestDataDict[MemberFirstName])[index])
                ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','05',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters member first name for keyword search")
                docsutil.insertImageInDocx(self.document,ss05_location)

                self.dpms.enterMemberMiddleName(memberMiddleName=list(masterSearchTestDataDict[MemberMiddleName])[index])
                ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','06',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters member middle name for keyword search")
                docsutil.insertImageInDocx(self.document,ss06_location)

                self.dpms.enterMemberLastName(memberLastName=list(masterSearchTestDataDict[MemberLastName])[index])
                ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','07',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters member middle name for keyword search")
                docsutil.insertImageInDocx(self.document,ss07_location)

                self.dpms.enterGuardianFirstName(guardianFirstName=list(masterSearchTestDataDict[GuardianFirstName])[index])
                ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','08',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters guardian first name for keyword search")
                docsutil.insertImageInDocx(self.document,ss08_location)

                self.dpms.enterGuardianMiddleName(GuardianMiddleName=list(masterSearchTestDataDict[GuardianMiddleName])[index])
                ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','09',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters guardian middle name for keyword search")
                docsutil.insertImageInDocx(self.document,ss09_location)

                self.dpms.enterGuardianLastName(guardianLastName=list(masterSearchTestDataDict[GuardianLastName])[index])
                ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','10',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters guardian last name for keyword search")
                docsutil.insertImageInDocx(self.document,ss10_location)

                self.dpms.enterRitwikFirstName(ritwikFirstName=list(masterSearchTestDataDict[RitwikFirstName])[index])
                ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','11',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters ritwik first name for keyword search")
                docsutil.insertImageInDocx(self.document,ss11_location)

                self.dpms.enterRitwikMiddleName(ritwikMiddleName=list(masterSearchTestDataDict[RitwikMiddleName])[index])
                ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','12',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters ritwik middle name for keyword search")
                docsutil.insertImageInDocx(self.document,ss12_location)

                self.dpms.enterRitwikLastName(ritwikLastName=list(masterSearchTestDataDict[RitwikLastName])[index])
                ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','13',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters ritwik last name for keyword search")
                docsutil.insertImageInDocx(self.document,ss13_location)

                self.dpms.enterInitiationDate(initiationDate=list(masterSearchTestDataDict[InitiationDate])[index])
                ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','14',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters initiation date for keyword search")
                docsutil.insertImageInDocx(self.document,ss14_location)

                self.dpms.enterAddress(address=list(masterSearchTestDataDict[Address])[index])
                ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','15',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters address for keyword search")
                docsutil.insertImageInDocx(self.document,ss15_location)

                self.dpms.enterPinCode(pinCode=list(masterSearchTestDataDict[PinCode])[index])
                ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','16',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters pincode for keyword search")
                docsutil.insertImageInDocx(self.document,ss16_location)

                #self.dpms.enterState(state=StateOption)
                #ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','16',self.driver)
                #docsutil.addSmallHeading(self.document,"Field Worker selects State from dropdown for keyword search")
                #docsutil.insertImageInDocx(self.document,ss16_location)

                #self.dpms.enterDistrict(district=DistrictOption)
                #ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','17',self.driver)
                #docsutil.addSmallHeading(self.document,"Field Worker selects District from dropdown for keyword search")
                #docsutil.insertImageInDocx(self.document,ss17_location)

                self.dpms.clickKeywordSearchSearchButton()
                ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','18',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker clicks on search button for keyword search")
                docsutil.insertImageInDocx(self.document,ss18_location)
                time.sleep(10)

                keywordSearchExtractDataFrame=self.dpms.extractKeywordSearchData(self.driver,self.keywordSearchDataExtractFilePath)
                #self.dpms.validateExtractKeywordSearchData(keywordSearchExtractDataFrame,self.keywordSearchDataExtractFilePath,self.testdatakeywordSearchExcelFilePath,index,str(list(masterSearchTestDataDict[MemberFirstName])[index]),self.testdatakeywordSearchExcelSheetName)

                self.dpms.clickKeywordSearchClearButton()
                ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','19',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker clicks on clear button to reset keyword search parameters")
                docsutil.insertImageInDocx(self.document,ss19_location)

                FWPendingDict,DAApprovedDict,FWCompletedDict,DARejectedDict,SURejectedDict,SUApprovedDict=self.dpms.getSerialNumberAndMemberForAllStatusTypes(keywordSearchExtractDataFrame)

                if FWPendingDict != "Null":
                    FWserialNumber=FWPendingDict.get('SerialNumber')
                    FWmemberName=FWPendingDict.get('MemberName')
                    self.dplp.clickUpdateFromMenu()
                    self.dpu.enterSerialNumber(FWserialNumber)
                    self.dpu.clickUpdateSearchButton()
                    time.sleep(2)
                    #self.dpu.clickUpdateUpdateButton()
                else:
                    pass



            self.dplp.clickLogoutButton()
            self.logging.info("Field Worker clicks on the logout button")
            self.dplp.waitForLoginPageAfterLogout()
            self.logging.info("Returns to the Initial Login Page")
            ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work Master Search Page - Keyword Search','20',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker returns to the login page on successful log out")
            docsutil.insertImageInDocx(self.document,ss20_location)

            self.logging.info("Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Tab - Pass")
            time.sleep(2)
            #self.dpms.validateExtractKeywordSearchData(self,keywordSearchExtractDataFrame,keywordSearchDataExtractFilePath,testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName)
            self.driver.close()
            docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Tab")

            assert True,"Successfully Validated Test Case - 002 - Test DpWork Master Search Page  - Keyword Search - Pass"            
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 002 - Test DpWork Master Search Page  - Keyword Search Page")
            raise CustomException(e,sys)