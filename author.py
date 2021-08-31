import os

import pandas as pd
import requests

end = 156


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def author():
    pg = 98
    while True:
        sbd, sp, lk, yr, hve = [], [], [], [], []
        dat = str(requests.get("https://hiveblocks.com/@streetstyle?page={}".format(pg)).content)
        indexes = list(find_all(str(dat), "author reward"))
        for k in indexes:
            txt = str(dat[k:k + 300])
            try:
                if "HP" in txt and "HIVE" in txt and "HBD" not in txt:
                    hve.append(txt[txt.index(":"):txt.index("HIVE")].replace(":", ""))
                    sp.append(txt[txt.index("and"):txt.index("HP")].replace("and", ""))
                    yr.append("2020")
                    lk.append(txt[txt.index("<"):txt.index(">")])
                if "HBD" in txt and "HIVE" in txt and "HP" not in txt:
                    hve.append(txt[txt.index(":"):txt.index("HIVE")].replace(":", ""))
                    sbd.append(txt[txt.index("and"):txt.index("HBD")].replace("and", ""))
                    yr.append("2020")
                    lk.append(txt[txt.index("<"):txt.index(">")])
            except Exception as e:
                print(e, " Author reward page:", pg)
                # print(sbd, stm, sp)
        data = [sbd, sp, lk, yr, hve]
        dataa = pd.DataFrame(data=data, index=["HBD", "HP", "Link", "Year", "Hive"])
        dataa = dataa.T
        dataa.to_csv("Author_reward_2_2020.csv", index=False, mode="a",
                     header=not (os.path.isfile("Author_reward_2_2020.csv")))

        print(pg)
        if pg == end:
            break
        pg += 1


def claim():
    pg = 1
    while True:
        sbd, sp, yr = [], [], []
        dat = str(requests.get("https://hiveblocks.com/@streetstyle?page={}".format(pg)).content)
        indexes = list(find_all(str(dat), "claim reward"))
        for k in indexes:
            txt = str(dat[k:k + 300])
            try:
                if "HBD" in txt:
                    sbd.append(txt[txt.index(":"):txt.index("HBD")].replace(":", ""))
                    sp.append(txt[txt.index("and"):txt.index("HP")].replace("and", ""))
                    yr.append("2020")
                if "HBD" not in txt:
                    sbd.append(txt[txt.index(":"):txt.index("HP")].replace(":", ""))
                    yr.append("2020")
            except Exception as e:
                print(e)
                print("For Claim:", pg)
        data = [sbd, sp, yr]
        dataa = pd.DataFrame(data=data, index=["HBD", "HP", "Year"])
        dataa = dataa.T
        dataa.to_csv("claim_reward_2020.csv", index=False, mode="a",
                     header=not (os.path.isfile("claim_reward_2020.csv")))
        print(pg)
        if pg == end:
            break
        pg += 1


def curation():
    pg = 1
    while True:
        sp, yr = [], []
        dat = str(requests.get("https://hiveblocks.com/@streetstyle?page={}".format(pg)).content)
        indexes = list(find_all(str(dat), "curation reward"))
        for k in indexes:
            txt = str(dat[k:k + 300])
            try:
                sp.append(txt[txt.index(":"):txt.index("HP")].replace(":", ""))
                yr.append("2020")
            except Exception as e:
                print(e)
                print("For curation:", pg)
        data = [sp, yr]
        dataa = pd.DataFrame(data=data, index=["HP", "Year"])
        dataa = dataa.T
        dataa.to_csv("curation_reward_2020.csv", index=False, mode="a",
                     header=not (os.path.isfile("curation_reward_2020.csv")))
        print(pg)
        if pg == end:
            break
        pg += 1


# t1 = Thread(target=claim, args=(), daemon=True)
# t2 = Thread(target=curation, args=(), daemon=True)
# t3 = Thread(target=author, args=(), daemon=True)
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
author()
