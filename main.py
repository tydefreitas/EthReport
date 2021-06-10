import os
import subprocess 
from subprocess import Popen
from selenium import webdriver
import selenium
from datetime import datetime
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3

connection = sqlite3.connect('eth_tracking.db')

driver = webdriver.Chrome()
driver.get('https://ethermine.org/miners/4dc05FCD625552d9Bc396ac9F0BD8923f13E0d8C/payouts')
wait = WebDriverWait(driver, 10)

maxProfit = 0

filename = 'payouts.csv'
f = open(filename, 'a')

today = datetime.now()

date = today.strftime("%m/%d/%Y")

###sql stuff hopefully###
cursor = connection.cursor()

# create stores table

command1 = """CREATE TABLE IF NOT EXISTS
track(track_id TEXT PRIMARY KEY, payouts TEXT, total_eth INTEGER, till_one_eth INTEGER, eth_price INTEGER, profit_usd INTEGER, profit_cad INTEGER)"""

cursor.execute(command1)

###sql stuff hopefully###

headers = 'Date: {} \n'.format(today)
"""
f.write(headers)

try:
    for x in range(1,100):
        date = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/main/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{}]/td[1]".format(x)))).text
        profit = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/main/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/table/tbody/tr[{}]/td[5]".format(x)))).text
        f.write(date + ',' + profit + '\n')
        maxProfit = maxProfit + float(profit)
except selenium.common.exceptions.TimeoutException:

    driver.get('https://www.coindesk.com/price/ethereum')
    wait = WebDriverWait(driver, 10)

    ethPrice = driver.find_element_by_xpath('.//*[@id="export-chart-element"]/div/section/div[1]/div[1]/div[2]/div').text

    driver.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=CAD')
    wait = WebDriverWait(driver, 10)

    cad = driver.find_element_by_xpath('.//*[@id="__next"]/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[2]').text

    cadA = float(cad.replace(' Canadian Dollars', ''))

    ethPriceA = ethPrice.replace(',', '')
    ethPriceB = ethPriceA.replace('$', '')
    
    usd = float(ethPriceB) * maxProfit
    usdA = int(usd)
    cadB = usd * cadA
    cadC = '$' + str(int(cadB))
    usdB = '$' + str(usdA)
    oneETH = 1 - maxProfit

    f.write("Total: " + str(("%.5f" % maxProfit))  +'\n')
    f.write("Till one ETH: " + str(oneETH) +'\n')
    f.write("Eth Price USD: " + ethPrice +'\n')
    f.write("USD: " + usdB +'\n')
    f.write("CAD: " + cadC +'\n')
    f.write(' '+ '\n')
    f.write(' '+ '\n')
    f.close()
    """
cursor.execute("INSERT INTO track VALUES (" + date + ", '31. May 2021 10:43,0.01112, 22. May 2021 19:32,0.01855, 08. May 2021 19:22,0.01322, 24. Apr. 2021 19:11,0.01527, 10. Apr. 2021 15:18,0.02196, 25. Mar. 2021 07:58,0.02554, 11. Mar. 2021 06:16,0.02107', 0.12673, 0.87327, 2571.32, 325, 394)")

cursor.execute("SELECT * FROM track")

results = cursor.fetchall()
print(results)  

driver.quit()
