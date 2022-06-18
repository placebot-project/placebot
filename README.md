# placebot
A bot for https://pl.g7kk.com/ace

# How to run

1. Download the source code using `git clone https://github.com/thatretrodev/placebot.git`
2. Run `pip install -r requirements.txt` (`py -m pip install -r requirements.txt` on Windows) to install all of the dependancies.
3. Use the DevTools in your browser to find the cookie for place.
4. Create a `.env` file that looks like this:  
	```
	CF_TOKEN="cf_clearance=CLOUDFLARE_COOKIE_HERE"
	USER_AGENT="USER_AGENT_HERE"
	```
5. Run `main.py` using this format:  
	```
	python3 main.py (image filename) (x) (y)
	```
	Windows:
	```
	py main.py (image filename) (x) (y)
	```

# It doesn't work!

Contact me on Discord: `thatretrodev#3049`
...or Matrix: `@thatretrodev:matrix.org`