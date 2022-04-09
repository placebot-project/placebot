# placebot
A bot for https://pl.g7kk.com/ace

# How to run

1. Download the source code using `git clone https://github.com/thatretrodev/placebot.git`
2. Run `pip install websockets` to install [websockets](https://pypi.org/project/websockets/) and then run `pip install python-dotenv` to install [python-dotenv](https://pypi.org/project/python-dotenv/)
3. Use the DevTools in your browser to find the cookie for place.
4. Create a `.env` file that looks like this:  
	```
	CF_TOKEN="cf_clearance=CLOUDFLARE_COOKIE_HERE"
	```
5. Run `main.py` using this format:  
	```
	python3 main.py (image filename) (x) (y)
	```