from setuptools import find_packages, setup
from typing import List

# editable-install marker in requirements (no leading space)
hypen = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''Reads the requirements from a file and returns them as a list of strings.'''
    with open(file_path) as file_obj:
        # strip whitespace/newlines, ignore blank lines and comments
        requirements = [req.strip() for req in file_obj.readlines() if req.strip() and not req.strip().startswith('#')]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sheethal',
    author_email='sheethalurs@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)