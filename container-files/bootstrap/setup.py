from setuptools import setup,find_packages

setup(
    name='bootstrap',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'termcolor', 'GitPython', 'python-crontab'
    ],
    entry_points='''
        [console_scripts]
        bootstrap=app.cli:cli
    ''',
)
