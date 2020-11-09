# Install software

    sudo apt-get install graphviz
    sudo apt-get install tcpdump
    sudo apt install pipenv

# Initialise the Python environment for the first time

## Pipenv

    # Install Python3 locally.
    pipenv install --three
    # Activate the pipenv shell.
    pipenv shell

## Install SCAPY

Install Python packages:

    pipenv install matplotlib PyX cryptography>=1.7 GraphViz
    pipenv install git+https://github.com/secdev/scapy#egg=scapy

Test that scapy works:

    ./scapy

> Missing packages are printed when run start `scapy`.

# Initialise the Python environment

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

 

 
 