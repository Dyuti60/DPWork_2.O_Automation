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

class oblateRegister:
    button_clickOblateRegisterFromNavigationPanel_Xpath='//span[@class="ml-12 sidebar-text" and contains(text(),"Oblate Register")]'
    check_oblateRegisterTitleText_Xpath='//span[@class="headingText ng-star-inserted" and contains(text(),"Oblate Register")]'
    text_enterSearchByAnyColumn_Xpath='//input[@class="search-input dp-input-control ng-pristine ng-valid ng-touched" and @type="text" and @placeholder="Search by any column"]'
    button_clickFilterButton_Xpath='//button[@class="filter-button dp-primary-btn"]'
    button_clickShowCountButton_Xpath='//button[@class="addButton dp-secondary-btn ng-star-inserted"]'
    button_clickAddToOblateButton_Xpath='//button[@class="addButton dp-primary-btn"]'
    
    #Filter
    check_filterTitleText_Xpath='//span[@class="fc-content" and contains(text(),"Filter By Date Range")]'
    check_customDateTitle_Xpath='//span[@class="content" and contains(text(),"Custom date range")]'
    check_FromDatefilterHeaderText_Xpath='span[@class="input-text" and contains(text(),"From Date")]'
    check_ToDatefilterHeaderText_Xpath='span[@class="input-text" and contains(text(),"To Date")]'
    check_subTitleTextMyOblate_Xpath='span[@class="dp-chip ng-star-inserted selected"] and contains(text(),"My Oblates")]'
    
    text_enterFromDateInFilterWindow_Xpath='input[@class="mat-datepicker-input mat-mdc-input-element datePickerInput ng-tns-c3736059725-18 mat-mdc-form-field-input-control mdc-text-field__input ng-pristine ng-valid cdk-text-field-autofill-monitored ng-touched" and @placeholder="dd/mm/yyyy"]'
    text_enterToDateInFilterWindow_Xpath='input[@class="mat-datepicker-input mat-mdc-input-element datePickerInput ng-tns-c3736059725-19 mat-mdc-form-field-input-control mdc-text-field__input ng-untouched ng-pristine ng-valid cdk-text-field-autofill-monitored" and @placeholder="dd/mm/yyyy"]'
    button_clickApplyFiltersButton_Xpath='button[@class="dp-primary-btn inp-div" and contains(text(),"Apply Filters")]'
    button_clickButtonToCloseSearchFilter_Xpath='button[@class="img-div" and @type="button"]'

    fetch_getAllOblateRegisterHeaderText_Xpath='//th[@class="ng-star-inserted"]'
    fetch_getAllOblateRegisterFieldValues_Xpath='//td[@class="ng-star-inserted"]'

    #Add Oblate:
    text_enterOblateMemberFirstName_Xpath='//input[@formcontrolname="firstName"]'
    text_enterOblateMemberMiddleName_Xpath='//input[@formcontrolname="middleName"]'
    text_enterOblateMemberLastName_Xpath='//input[@formcontrolname="lastName"]'
    options_getAllMemberLastName_Xpath='//*[contains(@id="mat-option")]'
    text_enterOblateMemberRitwikName_Xpath='//input[@formcontrolname="ritwikName"]'
    options_getAllOblateMemberRitwikName_Xpath='//*[contains(@id="mat-option")]'
    text_enterOblateMemberContactNumber_Xpath='//input[@formcontrolname="contactNo"]'
    text_enterOblateMemberGuardianFirstName_Xpath='//input[@formcontrolname="guardianFname"]'
    text_enterOblateMemberGuardianMiddleName_Xpath='//input[@formcontrolname="guardianMname"]'
    text_enterOblateMemberGuardianLastName_Xpath='//input[@formcontrolname="guardianLname"]'
    options_getAllOblateMemberGuardianLastName_Xpath='//*[contains(@id="mat-option")]'
    text_enterOblateMemberQualification_Xpath='//input[@formcontrolname="qualification"]'
    text_enterOblateMemberOccupation_Xpath='//input[@formcontrolname="occupation"]'
    text_enterOblateMemberAge_Xpath='//input[@formcontrolname="age"]'
    text_enterOblateMemberRace_Xpath='//input[@formcontrolname="race"]'
    text_enterOblateMemberVarna_Xpath='//input[@formcontrolname="varna"]'
    text_enterNumberOfInitiatedMembers_Xpath='//input[formcontrolname="initiatedMember"]'
    text_enterOblateMemberPresentAddress_Xpath='//input[formcontrolname="presAddress"]'
    text_enterOblateMemberPresentPincode_Xpath='//input[formcontrolname="presPincode"]'
    text_enterOblateMemberPermanentAddress_Xpath='//input[formcontrolname="permAddress"]'
    text_enterOblateMemberPermanentPincode_Xpath='//input[formcontrolname="permPincode"]'
    button_clickCheckboxPermanentSameAsPresentAddress_Xpath='//input[formcontrolname="checkBox"]'
    text_enterOblateMemberInitiationDate_Xpath='//input[formcontrolname="initiationDate"]'
    text_enterOblateMemberInitiationPlace_Xpath='//input[formcontrolname="initiationPlace"]'

    click_NextButtonInOblateRegister_Xpath='//*[@class="dp-primary-btn btn-name ng-star-inserted" and contains(text(),"Next")]'

    check_ErrorMessageOblateMemberFirstName_Xpath='//span[@class="error-text ng-star-inserted" and contains(text(),"Enter First Name")]'
    check_ErrorMessageOblateMemberLastName_Xpath='//span[@class="error-text ng-star-inserted" and contains(text(),"Select Last Name from Dropdown")]'
    check_ErrorMessageOblateMemberRitwikName_Xpath='//span[@class="error-text ng-star-inserted" and contains(text(),"Select Ritwik from Dropdown")]'
    check_ErrorMessageOblateContact_Xpath='//span[@class="error-text ng-star-inserted" and contains(text(),"Please enter valid phone number")]'
    check_ErrorMessageOblateGuardianFirstName_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter guardian's first name')]"
    check_ErrorMessageOblateGuardianLastName_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Select last name from dropdown')]"
    check_ErrorMessageOblateQualification_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter qualification')]"
    check_ErrorMessageOblateOccupation_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter occupation')]"
    check_ErrorMessageOblateAge_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter age')]"
    check_ErrorMessageOblateRace_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter race')]"
    check_ErrorMessageOblateVarna_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter varna')]"
    check_ErrorMessageOblateNumberOfInitiatedMember_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Please enter initiatedMember')]"
    check_ErrorMessageOblatePresentAddress_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter address')]"
    check_ErrorMessageOblatePresentPincode_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter Pincode')]"
    check_ErrorMessageOblatePermanentAddress_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter address')]"
    check_ErrorMessageOblatePermanentPincode_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter Pincode')]"
    #wrong Error Message
    check_ErrorMessageOblateInitiationDate_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter date of birth')]"
    check_ErrorMessageOblateInitiationPlace_Xpath="//span[@class='error-text ng-star-inserted' and contains(text(),'Enter initiation place')]"

    check_firstMemberNameOblateHeaderText_Xpath='//span[@class="input-text" and contains(text(),"First Name *")]'
    check_middleMemberNameOblateHeaderText_Xpath='//span[@class="input-text" and contains(text(),"Middle Name")]'
    check_lastMemberNameOblateHeaderText_Xpath='//span[@class="input-text" and contains(text(),"Last Name *")]'
    check_RitwikNameOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Ritwik's Name')]"
    check_contactNumberOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Contact *')]"
    check_guardianFirstNameOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Guardian's First Name*')]"
    check_guardianMiddleNameOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Guardian's Middle Name')]"
    check_guardianLastNameOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Guardian's Last Name *')]"
    check_qualificationOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Qualification *')]"
    check_occupationOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Occupation *')]"
    check_ageHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Age *')]"
    check_raceOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Race *')]"
    check_varnaOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Varna *')]"
    check_noOfInitiatedMemberOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'No of Initiated Member*')]"
    check_presentAddressOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Address *')]"
    check_permanentAddressOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Address *')]"
    check_presentPincodeOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Pincode *')]"
    check_permanentPincodeOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Pincode *')]"
    check_permanentDistrictOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'District')]"
    check_presentDistrictOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'District')]"
    check_permanentStateOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'State')]"
    check_presentStateOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'State')]"
    check_initiationDateOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Initiation Date *')]"
    check_initiationPlaceOblateHeaderText_Xpath="//span[@class='input-text' and contains(text(),'Initiation Place *')]"
    check_PersonalDetailsHeaderText_Xpath='//p[@class="sub-text" and contains(text(),"Personal Details")]'
    check_PresentAddressHeaderText_Xpath='//p[@class="sub-text" and contains(text(),"Present Address")]'
    check_PermanentAddressHeaderText_Xpath='//p[@class="sub-text" and contains(text(),"Permanent Address")]'
    check_DateDetailsHeaderText_Xpath='//p[@class="sub-text" and contains(text(),"Date Details")]'


    check_headingDikshayatriDetails_Xpath='//*[@class="headingText" and contains(text(),"Dikshyarthi Details")]'
    check_headingDikshayatriDetails_Xpath='//*[@class="headingText" and contains(text(),"Dikshyarthi Details")]'
    check_subHeadingDPFrontPage_Xpath='//*[@class="input-text" and contains(text(),"Diksha Patra Front Page *")]'
    check_subHeadingDPBackPage_Xpath='//*[@class="input-text" and contains(text(),"Diksha Patra Front Page *")]'
    check_uploadPhotoText_Xpath='//*[@class="sub-text" and contains(text(),"Upload photos")]'

    button_clickPreviousButton_Xpath='//button[@class="dp-secondary-btn btn-name ng-star-inserted" and contains(text(),"Previous")]'
    button_clickSubmitButton_Xpath='//button[@class="dp-primary-btn btn-name ng-star-inserted" and contains(text(),"Submit")]'
    button_crossClickToCloseOblateWindow='//*[@class="img-div" and type="button"]'

    insert_frontPageOfDP_Xpath='//input[@id="front-img" and @type="file"]'
    insert_backPageOfDP_Xpath='//input[@id="back-img" and @type="file"]'

    fetch_serialNumbergenerationText_Xpath='//h1[@class="title" and contains(text(),"Kindly note the serial number")]'
    fetch_serialNumberInlineText_Xpath='//h1[@class="subtitle" and contains(text(),"Please write the serial number on diksha patra page.")]'
    button_clickFinishButton_Xpath='//button[@class="save-button dp-primary-btn ng-star-inserted" and contains(text(),"Finish")]'
    button_clickCloseButton_Xpath='//*[@class="close-button" and type="button"]'
    

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
        
    