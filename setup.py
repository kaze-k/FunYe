from setuptools import setup, find_packages

setup(
    author="kaze-k",
    name="FunYe",
    packages=find_packages(),
    version="0.1.0",
    install_requires=[
        "pyinstaller>=5.5",
        "textual>=0.1.18",
        "textual-inputs>=0.2.6"
    ]
)
