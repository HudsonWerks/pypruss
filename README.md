PyPRUSS
=======
PyPRUSS is a Python binding for controlling the PRUs on the BeagleBone.

For examples and inspiration: [http://hipstercircuits.com/?cat=5](http://hipstercircuits.com/?cat=5)  
 
To install from a package on Angstrom: 
--------------------------------------
[http://wiki.thing-printer.com/index.php?title=PyPRUSS_on_BeagleBone](http://wiki.thing-printer.com/index.php?title=PyPRUSS_on_BeagleBone)
 
To install from source:
----------
    git clone https://bitbucket.org/intelligentagent/pypruss.git  
    cd pypruss
    python setup.py install
    export LD_LIBRARY_PATH=/usr/local/lib  
    
Update 06/21/15 (Debian) - With current Debian distros (Wheezy and Jessie) for the Beaglebone Black, the Device Tree fragment comes pre-loaded on the board's firmware. Therefore, the requirements for using PyPRUSS after compiling the library from source are the following:

1. apt-get install am335x-pru-package && ti-pru-cgt-installer
2. echo BB-BONE-PRU-01 >/sys/devices/bone_capemgr.9/slots

To try the blinkled example:  
----------------------------
    cd PyPRUSS/examples/blinkled  
    make  
    python blinkled.py  

You should then see three of the user leds blink rapidly 10 times. 
