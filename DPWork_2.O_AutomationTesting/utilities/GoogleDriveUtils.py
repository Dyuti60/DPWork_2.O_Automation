import io
import os
import pickle
from exception import CustomException
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
#from datetime import datetime
import pandas as pd
import sys

#class DpWorkConnectWithGoogleDrive:

#   def __init__(self,driver):
#        self.driver=driver

def Create_Service(client_secret_file, api_name, api_version, *scopes):
    try:
        print(client_secret_file, api_name, api_version, scopes, sep='-')
        CLIENT_SECRET_FILE = client_secret_file
        API_SERVICE_NAME = api_name
        API_VERSION = api_version
        SCOPES = [scope for scope in scopes[0]]
        print(SCOPES)

        cred = None

        pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'


        if os.path.exists(pickle_file):
            with open(pickle_file, 'rb') as token:
                cred = pickle.load(token)

        if not cred or not cred.valid:
            if cred and cred.expired and cred.refresh_token:
                cred.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
                cred = flow.run_local_server()

            with open(pickle_file, 'wb') as token:
                pickle.dump(cred, token)

        try:
            service=build(API_SERVICE_NAME,API_VERSION,credentials=cred)
            print(API_SERVICE_NAME,'service created successfully')
            return service
        except Exception as e:
            print('Unable to connect.')
            print(e)
            return None
    except Exception as e:
        raise CustomException(e,sys)

def getFileIdAndFileNameFromGoogleDriveFolderInList(service, folderId):
    try:
        folder_id=folderId
        query=f"parents = '{folder_id}'"

        response=service.files().list(q=query).execute()
        files=response.get('files')
        nextPageToken=response.get('nextPageToken')

        while nextPageToken:
            response=service.files().list(q=query).execute()
            files.extend(response.get('files'))
            nextPageToken=response.get('nextPageToken')
            
        pd.set_option('display.max_columns',100)
        pd.set_option('display.max_rows',500)
        pd.set_option('display.min_rows',500)
        pd.set_option('display.max_colwidth',150)
        pd.set_option('display.width',200)
        pd.set_option('expand_frame_repr',True)
        df=pd.DataFrame(files)

        dataframe=df[['id','name']]
        #headers=dataframe.columns.values.tolist()
        FileDetailsIn2DList=dataframe.values.tolist()
        #FileDetailsIn2DList.insert(0,headers)
        
        file_ids=[]
        file_names=[]
        for file in FileDetailsIn2DList:
            file_ids.append(file[0])
            file_names.append(file[1])
        
        return file_ids, file_names
    except Exception as e:
        raise CustomException(e,sys)

def downloadFilesFromGoogleDriveFolder(service,filePath,file_ids,file_names):
    try:
        for file_id, file_name in zip(file_ids,file_names):
            request=service.files().get_media(fileId=file_id)
            
            fh=io.BytesIO()
            downloader=MediaIoBaseDownload(fd=fh, request=request)
            done= False
            
            while not done:
                status, done=downloader.next_chunk()
                print('Download Progress {0}'.format(status.progress()*100))
                
            fh.seek(0)
            
            #with open(os.path.join('./Random Files',file_name),'wb') as f:
            with open(filePath+file_name,'wb') as f:
                f.write(fh.read())
                f.close()
    except Exception as e:
        raise CustomException(e,sys)

def uploadFileFromLocalToGoogleDriveFolder(service,file_paths,fileNames,folderId):
    try:
        folder_id=folderId
        file_names=fileNames

        mime_types=['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']*len(file_names)

        for file_path,file_name, mime_type in zip(file_paths,file_names, mime_types):
            file_metadata={
                'name': file_name,
                'parents':[folder_id]
            }
            media=MediaFileUpload(file_path,mimetype=mime_type)
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
    except Exception as e:
        raise CustomException(e,sys)


