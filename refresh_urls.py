import os, requests, subprocess
from bs4 import BeautifulSoup


def refresh_urls():
  current_blacklisted_domains = open("/etc/hosts").read()
  url = "https://github.com/helloorange8215/test/blob/master/test.py"
  domain_list = [i.text for i in BeautifulSoup(requests.get(url).text).findAll("td", attrs={"class":"blob-code blob-code-inner js-file-line"})]
  for i in domain_list:
    with open("/etc/hosts","a") as f:
      if ("127.0.0.1\t%s www.%s\n" %(i,i)) not in current_blacklisted_domains:
        if "*" in i:
          f.write("127.0.0.1\t%s\n"%i)
        else:
          f.write("127.0.0.1\t%s www.%s\n"%(i,i))

def uniq_etc_hosts():
  os.system("sudo sort -u -o /etc/hosts /etc/hosts")

def firefox_check():
  def check_output(cmd):
    return subprocess.check_output(cmd.split(), shell=False,stdin=None, stderr=None, close_fds=True).decode()
  if "46" not in check_output("/Applications/Firefox.app/Contents/MacOS/firefox-bin -v"):
    os.system("sudo rm -rf /Applications/Firefox.app")
    os.system("sudo cp -r /Applications/Firefox_46.app /Applications/Firefox.app")
    os.system("sudo touch /Users/paul/Notification_Recently_Reinstalled_Firefox46")


if __name__ == "__main__":
  refresh_urls()
  uniq_etc_hosts()
  firefox_check()


# Patched - 06.09.18 - Resolved all TLDS.

