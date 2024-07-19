import os
import time
import sys
import pandas as pd
import numpy as np
from exception import CustomException
from utilities import XLUtils

from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class EditDPNF:
    click_dpnfFromNavigationPanel_Xpath='//*[text()="DPNF "]'
    click_AddToDpnfButton_Xpath='//*[@class="addButton dp-primary-btn"]'
    text_firstname_Xpath='//input[@formcontrolname="fname"]'
    text_middlename_Xpath='//input[@formcontrolname="mname"]'
    text_lastname_Xpath='//input[@formcontrolname="lname"]'
    options_getAllLastName_Xpath='//*[contains(@id,"mat-option")]'
    text_ritwikname_Xpath='//input[@formcontrolname="rwname"]'

    options_getAllRitwikName_Xpath='//*[contains(@id,"mat-option")]'
    text_familyCode_Xpath='//input[@formcontrolname="fc"]'
    options_getAllFamilyCode_Xpath='//*[contains(@id,"mat-option")]'
    text_contact_Xpath='//input[@formcontrolname="contact"]'
    click_gender_Xpath='//*[@formcontrolname="gender"]'
    options_getAllGender_Xpath='//*[contains(@id,"mat-option")]'
    #select_genderFemale_Xpath="//span[text()=' Female ']"
    #select_genderMale_Xpath="//span[text()=' Male ']"
    click_maritalStatus_Xpath='//*[@formcontrolname="maritalStatus"]'
    options_getAllMaritalStatus_Xpath='//*[contains(@id,"mat-option")]'
    #select_maritalStatusMarried_Xpath="//span[text()=' Married ']"
    #select_maritalStatusUnmarried_Xpath="//span[text()=' Unmarried ']"
    text_guardianFirst_Xpath='//input[@formcontrolname="gfname"]'
    text_guardianMiddle_Xpath='//input[@formcontrolname="gmname"]'
    text_guardianLast_Xpath='//input[@formcontrolname="glname"]'
    options_getAllGuardianLastName_Xpath='//*[contains(@id,"mat-option")]'
    text_husbandFirst_Xpath='//input[@formcontrolname="hfname"]'
    text_husbandMiddle_Xpath='//input[@formcontrolname="hmname"]'
    text_husbandLast_Xpath='//input[@formcontrolname="hlname"]'
    options_getAllHusbandLastName_Xpath='//*[contains(@id,"mat-option")]'
    click_NextButton_Xpath="//*[text()=' Next']"
    click_PreviousButton_Xpath="//*[text()=' Previous']"

    text_dikshaAddress_Xpath='//input[@formcontrolname="dikshaAdd"]'
    text_dikshaLandmark_Xpath='//input[@formcontrolname="dikshaLandMark"]'
    text_dikshaPincode_Xpath='//input[@formcontrolname="dikshaPincode"]'
    text_presentAddress_Xpath='//input[@formcontrolname="presAdd"]'
    text_presentLandmark_Xpath='//input[@formcontrolname="presLandMark"]'
    text_presentPincode_Xpath='//input[@formcontrolname="presPincode"]'
    click_presentPostOffice_Xpath='//*[@formcontrolname="presPO"]'
    click_sameAsPresentAddress_Xpath='//span[@class="checkmark"]'
    text_permanentAddress_Xpath='//input[@formcontrolname="permAdd"]'
    text_permanentLandmark_Xpath='//input[@formcontrolname="permLandMark"]'
    text_permanentPincode_Xpath='//input[@formcontrolname="permPincode"]'
    click_permanentPostOffice_Xpath='//*[@formcontrolname="permPO"]'
    options_getAllPO_Xpath='//*[contains(@id,"mat-option")]'

    click_dateOfBirth_Xpath='//input[@formcontrolname="dob"]'
    click_dikshaYear_Xpath='//*[@formcontrolname="dikshaYear"]'
    options_getAllDikshaYear_Xpath='//*[contains(@id,"mat-option")]'
    click_dikshaMonth_Xpath='//*[@formcontrolname="dikshaMonth"]'
    options_getAllDikshaMonth_Xpath='//*[contains(@id,"mat-option")]'
    click_dikshaDay_Xpath='//*[@formcontrolname="dikshaDay"]'
    options_getAllDikshaDay_Xpath='//*[contains(@id,"mat-option")]'
    
    text_dpnfComments_Xpath='//input[@formcontrolname="comments"]'
    click_SubmitToDPNFButton_Xpath="//*[text()=' Submit to DPNF']"

    click_PersonalInfoTab_Xpath="//*[text()='Personal Info']"
    click_AddressInfoTab_Xpath="//*[text()='Address Info']"
    click_DateSummaryTab_Xpath="//*[text()='Date & Summary']"

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
        
    def clickDPNFFromNavigationPanel(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_dpnfFromNavigationPanel_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def iterateOverEachRecordAndclickRemoveEnabledDpnfRecord(self):
        try:
            time.sleep(1)
            remove_enabled_dpnf_records=[]
            edit_enabled_dpnf_records=[]
            all_rows=self.driver.find_elements(By.CSS_SELECTOR,'tr.mat-mdc-tooltip-trigger')
            for row in all_rows:
                time.sleep(1)
                self.click_unitil_interactable(row)
                time.sleep(2)
                if len(self.driver.find_elements(By.XPATH,'//*[contains(text(),"Remove")]'))>0:
                    remove_enabled_dpnf_records.append(row)
                    
                if len(self.driver.find_elements(By.XPATH,'//*[contains(text(),"Edit")]'))>0:
                    edit_enabled_dpnf_records[0].append(row)
            return remove_enabled_dpnf_records,edit_enabled_dpnf_records
        except Exception as e:
            raise CustomException(e,sys)
    def editDPNFByMemberName(self,dpnf_records):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)

        

    def enterMemberFirstName(self,MemberFirstName):
        try:
            time.sleep(1)
            if len(MemberFirstName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_firstname_Xpath)))
                self.driver.find_element(By.XPATH,self.text_firstname_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_firstname_Xpath).send_keys(MemberFirstName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberMiddleName(self,MemberMiddleName):
        try:
            time.sleep(1)
            if len(MemberMiddleName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_middlename_Xpath)))
                self.driver.find_element(By.XPATH,self.text_middlename_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_middlename_Xpath).send_keys(MemberMiddleName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterMemberLastName(self,MemberLastName):
        try:
            time.sleep(1)
            if len(MemberLastName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_lastname_Xpath)))
                self.driver.find_element(By.XPATH,self.text_lastname_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_lastname_Xpath).send_keys(MemberLastName)
                time.sleep(2)
                if len(MemberLastName)!=0:
                    lastname_locators=self.driver.find_elements(By.XPATH,self.options_getAllLastName_Xpath)
                    for element in lastname_locators:
                        if element.text.lower() == MemberLastName.lower():
                            element.click()
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(lastname_locators[0])
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterGuardianFirstName(self,GuardianFirstName):
        try:
            time.sleep(1)
            if len(GuardianFirstName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianFirst_Xpath)))
                self.driver.find_element(By.XPATH,self.text_guardianFirst_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_guardianFirst_Xpath).send_keys(GuardianFirstName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianMiddleName(self,GuardianMiddleName):
        try:
            time.sleep(1)
            if len(GuardianMiddleName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianMiddle_Xpath)))
                self.driver.find_element(By.XPATH,self.text_guardianMiddle_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_guardianMiddle_Xpath).send_keys(GuardianMiddleName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterGuardianLastName(self,GuardianLastName):
        try:
            if len(GuardianLastName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianLast_Xpath)))
                self.driver.find_element(By.XPATH,self.text_guardianLast_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_guardianLast_Xpath).send_keys(GuardianLastName)
                time.sleep(2)
                if len(GuardianLastName)!=0:
                    lastname_locators=self.driver.find_elements(By.XPATH,self.options_getAllLastName_Xpath)
                    for element in lastname_locators:
                        if element.text.lower() == GuardianLastName.lower():
                            element.click()
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(lastname_locators[0])
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterHusbandFirstName(self,HusbandFirstName):
        try:
            time.sleep(1)
            if len(HusbandFirstName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandFirst_Xpath)))
                self.driver.find_element(By.XPATH,self.text_husbandFirst_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_husbandFirst_Xpath).send_keys(HusbandFirstName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterHusbandMiddleName(self,HusbandMiddleName):
        try:
            time.sleep(1)
            if len(HusbandMiddleName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandMiddle_Xpath)))
                self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).send_keys(HusbandMiddleName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterHusbandLastName(self,HusbandLastName):
        try:
            time.sleep(1)
            if len(HusbandLastName)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandLast_Xpath)))
                self.driver.find_element(By.XPATH,self.text_husbandLast_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).send_keys(HusbandLastName)
                time.sleep(2)
                if len(HusbandLastName)!=0:
                    lastname_locators=self.driver.find_elements(By.XPATH,self.options_getAllLastName_Xpath)
                    for element in lastname_locators:
                        if element.text.lower() == HusbandLastName.lower():
                            element.click()
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(lastname_locators[0])
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterFamilyCode(self,FamilyCode,PhilMemberName):
        try:
            time.sleep(1)
            if len(FamilyCode)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_familyCode_Xpath)))
                self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
                time.sleep(2)
                if len(FamilyCode)!=0:
                    PhilMemberName_locators=self.driver.find_elements(By.XPATH,self.options_getAllFamilyCode_Xpath)
                    for element in PhilMemberName_locators:
                        if element.text.lower() == PhilMemberName.lower():
                            element.click()
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(PhilMemberName_locators[0])
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)


    def enterContactNumber(self,contactNumber):
        try:
            time.sleep(1)
            if len(contactNumber) == 0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_contact_Xpath)))
                self.driver.find_element(By.XPATH,self.text_contact_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_contact_Xpath).send_keys(contactNumber)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
        

    def enterGender(self,genderType):
        try:
            time.sleep(1)
            if len(genderType) !=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_gender_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_gender_Xpath))
                gender_elements=self.driver.find_elements(By.XPATH,self.options_getAllGender_Xpath)
                time.sleep(2)
                for gender_element in gender_elements:
                    if gender_element.text.lower()==genderType.lower():
                        self.click_unitil_interactable(gender_element)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(gender_element[0])
                return gender_element.text.lower()
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)


    def enterMaritalStatus(self,maritalStatus,genderType,husbandFirstName,husbandMiddleName,husbandLastName):
        try:
            time.sleep(1)
            if len(maritalStatus) != 0:
                gender_status=self.enterGender(genderType)
                if gender_status!='male':
                    WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_maritalStatus_Xpath)))
                    self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_maritalStatus_Xpath))
                    maritalstatus_elements=self.driver.find_elements(By.XPATH,self.options_getAllMaritalStatus_Xpath)
                    time.sleep(2)
                    for maritalstatus_element in maritalstatus_elements:
                        if maritalstatus_element.text.lower()==maritalStatus.lower():
                            self.click_unitil_interactable(maritalstatus_element)
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(maritalstatus_element[0])
                    marital_status=maritalstatus_element.text.lower()

                    if gender_status.strip()=='female' and marital_status.strip()=='married':
                        if len(husbandFirstName)==0:
                            husbandFirstName=''
                        if len(husbandMiddleName)==0:
                            husbandMiddleName=''
                        if len(husbandLastName)==0:
                            husbandLastName=''
                        self.enterHusbandFirstName(husbandFirstName)
                        self.enterHusbandMiddleName(husbandMiddleName)
                        self.enterHusbandLastName(husbandLastName)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    
    def clickNextButtonDPNF(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_NextButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDikhaAddress(self,dikshaAddress):
        try:
            time.sleep(1)
            if len(dikshaAddress) != 0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dikshaAddress_Xpath)))
                self.driver.find_element(By.XPATH,self.text_dikshaAddress_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_dikshaAddress_Xpath).send_keys(dikshaAddress)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterDikshaLandmark(self,dikshaLandmark):
        try:
            time.sleep(1)
            if len(dikshaLandmark) != 0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dikshaLandmark_Xpath)))
                self.driver.find_element(By.XPATH,self.text_dikshaLandmark_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_dikshaLandmark_Xpath).send_keys(dikshaLandmark)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterDikshaPincode(self,dikshaPincode):
        try:
            time.sleep(1)
            if len(dikshaPincode) != 0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dikshaPincode_Xpath)))
                self.driver.find_element(By.XPATH,self.text_dikshaPincode_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_dikshaPincode_Xpath).send_keys(dikshaPincode)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPresentAddress(self,presentAddress):
        try:
            time.sleep(1)
            if len(presentAddress) != 0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentAddress_Xpath)))
                self.driver.find_element(By.XPATH,self.text_presentAddress_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_presentAddress_Xpath).send_keys(presentAddress)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPresentLandmark(self,presentLandmark):
        try:
            time.sleep(1)
            if len(presentLandmark)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentLandmark_Xpath)))
                self.driver.find_element(By.XPATH,self.text_presentLandmark_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_presentLandmark_Xpath).send_keys(presentLandmark)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPresentPincode(self,presentPincode):
        try:
            time.sleep(1)
            if len(presentPincode)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_presentPincode_Xpath)))
                self.driver.find_element(By.XPATH,self.text_presentPincode_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_presentPincode_Xpath).send_keys(presentPincode)
            else: 
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPresentPostOffice(self,presentPostOffice):
        try:
            time.sleep(1)
            if len(presentPostOffice)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_presentPostOffice_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_presentPostOffice_Xpath))
                time.sleep(2)
                po_elements=self.driver.find_elements(By.XPATH,self.options_getAllPO_Xpath)
                for po_element in po_elements:
                    if po_element.text.lower()==presentPostOffice.lower():
                        self.click_unitil_interactable(po_element)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(po_element[0])
                return po_element.text.lower()
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def enterPermanentAddress(self, permanentAddress):
        try:
            time.sleep(1)
            if len(permanentAddress)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentAddress_Xpath)))
                self.driver.find_element(By.XPATH,self.text_permanentAddress_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_presentPincode_Xpath).send_keys(permanentAddress)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    def enterPermanentLandmark(self, permanentLandmark):
        try:
            time.sleep(1)
            if len(permanentLandmark)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentLandmark_Xpath)))
                self.driver.find_element(By.XPATH,self.text_permanentLandmark_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_permanentLandmark_Xpath).send_keys(permanentLandmark)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    def enterPermanentPincode(self, permanentPincode):
        try:
            time.sleep(1)
            if len(permanentPincode)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_permanentPincode_Xpath)))
                self.driver.find_element(By.XPATH,self.text_permanentPincode_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_permanentPincode_Xpath).send_keys(permanentPincode)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    def enterPermanentPostOffice(self, permanentPostOffice):
        try:
            time.sleep(1)
            if len(permanentPostOffice)!=0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_permanentPostOffice_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_permanentPostOffice_Xpath))
                time.sleep(2)
                po_elements=self.driver.find_elements(By.XPATH,self.options_getAllPO_Xpath)
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
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    def clickCheckboxAndEnterPermanentAddress(self,checkboxStatus,permanentAddress, PermanentLandmark, PermanentPincode,PermanentPO):
        try:
            time.sleep(1)
            if len(permanentAddress)!=0 or len(PermanentLandmark)!=0 or len(PermanentPincode)!=0 or len(PermanentPO)!=0:
                if checkboxStatus.lower()=='yes':
                    self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.clickCheckboxAndEnterPermanentAddress))
                else:
                    self.enterPermanentAddress(permanentAddress)
                    self.enterPermanentLandmark(PermanentLandmark)
                    self.enterPermanentPincode(PermanentPincode)
                    self.enterPermanentPostOffice(PermanentPO)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDateOfBirth(self,birthYear,birthMonth,birthDate):
        try:
            time.sleep(1)
            if len(birthYear)!=0 and len(birthMonth)!=0 and len(birthDate)!=0:
                dateOfBirth=str(birthDate)+str(birthMonth)+str(birthYear)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_dateOfBirth_Xpath)))
                self.driver.find_element(By.XPATH,self.click_dateOfBirth_Xpath).clear()
                self.driver.find_element(By.XPATH,self.click_dateOfBirth_Xpath).send_keys(dateOfBirth)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDikshaYear(self,dikshaYear,dikshaMonth,dikhaDay):
        try:
            if len(dikshaYear)== 4:
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_dikshaYear_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_dikshaYear_Xpath))
                time.sleep(2)
                years=self.driver.find_elements(By.XPATH,self.options_getAllDikshaYear_Xpath)
                for year in years:
                    if year.text.lower()==dikshaYear.lower():
                        self.click_unitil_interactable(year)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(year[0])
            if len(dikshaMonth)!= 0:
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_dikshaMonth_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_dikshaMonth_Xpath))
                time.sleep(2)
                months=self.driver.find_elements(By.XPATH,self.options_getAllDikshaMonth_Xpath)
                for month in months:
                    if month.text.lower()==dikshaMonth.lower():
                        self.click_unitil_interactable(month)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(month[0])

            if len(dikhaDay)!= 0:
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_dikshaDay_Xpath)))
                self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_dikshaDay_Xpath))
                time.sleep(2)
                days=self.driver.find_elements(By.XPATH,self.options_getAllDikshaDay_Xpath)
                for day in days:
                    if day.text.lower()==dikhaDay.lower():
                        self.click_unitil_interactable(day)
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    self.click_unitil_interactable(day[0])

        except Exception as e:
            raise CustomException(e,sys)
        
    def enterDpnfComment(self,comment):
        try:
            if len(comment)!=0:
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dpnfComments_Xpath)))
                self.driver.find_element(By.XPATH,self.text_dpnfComments_Xpath).clear()
                self.driver.find_element(By.XPATH,self.text_dpnfComments_Xpath).send_keys(comment)
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickSubmitAddToDPNF(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_SubmitToDPNFButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def navigateToPersonalInfoPage(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_PersonalInfoTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def navigateToAddressInfoPage(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_AddressInfoTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def navigateToDateAndSummarypage(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_DateSummaryTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickDoneSuccessButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_doneSuccessButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def enterFamilyCodeForAlreadyDpnfed(self, FamilyCode,PhilMemberName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_familyCode_Xpath)))
            self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).clear()
            self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
            time.sleep(2)

            if len(FamilyCode)!=0:
                PhilMemberName_locators=self.driver.find_elements(By.XPATH,self.options_getAllFamilyCode_Xpath)
                elements_text_value=[]
                for element in PhilMemberName_locators:
                    elements_text=str(element.text).lower().strip().split()
                    elements_text_value.append(" ".join(elements_text[:,-1]))
                print(elements_text_value)
                print(PhilMemberName_locators)
                print()

                element_dict=dict(zip(elements_text_value,PhilMemberName_locators))
                print(element_dict)
                
                for dict_key_text in element_dict.keys():
                    if dict_key_text == PhilMemberName.lower():
                        element_dict[dict_key_text].click()
                        #Check for error message
                        element=self.driver.find_elements(By.XPATH,self.text_checkForErrorMessage_Xpath)
                        if len(element)>0:
                            assert True, "Correct Error Message is being thrown on entering already added dpnfed data"
                        break
    
        except Exception as e:
            raise CustomException(e,sys)