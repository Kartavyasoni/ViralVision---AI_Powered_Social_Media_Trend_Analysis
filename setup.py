from setuptools import setup, find_packages

file_path = 'requirements.txt'
Hyphen_E_Dot = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return the list of requirements
    mentioned in the requirements.txt file
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)
             
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Kartavya Soni',
    author_email='sonikartavya2003@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') ,
    description='A brief description of your package',
    url='http://your.package.url',
) 