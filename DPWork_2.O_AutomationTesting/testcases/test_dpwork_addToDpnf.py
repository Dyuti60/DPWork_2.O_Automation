import pytest
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_loginpage_2_O import DpWorkLoginPage
from pageObjects.add_to_DPNF_2_O import AddToDPNF
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
birthYear_Dpnf,birthMonth_Dpnf,birthDate_Dpnf,dikshaYear_Dpnf,dikshaMonth_Dpnf,dikhaDay_Dpnf,comment_Dpnf,alreadyDpnfed_dpnf,TestCaseName_Dpnf,memberAlreadyUpdatedStatus_dpnf



class Test_002_MasterSearch:
    
    dot_env_filepath=os.getcwd()+'\\'+projectName+dot_env_file
    dpwork_url=readConfig.getDpWorkUrl()
    logging,log_file=LogGen.loggen()
    
    load_dotenv(dot_env_filepath)

    field_worker_username = os.getenv('field_worker_username')
    field_worker_password = os.getenv('field_worker_password')

    #sender=readConfig.getEmailSender()
    addToDpnf_Screenshot_folderName=dpwork_addToDpnf_Screenshot_folder
    addToDpnf_documentation_fileName=dpwork_addToDpnf_documentation_filename


    document=docsutil.createDocxFile()
    docsutil.addMainHeading(document,"DP Work DPNF- Add to DPNF - Functionality Testing Documentation")

    screenshot_location=docsutil.createDedicatedSSFolder(dpwork_addToDpnf_Screenshot_folder)
    
    emailSender=os.getenv('emailSender')
    emailSenderPassword=os.getenv('senderEmailPassword')
    receiversTo=readConfig.getEmailTOReceivers()
    receiversCC=readConfig.getEmailCCReceivers()


    addToDpnf_page_logs_attachment_filepath=os.getcwd()+"\\logs\\"+log_file+"\\"+log_file
    dpnf_testData_FilePath=os.getcwd()+"\\DPWork_2.O_AutomationTesting\\testdata\\"+dpnf_testDataFile


    def test_DpWorkAddToDPNF(self, setup):
        try:
            self.logging.info("Test Begins")
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.driver.get(self.dpwork_url)
            self.logging.info("Surfing to DpWork login page")
            time.sleep(2)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.dpnf_testData_FilePath,sheetName=addToDpnfSheetName)
            addToDpnfTestDataDict,addToDpnffieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)
            self.logging.info("Data taken from Test Data file")

            self.dplp=DpWorkLoginPage(self.driver)
            self.dtdpnf=AddToDPNF(self.driver)
            self.dplp.waitForLoginPage()

            ss00_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF - Add To DPNF','00',self.driver)
            docsutil.addMediumHeading(self.document,"Test Case - 001 - Test DpWork DPNF: Add To DPNF Page for A FW - Happy Path")
            docsutil.appendContentWithBlueColor(self.document,"DP Work DPNF Page - Add To DPNF: Test Case - 001 - Begins:")
            docsutil.insertImageInDocx(self.document,ss00_location)

            self.dplp.setDpWorkUserName(self.field_worker_username)
            self.logging.info("Username Entered- {}".format(self.field_worker_username))
            self.dplp.setDpWorkPassword(self.field_worker_password)
            self.logging.info("Corresponding Password Entered")

            ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','01',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Enters User Name and Password")
            docsutil.appendContent(self.document,"DP worker valid username - {}".format(self.field_worker_username))
            docsutil.appendContent(self.document,"DP worker valid password - **************")
            docsutil.insertImageInDocx(self.document,ss01_location)

            self.dplp.clickLoginButton()
            self.logging.info("Click on login button")
            self.logging.info("Member clicks on login button")
            time.sleep(2)

            ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','02',self.driver)
            docsutil.addSmallHeading(self.document,"Field Worker Clicks on Login Button")
            docsutil.insertImageInDocx(self.document,ss02_location)
            
            for index in range(addToDpnffieldValues_length):
                self.driver.refresh()
                self.dtdpnf.clickDPNFFromNavigationPanel()
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','03',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks DPNF Module from the Navigation Panel on the right")
                docsutil.insertImageInDocx(self.document,ss03_location)

                self.dtdpnf.clickAddtoDPNF()
                ss03A_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','03A',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker Clicks on Add to DPNF button to add member")
                docsutil.insertImageInDocx(self.document,ss03A_location)
            
            
                filenamePrefix=list(addToDpnfTestDataDict[TestCaseName_Dpnf])[index]
                self.dtdpnf.enterMemberFirstName(MemberFirstName=list(addToDpnfTestDataDict[MemberFirstName_Dpnf])[index])
                ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','04',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's First Name")
                docsutil.insertImageInDocx(self.document,ss04_location)

                self.dtdpnf.enterMemberMiddleName(MemberMiddleName=list(addToDpnfTestDataDict[MemberMiddleName_Dpnf])[index])
                ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','05',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Middle Name")
                docsutil.insertImageInDocx(self.document,ss05_location)

                self.dtdpnf.enterMemberLastName(MemberLastName=list(addToDpnfTestDataDict[MemberLastName_Dpnf])[index])
                ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','06',self.driver)
                docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Last Name")
                docsutil.insertImageInDocx(self.document,ss06_location)

                if str(list(addToDpnfTestDataDict[alreadyDpnfed_dpnf])[index]).lower()=='no':
                    self.dtdpnf.enterFamilyCode(FamilyCode=list(addToDpnfTestDataDict[FamilyCode_Dpnf])[index],\
                                                PhilMemberName=list(addToDpnfTestDataDict[PhilMemberName_Dpnf])[index],\
                                                MemberFirstName=list(addToDpnfTestDataDict[MemberFirstName_Dpnf])[index],\
                                                MemberMiddleName=list(addToDpnfTestDataDict[MemberMiddleName_Dpnf])[index],\
                                                MemberLastName=list(addToDpnfTestDataDict[MemberLastName_Dpnf])[index])
                    time.sleep(12)
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','10',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Family Code if any and maps with Philantropy Member Name")
                    docsutil.insertImageInDocx(self.document,ss10_location)

                    self.dtdpnf.enterGuardianFirstName(GuardianFirstName=list(addToDpnfTestDataDict[GuardianFirstName_Dpnf])[index])
                    ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','07',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's First Name")
                    docsutil.insertImageInDocx(self.document,ss07_location)

                    self.dtdpnf.enterGuardianMiddleName(GuardianMiddleName=list(addToDpnfTestDataDict[GuardianMiddleName_Dpnf])[index])
                    ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','08',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's Middle Name")
                    docsutil.insertImageInDocx(self.document,ss08_location)

                    self.dtdpnf.enterGuardianLastName(GuardianLastName=list(addToDpnfTestDataDict[GuardianLastName_Dpnf])[index])
                    ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','09',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Guardian's Last Name")
                    docsutil.insertImageInDocx(self.document,ss09_location)
                    
                    genderType_value=self.dtdpnf.enterGender(genderType=list(addToDpnfTestDataDict[GenderType_Dpnf])[index])
                    ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','11',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Gender")
                    docsutil.insertImageInDocx(self.document,ss11_location)

                    self.dtdpnf.enterMaritalStatus(maritalStatus=list(addToDpnfTestDataDict[MaritalStatus_Dpnf])[index],\
                                                genderType=genderType_value,\
                                                    husbandFirstName=list(addToDpnfTestDataDict[HusbandFirstName_Dpnf])[index],\
                                                    husbandMiddleName=list(addToDpnfTestDataDict[HusbandMiddleName_Dpnf])[index],\
                                                    husbandLastName=list(addToDpnfTestDataDict[HusbandLastName_Dpnf])[index])
                    ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','12',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Marital Status and Husband details if any")
                    docsutil.insertImageInDocx(self.document,ss12_location)

                    self.dtdpnf.enterContactNumber(contactNumber=list(addToDpnfTestDataDict[ContactNumber_Dpnf])[index])
                    ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','13',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Contact Number")
                    docsutil.insertImageInDocx(self.document,ss13_location)

                    self.dtdpnf.clickNextButtonDPNF()
                    ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','14',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Personal Information and click on Next Button")
                    docsutil.insertImageInDocx(self.document,ss14_location)

                    self.dtdpnf.enterDikhaAddress(dikshaAddress=list(addToDpnfTestDataDict[DikshaAddress_Dpnf])[index])
                    ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','15',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Address")
                    docsutil.insertImageInDocx(self.document,ss15_location)

                    self.dtdpnf.enterDikshaLandmark(dikshaLandmark=list(addToDpnfTestDataDict[DikshaLandmark_Dpnf])[index])
                    ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','16',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Landmark")
                    docsutil.insertImageInDocx(self.document,ss16_location)

                    self.dtdpnf.enterDikshaPincode(dikshaPincode=list(addToDpnfTestDataDict[DikshaPincode_Dpnf])[index])
                    ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','17',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Pncode")
                    docsutil.insertImageInDocx(self.document,ss07_location)

                    self.dtdpnf.enterPresentAddress(presentAddress=list(addToDpnfTestDataDict[PresentAddress_Dpnf])[index])
                    ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','18',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Address")
                    docsutil.insertImageInDocx(self.document,ss18_location)

                    self.dtdpnf.enterPresentLandmark(presentLandmark=list(addToDpnfTestDataDict[PresentLandmark_Dpnf])[index])
                    ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','19',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Landmark")
                    docsutil.insertImageInDocx(self.document,ss19_location)

                    self.dtdpnf.enterPresentPincode(presentPincode=list(addToDpnfTestDataDict[PresentPincode_Dpnf])[index])
                    ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','20',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Pincode")
                    docsutil.insertImageInDocx(self.document,ss20_location)

                    self.dtdpnf.enterPresentPostOffice(presentPostOffice=list(addToDpnfTestDataDict[PresentPostOffice_Dpnf])[index])
                    ss21_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','21',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Present Post Office")
                    docsutil.insertImageInDocx(self.document,ss21_location)

                    self.dtdpnf.clickCheckboxAndEnterPermanentAddress(checkboxStatus=list(addToDpnfTestDataDict[checkboxStatus_Dpnf])[index],\
                                                                    permanentAddress=list(addToDpnfTestDataDict[PermanentAddress_Dpnf])[index],\
                                                                    PermanentLandmark=list(addToDpnfTestDataDict[PermanentLandmark_Dpnf])[index],\
                                                                    PermanentPincode=list(addToDpnfTestDataDict[PermanentPincode_Dpnf])[index],\
                                                                    PermanentPO=list(addToDpnfTestDataDict[PermanentPostOffice_Dpnf])[index])
                    ss22_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','22',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Permanent Address Details")
                    docsutil.insertImageInDocx(self.document,ss22_location)

                    self.dtdpnf.clickNextButtonDPNF()
                    ss23_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','23',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's clicks on Next Button to move to Date and Summary Info")
                    docsutil.insertImageInDocx(self.document,ss23_location)

                    self.dtdpnf.enterDateOfBirth(birthYear=list(addToDpnfTestDataDict[birthYear_Dpnf])[index],
                                                birthMonth=list(addToDpnfTestDataDict[birthMonth_Dpnf])[index],
                                                birthDate=list(addToDpnfTestDataDict[birthDate_Dpnf])[index])
                    ss24_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','24',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Date of Birth")
                    docsutil.insertImageInDocx(self.document,ss24_location)

                    self.dtdpnf.enterDikshaYear(dikshaYear=list(addToDpnfTestDataDict[dikshaYear_Dpnf])[index],
                                                dikshaMonth=list(addToDpnfTestDataDict[dikshaMonth_Dpnf])[index],
                                                dikhaDay=list(addToDpnfTestDataDict[dikhaDay_Dpnf])[index])
                    ss25_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','25',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Diksha Date")
                    docsutil.insertImageInDocx(self.document,ss25_location)

                    self.dtdpnf.enterDpnfComment(comment=list(addToDpnfTestDataDict[comment_Dpnf])[index])
                    ss26_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','26',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's DPNF Comment")
                    docsutil.insertImageInDocx(self.document,ss26_location)

                    self.dtdpnf.navigateToPersonalInfoPage()
                    ss27_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','27',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Personal Info Title to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss27_location)

                    self.dtdpnf.navigateToAddressInfoPage()
                    ss28_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','28',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Address Info Title to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss28_location)

                    #self.dtdpnf.navigateToDateAndSummarypage()
                    self.dtdpnf.clickNextButtonDPNF()
                    ss29_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','29',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker clicks Date and Summary Page to navigate to that page")
                    docsutil.insertImageInDocx(self.document,ss29_location)

                    memberAlreadyUpdated=list(addToDpnfTestDataDict[memberAlreadyUpdatedStatus_dpnf])[index]
                    submitStatus=self.dtdpnf.clickSubmitAddToDPNF(memberAlreadyUpdated)
                    if submitStatus=="False":
                        ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','30',self.driver)
                        docsutil.addSmallHeading(self.document,"Field Worker clicks on Add to DPNF submit button")
                        docsutil.insertImageInDocx(self.document,ss30_location)
                        docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF ")
                        docsutil.saveDocument(self.document,str(self.addToDpnf_documentation_fileName)+"-TC-"+str(filenamePrefix))
                        assert False
                        
                    elif submitStatus=="alreadyUpdated":
                        ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','30',self.driver)
                        docsutil.addSmallHeading(self.document,"Field Worker clicks on Add to DPNF submit button")
                        docsutil.insertImageInDocx(self.document,ss30_location)
                        docsutil.appendContentWithPassColor(self.document,"Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF ")
                        docsutil.saveDocument(self.document,str(self.addToDpnf_documentation_fileName)+"-TC-"+str(filenamePrefix))
                        assert True
                    
                    else:
                        self.dtdpnf.clickDoneSuccessButton()
                        ss31_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','31',self.driver)
                        docsutil.addSmallHeading(self.document,"Field Worker clicks on Done success button")
                        docsutil.insertImageInDocx(self.document,ss31_location)


                        self.logging.info("Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF - Pass")
                        time.sleep(2)
                        #self.dpms.validateExtractKeywordSearchData(self,keywordSearchExtractDataFrame,keywordSearchDataExtractFilePath,testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName)
                        
                        docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF ")
                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.addToDpnf_documentation_fileName))
                        assert True

                if str(list(addToDpnfTestDataDict[alreadyDpnfed_dpnf])[index]).lower()=='yes':
                    print(list(addToDpnfTestDataDict[FamilyCode_Dpnf])[index])
                    self.dtdpnf.enterFamilyCodeForAlreadyDpnfed(FamilyCode=list(addToDpnfTestDataDict[FamilyCode_Dpnf])[index],\
                                                            PhilMemberName=list(addToDpnfTestDataDict[PhilMemberName_Dpnf])[index])
                    time.sleep(12)
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'DP Work DPNF Page - Add To DPNF','10',self.driver)
                    docsutil.addSmallHeading(self.document,"Field Worker enters DPNF Member's Family Code if any and maps with Philantropy Member Name")
                    docsutil.insertImageInDocx(self.document,ss10_location)

                    self.logging.info("Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF - Pass")
                    time.sleep(2)
                    #self.dpms.validateExtractKeywordSearchData(self,keywordSearchExtractDataFrame,keywordSearchDataExtractFilePath,testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName)
                    
                    docsutil.appendContentWithPassColor(self.document,"Successfully Validated Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF ")
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.addToDpnf_documentation_fileName))
                    assert True

            self.driver.close()
        except Exception as e:
            docsutil.appendContentWithFailColor(self.document,"Test Case - 001 - Test DpWork DPNF Page  - Add To DPNF ")
            raise CustomException(e,sys)