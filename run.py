import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print("[*] koneksi anda buruk,silahkan refresh data anda.")
	exit()
	
if __name__ == "__main__":
	os.system("git pull")
	os.system("OK")
	os.system("CP")
	os.system("/sdcard/OK")
	os.system("/sdcard/CP")
	if "Indonesia" == fc:
		__import__("silent").menu()
	else:
		__import__("silent").menu()