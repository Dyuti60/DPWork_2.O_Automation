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
    
    #old Locators
    text_username_ID="mat-input-0"
    text_password_ID="mat-input-1"
    text_afterlogoutUsername_ID="mat-input-2"
    text_afterlogoutPassword_ID="mat-input-3"
    button_loginButton_Xpath='//*[@class="mat-focus-indicator signIn mat-raised-button mat-button-base mat-primary"]'
    text_errorMessagetype1_Xpath='//*[contains(text(),"No such user found. Please check your email.")]'
    text_errorMessagetype2_Xpath='//*[contains(text(),"Invalid password. Authentication failed.")]'
    test_userRole_Xpath='//*[contains(text(),"{}")]'
    button_menu_Xpath='//*[@class="mat-focus-indicator mat-icon-button mat-button-base ng-star-inserted"]'
    button_logout_Xpath='//*[@class="mat-list-item-content"]'
    button_closeErrorMessage_Xpath='//*[@class="mat-focus-indicator mat-button mat-button-base"]'
    text_accessDeniedMessage_Xpath='//*[contains(text(),"You are not allowed to access.Please contact admin to approve your request.")]'
    text_accessBlockedMessage_Xpath='//*[contains(text(),"You are not allowed to access. Your account is blocked by super admin.")]'
    text_NewNotifcation_Xpath='//*[contains(text(),"Kindly Click on Bell Icon (top right corner) or go to Notification History Page to view notifications")]'
    button_closeNotification_Xpath='//*[@class="mat-ripple mat-button-ripple mat-button-ripple-round"]'
    button_logout_LINKTEXT="Logout"
    '''
    text_username_csslocator="input[formcontrolname='email']"
    text_password_csslocator="input[formcontrolname='password']"
    button_loginbutton_xpath='//*[@class="login-button dp-primary-btn"]'
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
        
    def waitForLoginPage(self):
        try:
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID, self.text_username_ID)))
        except Exception as e:
            raise CustomException(e,sys)

    def setDpWorkUserName(self, username):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.ID, self.text_username_ID)))
            self.driver.find_element(By.ID, self.text_username_ID).clear()
            self.driver.find_element(By.ID, self.text_username_ID).send_keys(username)
        except Exception as e:
            raise CustomException(e,sys)
    
    def setDpWorkPassword(self, password):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.ID, self.text_password_ID)))
            self.driver.find_element(By.ID, self.text_password_ID).clear()
            self.driver.find_element(By.ID, self.text_password_ID).send_keys(password)
        except Exception as e:
            raise CustomException(e,sys)

    def onLoginHandleNotification(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.text_NewNotifcation_Xpath)
            if(elements>0):
                element=self.driver.find_elements(By.XPATH,self.button_closeNotification_Xpath)
                print(element)
                self.click_unitil_interactable(element[-1])
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)

    def clickLoginButton(self):
        try:
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_loginButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def waitForLoginPageAfterLogout(self):
        try:
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID, self.text_afterlogoutUsername_ID)))
            WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID, self.text_afterlogoutPassword_ID)))
        except Exception as e:
            raise CustomException(e,sys)


    def errorMessageType1(self):
        try:
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH, self.text_errorMessagetype1_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

    def errorMessageType2(self):
        try:
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH, self.text_errorMessagetype2_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

    def errorMessageDisplayed(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.text_errorMessage_Xpath)
            return len(elements)
        except Exception as e:
            raise CustomException(e,sys)

    def accessDeniedMessage(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH, self.text_accessDeniedMessage_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

    def accessDeniedDisplayed(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.text_accessDeniedMessage_Xpath)
            return len(elements)
        except Exception as e:
            raise CustomException(e,sys)

    def accessBlockedMessage(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH, self.text_accessBlockedMessage_Xpath)))
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

    def accessBlockedDisplayed(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.text_accessBlockedMessage_Xpath)
            return len(elements)
        except Exception as e:
            raise CustomException(e,sys)

    def logoutButtonDisplayed(self):
        try:
            elements=self.driver.find_elements(By.XPATH,self.button_logout_Xpath)
            return len(elements)
        except Exception as e:
            raise CustomException(e,sys)

    def closeErrorMessage(self):
        try:
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_closeErrorMessage_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickMenu(self):
        try:
            time.sleep(1)
            WebDriverWait(self.driver,50).until(EC.visibility_of_element_located((By.XPATH, self.button_menu_Xpath)))
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_menu_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def waitForUserRole(self,userRole):
        try:
            print(self.test_userRole_Xpath.format(str(userRole)))
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.test_userRole_Xpath.format(userRole))))
        except Exception as e:
            raise CustomException(e,sys)

    def waitforLogoutButton(self):
        try:
            WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.LINK_TEXT, self.button_logout_LINKTEXT)))   
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_logout_Xpath))) 
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickLogoutButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.LINK_TEXT,self.button_logout_LINKTEXT))
            #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_logout_Xpath)))
            #logging_out=self.driver.find_elements(By.XPATH,self.button_logout_Xpath)
            #self.click_unitil_interactable(logging_out[-1])
            time.sleep(1)
        except Exception as e:
            raise CustomException(e,sys)

'''
    def createDedicatedSSFolder(self,foldername):
        try:
            os.chdir(".//screenshots")
            SS=foldername
            try:
                mkdir="mkdir {0}".format(SS)
                os.system(mkdir)
            except:
                pass
            location=os.getcwd()+'\\'+str(SS)+'\\'
            return location
        except Exception as e:
            raise CustomException(e,sys)
    
    def takeAndSaveScreenshotUnique(self,location,username,serialNumber):
        try:
            final_location=location+'\\SS-{} - {}.png'.format(serialNumber,username)
            self.driver.save_screenshot(final_location)
            return final_location
        except Exception as e:
            raise CustomException(e,sys)

    def takeAndSaveScreenshotCommon(self,location,username,serialNumber):
        try:
            final_location=location+'\\SS-{}-LoginTest_DpWorker_UserName - {}.png'.format(serialNumber,username)
            self.driver.save_screenshot(final_location)
        except Exception as e:
            raise CustomException(e,sys)

    def collectScreenshot(self,screenshotFolder,username):
        try:
            location=os.getcwd()+"//{}".format(screenshotFolder)
            desired_screenshots=[]
            for ss in os.listdir(location):
                if ss.__contains__(username):
                    desired_screenshots.append(location+"//{}".format(ss))
            return desired_screenshots
        except Exception as e:
            raise CustomException(e, sys)

    def deleteScreenshots(self,screenshotFolder,username):
        try:
            location=os.getcwd()+"//{}".format(screenshotFolder)
            desired_screenshots=[]
            for ss in os.listdir(location):
                if ss.__contains__(username):
                    os.remove(location+"//{}".format(ss))
        except Exception as e:
            raise CustomException(e,sys)
'''