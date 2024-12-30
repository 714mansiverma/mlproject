# with this file i will be able to my whole ml project as a pckg. and where ever it is required we can actually use it as pckg.
from setuptools import find_packages,setup
from typing import List

Hypen_e_dot='-e .'

def get_requirements(file_path:str):
    '''
        this function will retur the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        requirements= [req. replace("\n","") for req in requirements] 
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
        
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Mansi',
    author_email='vermamansi714@gmail.com',
    packages=find_packages(),
   requires=get_requirements('requirements.txt')   
)