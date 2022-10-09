from setuptools import find_packages, setup
setup(
    name="eeg_fConn",
    packages = find_packages(include=["eeg_fConn"]),
    version = '1.0.0',
    description = "To compute the functional connectivity from EEG in various bands",
    author = "Muhammad Salman Kabir",
    license = "MIT",
    install_requires = ['numpy','scipy'],
    test_requires = ['pytest'],
    setup_requires = ['pytest-runner'],
    test_suite = 'tests',


)