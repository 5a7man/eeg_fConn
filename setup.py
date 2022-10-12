from setuptools import find_packages, setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
print(long_description)
setup(
    name="eeg_fConn",
    packages = find_packages(include=["eeg_fConn"]),
    version = '1.1.0',
    description = "To compute the functional connectivity from EEG in various bands",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = "Muhammad Salman Kabir",
    author_email="kabir.msalman@gmail.com",
    url = "https://github.com/5a7man/eeg_fConn/",
    license = "GNU",
    install_requires = ['numpy','scipy'],
    test_requires = ['pytest'],
    setup_requires = ['pytest-runner'],
    test_suite = 'tests',
    platforms= ["Windows, Linux, Mac OS"] 


)