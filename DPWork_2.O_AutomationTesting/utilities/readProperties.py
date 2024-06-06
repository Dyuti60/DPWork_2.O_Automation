import configparser
from exception import CustomException
import sys
import os
from configurations.constants import projectName,config_ini
config=configparser.RawConfigParser()
config_ini_pathpath=os.getcwd()+'\\'+projectName+config_ini
config.read(config_ini_pathpath)


class readConfig():
    @staticmethod
    def getDpWorkUrl():
        try:
            dpWorkUrl = config.get('common info','dp_work_url')
            return dpWorkUrl
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getFieldWorkerUsername():
        try:
            FieldWorkerUsername=config.get('common info','field_worker_username')
            return FieldWorkerUsername
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getFieldWorkerPassword():
        try:
            FieldWorkerPassword=config.get('common info','field_worker_password')
            return FieldWorkerPassword
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getDistrictAdminUsername():
        try:
            DistrictAdminUsername=config.get('common info','district_admin_username')
            return DistrictAdminUsername
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getDistrictAdminPassword():
        try:
            DistrictAdminPassword=config.get('common info','district_admin_password')
            return DistrictAdminPassword
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getSuperUserRoleUsername():
        try:
            SuperUserRoleUsername=config.get('common info','super_user_role_username')
            return SuperUserRoleUsername
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getSuperUserRolePassword():
        try:
            SuperUserRolePassword=config.get('common info','super_user_role_password')
            return SuperUserRolePassword
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getEmailSender():
        try:
            emailSender=config.get('common info','emailSender')
            return emailSender
        except Exception as e:
            raise CustomException(e,sys)

    @staticmethod
    def getEmailTOReceivers():
        try:
            emailReceivers=config.get('common info','emailTOReceivers')
            return emailReceivers
        except Exception as e:
            raise CustomException(e,sys)


    @staticmethod
    def getEmailCCReceivers():
        try:
            emailReceivers=config.get('common info','emailCCReceivers')
            return emailReceivers
        except Exception as e:
            raise CustomException(e,sys)


    @staticmethod
    def getemailsenderpassword():
        try:
            SenderEmailPassword=config.get('common info','senderEmailPassword')
            return SenderEmailPassword
        except Exception as e:
            raise CustomException(e,sys)