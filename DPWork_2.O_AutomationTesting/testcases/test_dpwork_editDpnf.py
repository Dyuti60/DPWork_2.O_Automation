import pytest
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.edit_remove_moreDetails_DPNF_2_O import EditDPNF
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
from configurations.constants import dpwork_addToDpnf_Screenshot_folder,dpwork_addToDpnf_documentation_filename,\
addToDpnf_htmlReportFile,dpwork_editDpnf_Screenshot_folder,dpwork_editDpnf_documentation_filename,\
editDpnf_htmlReportFile,addToDpnfSheetName,editDpnfSheetName,dpnf_testDataFile,parametersFields,fieldValues
from configurations.constants import MemberFirstName_Dpnf,MemberMiddleName_Dpnf,MemberLastName_Dpnf,GuardianFirstName_Dpnf,\
GuardianMiddleName_Dpnf,GuardianLastName_Dpnf,HusbandFirstName_Dpnf,HusbandMiddleName_Dpnf,HusbandLastName_Dpnf,\
FamilyCode_Dpnf,PhilMemberName_Dpnf,ContactNumber_Dpnf,GenderType_Dpnf,MaritalStatus_Dpnf,DikshaAddress_Dpnf,\
DikshaLandmark_Dpnf,DikshaPincode_Dpnf,PresentAddress_Dpnf,PresentLandmark_Dpnf,PresentPincode_Dpnf,PresentPostOffice_Dpnf,\
PermanentAddress_Dpnf,PermanentLandmark_Dpnf,PermanentPincode_Dpnf,PermanentPostOffice_Dpnf,checkboxStatus_Dpnf,\
birthYear_Dpnf,birthMonth_Dpnf,birthDate_Dpnf,dikshaYear_Dpnf,dikshaMonth_Dpnf,dikhaDay_Dpnf,comment_Dpnf,alreadyDpnfed_dpnf



class Test_002_MasterSearch:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    field_worker_username = os.getenv('field_worker_username')
    field_worker_password = os.getenv('field_worker_password')

    #sender=readConfig.getEmailSender()
    editDpnf_Screenshot_folderName=dpwork_editDpnf_Screenshot_folder
    editDpnf_documentation_fileName=dpwork_editDpnf_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work DPNF- Edit DPNF - Functionality Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(editDpnf_Screenshot_folderName)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()


    addToDpnf_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    dpnf_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+dpnf_testDataFile


    def test_DpWorkEditDPNF(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.dpnf_testData_FilePath,sheetName=editDpnfSheetName)
            editDpnfTestDataDict,editDpnffieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)
            self.logging.info("Data taken from Test Data file")

            self.dplp=DpWorkLoginPage(self.driver)
            self.edpnf=EditDPNF(self.driver)
            self.dplp.waitForLoginPage()

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF - Edit DPNF','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork DPNF: Edit DPNF Page for A FW - Happy Path")
            docsutil.appendContentWithBlueColor(self.document,"DP Work DPNF Page - Edit DPNF: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            self.logging.info("Member clicks on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)
        
            self.edpnf.clickDPNFFromNavigationPanel()
            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','03',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks DPNF Module from the Navigation Panel on the right")
            docsutil.insertImageInDocx(self.document,ss03_location)

            for index in range(editDpnffieldValues_length):
                removeEnabledDpnfRecords,editEnabledDpnfRecords=self.edpnf.iterateOverEachRecord()
                print(editEnabledDpnfRecords)
                self.edpnf.clickEditEnabledDpnfRecord(editEnabledDpnfRecords,0)
                ss03A_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','03A',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Edit DPNF button to edit already dpnfed records")
                docsutil.insertImageInDocx(self.document,ss03A_location)
                

                self.edpnf.enterMemberFirstName(MemberFirstName=list(editDpnfTestDataDict[MemberFirstName_Dpnf])[index])
                ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','04',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's First Name")
                docsutil.insertImageInDocx(self.document,ss04_location)

                self.edpnf.enterMemberMiddleName(MemberMiddleName=list(editDpnfTestDataDict[MemberMiddleName_Dpnf])[index])
                ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','05',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Middle Name")
                docsutil.insertImageInDocx(self.document,ss05_location)

                self.edpnf.enterMemberLastName(MemberLastName=list(editDpnfTestDataDict[MemberLastName_Dpnf])[index])
                ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','06',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Last Name")
                docsutil.insertImageInDocx(self.document,ss06_location)

                self.edpnf.enterGuardianFirstName(GuardianFirstName=list(editDpnfTestDataDict[GuardianFirstName_Dpnf])[index])
                ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','07',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's First Name")
                docsutil.insertImageInDocx(self.document,ss07_location)

                self.edpnf.enterGuardianMiddleName(GuardianMiddleName=list(editDpnfTestDataDict[GuardianMiddleName_Dpnf])[index])
                ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','08',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's Middle Name")
                docsutil.insertImageInDocx(self.document,ss08_location)

                self.edpnf.enterGuardianLastName(GuardianLastName=list(editDpnfTestDataDict[GuardianLastName_Dpnf])[index])
                ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','09',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's Last Name")
                docsutil.insertImageInDocx(self.document,ss09_location)
                
                if str(alreadyDpnfed_dpnf).lower()!='yes':
                    self.edpnf.enterFamilyCode(FamilyCode=list(editDpnfTestDataDict[FamilyCode_Dpnf])[index],\
                                                PhilMemberName=list(editDpnfTestDataDict[PhilMemberName_Dpnf])[index],\
                                                MemberFirstName=list(editDpnfTestDataDict[MemberFirstName_Dpnf])[index],\
                                                MemberMiddleName=list(editDpnfTestDataDict[MemberMiddleName_Dpnf])[index],\
                                                MemberLastName=list(editDpnfTestDataDict[MemberLastName_Dpnf])[index])
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','10',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Family Code if any and maps with Philantropy Member Name")
                    docsutil.insertImageInDocx(self.document,ss10_location)
                    
                    genderType_value=self.edpnf.enterGender(genderType=list(editDpnfTestDataDict[GenderType_Dpnf])[index])
                    ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','11',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Gender")
                    docsutil.insertImageInDocx(self.document,ss11_location)

                    self.edpnf.enterMaritalStatus(maritalStatus=list(editDpnfTestDataDict[MaritalStatus_Dpnf])[index],\
                                                genderType=genderType_value,\
                                                    husbandFirstName=list(editDpnfTestDataDict[HusbandFirstName_Dpnf])[index],\
                                                    husbandMiddleName=list(editDpnfTestDataDict[HusbandMiddleName_Dpnf])[index],\
                                                    husbandLastName=list(editDpnfTestDataDict[HusbandLastName_Dpnf])[index])
                    ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','12',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Marital Status and Husband details if any")
                    docsutil.insertImageInDocx(self.document,ss12_location)

                    self.edpnf.enterContactNumber(contactNumber=list(editDpnfTestDataDict[ContactNumber_Dpnf])[index])
                    ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','13',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Contact Number")
                    docsutil.insertImageInDocx(self.document,ss13_location)

                    self.edpnf.clickNextButtonDPNF()
                    ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','14',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Personal Information and click on Next Button")
                    docsutil.insertImageInDocx(self.document,ss14_location)

                    self.edpnf.enterDikhaAddress(dikshaAddress=list(editDpnfTestDataDict[DikshaAddress_Dpnf])[index])
                    ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','15',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Address")
                    docsutil.insertImageInDocx(self.document,ss15_location)

                    self.edpnf.enterDikshaLandmark(dikshaLandmark=list(editDpnfTestDataDict[DikshaLandmark_Dpnf])[index])
                    ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','16',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Landmark")
                    docsutil.insertImageInDocx(self.document,ss16_location)

                    self.edpnf.enterDikshaPincode(dikshaPincode=list(editDpnfTestDataDict[DikshaPincode_Dpnf])[index])
                    ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','17',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Pncode")
                    docsutil.insertImageInDocx(self.document,ss07_location)

                    self.edpnf.enterPresentAddress(presentAddress=list(editDpnfTestDataDict[PresentAddress_Dpnf])[index])
                    ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','18',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Address")
                    docsutil.insertImageInDocx(self.document,ss18_location)

                    self.edpnf.enterPresentLandmark(presentLandmark=list(editDpnfTestDataDict[PresentLandmark_Dpnf])[index])
                    ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','19',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Landmark")
                    docsutil.insertImageInDocx(self.document,ss19_location)

                    self.edpnf.enterPresentPincode(presentPincode=list(editDpnfTestDataDict[PresentPincode_Dpnf])[index])
                    ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','20',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Pincode")
                    docsutil.insertImageInDocx(self.document,ss20_location)

                    self.edpnf.enterPresentPostOffice(presentPostOffice=list(editDpnfTestDataDict[PresentPostOffice_Dpnf])[index])
                    ss21_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','21',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Post Office")
                    docsutil.insertImageInDocx(self.document,ss21_location)

                    self.edpnf.clickCheckboxAndEnterPermanentAddress(checkboxStatus=list(editDpnfTestDataDict[checkboxStatus_Dpnf])[index],\
                                                                    permanentAddress=list(editDpnfTestDataDict[PermanentAddress_Dpnf])[index],\
                                                                    PermanentLandmark=list(editDpnfTestDataDict[PermanentLandmark_Dpnf])[index],\
                                                                    PermanentPincode=list(editDpnfTestDataDict[PermanentPincode_Dpnf])[index],\
                                                                    PermanentPO=list(editDpnfTestDataDict[PermanentPostOffice_Dpnf])[index])
                    ss22_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','22',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Permanent Address Details")
                    docsutil.insertImageInDocx(self.document,ss22_location)

                    self.edpnf.clickNextButtonDPNF()
                    ss23_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','23',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's clicks on Next Button to move to Date and Summary Info")
                    docsutil.insertImageInDocx(self.document,ss23_location)

                    self.edpnf.enterDateOfBirth(birthYear=list(editDpnfTestDataDict[birthYear_Dpnf])[index],
                                                birthMonth=list(editDpnfTestDataDict[birthMonth_Dpnf])[index],
                                                birthDate=list(editDpnfTestDataDict[birthDate_Dpnf])[index])
                    ss24_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','24',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Date of Birth")
                    docsutil.insertImageInDocx(self.document,ss24_location)

                    self.edpnf.enterDikshaYear(dikshaYear=list(editDpnfTestDataDict[dikshaYear_Dpnf])[index],
                                                dikshaMonth=list(editDpnfTestDataDict[dikshaMonth_Dpnf])[index],
                                                dikhaDay=list(editDpnfTestDataDict[dikhaDay_Dpnf])[index])
                    ss25_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','25',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Date")
                    docsutil.insertImageInDocx(self.document,ss25_location)

                    self.edpnf.enterDpnfComment(comment=list(editDpnfTestDataDict[comment_Dpnf])[index])
                    ss26_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','26',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's DPNF Comment")
                    docsutil.insertImageInDocx(self.document,ss26_location)

                    self.edpnf.navigateToPersonalInfoPage()
                    ss27_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','27',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Personal Info Title to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss27_location)

                    self.edpnf.navigateToAddressInfoPage()
                    ss28_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','28',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Address Info Title to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss28_location)

                    #self.edpnf.navigateToDateAndSummarypage()
                    self.edpnf.clickNextButtonDPNF()
                    ss29_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','29',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Date and Summary Page to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss29_location)

                    self.edpnf.clickSubmitAddToDPNF()
                    ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','30',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks on Edit DPNF submit button")
                    docsutil.insertImageInDocx(self.document,ss30_location)

                    self.edpnf.clickDoneSuccessButton()
                    ss31_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','31',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks on Done success button")
                    docsutil.insertImageInDocx(self.document,ss31_location)


                    self.logging.info("Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Edit DPNF - Pass")
                    time.sleep(2)
                    #self.dpms.validateExtractKeywordSearchData(self,keywordSearchExtractDataFrame,keywordSearchDataExtractFilePath,testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName)
                else:
                    self.edpnf.enterFamilyCodeForAlreadyDpnfed(FamilyCode=list(editDpnfTestDataDict[FamilyCode_Dpnf])[index],\
                                PhilMemberName=list(editDpnfTestDataDict[PhilMemberName_Dpnf])[index])
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Edit DPNF','10',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Family Code if any and maps with Philantropy Member Name")
                    docsutil.insertImageInDocx(self.document,ss10_location)
                
                self.driver.close()
                docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Edit DPNF ")
                docsutil.saveDocument(self.document,self.editDpnf_documentation_fileName)
            

        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork DPNF Page  - Edit DPNF ")
            raise CustomException(e,sys)