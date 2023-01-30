from flask import Flask # flask lets you quickly get things on the web

app = Flask(__name__) # boilerplate - thankfully flask doesn't have a ton ... 

@app.route("/") # this is how we would set up a route!
def hello():
  return "Hello, World" #what happens when we hit the route!


app.run(debug=True)