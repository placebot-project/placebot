from dotenv import load_dotenv
import platform
import os

if platform.system() != "Linux":
	print("WARNING: Only Linux is officially supported. This means that the maintainers will not help you if you have an OS-specific problem, and will only help with reproducible problems that also apply to Linux.")

load_dotenv()

headers = {
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0",
	"Accept": "*/*",
	"Accept-Language": "en-US,en;q=0.5",
	"Accept-Encoding": "gzip, deflate, br",
	"Origin": "https://pl.g7kk.com",
	"DNT": "1",
	"Connection": "keep-alive, Upgrade",
	"Cookie": os.environ["CF_TOKEN"],
	"Sec-Fetch-Dest": "websocket",
	"Sec-Fetch-Mode": "websocket",
	"Sec-Fetch-Site": "same-origin",
	"Pragma": "no-cache",
	"Cache-Control": "no-cache"
}
