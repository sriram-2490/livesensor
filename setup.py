from setuptools import setup, find_packages
def get_requirements()->list[str]:
    requirements_list : list[str]=[]
    return requirements_list
setup(
    name='sensor',
    version='0.0.1',
    author='prince',
    author_email='sriramchaowdary@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements() #['pymongo']
)