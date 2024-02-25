from flask import Flask, render_template, request, redirect

app = Flask(__name__)
JOBS=[
  {
    "id":1,
    "Title":"SDE-1",
    "Location":"Noida",
    "Salary": "Rs. 10,00,000"
  },
  {
    "id":2,
    "Title":"SDE-2",
    "Location":"Noida",
    "Salary": "Rs. 20,00,000"
  },
  {
    "id":3,
    "Title":"SDE-3",
    "Location":"Noida",
  },
]

@app.route("/")
def hello_world():
  return render_template('homeUsingBootstrap.html',jobs=JOBS,company_name="NS")

@app.route("/home1")
def about():
    return render_template('home.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
