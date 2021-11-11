# Monitoring-SSH-Login-client-server
alphaserver and alphaclient

first of all
(ALPHA SERVER - 192.168.0.140)
 - Running machine or docker
 - Running python3 alphaserver.py or running (./run.sh)

(ALPHA CLIENT 1 - 192.168.0.141)
 - Running machine or docker
 - Running python3 alphaclient1.py or running (./run.sh)

(ALPHA CLIENT 2 - 192.168.0.142)
 - Running machine or docker
 - Running python3 alphaclient2.py or running (./run.sh)

TESTING SSH LOGIN ATTEMPS
 TO DO:
  - open CMD and do this "ssh alphaclient1@192.168.0.141"
  - input password "bagas31" (my user password in alphaserver machine)
  - see in alphaserver if success will show the output : "NodeABC had 1 attemps ssh login"
  OR
  - open CMD and do this "ssh alphaclient2@192.168.0.142"
  - input password "bagas31" (my user password in alphaserver machine)
  - see in alphaserver if success will show the output : "NodeXYZ had 1 attemps ssh login"




