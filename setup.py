from typing import List
from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(filename:str) -> List[str]:
    ''' 
    Read requirements file and return list of requirements
    '''
    requirements = []
    with open(filename, 'r') as file:
        for line in file:
            requirements.append(line.strip())

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Amresh',
    author_email='amresh2000@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)