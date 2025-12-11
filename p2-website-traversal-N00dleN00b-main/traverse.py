# Name: Bristie Rahman
# Starter Code for P2

import urllib.request
import urllib.parse
import urllib.error
from collections import deque


def byte2str(b):
    """
    Input: byte sequence b of a string
    Output: string form of the byte sequence
    Required for python 3 functionality
    """
    return "".join(chr(a) for a in b)


def getLinks(url, baseurl="https://secon.utulsa.edu/cs2123/webtraverse/"):
    """
    Input: url to visit, Boolean absolute indicates whether URLs should include absolute path (default) or not
    Output: list of pairs of URLs and associated text
    """
    # Import the HTML parser package
    try:
        from bs4 import BeautifulSoup
    except:
        print('You must first install the BeautifulSoup package for this code to work')
        raise
    # Fetch the URL and load it into the HTML parser
    soup = BeautifulSoup(urllib.request.urlopen(
        url).read(), features="html.parser")
    # Pull out the links from the HTML and return
    return [baseurl+byte2str(a["href"].encode('ascii', 'ignore')) for a in soup.findAll('a')]


def find_shortest_path(url1, url2):
    """
    Find shortest path from *url1* to *url2* if one exists. If not, return "No path between URLs exists"
    """
    #establish set
    visited = set()
    #queue for links
    queue = deque([(url1, [url1])])

    while queue:
        current_url, path = queue.popleft()
        #checking to see the url is equivalent to check oath
        if current_url == url2:
            return path
        if current_url not in visited:
            visited.add(current_url)
            links = getLinks(current_url)
            queue.extend((link, path + [link]) for link in links if link not in visited)

    return "No path between URLs exists"

    


def find_max_depth(url): #-> list():
    """
    Find and return the "longest shortest path"
    from the given **start_url** to any other webpage.
    
    Args:
        start_url (str): The starting URL.

    Returns:
        list: A list containing the URL with the longest shortest path and its links.




          index 
        /   |   \       differences between shortest and longest distance of nodes
        |   |   | 1     
        a  1 b   c
        |    |  |
        f    |   d 2
        |    | /
        g  2  e 3

        [i, a, f, g] find how to calculate and get this result
        utilize shortest path?
        
    """





     
    #visited = set()
    #linkf = links_dfs(url)
    max = []

    visited = set()
    #list of URL
    queue = deque([url])
    #empty dictionary checking for parent value 
    backup = {url:None}

    trail = []

    while queue:
        trail = queue.popleft()
        #print("here" + trail)
        for x in getLinks(trail):
            if x in backup:
                continue
            backup[x] = trail
            queue.append(x)



    

    for a in list(backup.keys()):
        #temp variable
        b = a 
        path = [b]
        #backup incase if proper needs aren't met
        while backup[b] != None:
            path.append(backup[b])
            b = backup[b]
        if len(path) > len(max):
            path.reverse()
            max = list(path)

    #returning list
    return max    



  


def links_dfs(url):
    """
    Return a list of all links reachable from a starting **url** 
    in depth-first order
    """
    #discovered
    # Create set of explored nodes and lists of to-be explored nodes
    visited = set()
    stack = [url]
    result = []

    while stack:
        current_url = stack.pop()
        if current_url not in visited:
            visited.add(current_url)
            result.append(current_url)
            links = getLinks(current_url)
            stack.extend(link for link in links if link not in visited)

    return result


def links_bfs(url):
    """
    Return a list of all links reachable from a starting **url** 
    in breadth-first order
    """
    #Create a set of explored nodes and list of the to be explored nodes
    visited = set()
    queue = deque([url])
    result = []

    # iterate
    while queue:
        current_url = queue.popleft() # get one
        if current_url not in visited: #already visited? skip it
            visited.add(current_url) #we've visited it now
            result.append(current_url) #plan on visiting
            links = getLinks(current_url)
            queue.extend(link for link in links if link not in visited) #schedule all fellow bromeos

    return result


if __name__ == "__main__":
    starturl = "https://secon.utulsa.edu/cs2123/webtraverse/index.html"
    print("*********** Depth-first search   **********")
    print(links_dfs(starturl))
    print(links_dfs("https://secon.utulsa.edu/cs2123/webtraverse/clink.html"))
    print("*********** Breadth-first search **********")
    print(links_bfs(starturl))
    print(links_dfs("https://secon.utulsa.edu/cs2123/webtraverse/clink.html"))
    print("*********** Find shortest path between two URLs ********")
    print((find_shortest_path("https://secon.utulsa.edu/cs2123/webtraverse/index.html",
          "https://secon.utulsa.edu/cs2123/webtraverse/wainwright.html")))
    print((find_shortest_path("https://secon.utulsa.edu/cs2123/webtraverse/turing.html",
          "https://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html")))
    print("*********** Find the longest shortest path from a starting URL *****")
    print((find_max_depth(starturl)))
    print(find_max_depth("https://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html"))

"""
*********** Depth-first search   **********
['https://secon.utulsa.edu/cs2123/webtraverse/index.html', 'https://secon.utulsa.edu/cs2123/webtraverse/clink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/blink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p5.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p5b.html', 'https://secon.utulsa.edu/cs2123/webtraverse/turing.html', 'https://secon.utulsa.edu/cs2123/webtraverse/kings.html', 'https://secon.utulsa.edu/cs2123/webtraverse/bletchley.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p4.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p7.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p6.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p8.html', 'https://secon.utulsa.edu/cs2123/webtraverse/alink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/wainwright.html', 'https://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html']
*********** Breadth-first search **********
['https://secon.utulsa.edu/cs2123/webtraverse/index.html', 'https://secon.utulsa.edu/cs2123/webtraverse/alink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/blink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/clink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/dijkstra.html', 'https://secon.utulsa.edu/cs2123/webtraverse/turing.html', 'https://secon.utulsa.edu/cs2123/webtraverse/wainwright.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p4.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p5.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p6.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p7.html', 'https://secon.utulsa.edu/cs2123/webtraverse/kings.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p5b.html', 'https://secon.utulsa.edu/cs2123/webtraverse/p8.html', 'https://secon.utulsa.edu/cs2123/webtraverse/bletchley.html']
*********** Find shortest path between two URLs ********
['https://secon.utulsa.edu/cs2123/webtraverse/index.html', 'https://secon.utulsa.edu/cs2123/webtraverse/alink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/wainwright.html']
No path between URLs exists
*********** Find the longest shortest path from a starting URL *****
['https://secon.utulsa.edu/cs2123/webtraverse/index.html', 'https://secon.utulsa.edu/cs2123/webtraverse/alink.html', 'https://secon.utulsa.edu/cs2123/webtraverse/turing.html', 'https://secon.utulsa.edu/cs2123/webtraverse/kings.html', 'https://secon.utulsa.edu/cs2123/webtraverse/bletchley.html']
"""
