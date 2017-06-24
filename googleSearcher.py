import sys, glob
from optparse import OptionParser #requirement
from lxml import html
from shortRequests import shortRequests


GOOGLE_URL_PREFIX = 'https://www.google.com.sg'
SEARCH_URL_PREFIX = "/search?num=100&q="
#url = 'http://httpbin.org/post'
#url = 'http://httpbin.org/get'
#YOUTUBEURL = sys.argv[1]
#YOUTUBEURL_ENCODED = urllib.quote_plus(YOUTUBEURL)

parser = OptionParser(usage="usage: %prog -k search_keyword")
parser.add_option('-k', dest="search_keyword", help="keyword that you want to search")
options, args = parser.parse_args()

print options, args

if options.search_keyword is None:
	parser.print_help()
	sys.exit()

else:

	search_keyword = options.search_keyword
	outFileName = search_keyword + "_results"
	#Step 1: initiate overheads variables and functions
	pageUrl = GOOGLE_URL_PREFIX + SEARCH_URL_PREFIX + options.search_keyword
	
	"""
		Step 1: initiate overheads variables and functions
		Step 2: Fetch Google page
		Step 3: parse results
		Step 4: check got next page
		Step 5: give user choice to conitune or quit
		Step 6: Step 1
	"""
	while True:

		#Step 2: Fetch Google page
		pageReq = shortRequests(pageUrl)
		pageRes = pageReq.doGet()

		#Step 3: parse results
		pageTree = html.fromstring(pageRes.content)
		searchResults = pageTree.xpath('//div[@class="g"]//h3[@class="r"]/a/@href')
		output = ""
		for searchResult in searchResults:
			output = output + searchResult + "\n\r"

		with open(outFileName, 'a') as f:
			f.write(output)
		f.close()

		print "[+] Done outputing %s results of search keyword: %s" % (str(len(searchResults)), search_keyword)

		#Step 4: check got next page
		div_navi_as = pageTree.xpath('//div[@id="foot" and @role="navigation"]//td[@class="b navend"]')[1].xpath('.//a/@href')

		if (len(div_navi_as) > 0):
			nxtPage = div_navi_as[0]
		else:
			nxtPage = False

		#Step 5: give user choice to conitune or quit
		permission_nxt_page = False
		permission_str = '' 
		if nxtPage is False:
			sys.exit("[+] No more pages, done")
		else:
			while True:
				permission_str = raw_input("There is next page, wanna go? (y/n): ").lower()
				if permission_str == 'y':
					permission_nxt_page = True
					break
				elif permission_str == 'n':
					permission_nxt_page = False
					break
				else:
					print "[-] Invalid input. " 
		
		#Step 6: initiate overheads variables and functions
		pageUrl = GOOGLE_URL_PREFIX + nxtPage + "&num=100"
		if permission_nxt_page is False:
			sys.exit("[+] Not continueing, Done")
