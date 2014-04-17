BOT120 PICAXE-20X2
=

BOT120 PICAXE-20X2 Microbot scripts with web front-end

---


Project Layout
--

* Web controller is located at `web/controller`.  
* The PICAXE-20X2 compiler and CLI is located at `picaxe20x2`.  
	* [Other compilers located here](http://www.picaxe.com/Software/Drivers/PICAXE-Compilers/)
* There are multiple pre-configured scripts located in the `scripts` folder.

---



Getting started
--
First things first, you need to find out which port your Picaxe bot is running on. First unplug all USB devices from your computer. Then plug in your bot via USB (the bot does not event need to be on). Lastly execute and write down the result of the following command.  

	$ ls /dev/tty.USBserial*  
	/dev/tty.USBserial-00001014

Keep in mind, if you have multiple USB devices plugged in at once along with your Picaxe bot, you would have to test and find the correct USB port that which is connected to your Picaxe bot.

So. Now that I know which USB port your Picaxe bot is on, turn on your Picaxe bot and execute one of the preconfigured scripts.  

	$ ./picaxe20x2 -c/dev/tty.usbserial-00001014 scripts/shutup.bas 

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



Getting started (web controller)
--
If you want to move the bot via web requests, you need to configure the environment for a Flask Python application running a Redis-backed Celery  Distributed Task Queue.

There are three prerequisites in order to start the web controller. 

* [Redis](http://redis.io/)
* [Pip Installer](https://pypi.python.org/pypi/pip)
* [Foreman](https://github.com/ddollar/foreman)

### Redis

What you need to do is download/install [Redis](http://download.redis.io/releases/redis-2.8.8.tar.gz). Simply download, extract binary, compile, and execute the binary `redid-server`. 

### Pip Installer
You need to have python on your path with [pip](https://pypi.python.org/pypi/pip) installed via `sudo easy_install pip`.

### Foreman
Foreman is a process manager that helps manage the start/stopping of Clery queue and Flask web app. [Click here](http://assets.foreman.io/foreman/foreman.pkg) to download the .pkg installation file. And you may have to install the ruby gem, `gem install foreman`; not sure.

Next, to assist with setting up the correct environment, there is a pip `requirements.txt` file holding all the libraries needed. To set up the environment, do the following.

	cd web
	virtualenv venv
	pip install -r controller/requirements.txt
	source venv/bin/activate
	
To setup we need to tell the web app which USB port to find the Picaxe bot. Open the file `web/controller/dev.env` and add your USB port under the `USB_PORT` environment variable. For example, if my USB port is `/dev/tty.usbserial-00001014`, the the file will look like the following.
	
	export REDIS_URL='redis://localhost:6379/0'
	export COMPILER_PATH='lib/picaxe20x2'
	export USB_PORT='/dev/tty.usbserial-00001014'

The REDIS_URL and COMPILER_PATH are set to defaults, so if you move the compiler binary or changed Redis's port, update this file accordingly. 

Lastly, execute `web/controller/dev.env` to load the environment variables.

	source web/controller/dev.env
	
Now that you got the environment setup, Redis is running, and your Picaxe bot is plugged in; finally start the project via foreman.

	cd web/controller
	foreman start
	
### Web portal commands
#### Forward
Move the robot forward in a line.
[http://localhost:5000/robot/go/N](http://localhost:5000/)  
Where N is the number of feet the robot is to move.  

Example [http://localhost:5000/robot/go/3](http://localhost:5000/robot/go/3)

#### Square
Move the robot in a square.
[http://localhost:5000/robot/square/N](http://localhost:5000/)  
where the square is N by N feet.

Example [http://localhost:5000/robot/square/5](http://localhost:5000/robot/square/5)

Keep in mind, there is a delay between the time of the requests and the time the Picaxe bot actually moves. This delay is because the requested action has to generate, compile, and download the code to the Picaxe bot. This process normally takes around 5-7 seconds. That is the whole reason behind making execution of the commands to the Picaxe bot asynchronous. So the web request does not hang.


# Contributing

Fork the project and send pull requests. 


# License

The MIT License (MIT)

Copyright (c) [2014] [cevaris]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
	





