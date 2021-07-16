"""
setuptools描述
create by swm 2018/11/20
"""
from pathlib import Path

import setuptools

here = Path(__file__).parent
readme: Path = here / 'README.md'

with readme.open('r', encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    name="swmtools",  # 包的名字
    version="3.0.1",  # 版本控制
    description="util tools for daily dev",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Octoberr/swmpackages",
    author="october",
    author_email="sepjudy@gmail.com",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='daily work setup tools',
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'xlrd>=1.2.0',
        'pytz>=2021.1',
        'Pillow>=8.3.1',
    ],
    project_urls={
        'Source': 'https://github.com/Octoberr/swmpackages'
    }
)
