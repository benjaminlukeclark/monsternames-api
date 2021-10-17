from selenium import webdriver
from chromedriver_py import binary_path

def before_all(context):
    context.base_url = "http://localhost:5000"
    context.api_key = "helloworld"
    context.chrome_browser = webdriver.Chrome(executable_path=binary_path)
