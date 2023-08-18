from bs4 import BeautifulSoup
import requests


def extract_jobs_wwr(term):
  baseUrl = "https://weworkremotely.com"
  url = f"{baseUrl}/remote-jobs/search?utf8=✓&term={term}"
  request = requests.get(url)
  results = [] 
  if request.status_code == 200:
      soup = BeautifulSoup(request.text, "html.parser")
      views = soup.find_all("li", class_="view-all")
      for view in views:
        viewUrl = f"{baseUrl}{view.find('a')['href']}" 
        request = requests.get(viewUrl)
        if request.status_code == 200:
          soup = BeautifulSoup(request.text, "html.parser")
          jobs_list = soup.find("section", class_="jobs")
          jobs = jobs_list.find("ul").find_all("li")
          for job in jobs:
            tooltip = job.find("div", class_="tooltip")
            if tooltip != None:
              a = job.find("a", recursive=False)
              company = a.find("span", class_="company")
              position = a.find("span", class_="title")
              location = a.find("span", class_="region")
              link = f"{baseUrl}{a['href']}"
              if company:
                  company = company.string.strip().replace(",", " ")
              if position:
                  position = position.string.strip().replace(",", " ")
              if location:
                  location = location.string.strip().replace(",", " ")
  
              if company and position and location:
                result = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link' : link,
                }
                results.append(result)      
  else:
      print("[WWR] Can't get jobs.")
  return results