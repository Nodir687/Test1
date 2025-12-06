from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

laptop_brand = []
laptop_model_name = []
laptop_screen_size = []
laptop_ram = []
laptop_storage = []
laptop_cpu_model = []
laptop_operating_system = []
laptop_price = []
laptop_rating = []
laptop_review_count = []
laptop_graphics_card_description = []


next_url = 'https://www.amazon.in/s?k=laptop'
driver.get(next_url)
for i in range(10):
    driver.get(next_url)
    try:
        next_url = driver.find_element(By.XPATH,
                                       "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-button-accessibility s-pagination-separator']")
        next_url = next_url.get_attribute('href')
    except:
        print("This is last page")
        break
    laptop_urls = driver.find_elements(By.XPATH,
                                    "//a[@class='a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal']")
    laptop_links = []
    for url in laptop_urls:
        link = url.get_attribute('href')
        laptop_links.append(link)
    print(f"Number of laptops : {len(laptop_links)}")

    for link in laptop_links:
        driver.get(link)
        try:
            brand = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-brand']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            brand = "No brand"
        print(f"Laptop brand: {brand}")
        laptop_brand.append(brand)

        try:
            rating = driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-popover']"
                                                     "/preceding-sibling::span").text
        except:
            rating = "No rating"
        print(f"Laptop rating: {rating}")
        laptop_rating.append(rating)

        try:
            price = driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']"
                                                     "//span/span[@class='a-price-whole']").text
        except:
            price = "No price"
        print(f"Laptop price: {price}")
        laptop_price.append(price)

        try:
            model_name = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-model_name']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            model_name = "No model name"
        print(f"Laptop model name: {model_name}")
        laptop_model_name.append(model_name)

        try:
            screen_size = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-display.size']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            screen_size = "No screen size"
        print(f"Laptop screen size: {screen_size}")
        laptop_screen_size.append(screen_size)

        try:
            ram = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-ram_memory.installed_size']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            ram = "No ram"
        print(f"Laptop ram: {ram}")
        laptop_ram.append(ram)

        try:
            storage = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-hard_disk.size']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            storage = "No storage"
        print(f"Laptop storage: {storage}")
        laptop_storage.append(storage)

        try:
            cpu_model = driver.find_element(By.XPATH,"//tr[@class='a-spacing-small po-cpu_model.family']"
                                                     "//td[@class='a-span9']"
                                                     "//span[@class='a-size-base po-break-word']").text
        except:
            cpu_model = "No cpu model"
        print(f"Laptop cpu model: {cpu_model}")
        laptop_cpu_model.append(cpu_model)

        try:
            operating_system = driver.find_element(By.XPATH,"//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains(text(),'Operating System')]/../td").text
        except:
            operating_system = "No operating system"
        print(f"Laptop operating system: {operating_system}")
        laptop_operating_system.append(operating_system)

        try:
            review_count = driver.find_element(By.XPATH,"//a[@id='acrCustomerReviewLink']"
                                                          "//span[@class='a-size-small']").text
        except:
            review_count = "No review count"
        print(f"Laptop review count: {review_count}")
        laptop_review_count.append(review_count)

        try:
            graphics_card_description = driver.find_element(By.XPATH,"//th[@class='a-color-secondary a-size-base prodDetSectionEntry'][contains(text(),'Graphics Card Description')]/../td").text

        except Exception:
            graphics_card_description = "No graphics card description"
        print(f"Laptop graphics card description: {graphics_card_description}")
        laptop_graphics_card_description.append(graphics_card_description)

        print('/' * 50)

df = pd.DataFrame(
    {
        'brand': laptop_brand,
        'model_name': laptop_model_name,
        'screen_size(inch)': laptop_screen_size,
        'ram': laptop_ram,
        'storage': laptop_storage,
        'cpu_model': laptop_cpu_model,
        'operating_system': laptop_operating_system,
        'price(₹)': laptop_price,
        'rating': laptop_rating,
        'review_count': laptop_review_count,
        'graphics_card_description': laptop_graphics_card_description,

    }
)
df.to_csv('amazon_laptops.csv')