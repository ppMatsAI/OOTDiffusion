from setuptools import setup, find_packages

# Function to read the list of dependencies from requirements.txt
def load_requirements(filename='requirements.txt'):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='ootdiffusion',
    version='0.1',
    packages=find_packages(),
    install_requires=load_requirements(),
)