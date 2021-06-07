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

driver = webdriver.Chrome()
driver.get('https://ethermine.org/miners/4dc05FCD625552d9Bc396ac9F0BD8923f13E0d8C/payouts')
wait = WebDriverWait(driver, 10)

maxProfit = 0

filename = 'payouts.csv'
f = open(filename, 'a')

today = datetime.now()

#weeeeeeee

headers = 'Date: {} \n'.format(today)

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

    driver.quit()