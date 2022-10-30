from setuptools import setup, find_packages


setup(
    name="FunYe",
    author="kaze-k",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "textual==0.1.18",
        "textual-inputs==0.2.6"
    ],
    extras_require={
        'dev': [
            "wheel>=0.37.1",
            "py-make>=0.1.1",
            "pyinstaller>=5.6.1"
        ]
    }
)
