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
    '''
    def test_serialNumberUpdateActiveMemberByFW(self,setup):
        try:
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpup=DpWorkUpdatePage(self.driver)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.updateSerialNumber_testData_FilePath,sheetName=updateSerialNumberActiveSheetName1)
            updateSerialNumberActiveMemberTestDataDict,updateSerialNumberfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)
            self.logging.info("Read Data from test data file")
            docsutil.addMediumHeading(self.document,"Test Case - Update Serial Number Functionality")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Update: Test Case - Begins:")
            index=0
            

            for index in range(updateSerialNumberfieldValues_length):
                self.logging.info("Iterate Over the Test Driven Test Cases")
                self.driver.get(self.dpwork_url)
                self.logging.info("Surfing to DpWork login page")

                time.sleep(2)
                

                filenamePrefix=list(updateSerialNumberActiveMemberTestDataDict[update_testCaseName])[index]
                self.logging.info("Test Case Name: {}".format(str(filenamePrefix)))
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','01',self.driver)
                docsutil.addSmallHeading(self.document,"Test Case -{}- Update Serial Number Active".format(filenamePrefix))
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dplp.setDpWorkUserName(self.field_worker_username)
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','02',self.driver)
                docsutil.addSmallHeading(self.document,"User enters username -{} to login".format(self.field_worker_username))
                docsutil.insertImageInDocx(self.document,ss02_location)
                self.logging.info("User enters username -{} to login".format(self.field_worker_username))

                self.dplp.setDpWorkPassword(self.field_worker_password)
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','03',self.driver)
                docsutil.addSmallHeading(self.document,"User enters corresponding password *********")
                docsutil.insertImageInDocx(self.document,ss03_location)
                self.logging.info("User enters corresponding password *********")

                self.dplp.clickLoginButton()
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','04',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on login button")
                docsutil.insertImageInDocx(self.document,ss03_location)
                self.logging.info("User clicks on login button")

                self.dpup.clickUpdateFromNavigationPanel()
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','05',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on Update Option from the Navigation Panel")
                docsutil.insertImageInDocx(self.document,ss03_location)
                self.logging.info("User clicks on Update Option from the Navigation Panel")

                if(self.dpup.CheckForText_Search_by_member_id() and self.dpup.CheckForText_Update_Title() and self.dpup.CheckForButton_Clear() and self.dpup.CheckForButton_Search()):
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','06',self.driver)
                    docsutil.addSmallHeading(self.document,"User checks for Update Page Contents and validates")
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User checks for Update Page Contents and validates")

                    self.dpup.enterSerialNumber(list(updateSerialNumberActiveMemberTestDataDict[update_serialNumber])[index])
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','07',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters serial number to update")
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User enters serial number to update")

                    self.dpup.clickUpdateClearButton()
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','08',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on clear button, to clear the entered Serial number")
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User clicks on clear button, to clear the entered Serial number")

                    self.dpup.enterSerialNumber(list(updateSerialNumberActiveMemberTestDataDict[update_serialNumber])[index])
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','09',self.driver)
                    docsutil.addSmallHeading(self.document,"User again enters the same serial number to update")
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User again enters the same serial number to update")


                    self.dpup.clickUpdateSearchButton()
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','10',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on search button to update the serial number")
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User clicks on search button to update the serial number")

                    updateStatus,memberName, memberGuardianName, memberAddress=self.dpup.fetchDataFromUpdateCard()
                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','11',self.driver)
                    docsutil.addSmallHeading(self.document,"User gets update of the serial number searched: memberName-{}, updateStatus-{}, memberGuardianName-{}".format(memberName,updateStatus, memberGuardianName))
                    docsutil.insertImageInDocx(self.document,ss03_location)
                    self.logging.info("User gets update of the serial number searched: memberName-{}, updateStatus-{}, memberGuardianName-{}".format(memberName,updateStatus, memberGuardianName))
                    
                    if self.dpup.validateUpdateStatus(updateStatus):
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','12',self.driver)
                        docsutil.addSmallHeading(self.document,"User validates that the serial number is yet to be updated")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User validates that the serial number is yet to be updated")

                        self.dpup.clickUpdateUpdateButton()
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','13',self.driver)
                        docsutil.addSmallHeading(self.document,"User clicks on Update Button")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User clicks on Update Button")

                        self.dpup.enterSuggestedMemberName(list(updateSerialNumberActiveMemberTestDataDict[update_suggestedMemberName])[index])
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','14',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested member name")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User enters the suggested member name")

                        self.dpup.enterSuggestedGuardianName(list(updateSerialNumberActiveMemberTestDataDict[update_suggestedGuardianName])[index])
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','15',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested guardian name")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User enters the suggested guardian name")

                        self.dpup.enterSuggestedRitwikName(list(updateSerialNumberActiveMemberTestDataDict[update_suggestedRitwikName])[index])
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','16',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested Ritwik name")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User enters the suggested Ritwik name")

                        self.dpup.clickNextButton()
                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','17',self.driver)
                        docsutil.addSmallHeading(self.document,"User clicks on next button")
                        docsutil.insertImageInDocx(self.document,ss03_location)
                        self.logging.info("User clicks on next button")

                        if self.dpup.checkInitiationInformationErrorMessage(dikshayatriStatus='',familyCode='',phoneNumber=''):
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','18',self.driver)
                            docsutil.addSmallHeading(self.document,"User validates the error message thrown for each mandatory field in Initiation Information page")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User validates the error message thrown for each mandatory field in Initiation Information page")

                            self.dpup.enterDikshayarthiStatus(list(updateSerialNumberActiveMemberTestDataDict[update_dikshayarthiStatus])[index])
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','19',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the dikshayarthi status as Active")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User enters the dikshayarthi status as Active")

                            self.dpup.enterPhoneNumber(list(updateSerialNumberActiveMemberTestDataDict[update_phoneNumber])[index])
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','20',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters phone number")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User enters phone number")

                            self.dpup.enterFamilyCode(list(updateSerialNumberActiveMemberTestDataDict[update_familyCode])[index],list(updateSerialNumberActiveMemberTestDataDict[update_philMemberName])[index])
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','21',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters family code")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User enters family code")

                            self.dpup.enterEmailAddress(list(updateSerialNumberActiveMemberTestDataDict[update_emailAddress])[index])
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','22',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters email address")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User enters email address")

                            self.dpup.clickNextButton()
                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','23',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on Next Button")
                            docsutil.insertImageInDocx(self.document,ss03_location)
                            self.logging.info("User clicks on Next Button")

                            if self.dpup.checkPermanentAddressInformationErrorHandling(permanentAddress='',permanentLandmark='',permanentPincode='',permanentPostoffice=''):
                                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','24',self.driver)
                                docsutil.addSmallHeading(self.document,"User checks the permanent address section and validates the contents")
                                docsutil.insertImageInDocx(self.document,ss03_location)
                                self.logging.info("User checks the permanent address section and validates the contents")

                                self.dpup.enterPermanentAddress(list(updateSerialNumberActiveMemberTestDataDict[update_permanentAddress])[index])
                                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','25',self.driver)
                                docsutil.addSmallHeading(self.document,"User checks the permanent address section and validates the contents")
                                docsutil.insertImageInDocx(self.document,ss03_location)
                                self.logging.info("User enters the permanent address")

                                self.dpup.enterPermanentLandmark(list(updateSerialNumberActiveMemberTestDataDict[update_permanentLandmark])[index])
                                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','26',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters the permanent landmark")
                                docsutil.insertImageInDocx(self.document,ss03_location)
                                self.logging.info("User enters the permanent landmark")

                                self.dpup.enterPermanentPincode(list(updateSerialNumberActiveMemberTestDataDict[update_permanentPincode])[index])
                                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','27',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters the permanent pincode")
                                docsutil.insertImageInDocx(self.document,ss03_location)
                                self.logging.info("User enters the permanent pincode")

                                self.dpup.enterPermanentPostOffice(list(updateSerialNumberActiveMemberTestDataDict[update_permanentPostoffice])[index])
                                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','28',self.driver)
                                docsutil.addSmallHeading(self.document,"User selects the permanent post office")
                                docsutil.insertImageInDocx(self.document,ss03_location)
                                self.logging.info("User selects the permanent post office")

                                if self.dpup.checkPresentAddressInformationErrorHandling(checkBoxStatus='No',presentAddress='',presentLandmark='',presentPincode='',presentPostoffice=''):
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','29',self.driver)
                                    docsutil.addSmallHeading(self.document,"User checks the Present Address section and validates the contents")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User checks the Present Address section and validates the contents")

                                    self.dpup.enterPresentAddress(list(updateSerialNumberActiveMemberTestDataDict[update_presentAddress])[index])
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','30',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Address")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User enters the Present Address")

                                    self.dpup.enterPresentLandmark(list(updateSerialNumberActiveMemberTestDataDict[update_presentLandmark])[index])
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','31',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Landmark")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User enters the Present Landmark")

                                    self.dpup.enterPresentPincode(list(updateSerialNumberActiveMemberTestDataDict[update_presentPincode])[index])
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','32',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Pincode")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User enters the Present Pincode")

                                    self.dpup.enterPresentPostOffice(list(updateSerialNumberActiveMemberTestDataDict[update_presentPostoffice])[index])
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','33',self.driver)
                                    docsutil.addSmallHeading(self.document,"User selects the Present Post Office")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User selects the Present Post Office")

                                    self.dpup.clickNextButton()
                                    ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','34',self.driver)
                                    docsutil.addSmallHeading(self.document,"User clicks on Next Button")
                                    docsutil.insertImageInDocx(self.document,ss03_location)
                                    self.logging.info("User clicks on Next Button")

                                    if self.dpup.checkUpdateCommentErrorMessage(comment=''):
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','35',self.driver)
                                        docsutil.addSmallHeading(self.document,"User validates the comment screen content")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User validates the comment screen content")

                                        self.dpup.enterUpdateComment(list(updateSerialNumberActiveMemberTestDataDict[update_comments])[index])
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','36',self.driver)
                                        docsutil.addSmallHeading(self.document,"User enters the update comment")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User enters the update comment")
                                        time.sleep(2)

                                        self.dpup.clickPreviousButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','37',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Address page")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Previous Button to move to Address page")

                                        self.dpup.clickPreviousButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','38',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Initiation Page")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Previous Button to move to Initiation Page")

                                        self.dpup.clickPreviousButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','39',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Suggested Members Page")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Previous Button to move to Suggested Members Page")

                                        self.dpup.clickNextButton()
                                        self.dpup.clickNextButton()
                                        self.dpup.clickNextButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','40',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Next Button muliple times to move to comments page")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Next Button muliple times to move to comments page")

                                        self.dpup.clickUpdateSubmitButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','41',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Submit Button to update the changes made")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Submit Button to update the changes made")
                                        time.sleep(3)

                                        self.dpup.clickDoneButtonFromSuccessMessage()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','42',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Done Button from the Success Message Window")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Done Button from the Success Message Window")

                                        #self.driver.refresh()
                                        self.dpup.clickUpdateFromNavigationPanel()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','43',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Update from the Navigation Panel")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on Update from the Navigation Panel")

                                        self.dpup.enterSerialNumber(list(updateSerialNumberActiveMemberTestDataDict[update_serialNumber])[index])
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','44',self.driver)
                                        docsutil.addSmallHeading(self.document,"User enters the serial Number that has been updated by him -{}".format(list(updateSerialNumberActiveMemberTestDataDict[update_serialNumber])[index]))
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User enters the serial Number that has been updated by him -{}".format(list(updateSerialNumberActiveMemberTestDataDict[update_serialNumber])[index]))
                                        
                                        self.dpup.clickUpdateSearchButton()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','45',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on search button")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User clicks on search button")

                                        updateStatus,memberName, memberGuardianName, memberAddress=self.dpup.fetchDataFromUpdateCard()
                                        ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','46',self.driver)
                                        docsutil.addSmallHeading(self.document,"User checks the status of the serial number searched")
                                        docsutil.insertImageInDocx(self.document,ss03_location)
                                        self.logging.info("User checks the status of the serial number searched")

                                        if not self.dpup.validateUpdateStatus(updateStatus):
                                            ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','47',self.driver)
                                            docsutil.insertImageInDocx(self.document,ss03_location)
                                            docsutil.appendContentWithPassColor(self.document,"{} has been updated successfully having status- {}".format(memberName,updateStatus))
                                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                            self.logging.info("{} has been updated successfully having status- {}".format(memberName,updateStatus))
                                            self.driver.refresh()
                                        else:
                                            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','0F',self.driver)
                                            docsutil.appendContentWithFailColor(self.document,"Updating Member- {}  was not successful".format(memberName))
                                            docsutil.insertImageInDocx(self.document,ss0F_location)
                                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                            self.logging.info("Updating Member- {}  was not successful".format(memberName))
                                            assert False,"Updating Member- {}  was not successful".format(memberName)
                                    else:
                                        ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','1F',self.driver)
                                        docsutil.appendContentWithFailColor(self.document,"Update-- Invalid comment was not handled")
                                        docsutil.insertImageInDocx(self.document,ss0F_location)
                                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                        self.logging.info("Update-- Invalid comment was not handled")
                                        assert False,"Update-- Invalid comment was not handled"
                                else:
                                    ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','2F',self.driver)
                                    docsutil.appendContentWithFailColor(self.document,"Update - Present Address Section doesn't have the prerequisite contents")
                                    docsutil.insertImageInDocx(self.document,ss0F_location)
                                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                    self.logging.info("Update - Present Address Section doesn't have the prerequisite contents")
                                    assert False,"Update - Present Address Section doesn't have the prerequisite contents"
                            else:
                                ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','3F',self.driver)
                                docsutil.appendContentWithFailColor(self.document,"Update - Permanent Address Section doesn't have the prerequisite contents")
                                docsutil.insertImageInDocx(self.document,ss0F_location)
                                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                self.logging.info("Update - Permanent Address Section doesn't have the prerequisite contents")
                                assert False,"Update - Permanent Address Section doesn't have the prerequisite contents"
                        else:
                            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','4F',self.driver)
                            docsutil.appendContentWithFailColor(self.document,"Update - Initiation Infomation doesn't have the prerequisite contents")
                            docsutil.insertImageInDocx(self.document,ss0F_location)
                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                            self.logging.info("Update - Initiation Infomation doesn't have the prerequisite contents")
                            assert False,"Update - Initiation Infomation doesn't have the prerequisite contents"
                    else:
                        ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','5F',self.driver)
                        docsutil.appendContentWithFailColor(self.document,"Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus))
                        docsutil.insertImageInDocx(self.document,ss0F_location)
                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                        self.logging.info("Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus))
                        assert True,"Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus)
                else:
                    ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','6F',self.driver)
                    docsutil.appendContentWithFailColor(self.document,"Update Screen doesn't have the prerequisites content")
                    docsutil.insertImageInDocx(self.document,ss0F_location)
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                    self.logging.info("Update Screen doesn't have the prerequisites content")
                    assert False,"Update Screen doesn't have the prerequisites content"
                    
            self.driver.quit()
            self.logging.info("User closes all the browsers open")
        except Exception as e:
            filenamePrefix=list(updateSerialNumberActiveMemberTestDataDict[update_testCaseName])[index]
            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','7F',self.driver)
            docsutil.appendContentWithFailColor(self.document,"User faces somes exception on updating serial number")
            docsutil.insertImageInDocx(self.document,ss0F_location)
            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
            self.driver.quit()
            self.logging.info("User faces somes exception on updating serial number")
            raise CustomException(e,sys)
        '''
    def test_serialNumberUpdateInActiveMember(self,setup):
        try:
            self.driver=setup
            self.logging.info("Driver Initiated")
            self.driver.implicitly_wait(4)
            self.driver.maximize_window()
            self.dplp=DpWorkLoginPage(self.driver)
            self.dpup=DpWorkUpdatePage(self.driver)

            dataframe=XLUtils.convert_excelSheetIntoDataFrame(excelFilePath=self.updateSerialNumber_testData_FilePath,sheetName=updateSerialNumberInActiveSheetName2)
            updateSerialNumberInActiveMemberTestDataDict,updateSerialNumberfieldValues_length=XLUtils.ReturnDictionaryforselectedColumnsInDataframe(dataframe, ParameterField=parametersFields,FieldValues=fieldValues)
            self.logging.info("Read Data from test data file")
            docsutil.addMediumHeading(self.document,"Test Case - Update Serial Number Functionality")
            docsutil.appendContentWithBlueColor(self.document,"DP Work Update: Test Case - Begins:")
            
            index=0
            for index in range(updateSerialNumberfieldValues_length):
                self.logging.info("Iterate Over the Test Driven Test Cases")
                self.driver.get(self.dpwork_url)
                self.logging.info("Surfing to DpWork login page")

                time.sleep(2)
                

                filenamePrefix=list(updateSerialNumberInActiveMemberTestDataDict[update_testCaseName])[index]
                self.logging.info("Test Case Name: {}".format(str(filenamePrefix)))
                ss01_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','01',self.driver)
                docsutil.addSmallHeading(self.document,"Test Case -{}- Update Serial Number Active".format(filenamePrefix))
                docsutil.insertImageInDocx(self.document,ss01_location)

                self.dplp.setDpWorkUserName(self.field_worker_username)
                ss02_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','02',self.driver)
                docsutil.addSmallHeading(self.document,"User enters username -{} to login".format(self.field_worker_username))
                docsutil.insertImageInDocx(self.document,ss02_location)
                self.logging.info("User enters username -{} to login".format(self.field_worker_username))

                self.dplp.setDpWorkPassword(self.field_worker_password)
                ss03_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','03',self.driver)
                docsutil.addSmallHeading(self.document,"User enters corresponding password *********")
                docsutil.insertImageInDocx(self.document,ss03_location)
                self.logging.info("User enters corresponding password *********")

                self.dplp.clickLoginButton()
                ss04_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','04',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on login button")
                docsutil.insertImageInDocx(self.document,ss04_location)
                self.logging.info("User clicks on login button")

                self.dpup.clickUpdateFromNavigationPanel()
                ss05_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','05',self.driver)
                docsutil.addSmallHeading(self.document,"User clicks on Update Option from the Navigation Panel")
                docsutil.insertImageInDocx(self.document,ss05_location)
                self.logging.info("User clicks on Update Option from the Navigation Panel")

                if(self.dpup.CheckForText_Search_by_member_id() and self.dpup.CheckForText_Update_Title() and self.dpup.CheckForButton_Clear() and self.dpup.CheckForButton_Search()):
                    ss06_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','06',self.driver)
                    docsutil.addSmallHeading(self.document,"User checks for Update Page Contents and validates")
                    docsutil.insertImageInDocx(self.document,ss06_location)
                    self.logging.info("User checks for Update Page Contents and validates")

                    self.dpup.enterSerialNumber(list(updateSerialNumberInActiveMemberTestDataDict[update_serialNumber])[index])
                    ss07_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','07',self.driver)
                    docsutil.addSmallHeading(self.document,"User enters serial number to update")
                    docsutil.insertImageInDocx(self.document,ss07_location)
                    self.logging.info("User enters serial number to update")

                    self.dpup.clickUpdateClearButton()
                    ss08_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','08',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on clear button, to clear the entered Serial number")
                    docsutil.insertImageInDocx(self.document,ss08_location)
                    self.logging.info("User clicks on clear button, to clear the entered Serial number")

                    self.dpup.enterSerialNumber(list(updateSerialNumberInActiveMemberTestDataDict[update_serialNumber])[index])
                    ss09_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','09',self.driver)
                    docsutil.addSmallHeading(self.document,"User again enters the same serial number to update")
                    docsutil.insertImageInDocx(self.document,ss09_location)
                    self.logging.info("User again enters the same serial number to update")


                    self.dpup.clickUpdateSearchButton()
                    ss10_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Active','10',self.driver)
                    docsutil.addSmallHeading(self.document,"User clicks on search button to update the serial number")
                    docsutil.insertImageInDocx(self.document,ss10_location)
                    self.logging.info("User clicks on search button to update the serial number")

                    updateStatus,memberName, memberGuardianName, memberAddress=self.dpup.fetchDataFromUpdateCard()
                    ss11_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','11',self.driver)
                    docsutil.addSmallHeading(self.document,"User gets update of the serial number searched: memberName-{}, updateStatus-{}, memberGuardianName-{}".format(memberName,updateStatus, memberGuardianName))
                    docsutil.insertImageInDocx(self.document,ss11_location)
                    self.logging.info("User gets update of the serial number searched: memberName-{}, updateStatus-{}, memberGuardianName-{}".format(memberName,updateStatus, memberGuardianName))
                    
                    if self.dpup.validateUpdateStatus(updateStatus):
                        ss12_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','12',self.driver)
                        docsutil.addSmallHeading(self.document,"User validates that the serial number is yet to be updated")
                        docsutil.insertImageInDocx(self.document,ss12_location)
                        self.logging.info("User validates that the serial number is yet to be updated")

                        self.dpup.clickUpdateUpdateButton()
                        ss13_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','13',self.driver)
                        docsutil.addSmallHeading(self.document,"User clicks on Update Button")
                        docsutil.insertImageInDocx(self.document,ss13_location)
                        self.logging.info("User clicks on Update Button")

                        self.dpup.enterSuggestedMemberName(list(updateSerialNumberInActiveMemberTestDataDict[update_suggestedMemberName])[index])
                        ss14_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','14',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested member name")
                        docsutil.insertImageInDocx(self.document,ss14_location)
                        self.logging.info("User enters the suggested member name")

                        self.dpup.enterSuggestedGuardianName(list(updateSerialNumberInActiveMemberTestDataDict[update_suggestedGuardianName])[index])
                        ss15_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','15',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested guardian name")
                        docsutil.insertImageInDocx(self.document,ss15_location)
                        self.logging.info("User enters the suggested guardian name")

                        self.dpup.enterSuggestedRitwikName(list(updateSerialNumberInActiveMemberTestDataDict[update_suggestedRitwikName])[index])
                        ss16_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','16',self.driver)
                        docsutil.addSmallHeading(self.document,"User enters the suggested Ritwik name")
                        docsutil.insertImageInDocx(self.document,ss16_location)
                        self.logging.info("User enters the suggested Ritwik name")

                        self.dpup.clickNextButton()
                        ss17_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Inactive','17',self.driver)
                        docsutil.addSmallHeading(self.document,"User clicks on next button")
                        docsutil.insertImageInDocx(self.document,ss17_location)
                        self.logging.info("User clicks on next button")

                        if self.dpup.checkInitiationInformationErrorMessage(dikshayatriStatus='',familyCode='',phoneNumber=''):
                            ss18_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - Inactive','18',self.driver)
                            docsutil.addSmallHeading(self.document,"User validates the error message thrown for each mandatory field in Initiation Information page")
                            docsutil.insertImageInDocx(self.document,ss18_location)
                            self.logging.info("User validates the error message thrown for each mandatory field in Initiation Information page")

                            self.dpup.enterDikshayarthiStatus(list(updateSerialNumberInActiveMemberTestDataDict[update_dikshayarthiStatus])[index])
                            ss19_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','19',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the dikshayarthi status as InActive")
                            docsutil.insertImageInDocx(self.document,ss19_location)
                            self.logging.info("User enters the dikshayarthi status as InActive")

                            self.dpup.enterDeceasedReason(list(updateSerialNumberInActiveMemberTestDataDict[update_dikshayarthiStatus])[index])
                            ss20_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','20',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters the dikshayarthi inactive reason as deceased")
                            docsutil.insertImageInDocx(self.document,ss20_location)
                            self.logging.info("User enters the dikshayarthi inactive reason as deceased")

                            self.dpup.enterPhoneNumber(list(updateSerialNumberInActiveMemberTestDataDict[update_phoneNumber])[index])
                            ss21_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','21',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters phone number")
                            docsutil.insertImageInDocx(self.document,ss21_location)
                            self.logging.info("User enters phone number")

                            self.dpup.enterFamilyCode(list(updateSerialNumberInActiveMemberTestDataDict[update_familyCode])[index],list(updateSerialNumberInActiveMemberTestDataDict[update_philMemberName])[index])
                            ss22_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','22',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters family code")
                            docsutil.insertImageInDocx(self.document,ss22_location)
                            self.logging.info("User enters family code")

                            self.dpup.enterEmailAddress(list(updateSerialNumberInActiveMemberTestDataDict[update_emailAddress])[index])
                            ss23_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','23',self.driver)
                            docsutil.addSmallHeading(self.document,"User enters email address")
                            docsutil.insertImageInDocx(self.document,ss23_location)
                            self.logging.info("User enters email address")

                            self.dpup.clickNextButton()
                            ss24_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','24',self.driver)
                            docsutil.addSmallHeading(self.document,"User clicks on Next Button")
                            docsutil.insertImageInDocx(self.document,ss24_location)
                            self.logging.info("User clicks on Next Button")

                            if self.dpup.checkPermanentAddressInformationErrorHandling(permanentAddress='',permanentLandmark='',permanentPincode='',permanentPostoffice=''):
                                ss25_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','25',self.driver)
                                docsutil.addSmallHeading(self.document,"User checks the permanent address section and validates the contents")
                                docsutil.insertImageInDocx(self.document,ss25_location)
                                self.logging.info("User checks the permanent address section and validates the contents")

                                self.dpup.enterPermanentAddress(list(updateSerialNumberInActiveMemberTestDataDict[update_permanentAddress])[index])
                                ss26_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','26',self.driver)
                                docsutil.addSmallHeading(self.document,"User checks the permanent address section and validates the contents")
                                docsutil.insertImageInDocx(self.document,ss26_location)
                                self.logging.info("User enters the permanent address")

                                self.dpup.enterPermanentLandmark(list(updateSerialNumberInActiveMemberTestDataDict[update_permanentLandmark])[index])
                                ss27_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','27',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters the permanent landmark")
                                docsutil.insertImageInDocx(self.document,ss27_location)
                                self.logging.info("User enters the permanent landmark")

                                self.dpup.enterPermanentPincode(list(updateSerialNumberInActiveMemberTestDataDict[update_permanentPincode])[index])
                                ss28_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','28',self.driver)
                                docsutil.addSmallHeading(self.document,"User enters the permanent pincode")
                                docsutil.insertImageInDocx(self.document,ss28_location)
                                self.logging.info("User enters the permanent pincode")

                                self.dpup.enterPermanentPostOffice(list(updateSerialNumberInActiveMemberTestDataDict[update_permanentPostoffice])[index])
                                ss29_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','29',self.driver)
                                docsutil.addSmallHeading(self.document,"User selects the permanent post office")
                                docsutil.insertImageInDocx(self.document,ss29_location)
                                self.logging.info("User selects the permanent post office")

                                if self.dpup.checkPresentAddressInformationErrorHandling(checkBoxStatus='No',presentAddress='',presentLandmark='',presentPincode='',presentPostoffice=''):
                                    ss30_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','30',self.driver)
                                    docsutil.addSmallHeading(self.document,"User checks the Present Address section and validates the contents")
                                    docsutil.insertImageInDocx(self.document,ss30_location)
                                    self.logging.info("User checks the Present Address section and validates the contents")

                                    self.dpup.enterPresentAddress(list(updateSerialNumberInActiveMemberTestDataDict[update_presentAddress])[index])
                                    ss31_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','31',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Address")
                                    docsutil.insertImageInDocx(self.document,ss31_location)
                                    self.logging.info("User enters the Present Address")

                                    self.dpup.enterPresentLandmark(list(updateSerialNumberInActiveMemberTestDataDict[update_presentLandmark])[index])
                                    ss32_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','32',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Landmark")
                                    docsutil.insertImageInDocx(self.document,ss32_location)
                                    self.logging.info("User enters the Present Landmark")

                                    self.dpup.enterPresentPincode(list(updateSerialNumberInActiveMemberTestDataDict[update_presentPincode])[index])
                                    ss33_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','33',self.driver)
                                    docsutil.addSmallHeading(self.document,"User enters the Present Pincode")
                                    docsutil.insertImageInDocx(self.document,ss33_location)
                                    self.logging.info("User enters the Present Pincode")

                                    self.dpup.enterPresentPostOffice(list(updateSerialNumberInActiveMemberTestDataDict[update_presentPostoffice])[index])
                                    ss34_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','34',self.driver)
                                    docsutil.addSmallHeading(self.document,"User selects the Present Post Office")
                                    docsutil.insertImageInDocx(self.document,ss34_location)
                                    self.logging.info("User selects the Present Post Office")

                                    self.dpup.clickNextButton()
                                    ss35_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','35',self.driver)
                                    docsutil.addSmallHeading(self.document,"User clicks on Next Button")
                                    docsutil.insertImageInDocx(self.document,ss35_location)
                                    self.logging.info("User clicks on Next Button")

                                    if self.dpup.checkUpdateCommentErrorMessage(comment=''):
                                        ss36_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','36',self.driver)
                                        docsutil.addSmallHeading(self.document,"User validates the comment screen content")
                                        docsutil.insertImageInDocx(self.document,ss36_location)
                                        self.logging.info("User validates the comment screen content")

                                        self.dpup.enterUpdateComment(list(updateSerialNumberInActiveMemberTestDataDict[update_comments])[index])
                                        ss37_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','37',self.driver)
                                        docsutil.addSmallHeading(self.document,"User enters the update comment")
                                        docsutil.insertImageInDocx(self.document,ss37_location)
                                        self.logging.info("User enters the update comment")
                                        time.sleep(2)

                                        self.dpup.clickPreviousButton()
                                        ss38_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','38',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Address page")
                                        docsutil.insertImageInDocx(self.document,ss38_location)
                                        self.logging.info("User clicks on Previous Button to move to Address page")

                                        self.dpup.clickPreviousButton()
                                        ss39_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','39',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Initiation Page")
                                        docsutil.insertImageInDocx(self.document,ss39_location)
                                        self.logging.info("User clicks on Previous Button to move to Initiation Page")

                                        self.dpup.clickPreviousButton()
                                        ss40_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','40',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Previous Button to move to Suggested Members Page")
                                        docsutil.insertImageInDocx(self.document,ss40_location)
                                        self.logging.info("User clicks on Previous Button to move to Suggested Members Page")

                                        self.dpup.clickNextButton()
                                        self.dpup.clickNextButton()
                                        self.dpup.clickNextButton()
                                        ss41_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','41',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Next Button muliple times to move to comments page")
                                        docsutil.insertImageInDocx(self.document,ss41_location)
                                        self.logging.info("User clicks on Next Button muliple times to move to comments page")

                                        self.dpup.clickUpdateSubmitButton()
                                        ss42_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','42',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Submit Button to update the changes made")
                                        docsutil.insertImageInDocx(self.document,ss42_location)
                                        self.logging.info("User clicks on Submit Button to update the changes made")
                                        time.sleep(3)

                                        self.dpup.clickDoneButtonFromSuccessMessage()
                                        ss43_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','43',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Done Button from the Success Message Window")
                                        docsutil.insertImageInDocx(self.document,ss43_location)
                                        self.logging.info("User clicks on Done Button from the Success Message Window")

                                        #self.driver.refresh()
                                        self.dpup.clickUpdateFromNavigationPanel()
                                        ss44_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','44',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on Update from the Navigation Panel")
                                        docsutil.insertImageInDocx(self.document,ss44_location)
                                        self.logging.info("User clicks on Update from the Navigation Panel")

                                        self.dpup.enterSerialNumber(list(updateSerialNumberInActiveMemberTestDataDict[update_serialNumber])[index])
                                        ss45_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','45',self.driver)
                                        docsutil.addSmallHeading(self.document,"User enters the serial Number that has been updated by him -{}".format(list(updateSerialNumberInActiveMemberTestDataDict[update_serialNumber])[index]))
                                        docsutil.insertImageInDocx(self.document,ss45_location)
                                        self.logging.info("User enters the serial Number that has been updated by him -{}".format(list(updateSerialNumberInActiveMemberTestDataDict[update_serialNumber])[index]))
                                        
                                        self.dpup.clickUpdateSearchButton()
                                        ss46_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','46',self.driver)
                                        docsutil.addSmallHeading(self.document,"User clicks on search button")
                                        docsutil.insertImageInDocx(self.document,ss46_location)
                                        self.logging.info("User clicks on search button")

                                        updateStatus,memberName, memberGuardianName, memberAddress=self.dpup.fetchDataFromUpdateCard()
                                        ss47_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','47',self.driver)
                                        docsutil.addSmallHeading(self.document,"User checks the status of the serial number searched")
                                        docsutil.insertImageInDocx(self.document,ss47_location)
                                        self.logging.info("User checks the status of the serial number searched")

                                        if not self.dpup.validateUpdateStatus(updateStatus):
                                            ss48_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','48',self.driver)
                                            docsutil.insertImageInDocx(self.document,ss48_location)
                                            docsutil.appendContentWithPassColor(self.document,"{} has been updated successfully having status- {}".format(memberName,updateStatus))
                                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                            self.logging.info("{} has been updated successfully having status- {}".format(memberName,updateStatus))
                                            self.driver.refresh()
                                        else:
                                            ss0F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','0F',self.driver)
                                            docsutil.appendContentWithFailColor(self.document,"Updating Member- {}  was not successful".format(memberName))
                                            docsutil.insertImageInDocx(self.document,ss0F_location)
                                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                            self.logging.info("Updating Member- {}  was not successful".format(memberName))
                                            assert False,"Updating Member- {}  was not successful".format(memberName)
                                    else:
                                        ss1F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','1F',self.driver)
                                        docsutil.appendContentWithFailColor(self.document,"Update-- Invalid comment was not handled")
                                        docsutil.insertImageInDocx(self.document,ss1F_location)
                                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                        self.logging.info("Update-- Invalid comment was not handled")
                                        assert False,"Update-- Invalid comment was not handled"
                                else:
                                    ss2F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','2F',self.driver)
                                    docsutil.appendContentWithFailColor(self.document,"Update - Present Address Section doesn't have the prerequisite contents")
                                    docsutil.insertImageInDocx(self.document,ss2F_location)
                                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                    self.logging.info("Update - Present Address Section doesn't have the prerequisite contents")
                                    assert False,"Update - Present Address Section doesn't have the prerequisite contents"
                            else:
                                ss3F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','3F',self.driver)
                                docsutil.appendContentWithFailColor(self.document,"Update - Permanent Address Section doesn't have the prerequisite contents")
                                docsutil.insertImageInDocx(self.document,ss3F_location)
                                docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                                self.logging.info("Update - Permanent Address Section doesn't have the prerequisite contents")
                                assert False,"Update - Permanent Address Section doesn't have the prerequisite contents"
                        else:
                            ss4F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','4F',self.driver)
                            docsutil.appendContentWithFailColor(self.document,"Update - Initiation Infomation doesn't have the prerequisite contents")
                            docsutil.insertImageInDocx(self.document,ss4F_location)
                            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                            self.logging.info("Update - Initiation Infomation doesn't have the prerequisite contents")
                            assert False,"Update - Initiation Infomation doesn't have the prerequisite contents"
                    else:
                        ss5F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','5F',self.driver)
                        docsutil.appendContentWithPassColor(self.document,"Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus))
                        docsutil.insertImageInDocx(self.document,ss5F_location)
                        docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                        self.logging.info("Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus))
                        assert True,"Member Name: {} having guardian- {} address- {} is already in the update pipeline :{}".format(memberName,memberGuardianName,memberAddress,updateStatus)
                else:
                    ss6F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','6F',self.driver)
                    docsutil.appendContentWithFailColor(self.document,"Update Screen doesn't have the prerequisites content")
                    docsutil.insertImageInDocx(self.document,ss6F_location)
                    docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
                    self.logging.info("Update Screen doesn't have the prerequisites content")
                    assert False,"Update Screen doesn't have the prerequisites content"
                    
            self.driver.quit()
            self.logging.info("User closes all the browsers open")
        except Exception as e:
            filenamePrefix=list(updateSerialNumberInActiveMemberTestDataDict[update_testCaseName])[index]
            ss7F_location=docsutil.takeAndSaveScreenshotUnique(self.screenshot_location,'Update Serial Number - InActive','7F',self.driver)
            docsutil.appendContentWithFailColor(self.document,"User faces somes exception on updating serial number")
            docsutil.insertImageInDocx(self.document,ss7F_location)
            docsutil.saveDocument(self.document,"TC-"+str(filenamePrefix)+"-"+str(self.updateSerialNumber_documentation_fileName))
            self.driver.quit()
            self.logging.info("User faces somes exception on updating serial number")
            raise CustomException(e,sys)
