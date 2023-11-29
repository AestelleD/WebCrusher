# WebCrusher
ELEVATOR PITCH
A Python Program to find the connections between various items, ie to make a web graph showing the relations between peoples music taste.
I programmed this so I could map the connections between bands people like.

HOW IT WORKS
In a nutshell, It (Currently) takes in strings with values seperated by commas, like "Rush,KGLW,Destroy Boys"
1. makes a pair for each value pair possible, in this case Rush_KGLW, Rush_DestroyBoys and KGLW_DestroyBoys
2. Creates a dict with the number of times each pair is in the same string (for these 1 time each)
3. Takes in another string (as many times as you want) and does the same thing then adds it to the connected count
4. for example, if we now input "Rush,KGLW", our Counts will now be Rush_KGLW:2,  Rush_DestroyBoys:1 and KGLW_DestroyBoys:1
5. since theres been 2 strings that had both rush and kglw, and only 1 that had all 3 and so on


FEATURES:
Counts how many strings its taken
You can Save to Json
You can Dump Data Whenever
You can Quit Whenever
You can Change the Count

ISSUES / FUTURE UPDATES
Reading the data might be an issue because currently the delimiter for pairs is the same as the space replacement ("_")
Choose file name of JSON / JSON Selector, Currently set as bands.json
Figure how to make it take in .txt or .csv files, so I can dump data from sheets into it
Fix the weird issue with the values all being twice what they are supposted to be
