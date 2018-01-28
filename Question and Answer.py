1. Given a string representing a phrase e.g. om is in Austin, reverse each word with the location of the world being in the same place e.g. moT si ni nitsuA,

2. What other companies are you applying to, and why are you applying to them?

3. Pairs with Specific Difference: Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, 
such that x - y = k. If no such pairs exist, return an empty array.
input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[0, -1], [-1, -2], [2, 1], [1, 0]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

4. What is all of the HTTP response status codes?

Answer: information response - 100, Successful responses - 200, Redirection Message - 300, Client Error Response - 400, Server error responses - 500

5. How the web actually work? What happen when you actually type google

Browser checks the cache for a DNS record for the correcponding IP address. Check four different places: Borwser cache, OS cache, Router Cache, IPS Cache
If requested URL is not in cache, ISP's DNS server initiates a DNS query - small packet of small information. Browser initiates a TCP connection and does a three way handshake.
Then the browser sends an HTTP request to the web server. Server handles the request and sends back a HTML responses. 
The browser then run the HTML content and then additional elements on the web page is loaded, such as images, css, JS

6. How does the garbage collection works in python?

reference counting, count for each reference that exist, delete it when count reach 0. can't deal with renference cycles caveat. example: l = [], l.append(l)

7. What is multithreaded programming?

8. Local verse global variables

9. What is a regression test?

10.Describe your coding processes?

11.What is a mutex and semaphone?

12. Solve KnapSack probelm using buttom-up solution?

13. How to create a Django Application?


14. Implement Mergesort using python.

15. Inputs: unsorted list of integers of length n, and another integer k. Goal: determine if there are two integers in the list that sum up to k. Constraints: O(n) time complexity. 

16. Inputs: two sorted lists of integers of length 2n and n respectively. The list of size 2n has all its integers in first half, and the rest of the entries are blanks ("--"). 
Goal: merge the two lists into one sorted list of size 2n. Constraints: O(n) time complexity, AND O(1) space complexity. 

17. Build a hashtable using python? Build a stack and build a fancy stack that can return the least element in the stack

18. Code a sudoku Solver?

19. Design bit torrent (P2P)? Think about architecture decisions, approaches to scaling and potential performance bottlenecks

20. [Autocomplete search] Given a large dataset of CSS hierarchies. (e.g. “div.faq_cancel input.spanAB-wrap.tabs-container.contentRow”), 
design a Redis schema and the algorithm to autocomplete searches in a language that you like. Note that the solution should support prefix searching, i.e. (div.f i.sp.co) should match the hierarchy above.

21. Discuss and implement URL shortener with the twist that your design should support extracting URLs from a large string (e.g. blog post/comment) and replace it with the shortened link when displayed on the frontend.

22. Create a simple web app, hosted at a URL that can be visited; users can enter a URL of a page to fetch, web app fetches the HTML of the page and displays the source to the user- 
a summary of the document is displayed, listing which tags are present in the HTML and how many of each tag; (optional) 
clicking on the name of each tag in the summary will highlight the tags in the source code view

23. You are given x amount of steps. Find the number of combinations you can take going up these steps, taking either one, two or three steps. 

24. Phone: list of list of words, find most frequent words.  Whats the runtime? (usually nlogn because of sorting) how can you do it in O(n) 

25. Given an integer, return the largest integer created by swapping two numbers in the integer.
Examples:
58938   ==>   98538 
1234     ==>   4231