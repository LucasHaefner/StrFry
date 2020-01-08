import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name = 'StrFry',
  version = '0.0.1',
  license='MIT',
  description = 'The easiest way to create human-readable tables in Python!',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Lucas Haefner',
  author_email = 'lucashaefner360@gmail.com',
  url = 'https://github.com/LucasHaefner/StrFry',
  download_url = 'https://github.com/LucasHaefner/StrFry/archive/v_01.tar.gz',
  keywords = ['String', 'Str', 'Dunder', 'Special Method', 'Table', 'Tables', 'Data'],
  packages = setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)