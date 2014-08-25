from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name="nose-pattern-exclude",
    version='0.1.3',
    author="Jakub Roztocil",
    author_email="jakub@roztocil.name",
    description="Exclude specific files and directories from nosetests runs.",
    long_description=open('README.rst').read().strip(),
    license='BSD',
    url="http://github.com/jkbr/nose-pattern-exclude",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    py_modules=['nose_pattern_exclude'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'nose_pattern_exclude = nose_pattern_exclude:NosePatternExclude'
        ]
    },
    install_requires=['nose'],
)
