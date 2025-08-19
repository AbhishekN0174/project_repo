from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project/__init__.py
from project import __version__ as version

setup(
    name="project",
    version=version,
    description="Custom Project App for ERPNext / Frappe",
    author="Midocean Technologies Pvt Ltd",
    author_email="sagar@midocean.tech",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)

