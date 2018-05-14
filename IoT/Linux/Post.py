#--------------------------------------
#Program to Post the URL
#
#Author : Lal Bosco
#Date   : 14-May-2018
#--------------------------------------

#!/usr/bin/env python

import urllib2
import urllib

query_args = { 'RPI':'Active' }

#Update URL
URL = "http://www.bpiot.dx.am/health/health.php?t1=4&c=3&t2=2&p=1&s1=This_is_Sting1&s2=String2"
data = urllib.urlencode(query_args)
request = urllib2.Request(URL, data)
response = urllib2.urlopen(request).read()
print 'URL Posted'
