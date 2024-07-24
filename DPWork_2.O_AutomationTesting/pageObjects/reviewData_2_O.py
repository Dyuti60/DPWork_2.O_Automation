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
    serialNumberUpdated=''
    check_updateDetailsInManageSextionReviewDataTitleText_Xpath='//*[@class="topHead d-flex justify-content-between"]//*[contains(text(),"Review updated data ({})")]'.format(str(serialNumberUpdated))
    fetch_getAllUpdateHeaderFieldsInReviewDataManageSection='//*[@class="inpLabel"]'
    fetch_getAllUpdateFieldValuesInReviewDataManageSection=''
    button_clicktoCloseManageUpdateInReviewDataWindow_Xpath='//button[@class="close-button" and @type="button"]'

    #Update History in Review Data:
    serialNumberUpdated=''
    check_updateHistoryTitleText_Xpath='//*[@class="topHead d-flex justify-content-between"]//*[contains(text(),"Update History- {}")]'.format(str(serialNumberUpdated))
    fetch_getAllUpdateHistoryElements_Xpath='//*[@class="d-flex justify-content-between"]'

    fetch_getAllUpdateHistoryHeaderFields_Xpath='//span[@class="details-head"]'
    fetch_getAllUpdateHistoryFieldValues_Xpath='//span[@class="details-data"]'

    button_clicktoCloseUpdateHistoryWindow_Xpath='//button[@class="close-button" and @type="button"]'
    
    #Filter
    button_clickSearchFilterButtonInUpdatedReviewDataPage_Xpath='//button[@class="dp-secondary-btn btn-div d-flex ng-star-inserted"]'
    check_SearchFilterWindowTitleText_Xpath='//span[contains(text(),"Search Data")]'
    check_SearchFilterWindowSerialNumberHeaderText_Xpath='span[@class="input-text" and contains(text(),"Serial Number")]'
    check_SearchFilterWindowPincodeHeaderText_Xpath='span[@class="input-text" and contains(text(),"Pincode")]'
    check_SearchFilterWindowSerialNumberHeaderText_Xpath='span[@class="input-text" and contains(text(),"Field Worker")]'
    button_clickSearchFilterWindowCrossButton_Xpath='//*[@class="close-button"]'
    button_clickClearAllButton_Xpath='//button[@class="dp-secondary-btn btn-div" and contains(text(),"clear All")]'
    button_clickSearchButton_Xpath='//button[@class="dp-primary-btn btn-div" and contains(text(),"Search")]'

    text_enterSerialNumberInSearchFilterWindow_Xpath='//input[@class="search-input dp-input-control ng-pristine ng-valid ng-touched" and @type="tel" and @placeholder="Enter Sl. No"]'
    text_enterPincodeInSearchFilterWindow_Xpath='//input[@class="mat-mdc-autocomplete-trigger search-input dp-input-control ng-untouched ng-valid ng-dirty" and @type="tel" and @placeholder="Enter Pincode"]'
    text_selectPincodeAfterEnteringPincode_Xpath='//*[contains(@id,"mat-option")]'
    text_enterFieldWorkerInSearchFilterWindow_Xpath='//input[@class="mat-mdc-autocomplete-trigger search-input dp-input-control ng-untouched ng-pristine ng-valid" and @type="text" and @placeholder="Enter FW Name"]'

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