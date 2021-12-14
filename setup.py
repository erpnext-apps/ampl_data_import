from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ampl_data_import/__init__.py
from ampl_data_import import __version__ as version

setup(
	name="ampl_data_import",
	version=version,
	description="DMS IMporter",
	author="Frappe Technologies",
	author_email="hello@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
