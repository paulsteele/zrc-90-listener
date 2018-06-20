# ZRC-90 Listener
Converts Central Scene signals logged in OZW_Log.txt and sends a post request to homeassistant
Based off of https://community.home-assistant.io/t/support-to-scene-modes-using-remotec-zrc-90/4370/37

## Environment Variables
API-URI : uri to post the modified request (e.x. http://localhost:8123/api/events/custom_scene)
API-KEY : The password used to authenticate against home assistant
MASTER_NODE : The Zwave Node to send modifed signals as 
