Using python libraries requests and beautifulsoup4, return a CSV of the TOP 25 trending repository from Github

Part 0 Request Write a function prototyped: def request_github_trending(url) it will return the result of Request.

Part 1 Extract Write a function prototyped: def extract(page) in order to find_all instances of html code of repository rows and return it. You should use BeautifulSoup. :-)

Part 2 Transform Write a function prototyped: def transform(html_repos) taking an array of all the instances of html code of the repository row. It will return an array of hash following this format: [{'deverloper': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]

Part 3 Format Write a function prototyped: def format(repositories_data) taking a repository array of hash and transform it and return it into a CSV string. Each columns will be separated by , and each lines by \n The columns will be Developer, Repository Name, Number of Stars
