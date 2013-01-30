Skewer
======

Inventory tracking and management for household use.

Remote
------

The remote end is, ideally, a single-board computer (perhaps, like the [original design](http://agmlego.com/projects/skewer "Project Website"), you want to use a [Raspberry Pi](http://www.raspberrypi.org/ "Raspberry Pi Main Page") Model B?)with a parcode scanner, connected via some form of Ethernet (loopback, wired, WiFi, [6LoWPAN](https://en.wikipedia.org/wiki/6LoWPAN "Wikipedia article on 6LoWPAN"), whatever) to a server.

The remote end's job is to allow users to scan control codes and then UPC/EAN codes to check items into and out of an inventory, while using little power when not scanning.

Server
------

The server runs a webserver (to provide inventory data) and a relational database that PyODBC understands (to store the inventory).
