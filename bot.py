import os,time,platform
r='\033[7;91m'
B='\033[1;97m'
v='\033[7;92m'
R='\033[1;91m'
S='\033[0m'
phone=platform.architecture()[0]
if "64bit" in phone:
	path=("pagelike64")
	if os.path.exists(path):
		os.system("./pagelike64")
	else:
		os.system("clear")
		print(f"{R}[{B}-{R}Downloading PageLike for 64bit device... {S}")
		time.sleep(2)
		print()
		os.system("curl -L https://github.com/MrUser-404/Test/releases/download/MrUser/pagelike64 > pagelike64")
		os.system("chmod +x pagelike64")
		os.system("./pagelike64")
else:
	os.system("clear")
	print(f"{r}Your device is not supported for the moment{S}")
	time.sleep(2)
	exit()