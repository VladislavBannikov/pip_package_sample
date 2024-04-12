from setuptools import setup, find_packages

setup(
    name="test_package117",
    version="0.1",
    packages= find_packages(),

    author="VB",
    author_email="VB@VB.com",
    description="This is an Example Package",
    keywords="hello world example examples",
    url="http://example.com/HelloWorld/",
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ],

    entry_points={
        'console_scripts': ['test_package117_call=test_package117.script:main'],
    }
)