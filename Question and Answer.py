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

11.What is a mutex and semaphone? (JAVA)
Mutex is locking mechanism object that allows multiple program thred to access a single resource but not simultaneously
Semaphore is a signaling mechanism and integer variable allow multiple program thread to access a finite instance of resources

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
Find the largest index, swapping it with the first index. If the the largest index is in the first index, find the second largest.


26. WHat is AWS?
	AWS(Amazon Web Services) is a platform to provide secure cloud services, database storage, offerings to ocmputer power, content delivery, and other services to help business level and develop

27. What components involved in Amazon Web Services?
	4 components involved: 
	Amazon S3 - one can retrieve key information which are occupied in creating cloud structural design and amount of produced information also can be stored in this compoenent that is
	the consequence of the key specified.

	Amazon EC2 Instance: Helpful to run large distributed system on the hadoop cluster.

	Anazib SQS: this component acts as a mediator between different controllers.

	Amazon SimpleDB: Helps in storing the transitional position log and errands executed by the consumers


28. AWS (scaling from millions to tens or hundreds of millions of users) 
	Python 
	Infrastructure and Scaling/Scalability Experience 
	Object-Oriented Programming 
	Consumer facing product experience

29. What are the different relational databases structures
One to One, One to Many, Many to One, Many to Many

30. Different between flexibility and Scalability?
Scalability is the aptitude of any schema to enhance the task on hand on its present reources
Flexibility is the capability of a scheme to augment the tasks on hand on its present and supplementary hardware property

31. Generate all partitions for an integer
	def partitions(n):
		# base case of recursion: zero is the sum of the empty list
		if n == 0:
			yield []
			return
			
		# modify partitions of n-1 to form partitions of n
		for p in partitions(n-1):
			yield [1] + p
			if p and (len(p) < 2 or p[1] > p[0]):
				yield [p[0] + 1] + p[1:]

32. Hashmap implementation in python.
>>> h = hashlib.new('ripemd160')
>>> h.update("Nobody inspects the spammish repetition")
>>> h.hexdigest()
'cc4a5ce1b3df48aec5d22d1f16b894a0b894eccc'

33. What is the different type mongos and Redis?
MongoDB much easier to code, a nire schemaable data- store document. Disk base memory
But Redis offer more flexibility and it is much faster, a cache layer can probably be better implemented in redis. It store key value. Similar to a list or common data structures learn in classes. In memory

34. When to use noSQL verses SQL Database
SQL is digital, works best when a database is clearly defined and discrete items with exact specisc
NoSql is work best with data that is organic and has some type of variablity.

35. Using Redis on Caching
if (isset($queryParams['search'])) {

    $redis = new Client();
    $hash = md5($_SERVER['QUERY_STRING']);
    if (!$redis->get($hash . '-results')) {

        $diffbot = new Diffbot(DIFFBOT_TOKEN);

        // Building the search string
        $searchHelper = new SearchHelper();
        $string = (isset($queryParams['q']) && !empty($queryParams['q']))
            ? $queryParams['q']
            : $searchHelper->stringFromParams($queryParams);

        // Basics
        $search = $diffbot
            ->search($string)
            ->setCol('sp_search')
            ->setStart(($queryParams['page'] - 1) * $resultsPerPage)
            ->setNum($resultsPerPage);

        $redis->set($hash . '-results', serialize($search->call()));
        $redis->expire($hash . '-results', 86400);
        $redis->set($hash . '-info', serialize($search->call(true)));
        $redis->expire($hash . '-info', 86400);
    }

    $results = unserialize($redis->get($hash . '-results'));
    $info = unserialize($redis->get($hash . '-info'));