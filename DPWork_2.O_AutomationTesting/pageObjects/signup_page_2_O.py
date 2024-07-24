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

class SignupPage:
    check_registerNowText_Xpath='//*[@class="registration-ask-text" and contains(text(),"Not registered with DP Works?")]'
    check_beforePolicyText_Xpath='//*[@class="policy-text" and contains(text(),"By getting started, you agree to our")]'
    link_policy_partialLinkText='Privacy Policy'
    link_termsAndCondition_partialLinkText='Terms & Conditions'
    link_registerNow_PartiallinkText='Register now'
    text_FirstName_Xpath='//input[@formcontrolname="firstName"]'
    text_LastName_Xpath='//input[@formcontrolname="lastName"]'
    text_contactNumber_Xpath='//input[@formcontrolname="contactNumber"]'
    text_emailAddress_Xpath='//input[@formcontrolname="email"]'
    text_password_Xpath='//input[@formcontrolname="password"]'
    text_confirmPassword_Xpath='//input[@formcontrolname="reEnterPassword"]'
    text_address_Xpath='//input[@formcontrolname="address"]'
    text_pinCode_Xpath='//input[@formcontrolname="pinCode"]'
    text_getFirtNameErrorMessage='//*[contains(text(),"Enter first name")]'
    text_getLastNameErrorMessage='//*[contains(text(),"Enter last name")]'
    text_getContactNumberErrorMessage='//*[contains(text(),"Enter contact number")]'
    text_getEmailAddressErrorMessage='//*[contains(text(),"Enter valid email")]'
    text_getFirtNameErrorMessage='//*[contains(text(),"Enter first name")]'
    text_getPasswordErrorMessage='//*[contains(text(),"Password complexity is not matching")]'
    text_getAddressErrorMessage='//*[contains(text(),"Enter address")]'
    text_getPincodeErrorMessage='//*[contains(text(),"Enter pincode")]'
    click_RegisterButton_Xpath='//button[@class="signIn-button dp-primary-btn" and @type="submit"]'


    text_phoneOTP_Xpath='//input[@formcontrolname="phoneOtp"]'
    text_emailOTP_Xpath='//input[@formcontrolname="emailOtp"]'
    text_resendTimer_Xpath='//*[contains(text(),"Resend in")]'
    text_resend_Xpath='//*[@class="resend-text"]'
    click_resendLink_Xpath='//*[contains(@class,"resend-text")]'
    wait_AsCodeAlreadySentText_Xpath='//*[contains(text(),"A verification code has been sent already.")]'
    click_verfiyCodesButton_Xpath='//*[@type="submit" and @class="signIn-button dp-primary-btn"]'

    click_loginButtonSuccess_Xpath='//button[@class="save-button dp-primary-btn"]'

    text_messageOnSuccessRegsitration='//*[contains(text(),"Your account was created successfully!") and contains(text(),"You can login to DP using the new credentitals")]'

    click_loginNowButtonAtBottom_Xpath='//button[@class="save-button dp-primary-btn" and contains(text(),"Login now")]'
    click_closeSuccessSignUpWindow_Xpath='//*[@role="img" and contains(text(),"close")]'

    text_enterFamilyCode_Xpath='//input[@formcontrolname="fc"]'
    click_loginAfterEnteringFamilyCode_Xpath='//*[@class="login-button dp-primary-btn"]'
    #click_loginAfterEnteringFamilyCode_Xpath='//*[@class="ng-star-inserted" and contains(text(),"Login")]'
    text_getIncorrectErrorMessageForFamilyCodeField_Xpath='//*[contains(text(),"Could not find Family Code details. Please check the code again.")]'
    click_getAllFamilyMemberName_Xpath='//*[@role="option" and contains(@id,"mat-option")]'

    text_enterAuthenticatedCodeForFamilyCodePhilMemberMobileNumber_Xpath='//*[@formcontrolname="authenticationCode"]'
    click_loginButtonAfterFamilyCodeAuthentication_Xpath='//*[@class="login-button dp-primary-btn" and contains(text(),"login")]'
    check_resendTimerAfterFamilyCodeAuthentication_Xpath='//*[contains(text(),"Resend in")]'
    check_resendTextAfterFamilyCodeAuthentication_Xpath='//*[@class="resend ng-star-inserted" and contains(text(),"Resend")]'
    click_resendLinkAfterFamilyCode_Xpath='//*[@class="resend ng-star-inserted"]'
    check_authenticationCodeSendMessageAfterFamilyCodeAuthentication_Xpath='//*[@class="login-content-text" and contains(text(),"We’ve sent an authentication code to your phone ending with")]'

    waitForDAApprovalText_Xpath='//*[contains(text(),"You are not allowed")]'
    #Name0, Status1, AccounSettings2, Logout3
    fetch_getTextUserDetails_Xpath='//span[@class="sidebar-text ml-12"]'

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
        
    def clickRegisterNowButton(self):
        try:
            time.sleep(0.5)
            if len(self.driver.find_elements(By.XPATH,self.check_registerNowText_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_beforePolicyText_Xpath))>0 and len(self.driver.find_elements(By.PARTIAL_LINK_TEXT,self.link_policy_partialLinkText))>0 and len(self.driver.find_elements(By.PARTIAL_LINK_TEXT,self.link_termsAndCondition_partialLinkText))>0:
                self.click_unitil_interactable(self.driver.find_element(By.PARTIAL_LINK_TEXT,self.link_registerNow_PartiallinkText))
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def enterFirstName(self,memberFirstName):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_FirstName_Xpath)))
            self.driver.find_element(By.XPATH,self.text_FirstName_Xpath).clear()
            if len(memberFirstName)==0:
                memberFirstName=''
            self.driver.find_element(By.XPATH,self.text_FirstName_Xpath).send_keys(memberFirstName)
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterLastName(self,memberLastName):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_LastName_Xpath)))
            self.driver.find_element(By.XPATH,self.text_LastName_Xpath).clear()
            if len(memberLastName)==0:
                memberLastName=''
            self.driver.find_element(By.XPATH,self.text_LastName_Xpath).send_keys(memberLastName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterContactNumber(self,contactNumber):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_contactNumber_Xpath)))
            self.driver.find_element(By.XPATH,self.text_contactNumber_Xpath).clear()
            if len(contactNumber)==0:
                contactNumber=''
            self.driver.find_element(By.XPATH,self.text_contactNumber_Xpath).send_keys(contactNumber)
        except Exception as e:
            raise CustomException(e,sys)  

    def enterEmailAddress(self,emailAddress):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_emailAddress_Xpath)))
            self.driver.find_element(By.XPATH,self.text_emailAddress_Xpath).clear()
            if len(emailAddress)==0:
                emailAddress=''
            self.driver.find_element(By.XPATH,self.text_emailAddress_Xpath).send_keys(emailAddress)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterPassword(self,password):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_password_Xpath)))
            self.driver.find_element(By.XPATH,self.text_password_Xpath).clear()
            if len(password)==0:
                password=''
            self.driver.find_element(By.XPATH,self.text_password_Xpath).send_keys(password)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterConfirmPassword(self,confirmPassword):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_confirmPassword_Xpath)))
            self.driver.find_element(By.XPATH,self.text_confirmPassword_Xpath).clear()
            if len(confirmPassword)==0:
                confirmPassword=''
            self.driver.find_element(By.XPATH,self.text_confirmPassword_Xpath).send_keys(confirmPassword)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterAddress(self,address):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_address_Xpath)))
            self.driver.find_element(By.XPATH,self.text_address_Xpath).clear()
            if len(address)==0:
                address=''
            self.driver.find_element(By.XPATH,self.text_address_Xpath).send_keys(address)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterPincode(self,pincode):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_pinCode_Xpath)))
            self.driver.find_element(By.XPATH,self.text_pinCode_Xpath).clear()
            if len(pincode)==0:
                pincode=''
            self.driver.find_element(By.XPATH,self.text_pinCode_Xpath).send_keys(pincode)
        except Exception as e:
            raise CustomException(e,sys)

    def checkSignUpErrorMessage(self, firstName, lastName, contactNumber, emailAddress, password, confirmPassword, address, pincode ):
        su=[]
        if len(firstName)==0:
            error_fn=self.driver.find_elements(By.XPATH,self.text_getFirtNameErrorMessage)
            if error_fn >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")
        
        if len(lastName)==0:
            error_ln=self.driver.find_elements(By.XPATH,self.text_getLastNameErrorMessage)
            if error_ln >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(contactNumber)==0:
            error_pn=self.driver.find_elements(By.XPATH,self.text_getContactNumberErrorMessage)
            if error_pn >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(emailAddress)==0:
            error_ea=self.driver.find_elements(By.XPATH,self.text_getEmailAddressErrorMessage)
            if error_ea >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(address)==0:
            error_ea=self.driver.find_elements(By.XPATH,self.text_getAddressErrorMessage)
            if error_ea >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(emailAddress)==0:
            error_ea=self.driver.find_elements(By.XPATH,self.text_emailAddress_Xpath)
            if error_ea >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(pincode)==0:
            error_pc=self.driver.find_elements(By.XPATH,self.text_getPincodeErrorMessage)
            if error_pc >0:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")

        if len(password)==0:
            error_p=self.driver.find_elements(By.XPATH,self.text_getPasswordErrorMessage)
            if error_p >0 or password != confirmPassword:
                su.append("ErrorHandled")
            else:
                su.append("ErrorNotHandled")
        if "ErrorNotHandled" in su:
            return False
        else:
            return True
        
    def clickRegisterButtonAfterFillingRegisterPage(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_RegisterButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def waitFor3MinutesAsOtpAlreadySent(self):
        try:
            if len(self.driver.find_elements(By.XPATH,self.wait_AsCodeAlreadySentText_Xpath))>0:
                time.sleep(181)
                self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_RegisterButton_Xpath))
            else:
                pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterPhoneOTP(self,phoneOTP):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_phoneOTP_Xpath)))
            self.driver.find_element(By.XPATH,self.text_phoneOTP_Xpath).clear()
            if len(phoneOTP)==0:
                phoneOTP=''
            self.driver.find_element(By.XPATH,self.text_phoneOTP_Xpath).send_keys(phoneOTP)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterEmailOTP(self,emailOTP):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_emailOTP_Xpath)))
            self.driver.find_element(By.XPATH,self.text_emailOTP_Xpath).clear()
            if len(emailOTP)==0:
                emailOTP=''
            self.driver.find_element(By.XPATH,self.text_emailOTP_Xpath).send_keys(emailOTP)
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkPresenceofResetTimer(self):
        try:
            if(len(self.driver.find_elements(By.XPATH,self.text_resendTimer_Xpath))>0):
               return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkPresenceOfResendButton(self):
        try:
            if(len(self.driver.find_elements(By.XPATH,self.click_resendLink_Xpath))>1):
               return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickResenButtonToVerifyEmailPhone(self):
        try:
            time.sleep(3)
            elements=self.driver.find_elements(By.XPATH,self.click_resendLink_Xpath)
            self.click_unitil_interactable(elements[0])
            self.click_unitil_interactable(elements[1])
        except Exception as e:
            raise CustomException(e,sys)

    def clickVerifyOnEnteringMobileAndEmailOTP(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_verfiyCodesButton_Xpath))
        except Exception as e:
            raise CustomException(e,sys)


    def clickLoginNowButtonOnGettingSignUpSuccessMessage(self):
        try:
            time.sleep(2)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_loginNowButtonAtBottom_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        

    def clickCrossButtonOnGettingSignUpSuccessMessage(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_closeSuccessSignUpWindow_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkSuccessMessageOnSuccessfulSignUp(self):
        try:
            if len(self.driver.find_elements(By.XPATH,self.text_messageOnSuccessRegsitration))>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickLoginNowOnEnteringPasswordAndUsername(self):
        try:
            time.sleep(0.5)
            button_loginbutton_xpath='//*[@class="login-button dp-primary-btn"]'
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,button_loginbutton_xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickLoginNowButtonAtTheBottomOfRegistrationPage(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_loginNowButtonAtBottom_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def waitForApprovalFromDA(self):
        try:
            input("Write 'Yes' and press enter to confirm that DA has approved the user role: ")
            self.clickLoginNowOnEnteringPasswordAndUsername()
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterFamilycodeOneByOne(self,Familycode):
        for elementIndex in range(len(Familycode)):
            self.driver.find_element(By.XPATH,self.text_enterFamilyCode_Xpath).send_keys(Familycode[elementIndex])
            time.sleep(0.5)
        time.sleep(1)

    def getCorrectFamilyCode(self,FamilyCode):
        try:
            count=True
            while count:
                self.enterFamilycodeOneByOne(Familycode=FamilyCode)
                count=self.driver.find_elements(By.XPATH,self.text_getIncorrectErrorMessageForFamilyCodeField_Xpath)
        except Exception as e:
            raise CustomException(e,sys)

    def enterFamilyCode(self,FamilyCode,PhilMemberName):
        try:
            time.sleep(1)
            flag=False
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterFamilyCode_Xpath)))
            self.driver.find_element(By.XPATH,self.text_enterFamilyCode_Xpath).clear()
            if len(FamilyCode)==0:
                FamilyCode=''
            self.getCorrectFamilyCode(FamilyCode)
            #self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
            time.sleep(1)
            if len(FamilyCode)!=0:
                apicallIncorrect=self.driver.find_elements(By.XPATH,self.text_getIncorrectErrorMessageForFamilyCodeField_Xpath)
                PhilMemberName_locators=self.driver.find_elements(By.XPATH,self.click_getAllFamilyMemberName_Xpath)
                elements_text_value=[]
                for element in PhilMemberName_locators:
                    elements_text=str(element.text).lower().strip().split()
                    elements_text_value.append(" ".join(elements_text))

                element_dict=dict(zip(elements_text_value,PhilMemberName_locators))
                for dict_key_text in element_dict.keys():
                    if str(dict_key_text).lower() == str(PhilMemberName).lower():
                        element_dict[dict_key_text].click()
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    assert False, "Not able to fetch Phil Member on entering FC Code"
                
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterAuthenticatedCodeForFamilyCode(self,mobileAuthenticatedCode):
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterAuthenticatedCodeForFamilyCodePhilMemberMobileNumber_Xpath)))
            self.driver.find_element(By.XPATH,self.text_enterAuthenticatedCodeForFamilyCodePhilMemberMobileNumber_Xpath).clear()
            if len(mobileAuthenticatedCode)==0:
                mobileAuthenticatedCode=''
            self.driver.find_element(By.XPATH,self.text_enterAuthenticatedCodeForFamilyCodePhilMemberMobileNumber_Xpath).send_keys(mobileAuthenticatedCode)
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkResendTimerForFamilyCodeAuthentication(self):
        try:
            if len(self.driver.find_elements(By.XPATH,self.check_resendTimerAfterFamilyCodeAuthentication_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_authenticationCodeSendMessageAfterFamilyCodeAuthentication_Xpath))>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkResendLinkForFamilyCodeAuthentication(self):
        try:
            if len(self.driver.find_elements(By.XPATH,self.check_resendTextAfterFamilyCodeAuthentication_Xpath))>0 and len(self.driver.find_elements(By.XPATH,self.check_authenticationCodeSendMessageAfterFamilyCodeAuthentication_Xpath))>0:
                return True
            else:
                return False
        except Exception as e:
            raise CustomException(e,sys)

    def clickResendLinkToVerifyFC(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_resendLinkAfterFamilyCode_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
    def clickLoginButtonOnEnteringFC(self):
        try:
            time.sleep(0.5)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.click_loginAfterEnteringFamilyCode_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def checkAndReturnUserDetailsOnSuccessfulLogin(self):
        elements=self.driver.find_elements(By.XPATH,self.fetch_getTextUserDetails_Xpath)
        Name=elements[0]
        #Name0, Status1, AccounSettings2, Logout3
        Status=elements[1]
        AccounSettings=elements[2]
        LogOut=elements[3]
        return str(Name.text).lower().strip(), str(Status.text).lower().strip()
    
    #familyCodePhilNameVerification_MobileNumberOTPAuthentication
    #IsPrimaryAccountSetVerifictaion_EmailOTPAuthentication

    #def setPrimaryAccount(self,primaryAccountMail):
