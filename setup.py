from setuptools import setup, find_packages

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    description="Database backups locally or to aws s3",
    long_description=readme,
    author="Ouss",
    author_email="ouss@mail.com",
    install_requires=[],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
