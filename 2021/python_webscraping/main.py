# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv

import requests
import bs4


def get_url(start, end):
    # Use a breakpoint in the code line below to debug your script.
    url = (
        f"http://163.49.30.82/cgi-bin/DspWaterData.exe?KIND=7&"
        f"ID=309091289912040&BGNDATE={start}&ENDDATE={end}&KAWABOU=NO"
    )
    return url


def generate_parse_data(url):
    print(url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.content, "lxml")
    month_list = [
        item
        for item in soup.find_all("tr")
        if item.find("th") is not None and item.find("th").string.endswith("月")
    ]
    for month in month_list:
        yield [item.string for item in month.find_all("td")]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    begin_date = "20160101"
    end_date = "20161231"
    with open("test.csv", "w") as csv_file:
        data_writer = csv.writer(
            csv_file, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
        )
        for data in generate_parse_data(get_url(begin_date, end_date)):
            data_writer.writerow(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
