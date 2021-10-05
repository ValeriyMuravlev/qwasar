import requests
from bs4 import BeautifulSoup as bs

# here we check availability of website
def request_github_trending(url):
    response = requests.get(url)
    return response

# using BeautifulSoup pocket we are parsing information form website, and then we use DevTools to find header "article"
def extract(page):
    soup = bs(page.text, 'html.parser')
    return soup.find_all("article")

# finding repository name, number of stars and developer name. Adding all of these to result list
def transform(html_repos):
    result = []
    for row in html_repos:
        repos_name = ''.join(row.select_one('h1.h3.lh-condensed').text.split())
        nbr_stars = ' '.join(row.select_one('a.d-inline-block.mr-3').text.split())
        developer_name = row.select_one('img.avatar.mb-1.avatar-user')['alt']
        result.append({'developer': developer_name, 'repos_name': repos_name, 'nbr_stars': nbr_stars})
    return result

# taking a repository array of hash and transform it and return it into a CSV string. Each columns will be separated by , and each lines by \n
def format(repositories_data):
    result = ['Developer, Repository Name, Number of Stars']

    for repos in repositories_data:
        row = [repos['developer'], repos['repos_name'], repos['nbr_stars']]
        result.append(', '.join(row))
    return "\n".join(result)


response = request_github_trending('https://github.com/trending')
html_repos = extract(response)
repositories_data = transform(html_repos)
result = format(repositories_data)

# formatting the result for a better perception of the information. Separated by vertical lines.
str_format = "| %25s | %50s | %10s |"
print(str_format%tuple(repositories_data[0].keys()))
for el in repositories_data:
    print(str_format%tuple(el.values()))
