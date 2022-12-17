import requests
from bs4 import BeautifulSoup

page = 0
for i in range(1,5):
    job_title = []
    orgas = []
    datess = []
    closing_date = []
    result = requests.get(f"https://reliefweb.int/jobs?page={page}")
    src = result.content
    soup = BeautifulSoup(src,"html.parser")
    # print(soup)
    job_titles = soup.find_all("h3", {"class": "rw-river-article__title"})
    organizations = soup.find_all("a", {"class": "rw-entity-meta__tag-link"})
    date = soup.find_all("dd", {"class": "rw-entity-meta__tag-value rw-entity-meta__tag-value--posted rw-entity-meta__tag-value--date"})
    closingdate = soup.find_all("dd", {"class": "rw-entity-meta__tag-value rw-entity-meta__tag-value--closing-date rw-entity-meta__tag-value--date rw-entity-meta__tag-value--last"})
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text.strip().replace("\n",""))
        orgas.append(organizations[i].text)
        datess.append(date[i].text.strip().replace("\n", ""))
        closing_date.append(closingdate[i].text.strip().replace("\n", ""))
    print(f"page {page} is switched")
    print(job_title,orgas,datess,closing_date)
    page += 1
