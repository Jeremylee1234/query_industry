#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from create_driver import Driver

import requests
import consts
import time
import json

def clean(string:str):
    if isinstance(string, str):
        bad_str = [' ','    ','\r','\n','\t','\\','\\r','\\n','\\t']
        for b in bad_str:
            string = string.replace(b, '')
        return ''.join(string.split())
    else:
        return string

def write_cookies(new_cookies:str):
  """
  更新文件中的cookies.json
  """
  cookies_path = './cookies.json'
  if isinstance(new_cookies, (dict, list)):
    new_cookies = json.dumps(new_cookies)
  if isinstance(new_cookies, str):
    with open(cookies_path,'w',encoding='utf-8') as f:
      f.write(new_cookies)
  return 

def formate_cookie():
  """解析selenium格式的cookie并添加到cookiesJar"""
  cookie_path = './cookies.json'
  domain = 'qcc.com'
  with open(cookie_path,'r',encoding='utf-8') as f:
    cookies = json.loads(f.read())
    manual_cookies = {}
    for cookie in cookies:
        if cookie.get('domain') == '.' + domain or cookie.get('domain') == 'www.' + domain  or cookie.get('domain') == '.www.' + domain :
            name = cookie.get('name')
            value = cookie.get('value')
            if name and value:
                manual_cookies[name] = value
            else:
                continue
        else:
            continue
    cookiesJar = requests.utils.cookiejar_from_dict(manual_cookies, cookiejar=None, overwrite=True)
    return cookiesJar

def update_cookie():
  driver = Driver('https://www.qcc.com').create_driver()
  cookies = driver.get_cookies()
  write_cookies(cookies)
  driver.quit()

def get_session():
  session = requests.session()
  session.headers = consts.headers
  session.cookies = formate_cookie()
  return session

def get_industry(industry:str):
  """
  根据行业名获取其全部上级行业
  return:dict
  """
  with open('./industry.json','r',encoding='utf-8') as f:
    datas = json.loads(f.read())
    for data in datas:
      if industry == data['name']:
        print(data)
        return data
      else:
        continue
    print('未查询到对应行业名')
    return {
      'name': industry,
      '一级行业': industry
    }

def get_proxy():
  """
  获取ip代理的函数,暂未用到
  return:(ip,proxy)
  """
  try:
    data = requests.get('http://api.kuainiaoip.com/index.php?fetch_type=share&pool_id=&qty=1&time=100&province=%E6%89%80%E6%9C%89&city=%E6%89%80%E6%9C%89&protocol=1&format=json&dt=1').json()
    ip = f'{data["data"][0]["ip"]}:{data["data"][0]["port"]}'
    proxy = { 'http': 'http://'+ip, 'https': 'http://'+ip }
    proxy_test = requests.get('https://www.baidu.com', proxies=proxy, timeout=10)

    if proxy_test.status_code ==200:
      print(ip, proxy)
      return ip, proxy
    else:
      print(proxy_test)
      time.sleep(1)
      return None
  except Exception as e:
    print(e)
    time.sleep(3)
    return None
