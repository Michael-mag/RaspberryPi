### How to use this code

- Download clone the repository to your desired location.
- Note that at the moment the static folder is missing, I suspect that this might
    be because there are no contents in that folder yet on my local machine
- Change the IP adress in the main function, you can obtain the IP address by
    typing "ifconfig" on the pi terminal without the quatation marks. Look for
    the inet address, and you will find an address in this form, xxx.xxx.x.xxx
    where x is a number between 0 & 9.

    - If you are are not sure which one is the proper ip address type again on
      another unix command line, ifconfig, or on a windows cmd the command, ipconfig.
      Again, locate the inet address, if the pi and this computer you used are
      connected on the same network, ideally your personal network, they should
      have an incremental ip address by 1, i.e, the difference in the ip address
      of this particular computer and the pi should be the last digit and they
      should differ by one, if they are the only two devices on this network,
      otherwise, the difference is the number of devices between the pi and this
      computer connecting to the same network. If this network is yours, you should
      have an idea of how many devices are connected to your wifi.

- For the port, chose the desired port you would like to use that is not in use.
    - Default port is 80. It's best to assign a different port to this one, for
      your project, otherwise you are likely to have to move a lot of things around.
      A good example would be to use port 8080, depending on the use status
