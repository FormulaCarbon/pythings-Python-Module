import setuptools

with open("Documents\\Python_projects\\pythings\\App\\README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pythings",
    version="0.4.8",
    author="FormulaCarbon",
    author_email="siddhuk.learning@gmail.com",
    description="Extends Functionality of Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FormulaCarbon/pythings-Python-Module",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers"
    ],
    install_requires=[
        'setuptools',
        'plyer',
        'bs4',
        'pillow',
        'cryptography'
    ],
    package_dir={"": "Documents\\Python_projects\\pythings\\App"},
    packages=setuptools.find_packages(where="Documents\\Python_projects\\pythings\\App"),
    python_requires=">=3.6",
)
