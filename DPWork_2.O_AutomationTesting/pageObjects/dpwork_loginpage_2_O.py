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


class DpWorkLoginPage:

    text_username_csslocator="input[formcontrolname='email']"
    text_password_csslocator="input[formcontrolname='password']"
    button_loginbutton_xpath='//*[@class="login-button dp-primary-btn"]'
    button_logoutbutton_xpath='//*[@class="sidebar-text ml-12" and contains(text(),"Log out")]'
    text_InvalidEmail_Xpath='//*[contains(text(),"No such user found. Please check your email.")]'
    text_InvalidCredentials_Xpath='//*[contains(text(),"Invalid credentials. Authentication failed")]'

    button_clickMasterSearch_Xpath="//*[contains(text(),'Master Search')]"
    button_update_Xpath="//*[contains(text(),'Update')]"
    #button_clickMasterSearch_Xpath='//*[@class="ml-12 sidebar-text"]'


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
        
    def waitForLoginPage(self):
        try:
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.text_username_csslocator)))
        except Exception as e:
            raise CustomException(e,sys)

    def setDpWorkUserName(self, username):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_username_csslocator)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_username_csslocator).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_username_csslocator).send_keys(username)
        except Exception as e:
            raise CustomException(e,sys)
    
    def setDpWorkPassword(self, password):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_password_csslocator)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_password_csslocator).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_password_csslocator).send_keys(password)
        except Exception as e:
            raise CustomException(e,sys)


    def clickLoginButton(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_loginbutton_xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def waitForLoginPageAfterLogout(self):
        try:
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.text_username_csslocator)))
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.text_password_csslocator)))
        except Exception as e:
            raise CustomException(e,sys)


    def logoutButtonDisplayed(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.button_logoutbutton_xpath)
            return len(elements)
        except Exception as e:
            raise CustomException(e,sys)

    def clickLogoutButton(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_logoutbutton_xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickMasterSearchFromMenu(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickMasterSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickUpdateFromMenu(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_update_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def checkAndReturnUserDetailsOnSuccessfulLogin(self, userRoleName,userRole):
        fetch_getTextUserDetails_Xpath='//span[@class="sidebar-text ml-12"]'
        elements=self.driver.find_elements(By.XPATH,fetch_getTextUserDetails_Xpath)
        Name=elements[0]
        #Name0, Status1, AccounSettings2, Logout3
        Status=elements[2]
        Appearance=elements[1]
        LogOut=elements[3]
        if str(userRole).lower()==str(Status.text).lower().strip() and str(userRoleName).lower()==str(Name.text).lower().strip():
            return True
        else:
            return False
        
    def errorMessageInvalidCredentials(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_InvalidCredentials_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

    def errorMessageInvalidEmail(self):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_InvalidEmail_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)