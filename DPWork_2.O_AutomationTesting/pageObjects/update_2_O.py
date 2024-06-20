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

    text_enterfamilyCode_Xpath='//*[@class="search-input dp-input-control"]'
    button_clickUpdateClearButton_Xpath='//*[@class="clr dp-secondary-btn"]'
    button_clickUpdateSearchButton_Xpath='//*[@class="src dp-primary-btn"]'
    button_clickUpdateUpdateButton_Xpath='//*[@class="dp-primary-btn updateButton"]'
    

    #Update:
    button_clickSubmitDPNFButton_Xpath='//*[@class="dp-primary-btn updateButton"]'
    text_suggestedMemberName_CSSSelector='input[formcontrolname="memberName"]'
    text_suggestedGuardianName_CSSSelector='input[formcontrolname="gurdianName"]'
    text_suggestedRitwikName_CSSSelector='input[formcontrolname="ritwikName"]'

    button_clickPersonalInforNextButton_Xpath='//*[@class="personal-next dp-primary-btn"]'
    button_clickPersonalQuitUpdation_Xpath='//*[@class="quit-update"]'


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
        
    
    def enterSerialNumber(self,serialNumber):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterfamilyCode_Xpath)))
            self.driver.find_element(By.XPATH, self.text_enterfamilyCode_Xpath).clear()
            self.driver.find_element(By.XPATH, self.text_enterfamilyCode_Xpath).send_keys(serialNumber)
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
            
        
    def extractDateFetchedBySerialNumber(self):
        pass