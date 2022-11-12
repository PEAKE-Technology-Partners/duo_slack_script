Hello There,

Well, we have all done it. We put a user in Bypass for 2FA and it weakens our security. This script will alert you when a user is on Bypass. In our case, a user 
is on Bypass for troubleshooting and we forgot to put then back on Active in the Duo admin portal. 
Note, this script will need to by run manually. You can follow the commands in the Duo.sh file that I have added, but it will need to be modified to where the "testDuo" directory is located. 
You can have this script run periodically by using a cron tab. 

The duo.sh will create a python virtual env and import the reqired API's from Duo and Slack. 

TLDR:
This python script finds a user that you specify and checks to see if the user is on bypass, then sends a message as a slack webhook. 


FYI, this is a test envoriment and has access to nothing and I have revoked the API keys!


Instructions:
You will need to git clone,
https://github.com/duosecurity/duo_client_python.git

and then put the peake.py file in the "examples" folder.

Then Modifiy the duo.sh to point to the folder's path where you downloaded the duo_client folder. 

Modify peake.py with the correct API keys for Duo and Slack. 


