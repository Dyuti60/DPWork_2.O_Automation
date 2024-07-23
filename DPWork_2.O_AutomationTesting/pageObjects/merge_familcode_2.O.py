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

class MergeFamilyCode:
    click_DP2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"DP 2.0")]' #done
    click_MergeFC_DP_2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Merge FC")]' #done
    check_MergeFCHeadingTitleText_Xpath='//span[@class="heading-text" and contains(text(),"Merge FC")]' #done
    check_MergeFCModuleDescription_Xpath='//span[@class="search-text" and contains(text(),"Search for a serial number that you wish to merge family codes for")]' #done
    button_clickMergeHistory_Xpath='//*[@class="img-button dp-secondary-btn"]' #done

    fetchdata_getAllHeadersText_Xpath='//span[@class="heading-class"]'
    fetchdata_getAllHeadersContentText_Xpath='//span[@class="heading-content"]'
    click_closeButtonToCloseMergeHistory_Xpath='//*[@class="img-container" and @type="button"]'
    
    text_enterSerialNumberOnWhichMergeFCWillHappen_Xpath='//input[@class="dp-input-control input-content ng-untouched ng-pristine ng-valid" and type="tel" and @placeholder="Enter Serial No."]'
    fetch_headerDetailOfDAApprovedserialNumberMergeFC_Xpath='//span[@class="detail-heading"]'
    fetch_fieldvaluesOfDAApprovedserialNumberMergeFCOnlySerialNumber_Xpath='//span[@class="sl-text"]'
    fetch_fieldvaluesOfDAApprovedserialNumberMergeFCExceptSerialNumber_Xpath='//span[@class="detail-text"]'
    button_clickStartMergingButton_Xpath='//button[@class="dp-primary-btn img-button" and contains(text(),"Start Merging")]'
    text_enterFCCodeToMerge_Xpath='//input[@class="mat-mdc-autocomplete-trigger dp-input-control input-content ng-pristine ng-valid ng-touched" and @type="tel" and @placeholder="Enter FC code to merge"]'
    click_getAllFCPhilNameToMerge_Xpath='//*[contains(@id,"mat-option")]'
    check_confirmPhilNamePopupTitleText_Xpath='//*[@class="wishlist-text" and contains(text(),"Confirm Member Name")]'
    check_confirmPhilNamePopupDescriptionText_Xpath='//*[@class="select-wishlist mb-1" and contains(text(),"Member Name and Philanthropy name do not match")]'
    click_confirmPhilNameContinueButton_Xpath='//*[@class="dp-primary-btn wishlist-btn ms-3" and contains(text(),"Yes, Continue")]'
    click_confirmPhilNameCancelButton_Xpath='//*[@class="dp-secondary-btn wishlist-btn ms-3" and contains(text(),"No, cancel")]'

    button_clickDeleteMergedFC_Xpath='//button[@class="merge-btn ng-star-inserted"]'
    button_clickMergedFCCodes_Xpath='//button[@class="dp-primary-btn merge-code-btn ng-star-inserted"]'

    fetch_headerDetailOfSerialNumberMergeFCInteriior_Xpath='//span[@class="detail-heading"]'
    fetch_fieldvaluesOfSerialNumberMergeFCInterior_Xpath='//span[@class="detail-text"]'

    '''
    1. check for Merge FC Success message
    2. click cross button to cancel Merge FC Window
    3. click done button to close Merge FC window
    '''
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
        
    def clickDP2_OFromNavigationPanel(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_DP2_O_FromNavigationPanel_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickMergeFCFromDP2_OSubsectionInNavigationPanel(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_MergeFC_DP_2_O_FromNavigationPanel_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickMergeHistoryButton(self):
        try:
            time.sleep(0.5)
            if(len(self.driver.find_elements(self.check_MergeFCHeadingTitleText_Xpath))>0 and self.driver.find_elements(self.check_MergeFCHeadingTitleText_Xpath)>0):
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickMergeHistory_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def getAllFieldHeadersFromMergeHistory(self):
        try:
            headersMergeHistoryList=[]
            headerElements=self.driver.find_elements(By.XPATH,self.fetchdata_getAllHeadersText_Xpath)
            for headerElement in headerElements:
                headersMergeHistoryList.append(headerElement.text)
            return headersMergeHistoryList
        except Exception as e:
            raise CustomException(e,sys)
        
    