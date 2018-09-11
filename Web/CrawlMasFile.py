#coding:utf-8
import requests
import time
import os.path as op

def CrawlFile():
	str = input("Please input your url:\n")
	if str[0:4] == "http":
		url = str
	else:
		url = "https://" + str
	r = requests.get(url)
	if r.status_code == 200:
		print("Connected Successfully.")
		mainpath = "/home/andrew/Downloads"
		filename = input("Please input your save_filename:\n")
		path = mainpath + filename
		with open(path,"wb") as save_file:
			save_file.write(r.content)
		if op.isfile(path):
			print("File written into target path Successfully.")
		else:
			print("Failed to write into target path.")
	else:
		print("status_code == ")
		print(r.status_code)
		print("Failed to connect the target url.")
	print("Waiting 1 seconds to exit automatically.")
	time.sleep(1)

def main():
	for i in range(40):
		CrawlFile()

		
if __name__ == "__main__":
	main()














