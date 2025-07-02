from setuptools import setup

setup(
    name='mkdfile',
    version='0.1.0',
    py_modules=['cli'],
    packages=['generators'],
    install_requires=[
        'Click==8.1.7',
        'Jinja2==3.1.2'
    ],
    entry_points={
        'console_scripts': [
            'mkdfile=cli:cli'
        ]
    },
    description='Gerador de Dockerfile customizado',
    author='Alan Ramalho',
    license='MIT',
)
