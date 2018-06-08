import os, requests, subprocess
from bs4 import BeautifulSoup

def refresh_urls():
  r"""
  How to websurf less and restrict videogames on OS X
  1. In system preferences: Create an admin account and set a for-use account as standard privileges
  2. Restart computer
  3. Log in as admin and remove videogame applications
  4. In terminal: Use sudo crontab to read from a designated file in the standard account which acts as a 1-way add-only text file that lists domains to be added into /etc/hosts
  5. Change admin password to a not-to-be-memorized password that's written on paper and locked in a timed-unlock box and log out of admin
  """
  whitelisted_domains = []
  url = "https://github.com/helloorange8215/test/blob/master/test.py"
  domain_list = [i.text for i in BeautifulSoup(requests.get(url).text, "lxml").findAll("td", attrs={"class":"blob-code blob-code-inner js-file-line"})]
  for i in domain_list:
    current_blacklisted_domains = open("/etc/hosts").read()
    if (i not in current_blacklisted_domains) and (i not in whitelisted_domains):
      print("domain %s not currently in /etc/hosts, adding it" % i)
      with open("/etc/hosts", "a") as f:
        f.write("127.0.0.1\t{}\n".format(i))
        f.write("127.0.0.1\twww.{}\n".format(i))


if __name__ == "__main__":
  refresh_urls()
