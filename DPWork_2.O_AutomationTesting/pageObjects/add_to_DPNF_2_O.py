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

class AddToDPNF:
    click_dpnfFromNavigationPanel_Xpath='//*[text()="DPNF"]'
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
    click_gender_Xpath='//input[@formcontrolname="gender"]'
    options_getAllGender_Xpath='//*[contains(@id,"mat-option")]'
    #select_genderFemale_Xpath="//span[text()=' Female ']"
    #select_genderMale_Xpath="//span[text()=' Male ']"
    click_maritalStatus_Xpath='//input[@formcontrolname="maritalStatus"]'
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
    click_presentPostOffice_Xpath='//input[@formcontrolname="presPO"]'
    click_sameAsPresentAddress_Xpath='//span[@class="checkmark"]'
    text_permanentAddress_Xpath='//input[@formcontrolname="permAdd"]'
    text_permanentLandmark_Xpath='//input[@formcontrolname="permLandMark"]'
    text_permanentPincode_Xpath='//input[@formcontrolname="permPincode"]'
    click_presentPostOffice_Xpath='//input[@formcontrolname="permPO"]'
    options_getAllPO_Xpath='//*[contains(@id,"mat-option")]'

    click_dateOfBirth_Xpath='//input[@formcontrolname="dob"]'
    click_dikshaYear_Xpath='//input[@formcontrolname="dikshaYear"]'
    options_getAllDikshaYear_Xpath='//*[contains(@id,"mat-option")]'
    click_dikshaMonth_Xpath='//input[@formcontrolname="dikshaMonth"]'
    options_getAllDikshaMonth_Xpath='//*[contains(@id,"mat-option")]'
    click_dikshaDay_Xpath='//input[@formcontrolname="dikshaDay"]'
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
        
    def clickAddtoDPNF(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_AddToDpnfButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberFirstName(self,MemberFirstName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_firstname_Xpath)))
            self.driver.find_element(By.XPATH,self.text_firstname_Xpath).clear()
            if len(MemberFirstName)==0:
                MemberFirstName=''
            self.driver.find_element(By.XPATH,self.text_firstname_Xpath).send_keys(MemberFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberMiddleName(self,MemberMiddleName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_middlename_Xpath)))
            self.driver.find_element(By.XPATH,self.text_middlename_Xpath).clear()
            if len(MemberMiddleName)==0:
                MemberMiddleName=''
            self.driver.find_element(By.XPATH,self.text_middlename_Xpath).send_keys(MemberMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterMemberLastName(self,MemberLastName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_lastname_Xpath)))
            self.driver.find_element(By.XPATH,self.text_firstname_Xpath).clear()
            if len(MemberLastName)==0:
                MemberLastName=''
            self.driver.find_element(By.XPATH,self.text_firstname_Xpath).send_keys(MemberLastName)
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
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterGuardianFirstName(self,GuardianMiddleName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianFirst_Xpath)))
            self.driver.find_element(By.XPATH,self.text_guardianFirst_Xpath).clear()
            if len(GuardianMiddleName)==0:
                GuardianMiddleName=''
            self.driver.find_element(By.XPATH,self.text_guardianFirst_Xpath).send_keys(GuardianMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianMiddleName(self,GuardianMiddleName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianMiddle_Xpath)))
            self.driver.find_element(By.XPATH,self.text_guardianMiddle_Xpath).clear()
            if len(GuardianMiddleName)==0:
                GuardianMiddleName=''
            self.driver.find_element(By.XPATH,self.text_guardianMiddle_Xpath).send_keys(GuardianMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterGuardianLastName(self,GuardianLastName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_guardianLast_Xpath)))
            self.driver.find_element(By.XPATH,self.text_guardianLast_Xpath).clear()
            if len(GuardianLastName)==0:
                GuardianLastName=''
            self.driver.find_element(By.XPATH,self.text_guardianLast_Xpath).send_keys(GuardianLastName)
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
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterHusbandFirstName(self,HusbandFirstName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandFirst_Xpath)))
            self.driver.find_element(By.XPATH,self.text_husbandFirst_Xpath).clear()
            if len(HusbandFirstName)==0:
                HusbandFirstName=''
            self.driver.find_element(By.XPATH,self.text_husbandFirst_Xpath).send_keys(HusbandFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterHusbandMiddleName(self,HusbandMiddleName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandMiddle_Xpath)))
            self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).clear()
            if len(HusbandMiddleName)==0:
                HusbandMiddleName=''
            self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).send_keys(HusbandMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

        
    def enterHusbandLastName(self,HusbandLastName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_husbandLast_Xpath)))
            self.driver.find_element(By.XPATH,self.text_husbandLast_Xpath).clear()
            if len(HusbandLastName)==0:
                HusbandLastName=''
            self.driver.find_element(By.XPATH,self.text_husbandMiddle_Xpath).send_keys(HusbandLastName)
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
        except Exception as e:
            raise CustomException(e,sys)

    def enterFamilyCode(self,FamilyCode,PhilMemberName):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_familyCode_Xpath)))
            self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).clear()
            if len(FamilyCode)==0:
                FamilyCode=''
            self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
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
        except Exception as e:
            raise CustomException(e,sys)


    def enterContactNumber(self,contactNumber):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_contact_Xpath)))
            self.driver.find_element(By.XPATH,self.text_contact_Xpath).clear()
            if len(contactNumber)==0:
                contactNumber=''
            self.driver.find_element(By.XPATH,self.text_contact_Xpath).send_keys(contactNumber)
        except Exception as e:
            raise CustomException(e,sys)
        

    def enterGender(self,genderType):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_gender_Xpath)))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_gender_Xpath))
            gender_elements=self.driver.find_elements(By.XPATH,self.options_getAllGender_Xpath)
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
        except Exception as e:
            raise CustomException(e,sys)


    def enterMaritalStatus(self,maritalStatus,genderType,husbandFirstName,husbandMiddleName,husbandLastName):
        try:
            time.sleep(1)
            gender_status=self.enterGender(genderType)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.click_maritalStatus_Xpath)))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.click_maritalStatus_Xpath))
            maritalstatus_elements=self.driver.find_elements(By.XPATH,self.options_getAllMaritalStatus_Xpath)
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
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dikshaAddress_Xpath)))
            self.driver.find_element(By.XPATH,self.text_dikshaAddress_Xpath).clear()
            if len(dikshaAddress)==0:
                dikshaAddress=''
            self.driver.find_element(By.XPATH,self.text_dikshaAddress_Xpath).send_keys(dikshaAddress)
        except Exception as e:
            raise CustomException(e,sys)

    def enterDikshaLandmark(self,dikshaLandmark):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_dikshaLandmark_Xpath)))
            self.driver.find_element(By.XPATH,self.text_dikshaLandmark_Xpath).clear()
            if len(dikshaLandmark)==0:
                dikshaLandmark=''
            self.driver.find_element(By.XPATH,self.text_dikshaLandmark_Xpath).send_keys(dikshaLandmark)
        except Exception as e:
            raise CustomException(e,sys)

    def enterDikshaPincode(self,dikshaPincode):
        pass

    def enterPresentAddress(self,presentAddress):
        pass

    def enterPresentLandmark(self,presentLandmark):
        pass

    def enterPresentPincode(self,presentPincode):
        pass

    def enterPresentPostOffice(self,presentPostOffice):
        pass

    def enterPermanentAddress(self, permanentAddress):
        pass
    def enterPermanentLandmark(self, permanentLandmark):
        pass
    def enterPermanentPincode(self, permanentPincode):
        pass
    def enterPermanentPostOffice(self, permanentPostOffice):
        pass
    def clickCheckboxAndEnterPermanentAddress(self,checkboxStatus):
        pass