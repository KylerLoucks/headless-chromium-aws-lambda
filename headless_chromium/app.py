import boto3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lambda_handler(event, context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=1280x1696")
    options.binary_location = '/opt/headless-chromium'
    driver = webdriver.Chrome('/opt/chromedriver', chrome_options=options)
    
    
    driver.get("https://www.google.com/")
    driver.save_screenshot("/tmp/canvas.png")
    print("saved screenshot")
    print("saving screenshot to S3 bucket")
    s3 = boto3.client('s3', region_name="us-east-1")
    s3.upload_file('/tmp/canvas.png', 'sam-headless-chromium', 'canvas.png')
    print("file uploaded successfully!")
    
    response = {
        "statusCode": 200,
        "body": "Selenium Headless Chrome Initialized"
    }
    
    return response



