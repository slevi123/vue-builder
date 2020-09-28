import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sl-vue-builder",
    version="0.1.0",
    description="Unofficial Precompiler for Vue.js",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/slevi123/vue-builder",
    author="Simófi Levente",
    author_email="simofilevente@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["compiler"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vuebuilder = compiler.__main__:main",
        ]
    },
)