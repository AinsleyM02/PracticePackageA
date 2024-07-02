#New file
#I created a repo, chose MIT license, inlcuded readme, selected python gitignore file
#cloned locally
#the root of repo will be proj directory
#module and dunder init in the package, the setup.py in the main repo
#test these work?:
#
#run a command from bash to install the package to python: pip install . or pip intall -e (in all python) or pip install --user -e (in ur user directory)
# ^when you are just in the directory PracticePackageA, it adds the .egg-info

from setuptools import setup

setup(
    name="PracticePackageA", #is the module name
    version="0.1",
    description= "A simple demo package",
    url="https://github.com/AinsleyM02/PracticePackageA",
    author= "Ainsley McLaughlin",
    author_email="annerositamc01@gmail.com",
    license="MIT",
    packages=['mypackage'] #is the subdir name
)