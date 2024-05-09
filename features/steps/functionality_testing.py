import os
import logging
from datetime import datetime
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import json

base_url = 'https://demo-api.dealsdray.com/api/v1/mis/bulkOrdersValidation'

log_dir = os.path.join('logs', datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%H-%M-%S'))
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'test.log'), level=logging.INFO)

driver = None

@step('I am on the Dealsdray login page')
def open_login_page(context):
    global driver
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://demo.dealsdray.com/")
        logging.info("Opened Dealsdray login page")
    except Exception as e:
        logging.error(f"Failed to open Dealsdray login page: {str(e)}")
        raise

@step('I enter the username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    try:
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        logging.info("Entered username and password")
    except Exception as e:
        logging.error(f"Failed to enter username and password: {str(e)}")
        raise

@step('I click the "{WHICH_BUTTON}" button')
def click_login_button(context,WHICH_BUTTON):
    try:
        login_button = driver.find_element(By.XPATH, f"//button[contains(text(),'{WHICH_BUTTON}')]")
        login_button.click()
        time.sleep(5)
        logging.info(f'clicked the "{WHICH_BUTTON}" button')
    except Exception as e:
        logging.error(f'Failed to click "{WHICH_BUTTON}" button: {str(e)}')
        raise

@step('I click the "{text}" element')
def click_custom_span(context, text):
    click_span_by_text(driver, text)

def click_span_by_text(driver, text):
    try:
        span_element = driver.find_element(By.XPATH, f"//span[text()='{text}']")
        span_element.click()
        logging.info(f"Clicked span with text '{text}'")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Failed to click span with text '{text}': {str(e)}")
        raise

@step('I click the "{text}" link')
def click_custom_link(context, text):
    click_link_by_text(driver, text)

def click_link_by_text(driver, text):
    try:
        link_element = driver.find_element(By.XPATH, f"//a[contains(@href, '/mis/{text}')]")
        link_element.click()
        logging.info(f"Clicked link with text '{text}'")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Failed to click link with text '{text}': {str(e)}")
        raise

@step('I click the "Import" button to upload the "{file_path}" file')
def click_import_button(context, file_path):
    click_import_button_to_upload_file(driver, file_path)

def click_import_button_to_upload_file(driver, file_path):
    try:
        time.sleep(2)
        file_input = driver.find_element(By.XPATH, "//input[@type='file']")
        file_input.send_keys(file_path)
        logging.info(f"Uploaded file '{file_path}'")
        import_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Import')]")
        import_button.click()
        logging.info("Clicked the 'Import' button")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Failed to upload file '{file_path}' using 'Import' button: {str(e)}")
        raise

@step('check the response')
def check_the_response(context):
    try:
        context.payload = {"item":[{"created_at":1715173508771,"order_id":"404-0010045-6108360","delet_id":0,"order_date":"8/16/22","order_timestamp":"8/16/22 23:08","order_status":"DECLINED","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1893","old_item_details":"realme:c11","imei":"'861500044867056","gep_order":"FALSE","base_discount":"3700","vc_eligible":"FALSE","customer_declaration_physical_defect_present":"FALSE","delivery_fee":"0","exchange_facilitation_fee":"0","id":1},{"created_at":1715173508771,"order_id":"408-6840418-0712321","delet_id":1,"order_date":"8/16/22","order_timestamp":"8/16/22 13:48","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'865230046431794","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","gc_amount_redeemed":"2660","gc_redeem_time":"8/16/22 13:53","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"TRUE","customer_declaration_physical_defect_type":"bodyDamage","partner_price__no_defect":"3800","revised_partner_price":"2660","delivery_fee":"0","exchange_facilitation_fee":"0","id":2},{"created_at":1715173508771,"order_id":"402-0909506-0973953","delet_id":2,"order_date":"8/16/22","order_timestamp":"8/16/22 23:04","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'865230049314724","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","gc_amount_redeemed":"3800","gc_redeem_time":"8/16/22 23:09","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"3800","revised_partner_price":"3800","delivery_fee":"0","exchange_facilitation_fee":"0","id":3},{"created_at":1715173508771,"order_id":"171-0771026-4255557","delet_id":3,"order_date":"8/16/22","order_timestamp":"8/16/22 14:10","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'867702040666599","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","tracking_id":"'513383200696","gc_amount_redeemed":"3800","gc_redeem_time":"8/16/22 14:18","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"3800","revised_partner_price":"3800","delivery_fee":"0","exchange_facilitation_fee":"0","id":4},{"created_at":1715173508771,"order_id":"402-6825598-7150744","delet_id":4,"order_date":"8/16/22","order_timestamp":"8/16/22 14:57","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'861067049951871","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","tracking_id":"'513383432301","gc_amount_redeemed":"3800","gc_redeem_time":"8/16/22 14:59","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"3800","revised_partner_price":"3800","delivery_fee":"0","exchange_facilitation_fee":"0","id":5},{"created_at":1715173508771,"order_id":"171-7819599-4854751","delet_id":5,"order_date":"8/16/22","order_timestamp":"8/16/22 14:00","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1515","old_item_details":"realme:3 pro","imei":"'862162041928719","gep_order":"FALSE","base_discount":"4250","partner_purchase_price":"4250","gc_amount_redeemed":"4250","gc_redeem_time":"8/16/22 14:03","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"4250","revised_partner_price":"4250","delivery_fee":"0","exchange_facilitation_fee":"0","id":6},{"created_at":1715173508771,"order_id":"403-8067368-4803529","delet_id":6,"order_date":"8/16/22","order_timestamp":"8/16/22 11:22","order_status":"DECLINED","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'861261044297824","gep_order":"FALSE","base_discount":"3800","vc_eligible":"FALSE","customer_declaration_physical_defect_present":"FALSE","delivery_fee":"0","exchange_facilitation_fee":"0","id":7},{"created_at":1715173508771,"order_id":"406-6195575-8893939","delet_id":7,"order_date":"8/16/22","order_timestamp":"8/16/22 22:01","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'865179048677757","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","gc_amount_redeemed":"3800","gc_redeem_time":"8/16/22 22:04","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"3800","revised_partner_price":"3800","delivery_fee":"0","exchange_facilitation_fee":"0","id":8},{"created_at":1715173508771,"order_id":"404-3182917-6526706","delet_id":8,"order_date":"8/16/22","order_timestamp":"8/16/22 11:17","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1578","old_item_details":"xiaomi:redmi note 7s","imei":"'867702041523336","gep_order":"FALSE","base_discount":"3800","partner_purchase_price":"3800","gc_amount_redeemed":"3800","gc_redeem_time":"8/16/22 11:24","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"3800","revised_partner_price":"3800","delivery_fee":"0","exchange_facilitation_fee":"0","id":9},{"created_at":1715173508771,"order_id":"405-9343306-2377917","delet_id":9,"order_date":"8/16/22","order_timestamp":"8/16/22 13:31","order_status":"NEW","buyback_category":"Mobile","partner_id":"1613633867","partner_email":"connect@dealsdray.com","partner_shop":"Gurgaon_122016","item_id":"Mobile_1515","old_item_details":"realme:3 pro","imei":"'861488045942336","gep_order":"FALSE","base_discount":"4250","partner_purchase_price":"4250","tracking_id":"'513383235582","gc_amount_redeemed":"4250","gc_redeem_time":"8/16/22 13:32","vc_eligible":"TRUE","customer_declaration_physical_defect_present":"FALSE","partner_price__no_defect":"4250","revised_partner_price":"4250","delivery_fee":"0","exchange_facilitation_fee":"0","id":10}],"location":"Gurgaon_122016"}
        context.payload = json.dumps(context.payload)
        context.headers = {
            'Content-Type': 'application/json'
        }
        context.response = requests.post(base_url,headers=context.headers,data=context.payload).json().get("data",{})

        logging.info("These data has the errors: %s",context.response)
        for k,v in context.response.items():
            logging.info("%s -> %s", str(k), str(v))
    except Exception as e:
        logging.error("The post error: %s",str(e))

def after_all(context):
    global driver
    if driver is not None:
        time.sleep(2)
        driver.quit()
