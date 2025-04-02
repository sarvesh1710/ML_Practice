from bs4 import BeautifulSoup

# install the bs4: pip3 install bs4

# html
# - language used to design the web pages
# - tag
#   - also known as element
#   - words enclosed in angular brackets
#   - types
#     - opening tag
#     - closing tag
#     - empty tag or self-closing tag
#     - root tag

data = """
<html>
    <body>
        <h1>this is my website</h1>
        <h2>this is h2 tag</h2>
        <h3>this is h3 tag</h3>

        <div class="daily-list">daily list</div>
        <div class="hourly-list">hourly list</div>
        <div class="sunrise-list">sunrise and sunset</div>
        <br />
    </body>
</html>
"""

def function1():
    # create a soup
    # html.parser: used to parse the html data
    # soup represents the html data/contents
    soup = BeautifulSoup(data, 'html.parser')
    print(soup)

# function1()


def function2():
    soup = BeautifulSoup(data, "html.parser")
    
    # find the h1 tag from the data
    h1 = soup.find('h1')
    print(h1)

    # get the information from the tag
    print(f"text = {h1.text}")

# function2()

def function3():
    soup = BeautifulSoup(data, "html.parser")

    # find the h1 contents
    print(f"h1 contents = {soup.find('h1').text}")

    # find the h2 contents
    print(f"h2 contents = {soup.find('h2').text}")

    # find the h3 contents
    print(f"h3 contents = {soup.find('h3').text}")

# function3()


def function4():
    soup = BeautifulSoup(data, "html.parser")

    # find the div with class name hourly-list
    div_hourly_list = soup.find('div', {'class': 'hourly-list'})
    print(f"hourly list contents = {div_hourly_list.text}")

    # find the div with class name daily-list
    div_daily_list = soup.find('div', {'class': 'daily-list'})
    print(f"daily list contents = {div_daily_list.text}")


function4()
