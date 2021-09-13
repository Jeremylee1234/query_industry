from qcc import Qcc

import consts
import utils
import json

def query_industry(industry:str):
  """
  查询企业行业主函数
  industry:行业
  """
  qcc = Qcc()
  detail_url = qcc.query_url(industry)
  if not detail_url:
    print('未成功获取到公司详情页链接,请检查公司名错误或其他错误')
    return ''
  else:
    industry = qcc.query_industry(detail_url)
    if industry != '':
      return utils.get_industry(industry)
    else:
      return ''
        
if __name__ == '__main__':
  query_industry('腾讯')
