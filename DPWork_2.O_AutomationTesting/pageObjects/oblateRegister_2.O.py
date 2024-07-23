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
    
    #Filter
    check_filterTitleText_Xpath='//span[@class="fc-content" and contains(text(),"Filter By Date Range")]'
    check_customDateTitle_Xpath='//span[@class="content" and contains(text(),"Custom date range")]'



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
        
    