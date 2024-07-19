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

class forgotPassword:

    link_forgotPassword_Xpath='//*[@class="forgot-password-text" and contains(text(),"Forgot password?")]'
    button_loginNow_Xpath='//*[@class="login-now-text" and contains(text(),"Back to Login")]'

    enter_email_Xpath='//input[@formcontrolname="email"]'
    button_resetPassword_Xpath='//*[@class="reset-password-button dp-primary-btn" and contains(text(),"Reset password")]'
    #check
    check_resetPasswordText_Xpath='//*[@class="reset-password-title-text ng-star-inserted" and contains(text(),"Reset Password")]'
    check_registeredEmailAddressText_Xpath='//span[@class="input-level-text" and contains(text(),"Registered email address*")]'

    enter_emailOTP_Xpath='//input[@formcontrolname="emailOTP"]'
    button_verifyIdentity_Xpath='//*[@class="verify-button dp-primary-btn" and contains(text(),"Verify identity")]'
    #check
    check_emailOTPText_Xpath='//*[@class="input-level-text" and contains(text(),"Email OTP *"]'
    check_resendTimerText_Xpath='//*[@class="resend-countdown-text ng-star-inserted" and contains(text(),"Resend in")]'

    enter_newPassword_Xpath='//input[@formcontrolname="password"]'
    enter_confirmPassword_Xpath='//input[@formcontrolname="reEnterPassword"]'
    button_clickActivateAccount_Xpath='//*[@class="verify-button dp-primary-btn" and contains(text(),"Activate account")]'
    #check
    check_createPasswordText_Xpath='//*[@class="reset-password-title-text ng-star-inserted" and contains(text(),"Create password")]'
    check_createPasswordTitleText_Xpath='//*[@class="input-level-text" and contains(text(),"Create password*"]'
    check_reEnterPasswordTitleText_Xpath='//*[@class="input-level-text" and contains(text(),"Re-enter password*"]'
    check_errorMessageForPasswordComplexityMismatch_Xpath='//*[@class="error-message ng-star-inserted" and "Password complexity not matching"]'

    #check
    check_titleTextOnSuccessPasswordChange_Xpath='//*[@class="title" and contains(text(),"Your password has been successfully reset!")]'
    check_subtitleTextOnSuccessPasswordChange_Xpath='//*[@class="subtitle" and contains(text(),"You can login to DP using the new credentitals")]'

    button_clickLoginNow_Xpath='//*[@class="save-button dp-primary-btn ng-star-inserted" and contains(text(),"Login now")]'
    click_crossButton_Xpath='//*[@class="cross-icon-container"]'
    check_errorOTPResendMessage_Xpath='//*[@class="A verification code has been sent already. Please check your email or mobile and try again after 3 minutes"]'
    checkurl='http://65.2.189.74/login'

    check_emailBlankInlineErrorMessage_Xpath='//span[@class="validation-message ng-star-inserted" and contains(text(),"Email is required")]'
    check_emailOTPBlankInlineErrorMessage_Xpath='//span[@class="validation-message ng-star-inserted" and contains(text(),"OTP is required")]'
    click_resendButton_Xpath='//*[@class="resend-text ng-star-inserted" and contains(text(),"Resend")]'

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
        

    def clickOnForgotPassword(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.link_forgotPassword_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickLoginNowButtonAtBottom(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_loginNow_Xpath))
        except Exception as e:
            raise CustomException(e,sys)    
        
    def enterEmailAddressForPasswordReset(self, emailAddressForPasswordReset):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.enter_email_Xpath)))
            self.driver.find_element(By.XPATH,self.enter_email_Xpath).clear()
            if len(emailAddressForPasswordReset)==0:
                emailAddressForPasswordReset=''
            self.driver.find_element(By.XPATH,self.enter_email_Xpath).send_keys(emailAddressForPasswordReset)
        except Exception as e:
            raise CustomException(e,sys)
    def clickOnResetPasswordButton(self):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_resetPasswordText_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_registeredEmailAddressText_Xpath))>0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_resetPassword_Xpath))
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterEmailOTPForPasswordReset(self, emailOTPForPasswordReset):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.enter_emailOTP_Xpath)))
            self.driver.find_element(By.XPATH,self.enter_emailOTP_Xpath).clear()
            if len(emailOTPForPasswordReset)==0:
                emailOTPForPasswordReset=''
            self.driver.find_element(By.XPATH,self.enter_emailOTP_Xpath).send_keys(emailOTPForPasswordReset)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickVerifyIdentityButtonOnAddingEmailOTP(self):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_emailOTPText_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_resendTimerText_Xpath))>0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_verifyIdentity_Xpath))
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterNewPassword(self, newPassword):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.enter_newPassword_Xpath)))
            self.driver.find_element(By.XPATH,self.enter_newPassword_Xpath).clear()
            if len(newPassword)==0:
                newPassword=''
            self.driver.find_element(By.XPATH,self.enter_newPassword_Xpath).send_keys(newPassword)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterConfirmPassword(self, confirmPassword):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.enter_confirmPassword_Xpath)))
            self.driver.find_element(By.XPATH,self.enter_confirmPassword_Xpath).clear()
            if len(confirmPassword)==0:
                confirmPassword=''
            self.driver.find_element(By.XPATH,self.enter_confirmPassword_Xpath).send_keys(confirmPassword)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickActivateAccountButton(self,newPassword,confirmPassword):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_createPasswordText_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_createPasswordTitleText_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_reEnterPasswordTitleText_Xpath))>0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickActivateAccount_Xpath))
                return "ActivateButtonTrue"
            elif newPassword !=confirmPassword:
                if len(self.driver.find_elements(By.XPATH,self.check_errorMessageForPasswordComplexityMismatch_Xpath))>0:
                    return "ActivateButtonFalse"
            else:
                return "False"
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickLoginNowButtonAfterGettingSuccessPasswordChangeMessage(self,driver):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_titleTextOnSuccessPasswordChange_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_subtitleTextOnSuccessPasswordChange_Xpath))>0:
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickLoginNow_Xpath))
                login_url=self.checkurl
                if driver.current_url==login_url:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def clickCrossButtonToRedirectToLoginPage(self,driver):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_crossButton_Xpath))
            login_url=self.checkurl
            if driver.current_url==login_url:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
    
    def checkEmailAddressBlankErrorMessage(self):
        #span class="validation-message ng-star-inserted" and 'Email is required'
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_titleTextOnSuccessPasswordChange_Xpath))>0:
                    return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
    
    def checkEmailOTPNotRegisteredErrorMessage(self):
        #check_emailOTPBlankInlineErrorMessage_Xpath='//span[@class="validation-message ng-star-inserted" and contains(text(),"OTP is required")]'
        #span class="validation-message ng-star-inserted" and 'OTP is required'
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_emailOTPBlankInlineErrorMessage_Xpath))>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)

    def checkBlankCreatePasswordErrorMessage(self):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_errorMessageForPasswordComplexityMismatch_Xpath))>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
    def clickResendOTPButton(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_resendButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
    