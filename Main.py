from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from Data.jepStoreData import jepStoreData
from Test.jepStoreTest import JPetStoreTest

driver = webdriver.Chrome()
wdw = WebDriverWait(driver,5)
test=JPetStoreTest(driver,wdw)
print("Start with testData:")
""" אופציה שנייה:"""
"""רשימת מקרי בדיקה לפי לולאה של אובייקטים ברשימה ולא בSET כי ככה זה לפי הסדר"""
testData=[
    jepStoreData("wrongUser", "bahalul123", "failed", False),
    jepStoreData("bahalultamir", "wrongPass", "success", False),
    jepStoreData("avidan12", "avidan23", "failed", False),
    jepStoreData("bahalultamir", "bahalul123", "success", False),
    jepStoreData("idan", "idan12", "failed", True),
    jepStoreData("yair", "yair89", "failed", False),
    jepStoreData("moshe77", "moshe10", "failed", False),
    jepStoreData("tamir", "bahalul10", "success", False)
]
for data in testData:
    test.script(data.username,data.password,data.expected, data.beforeLogin)


print("I finished running loop script with List")

driver.quit()