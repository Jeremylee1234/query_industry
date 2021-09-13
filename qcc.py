#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lxml import etree

import requests
import consts
import utils


class Qcc(object):
  def __init__(self):
    self.err_times = 0
    self.session = utils.get_session()

  def query_url(self, company:str):
    """
    第一次请求,获取详情页链接
    company:企业名
    return:详情页url
    """
    if self.err_times >= 5:
      print('请求失败')
      return None
    payload = {
      'key': company
    }
    try:
      response = self.session.get('https://www.qcc.com/web/search',params=payload,allow_redirects=False)
      if response.status_code == 200:
        self.err_times = 0
        selector = etree.HTML(response.text)
        print(response.content)
        items = selector.xpath('//div[@class="app-search"]//table/tr//div[@class="maininfo"]/a[1]/@href')
        if len(items) >= 1:
          return items[0]
        else:
          print('未查询到此公司')
          return None
      elif response.status_code == 302:
        self.err_times += 1
        print('当前cookie已失效,尝试重新获取cookie')
        utils.update_cookie()
        self.session = utils.get_session()
        return self.query_url(company)
      else:
        self.err_times += 1
        return self.query_url(company)
    except Exception as e:
      print(f'出现异常{e},重试')
      self.err_times += 1
      return self.query_url(company)
  
  def query_industry(self,url:str):
    """
    请求详情页获取公司行业
    url:详情页链接
    return:一二三级行业对象
    """
    if self.err_times >= 5:
      print('请求失败')
      return ''
    response = self.session.get(url,allow_redirects=False)
    if response.status_code == 200:
      selector = etree.HTML(response.text)
      cells = selector.xpath('//section[@id="cominfo"]//table[@class="ntable"]//tr/td/text()')
      for index,cell in enumerate(cells):
        if '所属行业' in cell:
          return utils.clean(cells[index+1])
    elif response.status_code == 302:
      self.err_times += 1
      print('当前cookie已失效,尝试重新获取cookie')
      utils.update_cookie()
      self.session = utils.get_session()
      return self.query_industry(url)
    else:
      self.err_times += 1
      return self.query_industry(url)

if __name__ == '__main__':
  qcc = Qcc()

  qcc.query_industry('https://www.qcc.com/firm/f1c5372005e04ba99175d5fd3db7b8fc.html')

