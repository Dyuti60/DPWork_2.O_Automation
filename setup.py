from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirment libraries
    '''
    requirements=[]
    with open(file_path, 'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace('/n','') for r in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
name='DP Work 2.O Automation Testing',
author='Dyuti',
author_email='duttadyuti4@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),
include_package_data=True,
license='MIT',
description='DP Work Regression Testing Framework',
long_description=open('README.md').read()
)
