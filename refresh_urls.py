import os, requests, subprocess, json
from bs4 import BeautifulSoup
from datetime import datetime

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

def dns_reset():
  if "WIRELESS" in subprocess.getoutput("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'"):
    os.system("sudo networksetup -setdnsservers Wi-Fi \"Empty\"")

def other_check():
  if os.path.exists("/private/other_check_last_time.json") == True:
    last_opened_time = datetime.strptime(open("/private/other_check_last_time.json").read().replace('"',''), "%Y-%m-%d %H:%M:%S.%f")
    time_elapsed = (datetime.now() - last_opened_time).seconds
    if time_elapsed < 3600:
      return
    elif time_elapsed > 3600:
      os.system("rm /private/other_check_last_time.json")
  elif os.path.exists("/private/other_check_last_time.json") == False:
    if "Google Starbucks" in subprocess.getoutput("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'"):
      print("rming /etc/hosts")
      os.system("sudo rm -rf /etc/hosts")
      os.system("echo '' | sudo tee -a /etc/hosts && sleep 2")
      os.system("sudo networksetup -setdnsservers Wi-Fi \"Empty\"")
      json.dump(str(datetime.now()), open("/private/other_check_last_time.json", "w"))
      import sys
      sys.exit()

  r""" THIS BASICALLY DOES THE FOLLOWING : IF X DOES NOT EXIST-> CHECK IF WIFI IS ON GOOGLE STARBUCKS AND IF SO; INITIATE CLEAR HOSTS FOR ALLOW GOOGLE.COM CONNECTION TO ENABLE WI-FI"""
  r""" NOW IF LINE 1 WORKED, YOU ARE CLEARED OF HOSTS AND ABLE TO CONNECT TO WIFI. THEN, IT DUMPS THE CURRENT TIME (OF THIS RUNNING THING) TO X. SO NOW X EXISTS."""
  r""" IF U R HERE; X EXISTS AND U SHOULD HAVE BEEN ABLE TO CONNECT IN THAT MINUTE. (MAKE SURE ITS ON THE MINUTE.) WHETHER ITS 12:00:05 OR 12:00:30 OR 12:00:55; AFTER THIS CRONJOB RUNS U HAVE A MINUTE TO CONNECT WITH CLEARED HOSTS """
  r""" SINCE U R CONNECTED; VERIFIABLY THERE SHOULD BE A RUNNING 'OVER AN HOUR ELAPSED CHECK' AND THAT CHECK WILL HAPPEN BY CHECKING IF X EXISTS; WHICH IT STILL SHOULD. SO; EVERY MINUTE SINCE X EXISTED, UNTIL 61ST MINUTE, WILL BE A CHECK"""
  r""" ON THE 61ST MINUTE, X WILL BE REMOVED DUE TO >1 HOUR. WHICH WILL OPEN ANOTHER 1 MINUTE WINDOW FOR CONNECTION (VIA REMOVING /ETC/HOSTS) IF FOR ANY EVENT THE 'WIFI CONNECTION COOKIES' ARE GONE"""


  r""" double side note : if other_check runs in rming /etc/hosts; it will sys.exit() in order to not run refresh_urls.py Directly after it. \\o//"""
  r""" sidenote: this runs first since refresh_urls will actually require a stable wifi connection to work ; so as of now - other_check runs first, and then, the dns_reset which does not require wifi access; and then refresh_urls , etc"""


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
  other_check()
  refresh_urls()
  dns_reset()
  uniq_etc_hosts()
  firefox_check()


# Patched - 06.09.18 - Resolved all TLDS.




