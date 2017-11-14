import smtplib
import urllib2

curr_ip = urllib2.urlopen('http://ip.42.pl/raw').read()

prev_ip = open("/home/pi/.myip", "r").readline()
print curr_ip,
print prev_ip

if curr_ip != prev_ip:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("send@email", "passwordforsendemail")

  server.sendmail("send@email", "receive@email" curr_ip)
  server.quit()
  open("/home/pi/.myip", "w").write(curr_ip)

  
