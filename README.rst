``nose-pattern-exclude``
########################

A simple nose plugin that allows for excluding directories and files
from test discovery by path or glob pattern. Inspired by
`nose-exclude <https://pypi.python.org/pypi/nose-exclude>`_.


Installation
============


.. code-block:: bash

    $ pip install nose-pattern-exclude


Usage
=====

.. code-block:: bash

    $ nosetest \
        --exclude-path=./stuff \
        --exclude-path=/code/morestuff.py \
        --exclude-path=app/api/v?/*/tests.py
