from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f if line.strip()]

setup(
    name="channel_partner_system",
    version="0.0.1",
    description="Channel Partner System",
    author="ERPTronix",
    author_email="info@erptronix.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)