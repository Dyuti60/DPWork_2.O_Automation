import os
from selenium import webdriver
import time
import sys
from exception import CustomException
import requests
import pandas as pd
from bs4 import BeautifulSoup
from utilities import XLUtils
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DpWorkMasterSearchPage:
    #Tab Locator
    button_clickGlobalSearchTab_Xpath="//*[contains(text(),'Global Search')]"
    button_clickNameSearchTab_Xpath="//*[contains(text(),'Name Search')]"
    button_clickKeywordSearchTab_Xpath="//*[contains(text(),'Keyword Search')]"
    button_clickAreYouUpdatedTab_Xpath="//*[contains(text(),'Are You Updated')]"
    #Global Search Tab fields Locator
    text_globalSearchByName_Xpath='//*[contains(@class,"search-input dp-input-control")]'
    text_globalSearchByNameTouched_Xpath='//*[contains(@class,"search-input dp-input-control")]'
    button_globalSearchByNameClear_Xpath='//*[@class="dp-secondary-btn"]'
    button_globalSearchByNameSearch_Xpath='//*[@class="bprimary dp-primary-btn"]'
    #Keyword Search Tab fields Locator
    text_memberFirstName_CSSSelector="input[formcontrolname='firstName']"
    text_memberMiddleName_CSSSelector="input[formcontrolname='middleName']"
    text_memberLastName_CSSSelector="input[formcontrolname='lastName']"
    text_ritwikFirstName_CSSSelector="input[formcontrolname='ritwiki_first_name']"
    text_ritwikMiddleName_CSSSelector="input[formcontrolname='ritwiki_middle_name']"
    text_ritwikLastName_CSSSelector="input[formcontrolname='ritwiki_last_name']"
    options_getAllRitwikName_Xpath='//*[contains(@id,"mat-option")]'
    text_guardianFirstName_CSSSelector="input[formcontrolname='guardian_first_name']"
    text_guardianMiddleName_CSSSelector="input[formcontrolname='guardian_middle_name']"
    text_guardianLastName_CSSSelector="input[formcontrolname='guardian_last_name']"
    text_initiationDate_Xpath='//input[contains(@id,"mat-input") and @placeholder="dd/mm/yyyy"]'
    text_address_CSSSelector="input[formcontrolname='address']"
    text_pinCode_CSSSelector="input[formcontrolname='pinCode']"
    click_stateDropDown_CSSSelector="*[formcontrolname='state_name']"
    click_getAllOptionsState_Xpath='//*[contains(@id,"mat-option")]'
    select_stateDropDownOption_Xpath='//*[contains(text(),{})]'
    click_districtDropDown_CSSSelector="*[formcontrolname='district_name']"
    click_getAllOptionsDistrict_Xpath='//*[contains(@id,"mat-option")]'
    select_districtDropDownOption_Xpath='//*[contains(text(),{})]'
    button_keywordSearchClear_Xpath='//*[@class="clearBtn dp-secondary-btn"]'
    button_keywordSearchSearch_Xpath='//*[@class="bprimary dp-primary-btn ng-star-inserted"]'
    #Are you updated Tab fields locator
    text_enterFCForAreYouUpdated_Xpath='//*[contains(@class,"searchInput dp-input-control")]'
    button_areYouUpdatedSearchClear_Xpath='//*[@class="dp-secondary-btn"]'
    button_areYouUpdatedSearchSearch_Xpath='//*[@class="bprimary dp-primary-btn"]'

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
        
    def clickGlobalSearchTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickGlobalSearchTab_Xpath))
            #self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickGlobalSearchTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        

    def enterNameAndDoGlobalSearch(self,Name,fieldValueIndex):
        try:
            if fieldValueIndex ==0:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_globalSearchByName_Xpath)))
                self.driver.find_element(By.XPATH, self.text_globalSearchByName_Xpath).clear()
                self.driver.find_element(By.XPATH, self.text_globalSearchByName_Xpath).send_keys(Name)
            else:
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_globalSearchByNameTouched_Xpath)))
                self.driver.find_element(By.XPATH, self.text_globalSearchByNameTouched_Xpath).clear()
                self.driver.find_element(By.XPATH, self.text_globalSearchByNameTouched_Xpath).send_keys(Name)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickGlobalSearchClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_globalSearchByNameClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickGlobalSearchSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_globalSearchByNameSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def extractGlobalSearchData(self,driver,GlobalSearchDataExtractFilePath):
        data=BeautifulSoup(driver.page_source,'html.parser')
        #print(data.prettify())
        
        #CreateSerialNumberList
        SNumbers=data.find_all(class_="serial-no-text")
        SerialNumbersList=[]
        for serialNumber in SNumbers:
            SerialNumbersList.append(serialNumber.get_text().strip())
        #CreateSerialNumberList
        AllData=data.find_all(class_="cell-text")
        AllDataList=[]
        for d in AllData:
            AllDataList.append(d.get_text().strip())
        globalSearchDataframe=pd.DataFrame([AllDataList[n:n+8] for n in range(0,len(AllDataList),8)],columns=['MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Pincode','Address'])
        globalSearchDataframe['SerialNumber']=SerialNumbersList
        #globalSearchDataframe=pd.DataFrame(AllDataList,columns=['SerialNumberList','MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Address'])
        globalSearchDataframe=globalSearchDataframe[['SerialNumber','MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Pincode','Address']]
        #globalSearchDataframe.to_csv(GlobalSearchDataExtractFilePath,header=True, index=False)
        return globalSearchDataframe


    def validateGlobalSearchExtract(self,dataframe,testDataGlobalSearchFilePath,testDataGlobalSearchSheet,fieldvalueIndex,GlobalSearchDataExtractFilePath):
        try:
            fieldvalues=XLUtils.convert_excelSheetIntoDataFrame(testDataGlobalSearchFilePath,testDataGlobalSearchSheet)
            fieldvalues=list(fieldvalues.columns.values)[1:]

            searchListInitial=XLUtils.getDataInList(testDataGlobalSearchFilePath,testDataGlobalSearchSheet,row=XLUtils.getRowCount(testDataGlobalSearchFilePath,testDataGlobalSearchSheet),col=2+int(fieldvalueIndex))
            searchListFinal=[]
            splittedList=[]
            for element in searchListInitial:
                splittedList=element.split()
                for element in splittedList:
                    searchListFinal.append(element)
            searchListFinal.extend(searchListInitial)
            globalsearchNameListLength=len(searchListFinal)
            dataframeRowLength=dataframe.shape[0]
            dataframeColumnLength=dataframe.shape[1]
            dataframeColumns=dataframe.columns.values

            add_list=[]
            for rowIndex in range(dataframeRowLength):#0
                completeRowDataSeries=dataframe.iloc[rowIndex,:]
                fill_list=[]
                for searchName in searchListFinal: #Dyuti
                    for column in dataframeColumns: #'SerialNumber'
                        if searchName.upper() in str(completeRowDataSeries[column]):
                            fill_list.append('True')
                if 'True' in fill_list:
                    add_list.append('True')
                else:
                    add_list.append('False')
            dataframe['Data_Validation_Status']=add_list
            
            GlobalSearchDataExtractFilePath=GlobalSearchDataExtractFilePath.replace('.csv','')+"_"+str(fieldvalues[fieldvalueIndex]+"_validation")+".csv"
            dataframe.to_csv(GlobalSearchDataExtractFilePath,header=True,index=False)
                
            if 'False' in add_list:
                return 'Data Validation Fails please check documentation folder, global search extract'
            else:
                return 'Data Validation Pass'
        except Exception as e:
            raise CustomException(e,sys)
            
    def clickKeyWordSearchTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickKeywordSearchTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterMemberFirstName(self, memberFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberFirstName_CSSSelector).send_keys(memberFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberMiddleName(self, memberMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberMiddleName_CSSSelector).send_keys(memberMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterMemberLastName(self, memberLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_memberLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_memberLastName_CSSSelector).send_keys(memberLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterGuardianFirstName(self, guardianFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianFirstName_CSSSelector).send_keys(guardianFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianMiddleName(self, GuardianMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianMiddleName_CSSSelector).send_keys(GuardianMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterGuardianLastName(self, guardianLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_guardianLastName_CSSSelector).send_keys(guardianLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterRitwikFirstName(self, ritwikFirstName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector).send_keys(ritwikFirstName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterRitwikMiddleName(self, ritwikMiddleName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikMiddleName_CSSSelector).send_keys(ritwikMiddleName)
        except Exception as e:
            raise CustomException(e,sys)

    def enterRitwikLastName(self, ritwikLastName):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_ritwikLastName_CSSSelector).send_keys(ritwikLastName)
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterRitwikOneByOne(self,RitwikName):
        for elementIndex in range(len(RitwikName)):
            self.driver.find_element(By.CSS_SELECTOR,self.text_ritwikFirstName_CSSSelector).send_keys(RitwikName[elementIndex])
            time.sleep(0.15)
        time.sleep(0.5)
    def enterRitwikName(self,ritwikFirstName, ritwikMiddleName, ritwikLastName):
        try:
            if len(ritwikMiddleName)==0:
                RitwikName=ritwikFirstName+" "+ritwikLastName
                SearchRitwikName=RitwikName
            else:
                RitwikName=ritwikFirstName+" "+ritwikMiddleName+" "+ritwikLastName
                SearchRitwikName=ritwikFirstName+" "+ritwikMiddleName
            time.sleep(0.5)
            flag=False
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_ritwikFirstName_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR,self.text_ritwikFirstName_CSSSelector).clear()
            if len(RitwikName)==0:
                RitwikName=''
            self.enterRitwikOneByOne(SearchRitwikName)
            #self.driver.find_element(By.XPATH,self.text_familyCode_Xpath).send_keys(FamilyCode)
            time.sleep(2)
            if len(RitwikName)!=0:
                RitwikName_locators=self.driver.find_elements(By.XPATH,self.options_getAllRitwikName_Xpath)
                elements_text_value=[]
                for element in RitwikName_locators:
                    elements_text=str(element.text).lower().strip().split()
                    print(elements_text)
                    elements_text_value.append(" ".join(elements_text[:]))
                print(elements_text_value)
                print(RitwikName_locators)
                print()

                element_dict=dict(zip(elements_text_value,RitwikName_locators))
                print(element_dict)
                
                for dict_key_text in element_dict.keys():
                    if str(dict_key_text).lower() == RitwikName.lower():
                        element_dict[dict_key_text].click()
                        flag=True
                        break
                    else:
                        flag=False
                if not flag:
                    assert False, "Not able to fetch Phil Member on entering FC Code"
                
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterInitiationDate(self, initiationDate):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_initiationDate_Xpath)))
            self.driver.find_element(By.XPATH, self.text_initiationDate_Xpath).clear()
            self.driver.find_element(By.XPATH, self.text_initiationDate_Xpath).send_keys(initiationDate)
        except Exception as e:
            raise CustomException(e,sys)

    def enterPinCode(self, pinCode):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_pinCode_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_pinCode_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_pinCode_CSSSelector).send_keys(pinCode)
        except Exception as e:
            raise CustomException(e,sys)

    def enterAddress(self, address):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.text_address_CSSSelector)))
            self.driver.find_element(By.CSS_SELECTOR, self.text_address_CSSSelector).clear()
            self.driver.find_element(By.CSS_SELECTOR, self.text_address_CSSSelector).send_keys(address)
        except Exception as e:
            raise CustomException(e,sys)
    
    def enterState(self, pincode,state):
        try:
            if len(pincode)==0:
                #WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_stateDropDown_CSSSelector)))
                #self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR,self.click_stateDropDown_CSSSelector))
                #self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.select_stateDropDownOption_Xpath.format(state)))

                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_stateDropDown_CSSSelector)))
                if len(state)!=0:
                    flag=False
                    self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR, self.click_stateDropDown_CSSSelector))
                    time.sleep(2)
                    state_elements=self.driver.find_elements(By.XPATH,self.click_getAllOptionsState_Xpath)
                    for state_element in state_elements:
                        if str(state_element.text).strip().lower()==state.lower():
                            self.click_unitil_interactable(state_element)
                            flag=True
                            break
                        else:
                            flag=False
                    if not flag:
                        self.click_unitil_interactable(state_element[0])


        except Exception as e:
            raise CustomException(e,sys)

    def enterDistrict(self, pincode,district):
        try:
            if len(pincode)==0:
                #WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_districtDropDown_CSSSelector)))
                #self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR,self.click_districtDropDown_CSSSelector))
                #self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.select_districtDropDownOption_CSSSelector.format(district)))
                time.sleep(1)
                WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.click_districtDropDown_CSSSelector)))
                if len(district)!=0:
                    flag=False
                    self.click_unitil_interactable(self.driver.find_element(By.CSS_SELECTOR, self.click_districtDropDown_CSSSelector))
                    time.sleep(2)
                    self.click_unitil_interactable(self.driver.find_element(By.XPATH, self.select_districtDropDownOption_Xpath.format(str(district).upper())))
                    time.sleep(2)

                    #district_elements=self.driver.find_elements(By.XPATH,self.click_getAllOptionsDistrict_Xpath)
                    #for district_element in district_elements:
                    #    print(str(district_element.text).strip().lower())
                    #    print()
                    #    print(str(district).lower())
                    #    if str(district_element.text).strip().lower()==str(district).lower():
                    #        self.click_unitil_interactable(district_element)
                    #        flag=True
                    #        break
                    #    else:
                    #        flag=False
                    #if not flag:
                    #    self.click_unitil_interactable(district_element[0])

        except Exception as e:
            raise CustomException(e,sys)
        
    def clickKeywordSearchClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_keywordSearchClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickKeywordSearchSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_keywordSearchSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def extractKeywordSearchData(self,driver,KeywordSearchDataExtractFilePath):
        data=BeautifulSoup(driver.page_source,'html.parser')
        #print(data.prettify())
        
        #CreateSerialNumberList
        SNumbers=data.find_all(class_="serial-no-text")
        SerialNumbersList=[]
        for serialNumber in SNumbers:
            SerialNumbersList.append(serialNumber.get_text().strip())
        #CreateSerialNumberList
        AllData=data.find_all(class_="cell-text")
        AllDataList=[]
        for d in AllData:
            AllDataList.append(d.get_text().strip())
        KeywordSearchDataframe=pd.DataFrame([AllDataList[n:n+8] for n in range(0,len(AllDataList),8)],columns=['MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Pincode','Address'])
        KeywordSearchDataframe['SerialNumber']=SerialNumbersList
        #globalSearchDataframe=pd.DataFrame(AllDataList,columns=['SerialNumberList','MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Address'])
        KeywordSearchDataframe=KeywordSearchDataframe[['SerialNumber','MemberStatus','District','MemberName','GuardianName','InitiationDate','Ritwik','Pincode','Address']]
        #KeywordSearchDataframe.to_csv(KeywordSearchDataExtractFilePath,header=True, index=False)
        return KeywordSearchDataframe

    def validateExtractKeywordSearchData(self,dataframe,keywordSearchDataExtractFilePath,testdatakeywordSearchExcelFilePath,fieldvalueIndex,memberName,testdatakeywordSearchExcelSheetName):
        try:
            fieldvalues=XLUtils.convert_excelSheetIntoDataFrame(testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName)
            fieldvalues=list(fieldvalues.columns.values)[1:]
            searchList=XLUtils.getDataInList(testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName,row=XLUtils.getRowCount(testdatakeywordSearchExcelFilePath,testdatakeywordSearchExcelSheetName),col=2+int(fieldvalueIndex))
            globalsearchNameListLength=len(searchList)
            dataframeRowLength=dataframe.shape[0]
            dataframeColumnLength=dataframe.shape[1]
            dataframeColumns=dataframe.columns.values

            add_list=[]
            for rowIndex in range(dataframeRowLength):#0
                completeRowDataSeries=dataframe.iloc[rowIndex,:]
                fill_list=[]
                for searchName in searchList: #Dyuti
                    for column in dataframeColumns: #'SerialNumber'
                        if searchName.upper() in str(completeRowDataSeries[column]):
                            fill_list.append('True')
                if 'True' in fill_list:
                    add_list.append('True')
                else:
                    add_list.append('False')
            dataframe['Data_Validation_Status']=add_list
            
            keywordSearchDataExtractFilePath=keywordSearchDataExtractFilePath.replace('.csv','')+"_"+str(memberName)+"_"+str(fieldvalues[fieldvalueIndex])+"_validation.csv"
            dataframe.to_csv(keywordSearchDataExtractFilePath,header=True,index=False)
            if 'False' in add_list:
                return 'Data Validation Fails please check documentation folder, keyword search extract'
            else:
                return 'Data Validation Pass'
        except Exception as e:
            raise CustomException(e,sys)

    def clickAreYouUpdatedTab(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_clickAreYouUpdatedTab_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def enterFamilycodeOneByOne(self,Familycode):
        length=12-len(Familycode)
        string='0'*length
        self.driver.find_element(By.XPATH,self.text_enterFCForAreYouUpdated_Xpath).send_keys(string)
        for elementIndex in str(Familycode):
            self.driver.find_element(By.XPATH,self.text_enterFCForAreYouUpdated_Xpath).send_keys(elementIndex)
            time.sleep(0.3)
        time.sleep(1.5)

    def enterFCForAreYouUpdated(self,familyCode):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, self.text_enterFCForAreYouUpdated_Xpath)))
            self.driver.find_element(By.XPATH, self.text_enterFCForAreYouUpdated_Xpath).clear()
            self.enterFamilycodeOneByOne(familyCode)
            #self.driver.find_element(By.XPATH, self.text_enterFCForAreYouUpdated_Xpath).send_keys(familyCode)
        except Exception as e:
            raise CustomException(e,sys)
        
    def clickAreYouUpdatedSearchButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_areYouUpdatedSearchSearch_Xpath))
        except Exception as e:
            raise CustomException(e,sys)

    def clickAreYouUpdatedClearButton(self):
        try:
            time.sleep(1)
            self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_areYouUpdatedSearchClear_Xpath))
        except Exception as e:
            raise CustomException(e,sys)
        
    def extractAreYouUpdatedData(self,driver,AreYouUpdatedDataExtractFilePath):
        data=BeautifulSoup(driver.page_source,'html.parser')
        #print(data.prettify())

        #CreateAllDataList
        AllData=data.find_all(class_="cell-text")
        AllDataList=[]
        for d in AllData:
            AllDataList.append(d.get_text().strip())
        AreYouUpdatedDataframe=pd.DataFrame([AllDataList[n:n+6] for n in range(0,len(AllDataList),6)],columns=['SerialNumber','MemberName','Status','State','District','LastIstravrityDate'])

        #AreYouUpdatedDataframe.to_csv(AreYouUpdatedDataExtractFilePath,header=True, index=False)
        return AreYouUpdatedDataframe
    
    def validateAreYouUpdatedSearchExtract(self,dataframe,testDataAreYouUpdatedFilePath,testDataAreYouUpdatedSheet,fieldvalueIndex,AreYouUpdatedDataExtractFilePath):
        try:
            fieldvalues=XLUtils.convert_excelSheetIntoDataFrame(testDataAreYouUpdatedFilePath,testDataAreYouUpdatedSheet)
            fieldvalues=list(fieldvalues.columns.values)[1:]
            searchListInitial=XLUtils.getDataInList(testDataAreYouUpdatedFilePath,testDataAreYouUpdatedSheet,row=XLUtils.getRowCount(testDataAreYouUpdatedFilePath,testDataAreYouUpdatedSheet),col=2+int(fieldvalueIndex))
            splittedList=[]
            for element in searchListInitial:
                if ' ' in element:
                    splittedList=element.split()
                searchListInitial.extend(splittedList)
            searchList=set(searchListInitial)
            searchList=list(searchList)
            globalsearchNameListLength=len(searchList)
            dataframeRowLength=dataframe.shape[0]
            dataframeColumnLength=dataframe.shape[1]
            dataframeColumns=dataframe.columns.values

            add_list=[]
            for rowIndex in range(dataframeRowLength):#0
                completeRowDataSeries=dataframe.iloc[rowIndex,:]
                fill_list=[]
                for searchName in searchList: #Dyuti
                    for column in dataframeColumns: #'SerialNumber'
                        if searchName.upper() in str(completeRowDataSeries[column]):
                            fill_list.append('True')
                if 'True' in fill_list:
                    add_list.append('True')
                else:
                    add_list.append('False')
            dataframe['Data_Validation_Status']=add_list
            
            AreYouUpdatedDataExtractFilePath=AreYouUpdatedDataExtractFilePath.replace('.csv','')+"_"+str(fieldvalues[fieldvalueIndex]+"_validation")+".csv"
            dataframe.to_csv(AreYouUpdatedDataExtractFilePath,header=True,index=False)
            if 'False' in add_list:
                return 'Data Validation Fails please check documentation folder, global search extract'
            else:
                return 'Data Validation Pass'
        except Exception as e:
            raise CustomException(e,sys)


    def getSerialNumberAndMemberForAllStatusTypes(self, dataframe):
        FWPendingDataFrame=dataframe[dataframe['MemberStatus']=='FW Pending']
        FWPendingDataFrame=FWPendingDataFrame[['SerialNumber','MemberName']]
        if len(FWPendingDataFrame) !=0:
            FWPendingDict=FWPendingDataFrame.iloc[1,:].to_dict()
        else:
            FWPendingDict='Null'

        DAApprovedDataframe=dataframe[dataframe['MemberStatus']=='DA Approved']
        DAApprovedDataframe=DAApprovedDataframe[['SerialNumber','MemberName']]
        if len(DAApprovedDataframe) !=0:
            DAApprovedDict=DAApprovedDataframe.iloc[1,:].to_dict()
        else:
            DAApprovedDict='Null'
        

        FWCompletedDataframe=dataframe[dataframe['MemberStatus']=='FW Completed']
        FWCompletedDataframe=FWCompletedDataframe[['SerialNumber','MemberName']]
        if len(FWCompletedDataframe) !=0:
            FWCompletedDict=FWCompletedDataframe.iloc[1,:].to_dict()
        else:
            FWCompletedDict='Null'
        

        DARejectedDataframe=dataframe[dataframe['MemberStatus']=='DA Rejected']
        DARejectedDataframe=DARejectedDataframe[['SerialNumber','MemberName']]
        if len(DARejectedDataframe) !=0:
            DARejectedDict=DARejectedDataframe.iloc[1,:].to_dict()
        else:
            DARejectedDict='Null'
        

        SURejectedDataframe=dataframe[dataframe['MemberStatus']=='SU Rejected']
        SURejectedDataframe=SURejectedDataframe[['SerialNumber','MemberName']]
        if len(SURejectedDataframe) !=0:
            SURejectedDict=SURejectedDataframe.iloc[1,:].to_dict()
        else:
            SURejectedDict='Null'

        SUApprovedDataframe=dataframe[dataframe['MemberStatus']=='SU Approved']
        SUApprovedDataframe=SUApprovedDataframe[['SerialNumber','MemberName']]
        if len(SUApprovedDataframe) !=0:
            SUApprovedDict=SUApprovedDataframe.iloc[1,:].to_dict()
        else:
            SUApprovedDict='Null'

        return FWPendingDict,DAApprovedDict,FWCompletedDict,DARejectedDict,SURejectedDict,SUApprovedDict