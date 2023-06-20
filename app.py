from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'doctor',
    'location': 'beruwala',
    'salary': 'rs. 10,000'
  },
  {
    'id': 2,
    'title': 'cricketer',
    'location': 'bdvdvuwala',
    'salary': 'rs. 40,000'
  },
  {
    'id': 3,
    'title': 'freelance',
    'location': 'remote',
  },
]


@app.route('/')
def hello():
  return render_template('home.html', jobs=JOBS, company_n='MasH')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
