import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print("[*] koneksi anda buruk,silahkan refresh data anda.")
	exit()
	
if __name__ == "__main__":
	os.system("git pull")
	os.system("mkdir OK")
	os.system("mkdir CP")
	os.system("mkdir /sdcard/DUMP")
	if "Indonesia" == fc:
		__import__("silent").menu()
	else:
		__import__("silent").menu()