#!flask/bin/python
from app import app
#have augmented the run command to exclusively point to specific ip and port 
app.run(host="0.0.0.0", port=int("8000"), debug=True)