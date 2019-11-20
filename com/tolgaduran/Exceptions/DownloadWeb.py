from urllib import request

url = "http://" + input("Enter web page to download : ")
web_page = request.urlopen(url)
data = web_page.read()
file_name = input("Enter file name : ")
file_to_write = open(file_name, "w+")
file_to_write.write(data.decode('utf-8'))
file_to_write.close()
