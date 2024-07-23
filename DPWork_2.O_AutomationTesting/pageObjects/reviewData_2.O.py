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

class ReviewData:
    check_reviewDataTitleText_Xpath='//span[@class="ng-star-inserted" and contains(text(),"Review data")]'
    check_allCountryNavigationText_Xpath='//span[@class="eachBread" and contains(text(),"All countries")]'
    check_IndiaNavigationText_Xpath='//span[@class="eachBread ng-star-inserted" and contains(text(),"India")]'

    button_clickFCMergeDataTab_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"FC Merge data")]'
    button_clickUpdateDataTab_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Update data")]'
    fetch_getAllHeaderTextInIndiaNavigation_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllTableTextValuesInIndiaNavigation_Xpath='//td[@class="ng-star-inserted"]'
    state="WEST BENGAL"
    fetch_getAllStateLinkInIndiaNavigation_Xpath='//span[@class="text-details" and contains(text(),{})]'.format(str(state).upper())
    
    check_userSelectedStateInNavigationText_Xpath='//span[@class="eachBread ng-star-inserted" and contains(text(),{})]'.format(str(state).upper())
    fetch_getAllHeaderTextInUserSelectedStateNavigation_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllTableTextValuesInUserSelectedStateNavigation_Xpath='//td[@class="ng-star-inserted"]'
    district='KOLKATA'
    fetch_getAllDistrictLinkInStateNavigation_Xpath='//span[@class="text-details" and contains(text(),{})]'.format(str(district).upper())
    
    check_userSelectedDistrictInNavigationText_Xpath='//span[@class="eachBread ng-star-inserted" and contains(text(),{})]'.format(str(district).upper())
    fetch_getAllHeaderTextInUserSelectedDistrictNavigation_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllTableTextValuesInUserSelectedDistrictNavigation_Xpath='//td[@class="ng-star-inserted"]'
    button_clickManageButton_Xpath='//button[@class="manage-user-button dp-secondary-btn" and contains(text(),"Manage")]'

    #Manage in FC Merge:
    check_FCMergeTitle_Xpath='//span[contains(text(),"Review Merge FC data")]'
    check_FCMergeMemberDetailsSubtitle_Xpath='//span[@class="grid-head" and contains(text(),"Member Details")]'
    check_FCMergeDetailsSubtitle_Xpath='//span[@class="grid-head" and contains(text(),"Merge FC Details")]'

    fetch_getAllMemberDetailsHeaderText_Xpath='//div[@class="details d-flex justify-content-between"]//span[@class="details-head"]'
    fetch_getAllMergeFCDetailsHeaderText_Xpath='//div[@class="details d-flex justify-content-between"]//span[@class="details-head"]'
    button_clickCrossToCloseMergeFCManageWindow_Xpath='//*[@class="close-button" and @type="button"]'

    #Manage in Update:
    #fetch_getAllUpdateField

    #Filter




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