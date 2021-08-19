import json
with open('bdtb.json') as f:
    rownum = 0
    new_list = json.load(f)
    # print(type(new_list)) # list
    for j in new_list:
        for t in range(len(j["Title"])):
            rownum+=1
            print((str(rownum))+"Title:"+j["Title"][t]+" "+"Author:"+j["Author"][t])
