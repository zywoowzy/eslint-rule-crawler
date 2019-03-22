# eslint-rule-crawler
Crawl the eslint rule page to get all the recommended rules


Aside:
using grep & sed to replace string in a file through command line:
grep oldstr filepath | sed -e 's/oldstr/newstr/g' > objfile
example: $ grep 'warn' eslint-rule | sed -e 's/"warn"/1/g' > eslint-rule
