import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I add four different products to my wish list')
def add_products(context):
    chrome_options1 = webdriver.ChromeOptions()
    chrome_options1.add_argument('--disable-extensions')
    chrome_options1.add_argument("--window-size=200,200")
    chrome_options1.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
    context.driver = webdriver.Chrome(chrome_options=chrome_options1,
                                      executable_path="C:\\Users\\User\\PycharmProjects\\codility_bdd_selenium\\Drivers\\chromedriver.exe")
    context.driver.delete_all_cookies()
    #context.driver.maximize_window()
    context.driver.get("https://testscriptdemo.com")
    # context.driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(1)

    #Search and add first product
    prod_1_in = context.driver.find_element(By.XPATH,
                                              '//*[@id="site-content"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/ul/li[2]/a[1]')
    prod_1_in.click()

    black_image_wish = context.driver.find_element(By.XPATH, '//*[@id="product-14"]/div[2]/div[2]/div/a/i')
    black_image_wish.click()
    time.sleep(1)

    # go to home
    click_home = context.driver.find_element(By.XPATH, '// *[ @ id = "menu-item-309"] / a')
    click_home.click()

    #Search and add second product
    prod_2_in = context.driver.find_element(By.XPATH,
                                            '//*[@id="site-content"]/div/div/div/div/section[4]/div/div/div/div/div/div/div/ul/li[3]/a[1]/h2')
    prod_2_in.click()

    prod_2_wish = context.driver.find_element(By.XPATH, '//*[@id="product-20"]/div[2]/div[2]/div/a/i')
    prod_2_wish.click()
    time.sleep(1)

    # go to sale
    sale_clk = context.driver.find_element(By.XPATH, '//*[@id="menu-item-306"]/a')
    sale_clk.click()

    #Search and add third product
    prod_3_clk = context.driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div/ul/li[1]/a[1]')
    prod_3_clk.click()

    prod_3_wish = context.driver.find_element(By.XPATH, '//*[@id="product-15"]/div[2]/div[2]/div/a/i')
    prod_3_wish.click()
    time.sleep(1)

    # go to sale
    sale_clk_2 = context.driver.find_element(By.XPATH, '//*[@id="menu-item-306"]/a')
    sale_clk_2.click()
    time.sleep(1)

    #Search and add fourth product
    prod_4_clk = context.driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div/ul/li[2]/a[1]/img')
    prod_4_clk.click()

    prod_4_wish = context.driver.find_element(By.XPATH, '//*[@id="product-22"]/div[2]/div[2]/div/a/i')
    prod_4_wish.click()
    time.sleep(1)


@when('I view my wishlist table')
def viewWishlist(context):
    context.driver.get("https://testscriptdemo.com")
    viewWishlist = context.driver.find_element(By.XPATH, '//*[@id="blog"]/div[3]/div[1]/div/div/div[3]/div[3]/a/i')
    viewWishlist.click()
    time.sleep(1)


@then('I find total four selected items in my Wishlist')
def examinewishlist(context):
    prod_nm = context.driver.find_elements(By.XPATH, '//table/tbody/tr')
    print("----------------------------------------------------------------------------------------------")
    print(len(prod_nm))
    print("----------------------------------------------------------------------------------------------")
    for x in prod_nm:
        print(x)
    print("----------------------------------------------------------------------------------------------")
    if len(prod_nm) == 2:
        raise Exception("Total is above four selected items")

@when('I search for lowest price product')
def lowest_price(context):
    low_price = context.driver.find_elements(By.XPATH, '//table/tbody/tr')
    for i in low_price:
        print(i.text)

@when('I am able to add the lowest price item to my cart')
def addLowestct(context):
    prod_final_crt = context.driver.find_element(By.XPATH, '// *[ @ id = "menu-item-306"] / a')
    prod_final_crt.click()
    time.sleep(2)

    prod_final_clk = context.driver.find_element(By.XPATH, '//*[@id="site-content"]/div/div/div/ul/li[2]/a[2]')
    prod_final_clk.click()
    time.sleep(2)

@then("I am able to verify the item in my cart")
def viewCart(context):
    prod_final_vw = context.driver.find_element(By.XPATH,
                                                '//*[@id="blog"]/div[3]/div[1]/div/div/div[3]/div[1]/div/div/a/i')
    prod_final_vw.click()
    time.sleep(5)