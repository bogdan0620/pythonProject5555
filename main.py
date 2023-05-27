# def check_queue(clients):
#     for client in clients:
#         yield client
#
# all_clients = ['Pasha', 'Jordan', 'Vika']
# hospital = check_queue(all_clients)
# print(next(hospital))
# print(next(hospital))
# print(next(hospital))
#
# def check_queue1(clients):
#     for client in clients:
#         return client
#
# all_clients1 = ['Pasha', 'Jordan', 'Vika']
# hospital1 = check_queue1(all_clients1)
# print(hospital1)

# def week_days(list):
#     for i in list:
#         yield i
#
# list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# days = week_days(list)
#
# for i in days:
#     print(next(days))

import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def main():
    async with aiohttp.ClientSession() as session:
        responce = await session.get('https://quotes.toscrape.com/')
        web_content = await responce.text()
        soup = BeautifulSoup(web_content, 'html.parser')
        quotes = soup.findAll(class_='quote')

        result = []

        for i in quotes:
            main_text = i.find(class_='text')
            quote_text = main_text.text.strip('“”')
            author = i.find(class_='author').text
            tags = i.find(class_='keywords').attrs['content'].split(',')
            result.append({quote_text:{"by": author, "tags": tags}})

        with open('parsed_quotes.json', 'w', encoding='utf-8') as file:
            file.write(str(result))

asyncio.run(main())