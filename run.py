from scrapy import cmdline
import os
if os.path.exists("bdtb.json"):
    os.remove("bdtb.json")
    cmdline.execute("scrapy crawl tb -o bdtb.json".split())  # -o db.json
else:
    cmdline.execute("scrapy crawl tb -o bdtb.json".split())  # -o db.json