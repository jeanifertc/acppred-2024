from setuptools import setup, find_packages

setup(
    name="acppred",
    version="0.0.1", 
    packages=find_packages(),
    author="Jeanifer Teixeira Camacho",
    author_email="jeanifertm@gmail.com",
    description="anticancer peptide prediction tool",
    entry_points = {
        'console_scripts': [
            'acppred-preprocess = acppred.preprocess.main',
            'acprred-train = acppred.train:main',
            'acppred-predict = acppred.predict:main'
        ]
    }
)