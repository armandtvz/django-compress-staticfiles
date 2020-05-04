import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

description = (
    'A static files storage backend for compression using GZip and/or Brotli '
    'that inherits from Django''s ManifestFilesMixin and StaticFilesStorage; '
    'also minifies static files.'
)

setuptools.setup(
    name='django-compress-staticfiles',
    version='1.0.0-beta',
    author='Armandt van Zyl',
    author_email='armandtvz@gmail.com',
    description=description,
    license='GPL-3.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/armandtvz/django-compress-staticfiles',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.5',
    install_requires=[
        'Django >=2.2',
        'Brotli',
        'csscompressor',
        'rjsmin',
    ],
)
