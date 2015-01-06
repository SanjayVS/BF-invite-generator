import urllib2
import itertools

perm=list(itertools.permutations(['X','Y','G','O','T','6','4','5'],4))

response = urllib2.urlopen('https://account.oneplus.net/invite/claim/GLMS-YGMX-H4SR-TMNP')
html     = response.read()
begin = html.find('<article>')
end   = html.find('</article>',begin)
title1 = html[begin+len('<article>'):end].strip()


url= 'https://account.oneplus.net/invite/claim/GL2R-KTY9-DVOT-SLKF'
response = urllib2.urlopen(url)
html     = response.read()
begin = html.find('<article>')
end   = html.find('</article>',begin)
if(begin==-1):
	print url
title2 = html[begin+len('<article>'):end].strip()
print title1
print title2
if(title1!=title2):
	print url
