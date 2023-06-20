from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'doctor',
    'location': 'beruwala',
    'salary': 'rs. 10,000'
  },
  {
    'id': 1,
    'title': 'sdbdb',
    'location': 'bdvdvuwala',
    'salary': 'rs. 40,000'
  },
  {
    'id': 1,
    'title': 'dosvsdvctor',
    'location': 'bfffuwala',
    'salary': 'rs. 80,000'
  },
]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS, company_n='MasH')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
