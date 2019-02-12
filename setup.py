import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy-langdetect",
    version="0.1.1",
    author="Abhijit Balaji",
    author_email="balaabhijit5@gmail.com",
    description="Fully customizable language detection pipeline for spaCy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Abhijit-2592/spacy-langdetect",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pytest', 'langdetect==1.0.7']
)
