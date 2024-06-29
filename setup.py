from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as fileobj:
        requirements=fileobj.readlines()
        [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='arthi',
    author_email="arthis.aids2021@citchennai.net",
    install_requires=get_requirements('requirements.txt')

)