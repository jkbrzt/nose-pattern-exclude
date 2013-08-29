from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name="nose-pattern-exclude",
    version='0.1.0',
    author="Jakub Roztocil",
    author_email="jakub@roztocil.name",
    description="Exclude specific files and directories from nosetests runs.",
    license='BSD',
    url="http://github.com/jkbr/nose-pattern-exclude",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
    ],
    py_modules=['nose_pattern_exclude'],
    zip_safe=False,
    entry_points={
        'nose.plugins': [
            'nose_exclude = nose_pattern_exclude:NosePatternExclude'
        ]
    },
    install_requires=['nose'],
)