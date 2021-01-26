# 
import requests
import io
import argparse
#import asyncio
from fake_useragent import UserAgent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str, nargs=1)
    parser.add_argument('wordlist', type=str, nargs=1)
    args = parser.parse_args()
    
    fuzz(args.url[0], args.wordlist[0])

def fuzz(url, wordlist):
    ua = UserAgent()
    user_agent = ua.random
    with open(wordlist) as fp:
        line = fp.readline()
        while line:
            combined = url + line.strip() + '/'
            r = requests.get(combined, headers={'User-Agent': user_agent})
            if r.status_code == 200 or r.status_code == 403:
                print(url + line.strip(),' ----- ', r) # 200
                fuzz(combined, wordlist)
            #sleep(5)
            line = fp.readline()

if __name__ == '__main__':
    main()

# http://172.21.76.133/ common.txt