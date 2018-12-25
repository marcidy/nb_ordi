from setuptools import setup, find_packages

setup(
    name='ordi',
    version='0.1',
    description='ordiboot software architecture',
    packages=find_packages(),
    url='http://github.com/marcidy/nb_ordi',
    author='Matthew Arcidy',
    author_email='marcidy@gmail.com',
    license='MIT',
    install_requires=[
        'kivy'],
    include_package_data=True,
    zip_safe=False)
