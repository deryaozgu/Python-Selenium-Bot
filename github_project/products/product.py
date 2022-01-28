from multiprocessing.spawn import _main
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
product_src_list=[]
browser = webdriver.Chrome("C:\Program Files\driver\chromedriver.exe")
def page_url(url):
    browser.get(url)
    time.sleep(1)
    return browser
def page_number(browser):
    button_text=browser.find_element_by_class_name("paginator__button-page-indicator").text
    page_number=int(button_text[3])
    return page_number
def pages(page_number,kiz_url):
    for i in range(1,page_number+1):
       browser.get(kiz_url+str(i))
       time.sleep(2)
       for i in range(1, 4):
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
       products = browser.find_elements_by_class_name("product-image__image")
       time.sleep(3)
       for product in products:
            src=product.get_attribute("src")
            if src is not None:
             product_src_list.append(product.get_attribute("src"))
            else:
                continue
       products.clear()
       time.sleep(3)
def txt(name):
 with open(name,"w",encoding="UTF-8") as file:
    for src in product_src_list:
      file.write(src + "\n")
    time.sleep(3)
 product_src_list.clear()
if __name__ == "__main__":
   browser.get("https://www.lcwaikiki.com/tr-TR/TR")
   time.sleep(2)
   browser.get("https://www.lcwaikiki.com/tr-TR/TR/lp/32-33-bebek")
   time.sleep(2)
   browser.maximize_window()
   k_url="https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-bebek/tulum-125-c234"
   kiz_url="https://www.lcwaikiki.com/tr-TR/TR/kategori/kiz-bebek/tulum-125-c234?PageIndex="
   kiz_txt="kiz_bebek.txt"
   browser=page_url(k_url)
   pagenumber=page_number(browser)
   pages(pagenumber,kiz_url)
   txt(kiz_txt)
   e_url="https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-bebek/tulum-125-c181"
   erkek_url="https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek-bebek/tulum-125-c181?PageIndex="
   erkek_txt="erkek_bebek.txt"
   browser=page_url(e_url)
   pagenumber=page_number(browser)
   pages(pagenumber,erkek_url)
   txt(erkek_txt)
   browser.close()