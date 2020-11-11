# Description

This directory contains scripts that have been written as part of an introduction to SCAPY.

Please note that some scripts need to be executed by `root`.

# Install software

    sudo apt-get install graphviz
    sudo apt-get install tcpdump
    sudo apt install pipenv

If you need to install `pipenv` **locally**:

    pip install wheel
    pip install setuptools
    pip install --user pipenv

> You may need to set the path to `pipenv`. You may have to use `pip3` (instead of `pip`). 

# Initialise the Python environment for the first time

## Pipenv

    # Install Python3 locally.
    pipenv install --three
    # Activate the pipenv shell.
    pipenv shell

## Install SCAPY

Install Python packages:

    pipenv install matplotlib PyX "cryptography>=1.7" GraphViz
    pipenv install git+https://github.com/secdev/scapy#egg=scapy

Test that scapy works:

    ./scapy

> Missing packages are printed when run start `scapy`.

## Configure PyCharm

Find the path to the Python interpreter used by Pipenv:

    $  which python
    /home/denis/.local/share/virtualenvs/scapy-0YGVbhtG/bin/python

Under PyCharm: `File => Settings => Project => Python Interpreter` and set the
Python interpreter used with Pipenv.

> Find the path to the Scapy package: `python -c "import scapy; print(scapy.__file__)"`.

# Initialise the Python environment

Assuming that the file `Pipfile` already exists, you just need to execute:

    pipenv install

# Note about using the method sniff() and conversations()

You need to be `root`.

    xhost +
    sudo su

> In a multiuser environment you should make sure that nobody else use the X server: `ss -ltn`.
> If you are alone on your machine, that you can skip this verification.

# Run the script

    python introduction.py

> To generate network traffic, you can run `./generate-trafic.sh`.

# Notes for using SCAPY within scripts

The direction `from scapy.all import *` should allow IDEs to load all SCAPY symbols.
However, this does not work.

Why ?

Because modules are imported **dynamically** (at runtime), not statically. For example,
let's consider the file `scapy/layers/all.py`. You can see this code:

    for _l in conf.load_layers:
        log_loading.debug("Loading layer %s", _l)
        try:
            load_layer(_l, globals_dict=globals(), symb_list=__all__)
        except Exception as e:
            log.warning("can't import layer %s: %s", _l, e)

You can see that the modules are _loaded/imported_ at runtime.

* When the statement `from scapy.all import *` is encountered by a Python interpreted, the modules are imported
(because the interpreter interprets the Python script).
* But when the same statement is encountered by an IDE, the module are not loaded, because the IDE does not
interpret the Python script. 

Thus, if you want to use Scapy with an IDE, you need to find out the modules for each symbol you want to insert into your script.

For example: You need to execute the function `arping`, and you want your IDE to know about it.

One way to quickly find out the answer is to use the interactive interpreter:

    $ git clone https://github.com/secdev/scapy.git
    $ cd scapy
    $ ./run_scapy  
    >>> print(arping.__module__)
    scapy.layers.l2
    >>> 
 
Here you have the answer: you need to import `scapy.layers.l2`.
Thus: `from scapy.layers.l2 import arping`.

