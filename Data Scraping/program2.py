from bs4 import BeautifulSoup

def function1():
    # read the html data from the file
    with open('page.html', 'r') as file:
        data = file.read()

    # create the soup
    soup = BeautifulSoup(data, "html.parser")

    # find the div with class "daily-list-body"
    div = soup.find('div', {'class': 'daily-list-body'})

    # find the all a tags from the div
    a_tags = div.find_all('a')

    # create a list to store the data
    data = []

    # iterate over the list and process each a tag
    for a_tag in a_tags:
        # print(a_tag.text)

        # find the div for date 
        div_date = a_tag.find('div', {'class': 'date'})

        # find the paragraph for date
        date = div_date.find_all('p')[1].text
        
        # get the high temperature
        temp_high = a_tag.find('span', {'class': 'temp-hi'}).text
        temp_low = a_tag.find('span', {'class': 'temp-lo'}).text

        # get the precipitation
        precipitation = a_tag.find('div', {'class': 'precip'}).text.strip()
        # print(f"Date: {date}, High: {temp_high}, Low: {temp_low}, Precipitation: {precipitation}")

        # append the data to the list
        data.append({
            'date': date,
            'temp_high': temp_high,
            'temp_low': temp_low,
            'precipitation': precipitation
        })


    # save the data to a csv file
    with open('temperature_data.csv', 'w') as file:
        # write the header
        file.write('Date,High,Low,Precipitation\n')

        # write the data
        for item in data:
            file.write(f"{item['date']},{item['temp_high']},{item['temp_low']},{item['precipitation']}\n")

function1()