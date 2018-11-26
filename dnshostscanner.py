import socket
import logging

logging.basicConfig(filename='/tmp/scanner.log', filemode='w', format='%(message)s', level=logging.INFO)
console = logging.StreamHandler()
logging.getLogger('').addHandler(console)

with open('/tmp/ips') as fp:
  line = fp.readline()
  while line:
    try:
      dnsLookup = socket.gethostbyaddr(line.strip())
      logging.info(("Found a host! %s -> %s") % ( dnsLookup[2][0], dnsLookup[0] ))
      line = fp.readline()
    except:
      line = fp.readline()
      continue
