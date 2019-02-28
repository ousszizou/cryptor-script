from setuptools import setup, find_packages

setup(
    name='cryptoR script',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click'
    ],
    python_requires='>=3',
    entry_points='''
        [console_scripts]
        cryptor=app:cli
    ''',
    author="algorithm",
    author_email="odjaidri@gmail.com",
    description="cryptoR script Project",
)
