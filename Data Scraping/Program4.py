from bs4 import BeautifulSoup

def DataScraping():
    with open('stock_page.html','r',encoding="utf-8") as file:
        data = file.read()

    soup = BeautifulSoup(data,"html.parser")

    data = []

    Products = soup.findAll('td', {"class": 'productHead'})[:-1]
    product_list = [product.text.strip() for product in Products]  # Store all product names

    Volume = soup.find('tbody').findAll('tr', class_=['Equity', 'Currency', 'Interest', 'Commodity', 'Mutual'])

    Value = soup.find('tbody').findAll('tr', class_=['Equity', 'Currency', 'Interest', 'Commodity', 'Mutual'])

    Open_interest = soup.find('tbody').findAll('tr', class_=['Equity', 'Currency', 'Interest', 'Commodity', 'Mutual'])

    Updated_at = soup.find('tbody').findAll('tr', class_=['Equity', 'Currency', 'Interest', 'Commodity', 'Mutual'])


    for i in range(len(Volume)):
        volume = Volume[i].findAll('td')[1].text.strip().replace(",","")

        value = Value[i].findAll('td')[2].text.strip().replace(",","")

        oe = Open_interest[i].findAll('td')[3].text.strip().replace(",","")
        
        ua = Updated_at[i].findAll('td')[4].text.strip().replace(",","")

        data.append({
            'Product': product_list[i] if i < len(product_list) else "N/A",
            'Volume': volume,
            'Value': value,
            'Open Interest': oe,
            'Updated At': ua
        })
    
    with open('stock_data.csv','w') as file:
        file.write('Products,Volume,Value,Open Interest,Updated At\n')

        for item in data:
            file.write(f"{item['Product']},{item['Volume']},{item['Value']},{item['Open Interest']},{item['Updated At']}\n")

DataScraping()


