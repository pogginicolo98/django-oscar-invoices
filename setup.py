from setuptools import find_packages, setup


setup(
    name='django-oscar-3.2.2-invoices',
    version='0.2.3',
    url='https://github.com/pogginicolo98/django-oscar-invoices.git',
    author='Nicolò Poggi',
    author_email='poggi.nicolo.bsnss@outlook.com',
    description='Invoices generation for Django Oscar 3.2.2',
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9.18',
    ],
    install_requires=[
        'phonenumbers',
        'pillow',
        'django>=4.2.6',
        'django-oscar>=3.2.2',
        'django-phonenumber-field>=6.4.0',
    ]
)
