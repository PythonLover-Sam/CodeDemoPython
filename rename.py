import os

path = "d:/rename/"

filenames = os.listdir(path)

for file in filenames:
	if file != "rename.py":
		os.rename(file, "灰灰的礼物-Eternel Love of Dream%s"%file[-2:]+".mp4")