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
First things first, you need to find out which port your Picaxe bot is running on. First unplug all USB devices from your computer. Then plug in your bot via USB (the bot does not event need to be on). Lastly execute and write down the result of the follwing command.  
```bash
$ ls /dev/tty.USBserial*  
/dev/tty.USBserial-00001014
```  
Keep in mind, if you have multiple USB devices plugged in at once along with your Picaxe bot, you would have to test and find the correct USB port that which is connected to your Picaxe bot.

So. Now that I know which USB port your Picax bot is on, turn on your Picaxe bot and exucute one of the preconfigured scripts.  
`
$ ./picaxe20x2 -c/dev/tty.usbserial-00001014 scripts/shutup.bas 
`

	PICAXE-20X2 Enhanced Compiler. Version 2.4
	Copyright (c) 1996-2012 Revolution Education Ltd
	All rights reserved.
	www.picaxe.com

	Compiled successfully.
	Memory used = 5 out of 4096 bytes.

	Searching for hardware on /dev/tty.usbserial-00001014.
	Downloading program.
	..................
	Downloading program/table.
	..................
	Downloading data.
	..................

	PASS - programmed PICAXE-20X2 vC.1 successfully.



Getting started (web portal)
--

