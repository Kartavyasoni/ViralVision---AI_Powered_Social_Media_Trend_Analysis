from setuptools import setup, find_packages

file_path = 'requirements.txt'
Hyphen_E_Dot = '-e .'

# Function to read requirements from requirements.txt
def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return the list of requirements
    mentioned in the requirements.txt file
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()


        # Remove '-e .' if present
        if Hyphen_E_Dot in requirements:
            requirements.remove(Hyphen_E_Dot)
             
    return requirements 

# Setup function for the package
setup(
    name='GlobalLens',  # Project name
    version='0.1.0',
    author='Kartavya Soni',
    author_email='sonikartavya2003@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='GlobalLens: A Clearer View of Global Progress and Stability',
    url='https://github.com/yourusername/GDERIS',  # Replace with GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
