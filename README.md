
# Website Traversal: Graph-Based Web Crawler

A Python-based web crawler implementing graph traversal algorithms to analyze link structures and discover relationships between web pages.

## Overview

This project implements an intelligent web crawler that maps internal website link structures and performs various graph analysis operations. Using depth-first search (DFS), breadth-first search (BFS), and pathfinding algorithms, the system can discover all reachable pages, find shortest paths between URLs, and calculate maximum traversal depths.

## Features

### Graph-Based Page Mapping
- Parses HTML content to extract internal links
- Builds adjacency list representation of website structure
- Maintains dictionary mapping URLs to their outbound links
- Handles relative and absolute URL paths

### Traversal Algorithms

**Depth-First Search (DFS)**
- Discovers all reachable pages from a starting URL
- Returns pages in depth-first discovery order
- Explores each branch completely before backtracking

**Breadth-First Search (BFS)**
- Discovers all reachable pages level-by-level
- Returns pages in breadth-first discovery order
- Ideal for finding nearest neighbors

### Path Analysis

**Shortest Path Discovery**
- Finds minimum-link path between any two URLs
- Returns ordered list of URLs forming the path
- Handles disconnected pages with appropriate error messaging

**Maximum Depth Calculation**
- Identifies the furthest reachable page from a starting URL
- Calculates distance based on minimum number of link hops
- Returns both the distant URL and the complete path to reach it

## Implementation

### Core Functions

```python
links_dfs(url)
```
Returns all reachable links in depth-first order

```python
links_bfs(url)
```
Returns all reachable links in breadth-first order

```python
find_shortest_path(url1, url2)
```
Returns shortest path between two URLs or "No path between URLs exists"

```python
find_max_depth(url)
```
Returns the furthest URL and the path to reach it from the starting URL

### Helper Function

```python
getLinks(url, baseurl)
```
Fetches and parses HTML content, extracting all internal links

## Setup

### Dependencies

Install BeautifulSoup 4 for HTML parsing:

```bash
python3 -m pip install beautifulsoup4
```

### Test Environment

The project is designed to work with self-contained test websites:
- Example: `https://secon.utulsa.edu/cs2123/webtraverse/index.html`
- Contains only internal links for reliable testing
- No external dependencies or broken links

## Technical Implementation

### Data Structure
- **Graph Representation**: Adjacency list using Python dictionary
- **Format**: `G[url] = [list_of_linked_urls]`
- **Example**: `G['/index.html'] = ['alink.html', 'blink.html', 'clink.html']`

### Algorithm Complexity
- **DFS/BFS**: O(V + E) where V = pages, E = links
- **Shortest Path**: O(V + E) using BFS
- **Max Depth**: O(V + E) with distance tracking

## Key Concepts Demonstrated

- Graph traversal algorithms (DFS/BFS)
- Web scraping and HTML parsing
- Shortest path algorithms
- Distance calculation in unweighted graphs
- Data structure design for web topology
- Efficient crawling strategies

## Usage

```python
# Discover all pages using DFS
pages_dfs = links_dfs('https://example.com/index.html')

# Discover all pages using BFS
pages_bfs = links_bfs('https://example.com/index.html')

# Find shortest path between two pages
path = find_shortest_path('https://example.com/page1.html', 
                          'https://example.com/page2.html')

# Find most distant page
furthest_url, path_to_furthest = find_max_depth('https://example.com/index.html')
```

## Applications

- Website structure analysis
- SEO optimization and site mapping
- Broken link detection
- Content discovery and indexing
- Web topology research
```
