from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='kaba',
    version='0.1.0',
    author='Aria Karimi',
    author_email='aria.karimi@metu.edu.tr',
    description='Kaba: A parody programming language',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aria-karimi/Kaba',
    packages=find_packages(exclude=["tests*", "samples*", "plugins*", "docs*"]),
    include_package_data=True,
    install_requires=[
        'antlr4-python3-runtime>=4.9',
    ],
    entry_points={
        'console_scripts': [
            'kaba=kaba.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)