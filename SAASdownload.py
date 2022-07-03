url = "https://www.dropbox.com/s/68sll3bx02uxrkf/KVM%20COMMANDS.txt?dl=0"  # dl=1 is important
import urllib.request
u = urllib.request.urlopen(url)
data = u.read()
u.close()
 
with open("KVMcmdfinal.txt", "wb") as f :
    f.write(data)




import dropbox
dbx = dropbox.Dropbox("<ACCESS_TOKEN>")#Your access token

with open("KVMcmdfinal.txt", "wb") as f:
    metadata, res = dbx.files_download(path="/KVM COMMANDS.txt")
    f.write(res.content)
