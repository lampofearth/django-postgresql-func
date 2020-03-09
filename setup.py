import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-postgresql-func",
    version="0.0.1",
    author="lampofearth",
    author_email="lampofearth@gmail.com",
    description="PostgreSQL Functions and Operators for Django. Full support "
                "for classic Django SQL functions",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://https://github.com/lampofearth/django-postgresql-func",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Framework :: Django',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    project_urls={
        'Documentation': 'https://py-orm.com/chapter/django-postgresql-func/',
        'Source': 'https://https://github.com/lampofearth/'
                  'django-postgresql-func/',
        'Tracker': 'https://github.com/lampofearth/'
                   'django-postgresql-func/issues/',
    },
    python_requires=">=3.6",
    install_requires=[
       'django>=2.0.0',
    ]
)
