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

class NamesToUpdate:
    click_DP2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"DP 2.0")]'
    click_NamesToUpdate_DP_2_O_FromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Names To Update")]'
    check_NamesToUpdateModuleTitleText_Xpath='//*[contains(text(),"update-text")]'
    click_AllNamesTab_Xpath='//*[contains(@class,"dp-chip") and contains(text(),"All names")]'
    click_AssignedTab_Xpath='//*[contains(@class,"dp-chip") and contains(text(),"Assigned")]'
    click_NotAssignedTab_Xpath='//*[contains(@class,"dp-chip") and contains(text(),"Not Assigned")]'
    click_stateFilterDropdown_ID="state"
    click_getAllStateOptions_Xpath='//*[contains(@id,"mat-option")]'
    click_stateFilterDropdown_ID="district"
    click_getAllDistrictOptions_Xpath='//*[contains(@id,"mat-option")]'
    text_searchByNameOnFetchedResultNamesToUpdate_Xpath='//input[@class="dp-input-control input-field-control ng-untouched ng-pristine ng-valid" and @placeholder="Search by name"]'
    text_searchByAddressOnFetchedResultNamesToUpdate_Xpath='//input[@class="dp-input-control input-field-control ng-untouched ng-pristine ng-valid" and @placeholder="Search by address"]'
    text_searchByPinCodeOnFetchedResultNamesToUpdate_Xpath='//input[@class="dp-input-control input-field-control ng-untouched ng-pristine ng-valid" and @placeholder="Search by PIN"]'
    click_familyCodeColumnRecord_Xpath='//td[@class="fc-text"]'
    getAll_tableColumnHedderNamesToUpdate_ClassName='th'
    getAll_tableColumnValueNamesToUpdate_ClassName='td'
    check_AreYouUpdatedTitleText_Xpath='//*[@class="updated-text" and contains(text(),"Are you updated?")]'
    getAll_tableColumnHeaderAreYouUpdated_Xpath='//th[@class="ng-star-inserted"]'
    getAll_tableColumnValuesExceptSerialNumberAreYouUpdated_Xpath='//span[contains(@class,"cell-text")]'
    getAll_tableColumnValuesOnlySerialNumberAreYouUpdated_Xpath='//span[@class="mat-mdc-tooltip-trigger serial-no-text cursor-pointer" and @mattooltipposition,"below")]'
    click_rowFieldToExpand_Xpath='//tr[@class="mat-mdc-tooltip-trigger ng-star-inserted" and @mattooltip="Click to expand" and @mattooltipposition="below"]'
    getAll_interiorTableColumnValuesExcludingFC_Xpath='//span[@class="table-data-text"]'
    getAll_interiorTableColumnValuesOnlyFC_Xpath='//span[@class="fc-text"]'
    click_toCollapseNamesToUpdateRecord_Xpath='//span[@class="mat-mdc-tooltip-trigger collapse-container" and @mattooltip="Click to collapse" and @mattooltipposition="above"]'
    click_editButtonforRecordsNamesToUpdate_Xpath='//span[@class="ms-1" and contains(text(),"Edit")]'
    click_searchButtonforRecordsNamesToUpdate_Xpath='//span[@class="ms-1" and contains(text(),"Search")]'
    click_AssignToFWButtonforRecordsNamesToUpdate_Xpath='//button[@class="dp-primary-btn-disabled hover-btn btn-pointer ng-star-inserted dp-primary-btn"]'

    #Edit Button
    button_clickCrossButtonToRemoveSerialNumber_Xpath='//img[@class="input-cross-icon position-absolute"]'
    text_enterEditedContactNumber_Xpath='//input[@formcontrolname="contactNo"]'
    text_enterEditedAddress_Xpath='//input[@formcontrolname="address"]'
    button_saveEditedChanges_Xpath='//button[@class="dp-primary-btn save-btn edit-gap"]'
    button_clickCrossButtonToCancelEditWindow_Xpath='//button[@class="img-container" and @type="button"]'

    check_editPageTitle_Xpath='//span[@class="edit-details-text" and contains(text(),"Edit details")]'
    check_serialNumberHeaderText_Xpath='//*[@class="search-text" and contains(text(),"Serial no.")]'
    check_contactNumberHeaderText_Xpath='//*[@class="search-text" and contains(text(),"Contact no.")]'
    check_addressHeaderText_Xpath='//*[@class="search-text" and contains(text(),"Address")]'

    #Search Button
    check_masterSearchTitleText_Xpath='//*[@class="master-search-text" and contains(text(),"Master Search")]'
    get_masterSearchNameRitwikAddressHeader_Xpath='//*[@class="received-data d-flex flex-wrap"]//span//strong]'
    get_masterSearchNameRitwikAddressValues_Xpath='//*[@class="received-data d-flex flex-wrap"]//span]'

    button_clickMasterSearchSearchButton_Xpath='//button[@class="dp-primary-btn search-btn ms-3" and contains(text(),"Search")]'
    button_clickMasterSearchClearButton_Xpath='//button[@class="dp-secondary-btn clear-btn" and @type="reset" and contains(text(),"Clear Entries")]'
    button_closeMasterSearchWindow_Xpath='//*[@class="img-container"]'
    
    #Global Search
    text_enterSearchByNameStringGlobalSearch_Xpath='//input[@class="dp-input-control update-input mt-2 ng-pristine ng-valid ng-touched" and @placeholder="Search By Name"]'
    check_searchByNameHeaderTextGlobalSearch_Xpath='//*[@class="search-text" and contains(text(),"Search by name")]'

    button_clickGlobalSearchTab_Xpath='//li[contains(@class,"tab-link") and contains(text(),"Global Search")]'
    button_clickNameSearchTab_Xpath='//li[contains(@class,"tab-link") and contains(text(),"Name Search")]'
    button_clickKeywordSearchTab_Xpath='//li[contains(@class,"tab-link") and contains(text(),"Keyword Search")]'
    
    #Name Search
    check_MemberFirstNameHeaderNameSearch_Xpath="//*[@class='search-text' and contains(text(),'Member's First Name')]"
    check_MemberLastNameHeaderNameSearch_Xpath="//*[@class='search-text' and contains(text(),'Member's Last Name')]"
    check_GuardianFirstNameSearch_Xpath="//*[@class='search-text' and contains(text(),'Guardian's First Name')]"
    check_GuardianLastNameSearch_Xpath="//*[@class='search-text' and contains(text(),'Guardian's Last Name')]"
    check_radioButtonExactSearchHeaderNameSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and contains(text(),"Exact Search")]'
    check_radioButtonStartsWithSearchHeaderNameSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and contains(text(),"Start With Search")]'
    check_radioButtonContainsSearchHeaderNameSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and contains(text(),"Contains Search")]'

    text_enterMembersFirstNameNamesSearch_Xpath='//input[@formcontrolname="firstName" and @placeholder="Member First Name"]'
    text_enterMembersLastNameNamesSearch_Xpath='//input[@formcontrolname="lastName" and @placeholder="Member Last Name"]'
    text_enterGuardiansFirstNameNamesSearch_Xpath='//input[@formcontrolname="guardianFirstName" and @placeholder="Guardian First Name"]'
    text_enterGuardiansLastNameNamesSearch_Xpath='//input[@formcontrolname="guardianLastName" and @placeholder="Guardian Last Name"]'

    select_radioButtonExactSearchNamesSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and @value="EX"]'
    select_radioButtonStartsWithNamesSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and @value="SW"]'
    select_radioButtonContainsNamesSearch_Xpath='//input[@type="radio" and @formcontrolname="selectedRadioButton" and @name="selectedRadioButton" and @value="CN"]'

    #KeyWord Search
    check_MemberFirstNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Member's first name')]"
    check_MemberMiddleNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Member's middle name')]"
    check_MemberLastNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Member's last name')]"
    check_GuardianFirstNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Guardian's first name')]"
    check_GuardianMiddleNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Guardian's middle name')]"
    check_GuardianLastNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Guardian's last name')]"
    check_RitwiksFirstNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Ritwik's first name')]"
    check_RitwiksMiddleNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Ritwik's middle name')]"
    check_RitwiksLastNameHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Ritwik's last name')]"
    check_PincodeHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Pincode')]"
    check_AddressHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Address')]"
    check_StateHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'State')]"
    check_DistrictHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'District')]"
    check_InitiationDateHeaderKeywordSearch_Xpath="//span[@class='search-text' and contains(text(),'Initiation Date')]"

    text_enterMemberFirstNameKeywordSearch_Xpath='//input[@formcontrolname="firstName"]'
    text_enterMemberMiddleNameKeywordSearch_Xpath='//input[@formcontrolname="middleName"]'
    text_enterMemberLastNameKeywordSearch_Xpath='//input[@formcontrolname="lastName"]'
    text_enterGuardianFirstNameKeywordSearch_Xpath='//input[@formcontrolname="guardianFirstName"]'
    text_enterGuardianMiddleNameKeywordSearch_Xpath='//input[@formcontrolname="guardianMiddleName"]'
    text_enterGuardianLastNameKeywordSearch_Xpath='//input[@formcontrolname="guardianLastName"]'
    text_enterRitwikFirstNameKeywordSearch_Xpath='//input[@formcontrolname="ritwikFirstName"]'
    text_enterRitwikMiddleNameKeywordSearch_Xpath='//input[@formcontrolname="ritwikMiddleName"]'
    text_enterRitwikLastNameKeywordSearch_Xpath='//input[@formcontrolname="ritwikLastName"]'
    text_enterPincodeKeywordSearch_Xpath='//input[@formcontrolname="pincode"]'
    text_enterAddressKeywordSearch_Xpath='//input[@formcontrolname="address"]'
    text_enterRitwikLastNameKeywordSearch_Xpath='//input[@formcontrolname="ritwikLastName"]'
    text_clickStateToSelectState_Xpath='//*[@name="state" and @formcontrolname="stateName"]'
    select_getAllStateOptions_Xpath='//*[@id="mat-options"]'
    text_clickDistrictToSelectDistrict_Xpath='//*[@name="state" and @formcontrolname="districtName"]'
    select_getAllDistrictOptions_Xpath='//*[contains(@id,"mat-options")]'
    text_enterInitiationDateKeywordSearch_Xpath='//input[@formcontrolname="initiationDate"]'

    fetchdata_getAllHeaderFields_Xpath='//th[contains(@class,"ng-star-inserted")]'
    fetchdata_getAllColumnFieldValuesExceptSerialNumber_Xpath='//td[contains(@class,"ng-star-inserted")]//*[contains(@class,"cell-text")]'
    fetchdata_getAllColumnFieldValuesOnlySerialNumber_Xpath='//td[contains(@class,"ng-star-inserted")]//*[contains(@class,"serial-no-text")]'

    #Assign FW:
    check_AssignFWTitleText_Xpath='//span[@class="fw-assign-text" and contains(text(),"Select a Field worker to assign")]'
    check_AssignFWHeaderText_Xpath='//span[@class="fw-text" and contains(text(),"Field worker")]'
    link_clickCancelButtonToCloseAssignFWWindow_Xpath='//span[@class="cancel-text text-center fw-assign-gap" and type="button" and contains(text(),"No, cancel")]'
    button_clickAssignButton_Xpath='//button[@class="dp-primary-btn fw-assign-btn fw-assign-gap" and contains(text(),"Assign")]'
    click_AssignFWDropdown_Xpath='//*[@class="mat-mdc-select-value ng-tns-c1771602899-58"]'
    getAll_AssignFWOptionsFromDropdown_Xpath='//*[contains(@id="mat-option")]'

    button_ClickDoneButtonOnSuccessfulAssignment_Xpath='//button[@class="save-button dp-primary-btn ng-star-inserted" and contains(text(),"Done")]'
    button_closeAssignFWButton_Xpath='//*[@class="close-button"]'


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