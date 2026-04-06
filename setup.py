##find all packages in the ML application in the directory
from setuptools import find_packages, setup
from typing import  List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """"
    This function returns a List of requirements from requirments.txtx
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name ='2022 Final year project Update',
    version = '0.0.2',
    author = 'Noel Kuasmapa',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)