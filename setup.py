from setuptools import setup
import pathlib
 
PATH = pathlib.Path(__file__).parent

 
README = (PATH / "README.md").read_text()


setup(
    name='pystack-sdk',
    version='0.1.0',
    author='Gerald Maduabuchi',
    author_email='Mgeraldoj07@gmail.com',
    description='A Python API wrapper designed to streamline Paystack integrations within Python projects.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/grayoj/pystack',
    project_urls={
        'Bug Tracker': 'https://github.com/grayoj/pystack/issues',
        'Source Code': 'https://github.com/grayoj/pystack',
    },
    package_dir={'': 'src'}, 
    python_requires='>=3.6',
    install_requires=[
        'http.client',
        'json',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='paystack payment integration api wrapper python',
)

