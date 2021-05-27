from selenium import webdriver
from bs4 import BeautifulSoup
import time

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipeapi.settings")
import django
django.setup()
from recipe.serializers import RecipeSerializer

def find_ingredients():
    try:
        li = driver.find_element_by_css_selector('.lst_ingrd')
    except:
        return None
    ul = li.find_elements_by_tag_name('li')
    ret = list()
    for item in ul:
        d = dict()
        span = item.find_element_by_tag_name('span').text
        em = item.find_element_by_tag_name('em').text
        d['name'] = span
        d['amount'] = em
        ret.append(d)
    return ret

max_page = 201
for page_num in range(1, max_page):
    print(page_num)
    url = 'https://haemukja.com/recipes?category_group2%5B%5D=60&cooking_time=&difficulty=&healthy=&name=&page={}&sort='.format(page_num)
    driver = webdriver.Chrome('C:/Users/jyang/chromedriver/chromedriver.exe')
    driver.get(url)

    link_list = []
    title_list = []

    elements = driver.find_elements_by_xpath("//a[@class='call_recipe']")
    for el in elements:
        link = el.get_attribute('href')
        link_list.append(link)

    elements = driver.find_elements_by_xpath("//a[@class='call_recipe']//strong")
    for el in elements:
        title = el.text
        title_list.append(title)

    for i in range(len(link_list)):
        script = 'window.open(\'%s\');' % link_list[i]
        driver.execute_script(script)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)

        ing_data = find_ingredients()
        if ing_data is None:
            continue
        
        data = {
            "name": title_list[i],
            "ingredients": ing_data,
            "image": None
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        
        driver.close()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[0])

    driver.close()