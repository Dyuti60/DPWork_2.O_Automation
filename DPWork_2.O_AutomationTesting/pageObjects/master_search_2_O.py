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


class DpWorkMasterSearchPage:
    #Tab Locator
    button_clickGlobalSearchTab_Xpath="//*[contains(text(),'Global search')]"
    button_clickKeywordSearchTab_Xpath="//*[contains(text(),' Keyword search ')]"
    button_clickAreYouUpdatedTab_Xpath="//*[contains(text(),' Are you updated? ')]"
    #Global Search Tab fields Locator
    text_globalSearchByName_Xpath='//*[@class="search-input dp-input-control ng-untouched ng-pristine ng-valid"]'
    button_globalSearchByNameClear_Xpath='//*[@class="dp-secondary-btn"]'
    button_globalSearchByNameSearch_Xpath='//*[@class="bprimary dp-primary-btn"]'
    #Keyword Search Tab fields Locator
    text_memberFirstName_CSSSelector="input[formcontrolname='firstName']"
    text_memberMiddleName_CSSSelector="input[formcontrolname='middleName']"
    text_memberLastName_CSSSelector="input[formcontrolname='lastName']"
    text_ritwikFirstName_CSSSelector="input[formcontrolname='ritwiki_first_name']"
    text_ritwikMiddleName_CSSSelector="input[formcontrolname='ritwiki_middle_name']"
    text_ritwikLastName_CSSSelector="input[formcontrolname='ritwiki_last_name']"
    text_guardianFirstName_CSSSelector="input[formcontrolname='guardian_first_name']"
    text_guardianMiddleName_CSSSelector="input[formcontrolname='guardian_middle_name']"
    text_guardianLastName_CSSSelector="input[formcontrolname='guardian_last_name']"
    text_initiationDate_CSSSelector="input[formcontrolname='mship_date']"
    text_address_CSSSelector="input[formcontrolname='address']"
    text_pinCode_CSSSelector="input[formcontrolname='pinCode']"
    click_stateDropDown_CSSSelector="input[formcontrolname='state_name']"
    select_stateDropDownOption_Xpath='//*[contains(text(),{})]'
    click_districtDropDown_CSSSelector="input[formcontrolname='district_name']"
    select_districtDropDownOption_CSSSelector='//*[contains(text(),{})]'
    button_keywordSearchClear_Xpath='//*[@class="clearBtn dp-secondary-btn"]'
    button_keywordSearchSearch_Xpath='//*[@class="bprimary dp-primary-btn"]'
    #Are you updated Tab fields locator
    text_enterFCForAreYouUpdated_Xpath='//*[@class="searchInput dp-input-control ng-untouched ng-pristine ng-valid"]'
    button_areYouUpdatedSearchClear_Xpath='//*[@class="dp-secondary-btn"]'
    button_areYouUpdatedSearchSearch_Xpath='//*[@class="bprimary dp-primary-btn"]'

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
        
    def clickGlobalSearchTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickGlobalSearchTab_Xpath))
            #self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickGlobalSearchTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def enterNameAndDoGlobalSearch(self,Name):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_globalSearchByName_Xpath)))
            self.driver.find_element(By.XPATH, self.text_globalSearchByName_Xpath).clear()
            self.driver.find_element(By.XPATH, self.text_globalSearchByName_Xpath).send_keys(Name)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickGlobalSearchClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_globalSearchByNameClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickGlobalSearchSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_globalSearchByNameSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def extractGlobalSearchData(self):
        pass        

    def clickKeyWordSearchTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickKeywordSearchTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterMemberFirstName(self, memberFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector).send_keys(memberFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberMiddleName(self, memberMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector).send_keys(memberMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberLastName(self, memberLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberLastName_CSSSelector).send_keys(memberLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterGuardianFirstName(self, guardianFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector).send_keys(guardianFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianMiddleName(self, GuardianMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector).send_keys(GuardianMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianLastName(self, guardianLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector).send_keys(guardianLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterRitwikFirstName(self, ritwikFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector).send_keys(ritwikFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterRitwikMiddleName(self, ritwikMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector).send_keys(ritwikMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterRitwikLastName(self, ritwikLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector).send_keys(ritwikLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterInitiationDate(self, initiationDate):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_initiationDate_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_initiationDate_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_initiationDate_CSSSelector).send_keys(initiationDate)
        except Exception as e:
            raise CustomException(e,sys)

    def enterPinCode(self, pinCode):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_pinCode_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_pinCode_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_pinCode_CSSSelector).send_keys(pinCode)
        except Exception as e:
            raise CustomException(e,sys)

    def enterAddress(self, address):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_address_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_address_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_address_CSSSelector).send_keys(address)
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterState(self, state):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_stateDropDown_CSSSelector)))
            self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR,self.click_stateDropDown_CSSSelector))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.select_stateDropDownOption_Xpath.format(state)))
        except Exception as e:
            raise CustomException(e,sys)

    def enterDistrict(self, district):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_districtDropDown_CSSSelector)))
            self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR,self.click_districtDropDown_CSSSelector))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.select_districtDropDownOption_CSSSelector.format(district)))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickKeywordSearchClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_keywordSearchClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickKeywordSearchSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_keywordSearchSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def extractKeywordSearchData(self):
        pass

    def clickAreYouUpdatedTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_elements(By.XPATH,self.button_clickGlobalSearchTab_Xpath)[3])
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterFCForAreYouUpdated(self,familyCode):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterFCForAreYouUpdated_Xpath)))
            self.driver.find_element(By.XPATH, self.text_enterFCForAreYouUpdated_Xpath).clear()
            self.driver.find_element(By.XPATH, self.text_enterFCForAreYouUpdated_Xpath).send_keys(familyCode)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickAreYouUpdatedSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_areYouUpdatedSearchSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickAreYouUpdatedClickButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_areYouUpdatedSearchClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def extractAreYouUpdatedData(self):
        pass