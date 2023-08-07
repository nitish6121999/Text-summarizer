import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()


__version__ ='0.0.0'

REPO_NAME='Text-summarizer'
AUThOR_USER_NAME='nitish6121999'
SRC_REPO='textSummarizer'
AUTHOR_EMAIL='nitish6121999@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUThOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer NLP APP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com{AUThOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        'bug Tracker': f'https://github.com/{AUThOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
