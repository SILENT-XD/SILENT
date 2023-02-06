import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print("[*] koneksi anda buruk,silahkan refresh data anda.")
	exit()
	
if __name__=='__main__':
	try:os.mkdir('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/OK')
	except:pass
	try:os.mkdir('/sdcard/CP')
	except:pass
	if "Indonesia" == fc:
		__import__("silent").menu()
	else:
		__import__("silent").menu()