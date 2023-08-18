from flask import Flask, render_template, request, redirect, send_file
from extractors.remote import extract_jobs_remote
from extractors.wwr import extract_jobs_wwr
from file import save_to_file


app = Flask("JobScrapper")
db = {}

@app.route("/")
def home():
  return "home"


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
      return "home"
  if keyword in db:
      jobs = db[keyword]
  else:
      remote = extract_jobs_remote(keyword)
      wwr = extract_jobs_wwr(keyword)
      jobs = remote + wwr
      if jobs == []:
        return "no result"
      db[keyword] = jobs
    
  return "search"


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
      return "home"
  if keyword not in db:
      return "search"
  return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0")