#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from del_js import get_js_code
import time

class Driver(object):
  
  def __init__(self, site):
    self.site = site
  
  def create_driver(self,cookies=None):
    prefs = {
      'profile.default_content_setting_values': {
          'images': 2,
          'stylesheet': 2       #2即为禁用的意思
      },
      "webrtc.ip_handling_policy": "disable_non_proxied_udp",
      "webrtc.multiple_routes_enabled": False,
      "webrtc.nonproxied_udp_enabled": False
    }
    ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=OFF")  #修改debug信息等级
    options.add_argument('disable-infobars')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-extensions")
    options.add_argument("--dns-prefetch-disable")
    options.add_argument(f'user-agent={ ua }')
    options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    # options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": get_js_code()})
    driver.set_page_load_timeout(45)
    try:
      driver.get(self.site)
      time.sleep(1)
      if cookies:
        for c in cookies:
          try:
            driver.add_cookie(c)
          except Exception as e:
            print(e)
            print(c)
      return driver
    except TimeoutException:
      print('timeout to load site page')
      driver.quit()
      return self.create_driver(cookies)
    except Exception as e:
      print(e)
      driver.quit()
      return 

if __name__ == '__main__':
  pass
