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

class PrintAndMontor:
    click_DatumModuleFromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Datum")]'
    click_PrintAndMonitorFromDatumInNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Print & Monitor"]'

    check_PrintAndMontorTitleText_Xpath='//h1[@class="print-monitor-text" and contains(text(),"Print and monitor")]'
    check_allCountriesText_Xpath='//*[@class="brancd-prime me-2 cursor-pointer ng-star-inserted" and contains(text(),"All countries")]'
    check_IndiaText_Xpath='//*[@class="me-2 ng-star-inserted text-disable" and contains(text(),"India")]'

    fetch_getAllPrintAndMonitorStateHeaderTableData_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllPrintAndMonitorStateFieldValuesTableDataOnlyStates_Xpath='//span[@class="text-details"]'
    state='Odisha'
    link_clickPrintAndMonitorStateByName_Xpath='//span[@class="text-details" and contains(text(),{})]'.format(state)
    fetch_getAllPrintAndMonitorStateFieldValuesTableDataOtherThanStates_Xpath='//span[@class="cell-text"]'

    check_stateText_Xpath='//span[@class="text-disable me-2 ng-star-inserted" and contains(text(),{})]'.format(str(state).upper())
    fetch_getAllPrintAndMonitorDistrictHeaderTableData_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllPrintAndMonitorDistrictFieldValuesTableDataOnlyDistrict_Xpath='//span[@class="text-details"]'
    district='Cuttack'
    link_clickPrintAndMonitorDistrictByName_Xpath='//span[@class="text-details" and contains(text(),{})]'.format(str(district).upper())
    fetch_getAllPrintAndMonitorFieldValuesTableDataOtherThanDistrict_Xpath='//span[@class="cell-text"]'
    
    check_districtText_Xpath='//span[@class="text-disable me-2 ng-star-inserted" and contains(text(),{})]'.format(str(district).upper())
    fetch_getAllPrintAndMonitorPincodeHeaderTableData_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllPrintAndMonitorPincodeFieldValuesTableData_Xpath='//span[@class="cell-text"]'
    fetch_allPincodeRecordCountsAndClick_CSSSelector='dynamic-component.ng-star-inserted'

    pincode='722208'
    check_PincodeText_Xpath='//span[@class="text-disable me-2 ng-star-inserted" and contains(text(),{})]'.format(str(pincode))
    fetch_getAllPrintAndMonitorRecordHeaderTableData_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllPrintAndMonitorRecordFieldValuesTableDataExceptSerialNumber_Xpath='//span[@class="cell-text"]'
    fetch_getAllPrintAndMonitorRecordFieldValuesTableDataOnlySerialNumber_Xpath='//*[@class="serial-no"]'

    #Click Favourites Wishlist Contacts
    button_getAllFavWishContactClicked_Xpath='//button[contains(@class,"dp-secondary-btn btn-padding")]'
    button_getAllCheckMarkClicked_Xpath='//span[@class="checkmark"]'

    button_clickPrintAllButton_Xpath='//button[@class="print-selected-button dp-secondary-btn ng-star-inserted"]'
    button_clickPrintSelectedButton_Xpath='//button[@class="print-selected-button dp-primary-btn ng-star-inserted"]'

    button_clickMyWishlistDisplayIcon_Xpath='//button[@class="wishlist-btn dp-primary-btn ng-star-inserted"]'

    #Inside Wishlist Locators:
    getAll_Wishlist_Items='//span[@class="item-text"]'
    text_searchAWishlistByName_Xpath='//input[@class="dp-input-control wishlist-input ng-pristine ng-valid ng-touched" and contains(@placeholder,"Search for a wishlist by name")]'
    check_MyWishlistText_Xpath='//span[@class="wishlist-text" and contains(text(),"My wishlists")]'
    button_createNewWishlist_Xpath='//*[@class="ms-1" and contains(text(),"Create new")]'
    test_enterNameToCreateWishlist_Xpath='//*[@class="search-input dp-input-control ng-pristine ng-valid ng-touched" and @type="text" and @placeholder="Enter a name for the wishlist"]'
    button_clickSelectExistingButtonForWishlist_Xpath='//*[@class="dp-secondary-btn wishlist-btn" and @type="Select existing" and @type="button"]'
    button_clickSelectExistingButtonForWishlist_Xpath='//*[@class="dp-secondary-btn wishlist-btn" and @type="Create" and @type="submit"]'
    check_createWishlistHeaderText_Xpath='//*[@class="select-wishlist mb-1" and contains(text(),"Wishlist name")]'
    check_createWishlistWindowTitleText_Xpath='//span[@class="wishlist-text" and contains(text(),"Add to wishlist")]'
    MemberName=''
    check_AddToWishlistSuccessMessage_Xpath="//*[contains(text(),'Datum added to wishlist '{}' successfully!') and contains(text(),'Your can access all wish-lists from the ‘My wishlists’') ]".format(MemberName)
    click_EditDeleteWishlistButton_Xpath="//*[@class='icon-img']"
    getName_wishlistTobeDeletedOrEdited_Xpath='//*[@class="icon-img"]//..//..//span[@class="item-text"]'
    click_closeButtonOfWishlistWindow_Xpath="//*[@class='img-container']"
    











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