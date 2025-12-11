[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11927076&assignment_repo_type=AssignmentRepo)
# Project 2: Website Traversal

In this problem you will write code to efficiently crawl webpages, as well as answer questions about the links between webpages.

Consider the following example website: <https://secon.utulsa.edu/cs2123/webtraverse/index.html>. This website has only internal links to other pages on the same website, which makes it ideal for testing. 

Starter code for your program is available in the `traverse.py` file.
You may use the helper function `getLinks(url, baseurl)`, which fetches a given URL and extracts all links, returning them as a list of URLs.

**Note:** you must install the Python package BeautifulSoup 4 (https://www.crummy.com/software/BeautifulSoup/), which parses HTML code.
Install BeautifulSoup using pip, Python's package installer. 

See the following example command to install the package. Note that this may differ on your system: 

```bash
python3 -m pip install beautifulsoup4
```

When crawling webpages, you should create a dictionary object mapping a URL to a list of links contained in that URL. For example:

```python
G['/index.html']= ['alink.html', 'blink.html', 'clink.html', 'index.html']
```

You are strongly encouraged to write additional functions that can be called from the required functions in the question.

### Required functions:

1. `links_dfs(url)`: Return a list of all links reachable from a starting URL, ordered as they are discovered in depth-first order.

2. `links_bfs(url)`: Return a list of all links reachable from a starting URL,  ordered as they are discovered in breadth-first order.

3. `find_shortest_path(url1, url2)`: Find and return the shortest path from `url1` to `url2` if one exists. Return an ordered list with the `url1` as the first element and `url2` as the last element. If no path exists return the string "No path between URLs exists".

4. `find_max_depth(url)`: Find and return the URL that is the greatest distance from `url`, along with the sequence of links that must be followed to reach the page. For this problem, distance is defined as the minimum number of links that must be followed to reach the page. First URL in the list is `start_url`, last URL is the URL that is the greatest distance from `start_url`.
