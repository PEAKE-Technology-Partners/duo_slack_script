Hello There,
This is a test Repo for my Python Script.

Well, we have all done it. We put a user in Bypass for 2FA and it weakens our security. This script will alert you when a user is on Bypass. In our case, a user 
is on Bypass for troubleshooting and we forgot to put then back on Active in the Duo admin portal. 
Note, this script will need to by run manually. You can follow the commands in the Duo.sh file that I have added, but it will need to be modified to where the "testDuo" directory is located. 
You can have this script run periodically by using a cron tab. 

The duo.sh will create a python virtual env and import the reqired API's from Duo and Slack. 

TLDR:
This python script finds a user named "PeakeAdmin" and checks to see if the user is on bypass, then sends a message as a slack webhook. 
