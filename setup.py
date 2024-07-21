'''from setuptools import setup, find_packages
from typing import List


def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name = "Xray",
    version="0.1",
    author="Abdul Qadir",
    author_email= "abdulkadir9929@gmail.com",
    install_requires = get_requirements(),
    packages = find_packages()
)'''

from setuptools import setup, find_packages

setup(
    name = "Xray_lungs",
    version="0.1",
    author="Abdul Qadir",
    author_email= "abdulkadir9929@gmail.com",
    packages = find_packages()
)
