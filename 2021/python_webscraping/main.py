# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    begin_date = "20160101"
    end_date = "20161231"
    url = (
        f"http://163.49.30.82/cgi-bin/DspWaterData.exe?KIND=7&"
        f"ID=309091289912040&BGNDATE={2}&ENDDATE={1}&KAWABOU=NO"
    )
    res = requests.get(url)
    print(f"Hi, {res}")  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
