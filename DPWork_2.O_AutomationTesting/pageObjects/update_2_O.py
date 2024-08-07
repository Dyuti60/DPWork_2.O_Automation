import os
from selenium import webdriver
import time
import sys
from exception import CustomException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DpWorkUpdatePage:

    #Locate Update in Navigation Panel:
    button_clickUpdate_Xpath='//*[text()="Update "]'

    #Serial Number Input:
    text_enterSerialNumber_Xpath='//input[contains(@class,"search-input") and @placeholder="Enter/paste member id" and @type="text"]'
    #update button clicks
    button_clickUpdateClearButton_Xpath='//*[contains(@class,"clr-btn dp-secondary-btn")]'
    button_clickUpdateSearchButton_Xpath='//*[contains(@class,"src-btn dp-primary-btn")]'
    button_clickUpdateUpdateButton_Xpath='//*[@class="dp-primary-btn updateButton"]'
    

    #Update UI: Title Filter Search and Clear Button
    text_checkForUpdateScreenTitle_Xpath='//*[text()="Update"]'
    text_checkForUpdateScreenDescription_Xpath='//*[text()="Search member to update"]'
    text_checkForClearButton_Xpath='//button[@type="reset" and contains(text(),"Clear")]'
    text_checkForSearchButton_Xpath='//button[@type="submit" and contains(text(),"Search")]'
    fetch_allValues_Xpath='//span[@class="update-value"]'
    #Status=0, Name=1, Guardian=2, Address=3

    #Update Member Detail Suggestions Page
    fetchtext_getSerialNumber_Xpath='//span[@class="serial-no-text cursor-pointer"]'
    text_suggestedMemberName_Xpath='//input[@formcontrolname="memberName"]'
    text_suggestedGuardianName_Xpath='//input[@formcontrolname="gurdianName"]'
    text_suggestedRitwikName_Xpath='//input[@formcontrolname="ritwikName"]'

    #Update Next and Clear Button
    button_nextButton_Xpath='//button[contains(text(),"Next")]'
    button_previousButton_Xpath='//button[contains(text(),"Previous")]'
    
    #Update Member Initiation Details
    click_DikhshyatriStatus_Xpath='//*[@formcontrolname="dikshyarthiStatus"]'
    dikhshyatriStatus_getAllOPtions_Xpath='//*[contains(@id,"mat-option")]'
    click_inactiveReason_Xpath='//*[@formcontrolname="inactivityReason"]'
    click_inactiveReasonOption_Xpath='//*[contains(text(),"Deceased")]'
    text_mobileNumber_Xpath='//input[@formcontrolname="phoneNumber"]'
    click_dikshayatriStatusclearButton_Xpath='//*[@role="img" and contains(text(),"clear")]'
    click_inactiveReasonclearButton_Xpath='//*[@role="img" and contains(text(),"clear")]'
    text_enterFamilyCode_Xpath='//input[@formcontrolname="familyCode"]'
    click_getAllFamilyMemberName_Xpath='//*[@role="option" and contains(@id,"mat-option")]'
    text_enterEmail_Xpath='//input[@formcontrolname="email"]'
    popup_fcConfirmMapping_Xpath='//*[contains(text(),"Yes, Continue")]'
    popup_fccancelMapping_Xpath='//*[contains(text(),"No, cancel")]'

    #Update Member Permanent Address
    text_permanentCompleteAddress_Xpath='//input[@formcontrolname="completeAddress"]'
    text_permanentLandmark_Xpath='//input[@formcontrolname="landmark"]'
    text_permanentpinCode_Xpath='//input[@formcontrolname="pinCode"]'
    click_permanentPostOffice_Xpath='//*[@formcontrolname="postOffice"]'
    click_getAllOptionsPermanentPostOffice_Xpath='//*[@role="option" and contains(@id,"mat-option")]'
    click_sameAsPermanentAddress_Xpath='//span[@class="checkmark"]'

    #Update Member Present Address
    text_presentCompleteAddress_Xpath='//input[@formcontrolname="presentCompleteAddress"]'
    text_presentLandmark_Xpath='//input[@formcontrolname="presentLandmark"]'
    text_presentpinCode_Xpath='//input[@formcontrolname="presentPinCode"]'
    click_presentpostOffice_Xpath='//*[@formcontrolname="presentPostOffice"]'
    click_getAllOptionsPresentPostOffice_Xpath='//*[@role="option" and contains(@id,"mat-option")]'
    text_enterUpdateComment_Xpath='//*[@formcontrolname="comments"]'
    button_submit_Xpath='//button[@type="submit" and contains(text(),"Submit")]'
    button_clickQuitUpdation_Xpath='//*[@class="hover-pointer" and contains(text(),"Quit Updation")]'

    #All Error messages Handling
    text_getErrorMessageForDikshyartriStatusField_Xpath='//span[contains(text(),"Dikshyarthi status is required")]'
    text_getErrorMessageForInactiveReasonField_Xpath='//span[contains(text(),"Inactivity Reason is required")]'
    text_getErrorMessageForPhoneNumberField_Xpath='//span[contains(text(),"Phone number is required")]'
    text_getErrorMessageForFamilyCodeField_Xpath='//span[contains(text(),"Family code is required")]'
    text_getIncorrectErrorMessageForFamilyCodeField_Xpath='//*[contains(text(),"Could not find Family Code details. Please check the code again.")]'


    text_getErrorMessageForPermanentAddressField_Xpath='//span[contains(text(),"Please enter an address with at least 10 characters")]'
    text_getErrorMessageForPermanentLandmarkField_Xpath='//span[contains(text(),"Landmark is required")]'
    text_getErrorMessageForPermanentPincodeField_Xpath='//span[contains(text(),"Pincode is required")]'
    text_getErrorMessageForPermanentPostOfficeField_Xpath='//span[contains(text(),"Post office is required")]'
    text_getErrorMessageForPermanentStateField_Xpath='//span[contains(text(),"District is required")]'
    #text_getErrorMessageForPermanentDistrictField_Xpath='//span[contains(text(),"State is required")]'

    text_getErrorMessageForPresentAddressField_Xpath='//span[contains(text(),"Please enter an address with at least 10 characters")]'
    text_getErrorMessageForPresentLandmarkField_Xpath='//span[contains(text(),"Landmark is required")]'
    text_getErrorMessageForPresentPincodeField_Xpath='//span[contains(text(),"Pincode is required")]'
    text_getErrorMessageForPresentPostOfficeField_Xpath='//span[contains(text(),"Present Post office is required")]'
    text_getErrorMessageForPresentStateField_Xpath='//span[contains(text(),"Present District Name is required")]'
    #text_getErrorMessageForPresentDistrictField_Xpath='//span[contains(text(),"State is required")]'

    text_getErrorMessageForUpdateCommentsField_Xpath='//span[contains(text(),"Comments is required")]'
    click_updateSubmitButton_Xpath='//button[contains(@class,"dp-primary-btn next-btn mt-4") and @type="button" and contains(text(),"Submit")]'

    #Click Done Button
    button_clickDoneButtonInSuccessMessage_Xpath='//button[@class="save-button dp-primary-btn ng-star-inserted"]'

    def __init__(self,driver):
        self.driver=driver

    def click_unitil_interactable(self,element) -> bool:
        try:
            element_is_interactable=False
            counter=1
            if element:
                while not element_is_interactable:
                    try:
                        element.click()
                        element_is_interactable=True
                    except(ElementClickInterceptedException,ElementNotInteractableException,StaleElementReferenceException):
                        counter=counter+1
            return element_is_interactable
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickUpdateFromNavigationPanel(self):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.button_clickUpdate_Xpath)))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.button_clickUpdate_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
    def enterSerialNumber(self,serialNumber):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterSerialNumber_Xpath)))
            if len(serialNumber)==0:
                serialNumber=''
            self.driver.find_element(By.XPATH, self.text_enterSerialNumber_Xpath).clear()
            self.driver.find_element(By.XPATH, self.text_enterSerialNumber_Xpath).send_keys(serialNumber)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickUpdateClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickUpdateClearButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickUpdateSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickUpdateSearchButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickUpdateUpdateButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickUpdateUpdateButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
            
    def CheckForText_Search_by_member_id(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_checkForUpdateScreenDescription_Xpath)))
            descMessageCount=self.driver.find_elements(By.XPATH,self.text_checkForUpdateScreenDescription_Xpath)
            if len(descMessageCount)>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
    
    def CheckForText_Update_Title(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_checkForUpdateScreenTitle_Xpath)))
            titleMessageCount=self.driver.find_elements(By.XPATH,self.text_checkForUpdateScreenTitle_Xpath)
            if len(titleMessageCount)>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys) 

    def CheckForButton_Clear(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_checkForClearButton_Xpath)))
            clearButtonCount=self.driver.find_elements(By.XPATH,self.text_checkForClearButton_Xpath)
            if len(clearButtonCount)>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys) 

    def CheckForButton_Search(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_checkForSearchButton_Xpath)))
            clearButtonCount=self.driver.find_elements(By.XPATH,self.text_checkForSearchButton_Xpath)
            if len(clearButtonCount)>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)

    def fetchDataFromUpdateCard(self):
        #fetch_allValues_Xpath='//span[@class="update-value"]'
        #Status=0, Name=1, Guardian=2, Address=3
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.fetch_allValues_Xpath)))
        fetch_allValues=self.driver.find_elements(By.XPATH, self.fetch_allValues_Xpath)
        updateStatus=str(fetch_allValues[0].text).lower()
        #serialNumber=str(fetch_allValues[1].text)
        memberName=str(fetch_allValues[1].text).lower()
        memberGuardianName=str(fetch_allValues[2].text).lower()
        memberAddress=str(fetch_allValues[3].text).lower()
        return updateStatus ,memberName, memberGuardianName, memberAddress
    
    def validateUpdateStatus(self,updateStatus):
        if updateStatus in ['not updated','da rejected','su rejected']:
            return True
        elif updateStatus in ['updated','da approved','fw completed','su approved']:
            return False
            
    def enterSuggestedMemberName(self, suggestedMemberName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_suggestedMemberName_Xpath)))
            self.driver.find_element(By.XPATH, self.text_suggestedMemberName_Xpath).clear()
            if len(suggestedMemberName)==0:
                suggestedMemberName=''
            self.driver.find_element(By.XPATH, self.text_suggestedMemberName_Xpath).send_keys(suggestedMemberName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterSuggestedGuardianName(self, suggestedGuardianName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_suggestedGuardianName_Xpath)))
            self.driver.find_element(By.XPATH, self.text_suggestedGuardianName_Xpath).clear()
            if len(suggestedGuardianName)==0:
                suggestedGuardianName=''
            self.driver.find_element(By.XPATH, self.text_suggestedGuardianName_Xpath).send_keys(suggestedGuardianName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterSuggestedRitwikName(self, suggestedRitwikName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_suggestedRitwikName_Xpath)))
            self.driver.find_element(By.XPATH, self.text_suggestedRitwikName_Xpath).clear()
            if len(suggestedRitwikName)==0:
                suggestedRitwikName=''
            self.driver.find_element(By.XPATH, self.text_suggestedRitwikName_Xpath).send_keys(suggestedRitwikName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDikshayarthiStatus(self,dikshyarthiStatus):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_DikhshyatriStatus_Xpath)))
            if len(dikshyarthiStatus)!=0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_DikhshyatriStatus_Xpath))
                time.sleep(2)
                po_elements=self.driver.find_elements(By.XPATH,self.dikhshyatriStatus_getAllOPtions_Xpath)
                for po_element in po_elements:
                    if po_element.text.lower()==dikshyarthiStatus.lower():
                        self.click_unitil_interactable(po_element)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(po_element[0])
                return po_element.text.lower()
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDeceasedReason(self,dikhayarthiStatus):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_inactiveReason_Xpath)))
            if str(dikhayarthiStatus).lower()=='inactive':
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_inactiveReason_Xpath))
                time.sleep(2)
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_inactiveReasonOption_Xpath))
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPhoneNumber(self, phoneNumber):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_mobileNumber_Xpath)))
            self.driver.find_element(By.XPATH, self.text_mobileNumber_Xpath).clear()
            if len(phoneNumber)==0:
                phoneNumber=''
            self.driver.find_element(By.XPATH, self.text_mobileNumber_Xpath).send_keys(phoneNumber)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterFamilycodeOneByOne(self,Familycode):
        for elementIndex in range(len(Familycode)):
            self.driver.find_element(By.XPATH,self.text_enterFamilyCode_Xpath).send_keys(Familycode[elementIndex])
            time.sleep(0.5)
        time.sleep(1)

    def getCorrectFamilyCode(self,FamilyCode):
        try:
            count=True
            while count:
                self.enterFamilycodeOneByOne(Familycode=FamilyCode)
                count=self.driver.find_elements(By.XPATH,self.text_getIncorrectErrorMessageForFamilyCodeField_Xpath)
        except Exception as e:
            raise CustomException(e,sys)
    def enterFamilyCode(self,FamilyCode,PhilMemberName):
        try:
            time.sleep(1)
            flag=False
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterFamilyCode_Xpath)))
            self.driver.find_element(By.XPATH,self.text_enterFamilyCode_Xpath).clear()
            if len(FamilyCode)==0:
                FamilyCode=''
            self.getCorrectFamilyCode(FamilyCode)
            #self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
            time.sleep(1)
            if len(FamilyCode)!=0:
                apicallIncorrect=self.driver.find_elements(By.XPATH,self.text_getIncorrectErrorMessageForFamilyCodeField_Xpath)
                PhilMemberName_locators=self.driver.find_elements(By.XPATH,self.click_getAllFamilyMemberName_Xpath)
                elements_text_value=[]
                for element in PhilMemberName_locators:
                    elements_text=str(element.text).lower().strip().split()
                    elements_text_value.append(" ".join(elements_text[:-1]))

                element_dict=dict(zip(elements_text_value,PhilMemberName_locators))
                
                for dict_key_text in element_dict.keys():
                    if dict_key_text == PhilMemberName.lower():
                        element_dict[dict_key_text].click()
                        self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.popup_fcConfirmMapping_Xpath))
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    assert False, "Not able to fetch Phil Member on entering FC Code"
                
        except Exception as e:
            raise CustomException(e,sys)
        

        
    def enterEmailAddress(self,emailAddress):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterEmail_Xpath)))
            self.driver.find_element(By.XPATH, self.text_enterEmail_Xpath).clear()
            if len(emailAddress)==0:
                emailAddress=''
            self.driver.find_element(By.XPATH, self.text_enterEmail_Xpath).send_keys(emailAddress)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterPermanentAddress(self, permanentAddress):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentCompleteAddress_Xpath)))
            self.driver.find_element(By.XPATH, self.text_permanentCompleteAddress_Xpath).clear()
            if len(permanentAddress)==0:
                permanentAddress=''
            self.driver.find_element(By.XPATH, self.text_permanentCompleteAddress_Xpath).send_keys(permanentAddress)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterPermanentLandmark(self,permanentLandmark):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentLandmark_Xpath)))
            self.driver.find_element(By.XPATH, self.text_permanentLandmark_Xpath).clear()
            if len(permanentLandmark)==0:
                permanentLandmark=''
            self.driver.find_element(By.XPATH, self.text_permanentLandmark_Xpath).send_keys(permanentLandmark)
        except Exception as e:
            raise CustomException(e,sys)
    

    def enterPermanentPincode(self,permanentPincode):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentpinCode_Xpath)))
            self.driver.find_element(By.XPATH, self.text_permanentpinCode_Xpath).clear()
            if len(permanentPincode)==0:
                permanentPincode=''
            self.driver.find_element(By.XPATH, self.text_permanentpinCode_Xpath).send_keys(permanentPincode)
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def enterPermanentPostOffice(self,permanentPostOffice):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_permanentPostOffice_Xpath)))
            if len(permanentPostOffice)!=0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_permanentPostOffice_Xpath))
                time.sleep(2)
                po_elements=self.driver.find_elements(By.XPATH,self.click_getAllOptionsPermanentPostOffice_Xpath)
                for po_element in po_elements:
                    if po_element.text.lower()==permanentPostOffice.lower():
                        self.click_unitil_interactable(po_element)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(po_element[0])
                return po_element.text.lower()
        except Exception as e:
            raise CustomException(e,sys)
        
       
    def enterPresentAddress(self, presentAddress,checkBox_flag):
        try:
            if str(checkBox_flag).lower()=='no':
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentCompleteAddress_Xpath)))
                self.driver.find_element(By.XPATH, self.text_presentCompleteAddress_Xpath).clear()
                if len(presentAddress)==0:
                    presentAddress=''
                self.driver.find_element(By.XPATH, self.text_presentCompleteAddress_Xpath).send_keys(presentAddress)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterPresentLandmark(self,presentLandmark,checkBox_flag):
        try:
            if str(checkBox_flag).lower()=='no':
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentLandmark_Xpath)))
                self.driver.find_element(By.XPATH, self.text_presentLandmark_Xpath).clear()
                if len(presentLandmark)==0:
                    presentLandmark=''
                self.driver.find_element(By.XPATH, self.text_presentLandmark_Xpath).send_keys(presentLandmark)
        except Exception as e:
            raise CustomException(e,sys)
    

    def enterPresentPincode(self,presentPincode,checkBox_flag):
        try:
            if str(checkBox_flag).lower()=='no':
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentpinCode_Xpath)))
                self.driver.find_element(By.XPATH, self.text_presentpinCode_Xpath).clear()
                if len(presentPincode)==0:
                    presentPincode=''
                self.driver.find_element(By.XPATH, self.text_presentpinCode_Xpath).send_keys(presentPincode)
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def enterPresentPostOffice(self,presentPostOffice,checkBox_flag):
        try:
            if str(checkBox_flag).lower()=='no':
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_presentpostOffice_Xpath)))
                if len(presentPostOffice)!=0:
                    self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_presentpostOffice_Xpath))
                    time.sleep(2)
                    po_elements=self.driver.find_elements(By.XPATH,self.click_getAllOptionsPresentPostOffice_Xpath)
                    for po_element in po_elements:
                        if po_element.text.lower()==presentPostOffice.lower():
                            self.click_unitil_interactable(po_element)
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(po_element[0])
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterUpdateComment(self,updateComment):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterUpdateComment_Xpath)))
            self.driver.find_element(By.XPATH, self.text_enterUpdateComment_Xpath).clear()
            if len(updateComment)==0:
                updateComment=''
            self.driver.find_element(By.XPATH, self.text_enterUpdateComment_Xpath).send_keys(updateComment)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickCheckBoxForPresentAddressSameAsPermanentAddress(self,checkBox_flag):
        try:
            if str(checkBox_flag).lower()=='yes':
                time.sleep(1)
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_sameAsPermanentAddress_Xpath))
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)


        
    def clickNextButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_nextButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickPreviousButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_previousButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickQuitUpdationButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickQuitUpdation_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkInitiationInformationErrorMessage(self, dikshayatriStatus, familyCode, phoneNumber):
        self.clickNextButton()
        ii=[]
        if len(dikshayatriStatus)==0:
            error_ds=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForDikshyartriStatusField_Xpath)
            if len(error_ds) >0:
                ii.append("ErrorHandled")
            else:
                ii.append("ErrorNotHandled")
        
        if len(familyCode)==0:
            error_fc=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForFamilyCodeField_Xpath)
            if len(error_fc) >0:
                ii.append("ErrorHandled")
            else:
                ii.append("ErrorNotHandled")

        if len(phoneNumber)==0:
            error_pn=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPhoneNumberField_Xpath)
            if len(error_pn) >0:
                ii.append("ErrorHandled")
            else:
                ii.append("ErrorNotHandled")

        if "ErrorNotHandled" in ii:
            return False
        else:
            return True

        
    def checkPermanentAddressInformationErrorHandling(self, permanentAddress, permanentLandmark, permanentPincode, permanentPostoffice):
        self.clickNextButton()
        pa=[]
        if len(permanentAddress)==0:
            error_pa=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPermanentAddressField_Xpath)
            if len(error_pa) >0:
                pa.append("ErrorHandled")
            else:
                pa.append("ErrorNotHandled")
        
        if len(permanentLandmark)==0:
            error_pl=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPermanentLandmarkField_Xpath)
            if len(error_pl) >0:
                pa.append("ErrorHandled")
            else:
                pa.append("ErrorNotHandled")

        if len(permanentPincode)==0:
            error_pc=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPermanentPincodeField_Xpath)
            if len(error_pc) >0:
                pa.append("ErrorHandled")
            else:
                pa.append("ErrorNotHandled")

        if len(permanentPostoffice)==0:
            error_pl=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPermanentPostOfficeField_Xpath)
            if len(error_pl) >0:
                pa.append("ErrorHandled")
            else:
                pa.append("ErrorNotHandled")

        if "ErrorNotHandled" in pa:
            return False
        else:
            return True
        
    
    def checkPresentAddressInformationErrorHandling(self,checkBoxStatus,presentAddress, presentLandmark, presentPincode, presentPostoffice):
        self.clickNextButton()
        if str(checkBoxStatus).lower() !='yes':
            pa=[]
            if len(presentAddress)==0:
                error_pa=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPresentAddressField_Xpath)
                if len(error_pa) >0:
                    pa.append("ErrorHandled")
                else:
                    pa.append("ErrorNotHandled")
            
            if len(presentLandmark)==0:
                error_pl=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPresentLandmarkField_Xpath)
                if len(error_pl) >0:
                    pa.append("ErrorHandled")
                else:
                    pa.append("ErrorNotHandled")

            if len(presentPincode)==0:
                error_pc=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPresentPincodeField_Xpath)
                if len(error_pc) >0:
                    pa.append("ErrorHandled")
                else:
                    pa.append("ErrorNotHandled")

            if len(presentPostoffice)==0:
                error_pl=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForPresentPostOfficeField_Xpath)
                if len(error_pl) >0:
                    pa.append("ErrorHandled")
                else:
                    pa.append("ErrorNotHandled")

            if "ErrorNotHandled" in pa:
                return False
            else:
                return True
        else:
            return True
        
    def checkUpdateCommentErrorMessage(self, comment):
        self.enterUpdateComment(comment)
        self.clickUpdateSubmitButton()
        if len(comment)==0:
            error_comment=self.driver.find_elements(By.XPATH,self.text_getErrorMessageForUpdateCommentsField_Xpath)
            if len(error_comment) >0:
                return True
            else:
                return False

    def clickUpdateSubmitButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_updateSubmitButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickDoneButtonFromSuccessMessage(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickDoneButtonInSuccessMessage_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
