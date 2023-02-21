import requests
from bs4 import BeautifulSoup

# get the main page o scrape
URL = "https://realpython.github.io/fake-jobs/"

# store the static html inside of pafe object
page = requests.get(URL)

# create BS object to store page content like with page, but without character encoding
soup = BeautifulSoup(page.content, "html.parser")

# find all content within a certain id
results = soup.find(id="ResultsContainer")

#print(results.prettify())

# create iterable of objects that are a div with class card-content
job_elements = results.find_all("div", class_="card-content")


# prints out all divs of content
#for je in job_elements:
 #   print(je, end="\n"*2)

# prints for specfic divs within the card content to narrow down info
for je in job_elements:
    title_element = je.find("h2", class_="title")
    company_element = je.find("h3", class_="company")
    location_element = je.find("p", class_="location")
    # .text prints with content without tags
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# filter job listing results by the ones that say Python in title. Pas lambda function to BS to find python no matter vase or whitespace
# text is the incoming string
# onlt stores that tag, not its sibling or child content
python_results = results.find_all("h2", string=lambda text: "python" in text.lower())

print(python_results)

python_job_elements = [ # get the parent of the h2 tag 3 stages up all the way to card content which contains all the content for that filter
    h2_element.parent.parent.parent for h2_element in python_results
    ]

for pr in python_job_elements:
    title_element = pr.find("h2", class_="title")
    company_element = pr.find("h3", class_="company")
    location_element = pr.find("p", class_="location")
    # .text prints with content without tags
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# to find all links at footer of cards
for pl in python_job_elements:
    links = pl.find_all("a")

    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")