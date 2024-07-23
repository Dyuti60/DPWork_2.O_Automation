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

class FindDetails:
    click_DP2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"DP 2.0")]'
    click_FindDetails_DP_2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Find Details")]'
    check_FindDetailsPageTitle_Xpath='//span[@class="details-text" and contains(text(),"Find details")]'
    click_AssignedTabFromTopFindDetails_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Assigned List")]'
    click_TransferRequestsFromTopFindDetails_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Transfer Requests")]'
    click_NotFoundListFromTopFindDetails_Xpath='//*[contains(@class,"dp-chip ng-star-inserted") and contains(text(),"Not Found List")]'
    click_stateFilterDropdown_ID="state"
    click_getAllStateOptions_Xpath='//*[contains(@id,"mat-option")]'
    click_stateFilterDropdown_ID="district"
    click_getAllDistrictOptions_Xpath='//*[contains(@id,"mat-option")]'
    text_searchByNameInDisplayedData_Xpath='//input[@class="dp-input-control input-field-control ng-untouched ng-pristine ng-valid" and @placeholder="Search by name"]'
    text_searchByAddressInDisplayedData_Xpath='//input[@class="dp-input-control input-field-control ng-untouched ng-pristine ng-valid" and @placeholder="Search by name"]'
    click_myWishlistIcon_Xpath='//*[@class="wishlist-btn dp-primary-btn"]'
    click_FavouritesButtonForRecord_Xpath='//span[@class="ms-1" and contains(text(),"Favourites")]'
    click_WishlistButtonForRecord_Xpath='//span[@class="ms-1" and contains(text(),"Wishlist")]'
    click_MigrateButtonForRecord_Xpath='//span[@class="ms-1" and contains(text(),"Migrate")]'
    click_DataNotFoundButtonForRecord_Xpath='//span[@class="ms-1" and contains(text(),"Data not found")]'
    click_CollapseRecordButton_Xpath='//*[@class="mat-mdc-tooltip-trigger collapse-container" and @mattooltip="Click to collapse"]'

    tableColValue_exteriorTableData_Tag='td'
    tableColValue_interiorTableData_Xpath='//span[@class="table-data-text")]'
    tableColValue_interiorTableDataFamilyCodeOnly_Xpath='//span[@class="fc-text")]'

    click_4DoneButton_Xpath='//button[@class="save-button dp-primary-btn ng-star-inserted" and contains(text(),"Done")]'
    click_close4SuccessMessage_Xpath='//*[@class="close-button"]'
    MemberName=''
    check_favouritesSuccessMessage_Xpath='//*[contains(text(),"{} has been successfully added to your Favourites.")]'.format(MemberName)
    getAll_Wishlist_Items='//span[@class="item-text"]'
    text_searchAWishlistByName_Xpath='//input[@class="dp-input-control wishlist-input ng-pristine ng-valid ng-touched" and contains(@placeholder,"Search for a wishlist by name")]'
    check_MyWishlistText_Xpath='//span[@class="wishlist-text" and contains(text(),"My wishlists")]'
    button_createNewWishlist_Xpath='//*[@class="ms-1" and contains(text(),"Create new")]'
    MemberName=''
    check_AddToWishlistSuccessMessage_Xpath="//*[contains(text(),'Datum added to wishlist '{}' successfully!') and contains(text(),'Your can access all wish-lists from the ‘My wishlists’') ]".format(MemberName)
    click_EditDeleteWishlistButton_Xpath="//*[@class='icon-img']"
    getName_wishlistTobeDeletedOrEdited_Xpath='//*[@class="icon-img"]//..//..//span[@class="item-text"]'
    click_closeButtonOfWishlistWindow_Xpath="//*[@class='img-container']"

    click_migrateStateDistrictPincode_123_Dropdown_Xpath='//*[@id="state"]'
    getAll_migrateState_Options="//*[@contains(@id,'mat-option')]"
    getAll_migrateDistrictFromState_Options="//*[@contains(@id,'mat-option')]"
    getAll_migratePincodeFromDistrict_Options="//*[@contains(@id,'mat-option')]"
    click_migrateButton_Xpath="//button[@class='dp-primary-btn save-btn edit-gap ng-star-inserted' and contains(text(),'Yes,Migrate')]"
    click_cancelMigrate_Xpath="//button[@class='dp-secondary-btn save-btn edit-gap' and @type='button' and contains(text(),'No,cancel')]"
    click_closeMigrateWindow_Xpath="//*[@class='img-container']"
    memberName=''
    check_migrateMemberDetails_Xpath='//*[contains(text(),"Migrate - {}")]'.format(memberName)
    check_migrateStateText_Xpath='//*[contains(text(),"Enter State*")]'
    check_migrateDistrictText_Xpath='//*[contains(text(),"Enter district*"]'
    check_migratePincodeText_Xpath='//*[contains(text(),"Enter pincode (Optional)"]'

    enter_dataNotFoundComments_Xpath='//*[formcontrolname="comments"]'
    check_dataNotFoundCommentsTitle_Xpath='//*[contains(text(),"Add Comments")]'
    check_dataNotFooundCommentsHeading_Xpath='//*[contains(text(),"Comments *")]'
    click_closeDataNotFoundWindow_Xpath="//*[@class='img-container']"
    button_clickSubmitButton_Xpath='//button[@class="dp-primary-btn save-btn edit-gap" and contains(text(),"Submit")]'
    get_errorMessageDataNotFound_Xpath="//*[contains(text(),'Last istravrity date of the datum must be before 2023 to mark it as untrackable')]"
    get_errorMessageForInvalidComment_Xpath='//*[contains(text(),"Comments is invalid.")]'


    
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
        
    