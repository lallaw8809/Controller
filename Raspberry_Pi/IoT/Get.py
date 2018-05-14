#--------------------------------------
#Program to Read the URL
#
#Author : Lal Bosco
#Date   : 14-May-2018
#--------------------------------------

#!/usr/bin/env python

import requests
  
URL = "http://www.bpiot.dx.am/health/display.php"

#Read the URL
r = requests.get(URL)

print r.text
