import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name='DPWork_2.O_AutomationTesting'

list_of_files=[
    '.gitignore',
    'readme.md',
    'requirements.txt',
    'main.py',
    'Dockerfile.py',
    'requirements.txt',
    'setup.py',
    f'documentation/sample_evidence.docx',
    f'logs/sample.log',
    f'reports/sample.html',
    f'screenshots/screenshot.png',
    f'{project_name}/__init__.py',
    f'{project_name}/configurations/config.ini',
    f'{project_name}/pageObjects/__init__.py',
    f'{project_name}/testcases/__init__.py',
    f'{project_name}/testcases/conftest.py',
    f'{project_name}/utilities/__init__.py',
    f'{project_name}/utilities/docsutil.py',
    f'{project_name}/utilities/emailUtil.py',
    f'{project_name}/utilities/readProperties.py',
    f'{project_name}/utilities/XLUtils.py',
    f'{project_name}/utilities/GoogleDriveUtils.py',
    f'{project_name}/exception.py',
    f'{project_name}/logger.py',
]

for file in list_of_files:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)
    print(filepath)

    #creates only directory if exists or not
    if filedir !='':
        print(filedir)
        print(filename)
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Directory {filedir} for file - {filename} created')

    #checks if filepath doesn't exists or if filepath size is zero then, create empty file else does nothing
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as file_obj:
            pass
            logging.info(f'creating empty file :{filepath}')
    else:
        logging.info(f'File {filename} already exists')