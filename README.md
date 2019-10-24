# STEPS IN INSTALLING AND DOING A PROJECT USING MONGODB AND PYTHON

## INSTALLING AND SET UP MONGODB AND FLASK
### Go to cloud.mongodb.com and create an account
- go to the **Cluster** and build a new cluster under AWS (if you using AWS)
- click on **collections** and add your desired database and collections name
- go to **Cluster** and click on **connect**, choose **Connect your Applications**
- copy the **Connection String Only** and go to your AWS

### In AWS 
- got to bashrc under c9 folder (set all viewing for bashrc)
- add in the liner - *export MONGO_URI="< paste __Connection String__ link here >"*
- save and close the file, close the bash terminal and restart

### in bash terminal
 - sudo pip3 install dnspython
 - sudo pip3 install pymongo
 - pip3 install flask

_installation of mongodb completed_