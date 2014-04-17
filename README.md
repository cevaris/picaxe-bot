BOT120 PICAXE-20X2
=

BOT120 PICAXE-20X2 Microbot scripts with web frontend

---


Project Layout
--

* Web portal controller is located at `web/controller`.  
* The PICAXE-20X2 compiler and CLI is located at `picaxe20x2`.  
	* [Other compilers located here](http://www.picaxe.com/Software/Drivers/PICAXE-Compilers/)
* There are multiple pre-configured scripts located in the `scripts` folder.

---



Getting started
--
First things first, you need to find out which port your Picaxe bot is running on. First unplug all usb devices from your computer. Then plug in your bot via USB (the bot does not event need to be on). Lastly execute and write down the result of the follwing command.  
```bash
$ ls /dev/tty.usbserial*  
/dev/tty.usbserial-00001014
```



Getting started (web portal)
--

