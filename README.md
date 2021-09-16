# READMD
## 入口函数
main.py中的query_industry

## 主体流程
1. 输入title和intro字典到processing函数
2. 调用extract_company函数
3. 如果title或者intro中只有一个公司出现则直接添加company键值到原字典中
4. 如果有多个公司出现，则通过句子中的语义关系找到ARG0施事方并添加到原字典company键值中
5. 如果没有找到ARG0标签的组织,则添加root（动词，或者介词）前的组织名称到字典中
6. 如果没有公司出现，则添加None到company键值中
7. 调用query_industry函数输入字典中company键的值
8. 6. 创建对象qcc
9. 初始化requests.session
10. 根据公司名请求详情页url,过程中判断cookie是否仍可用
   1. 不可用:
      1. 创建selenium窗口,访问qcc.com,获取cookies,更新到./cookies.json
   2. 可用: 转4.
11. 返回详情页链接
12. 调用qcc.query_industry,请求详情页链接返回所显示行业名
13. 从行业数据中找到对应的行业,返回其全部每一级的行业
14. 添加query_industry的返回值到字典中industry键中

## Notes:
1. 尝试高频率请求仍未遇到封禁ip现象，均可正常请求，后续如发现非cookie错误、公司名错误下的无法请求问题，请回馈并添加请求代理到代码中
2. 所写流程为查询传入一个企业名查询其行业
3. **需要修改为全局变量的局部变量**：
   1. utils.py:get_industry:datas(读取文件industry.json解析为行业数据)
   2. main.py:qcc对象(涉及到初始化requests.session)
   3. 说明：
      1. **后续需求为每日查询次数约50-200次,为执行效率,建议将代码中的utils.get_industry函数(用以获取父行业)中的变量datas(读取存储于./industry.json中的行业数据)修改为全局变量以防止每次查询行业时都要加载一次该文件以提升效率**
      2. **因主函数(main.py:query_industry())中调用时创建对象qcc,创建对象qcc时需要初始化session,建议将qcc对象所存储的变量也修改该全局变量**
