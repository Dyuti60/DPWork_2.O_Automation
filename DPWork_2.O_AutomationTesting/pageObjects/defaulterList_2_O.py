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

class DefaulterLists:

    button_clickDP3_O_Button_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"DP 3.0")]'
    button_clickDefaulterListInDP3_OButton_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Defaulter List")]'
    text_ReachDefaultersHeaderTitleText_Xpath='//span[@class="heading-text ng-star-inserted" and contains(text(),"Reach Defaulter")]'
    button_defaultersTabButton_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Defaulters")]'
    button_reachedTabButton_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Reached")]'
    button_restoreTabButton_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Restored")]'

    button_clickStateDropdown_ID='mat-select-value-1'
    options_getAllStatesFromDropdown_Xpath='//*[contains(@id,"mat-option")]'
    button_clickDistrictDropdown_ID='mat-select-value-11'
    options_getAllDistrictFromDropdown_Xpath='//*[contains(@id,"mat-option")]'

    text_SearchByAnyText_Xpath='//*[@class="search-input dp-input-control ng-untouched ng-pristine ng-valid" and @type="text" and @placeholder="Search by any column"]'
    text_getAllReachDefaultersTableHeaderText_TagName='th'
    text_getAllReachDefaultersTableFieldValues_TagName='td'
    click_getAllFamilyCodeInReachDefaultersTableFieldValues_Xpath='//td[@class="fc-text"]'

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

    #Click Each Records to Expand
    click_getEachRecordToExpand_Xpath='//tr[@class="ng-star-inserted" and @mattooltip="Click to expand"]'
    fetch_getAllHeadersFromInteriorTableReachDefaulters_Xpath='//span[@class="header-text"]'
    fetch_getAllFieldValuesExceptFamilyCodeFromInteriorTableReachDefaulters_Xpath='//span[@class="table-data-text"]'
    fetch_getAllFieldValuesOnlyFamilyCodeFromInteriorTableReachDefaulters_Xpath='//span[@class="fc-text"]'

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