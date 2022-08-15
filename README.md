# placebot
A bot for https://pl.g7kk.com/ace

# ⚠️ WARNING ⚠️

Windows is **not** supported.  
Placebot is **only** supported on Linux.  
All issues on Windows **will** be closed unless you can reproduce it on Linux without using WSL.  

# How to run

1. Download the source code using `git clone https://github.com/thatretrodev/placebot.git`
2. Run `pip install -r requirements.txt` to install all of the dependencies.
3. Use the Developer Tools in your browser to find the `cf_clearance` cookie.
4. Create a `.env` file that looks like this:  
	```
	CF_TOKEN="cf_clearance=CLOUDFLARE_COOKIE_VALUE_HERE"
	USER_AGENT="USER_AGENT_HERE"
	```
5. Run `main.py`:  
	```
	python3 main.py (image filename) (x) (y)
	```
6. Go to `http://localhost:4000/` in your browser to verify that it is working.

# It doesn't work!

Send me a DM on Discord: `thatretrodev#3049`  
...or Matrix: `@thatretrodev:matrix.org`