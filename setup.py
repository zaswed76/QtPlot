from os.path import join, dirname

import qtplot
from setuptools import setup, find_packages

setup(
        name="qtplot",
        # в __init__ пакета
        version=qtplot.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),

        install_requires=["PyQt5", "pandas",
                          "matplotlib"],
        entry_points={
            'console_scripts':
                ['qtplot = qtplot.main:main']
        }

)

