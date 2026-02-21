from setuptools import setup, find_packages
from typing import List
HYPHON_E_D = '-e .'

def get_requirements(file_path: str) -> List[str]:

    '''This function will return the list of requirements'''

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]
        
        if HYPHON_E_D in requirements:
            requirements.remove(HYPHON_E_D)
    
    return requirements







setup(
    name='mlproject_basic',
    version='0.1',
    author="ibrarhussain",
    author_email="ibrar.ali69.ia@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"))
