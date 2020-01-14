import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name = 'StrFry',
  version = '1.0.0',
  license='MIT',
  description = 'The easiest way to create human-readable tables in Python!',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Lucas Haefner',
  author_email = 'lucashaefner360@gmail.com',
  url = 'https://github.com/LucasHaefner/StrFry',
  download_url = 'https://github.com/LucasHaefner/StrFry/archive/v1.0.0.tar.gz',
  keywords = ['String', 'Str', 'Dunder', 'Special Method', 'Table', 'Tables', 'Data', 'List', 'Iterable'],
  packages = setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.0',
)