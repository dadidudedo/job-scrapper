from bs4 import BeautifulSoup
import requests


def extract_jobs_remote(term):
    baseUrl = "https://remoteok.com"
    url = f"{baseUrl}/remote-{term}-jobs"
    request = requests.get(url)
    results = [] 
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
      
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            link = f"{baseUrl}{job['data-href']}"
            if company:
                company = company.string.strip().replace(",", " ")
            if position:
                position = position.string.strip().replace(",", " ")
            if location:
                location = location.string.strip().replace(",", " ")
            if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link': link,
                }
                results.append(job)
    else:
        print("[REMOTE] Can't get jobs.")
    return results

