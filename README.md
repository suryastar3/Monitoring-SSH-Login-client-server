# Monitoring-SSH-Login-client-server
alphaserver and alphaclient
-----------------------------------------------------------------------
Prerequisite
-----------------------------------------------------------------------
Before we go we need the following application installed on the system:

docker
docker-compose

OR

SERVER
-----------------------------------------------------------------------
Install Ubuntu 20.04:
Settings the network to bridge (192.168.0.140)
 - apt-get update -y
 - apt-get install -y openssh-server
 - apt-get install -y python3-pip
 
 Next uncommand PermitRootLogin in /etc/ssh/sshd_config and change like this:
 (PermitRootLogin yes)
 
 restart ssh system:
 -systemctl restart ssh
 
 check status ssh:
 -systemctl status ssh
 
 Next create file "alphaserver.py" as a service to monitoring ssh login attemps
 
 Next create file bash script "run.sh"
 python3 ./alphaserver.py
 
CLIENT 1
-----------------------------------------------------------------------
Install Ubuntu 20.04:
Settings the network to bridge (192.168.0.141)
 - apt-get update -y
 - apt-get install -y openssh-server
 - apt-get install -y python3-pip
 - pip install tailer
 
 Next uncommand PermitRootLogin in /etc/ssh/sshd_config and change like this:
 (PermitRootLogin yes)
 
 restart ssh system:
 - systemctl restart ssh
 
 check status ssh:
 - systemctl status ssh
 
 Next create file "alphaclient1.py" to get data login attemps from /var/log/auth.log
 
 Next create file bash script "run.sh"
 python3 ./alphaclient1.py

CLIENT 2
-----------------------------------------------------------------------
Install Ubuntu 20.04:
Settings the network to bridge (192.168.0.142)
 - apt-get update -y
 - apt-get install -y openssh-server
 - apt-get install -y python3-pip
 - pip install tailer
 
 Next change PermitRootLogin in /etc/ssh/sshd_config
 (PermitRootLogin yes)
 
 restart ssh system:
 - systemctl restart ssh
 
 check status ssh:
 - systemctl status ssh
 
 Next create file "alphaclient2.py" to get data login attemps from /var/log/auth.log
 
 Next create file bash script "run.sh"
 python3 ./alphaclient2.py

THEN

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




