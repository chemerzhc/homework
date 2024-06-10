import json
import requests
# csv模块（内置）
import csv
#创建csv初始文件
f = open('data.csv', mode='w', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
            '昵称',
            '点赞数',
            'IP属地',
            '评论',
])
csv_writer.writeheader()
#请求头
headers = {
      "Cookie":"ttwid=1%7CnOraEXB51qlw-sJ1wxrI5Z1KmfVmgDXHJPfDDl1qoLM%7C1696732232%7C320e3f68cc60fdee6d0d0b99457c37ae671be7405cc7af0fd83af7e5614421fd; _ga=GA1.1.952674870.1696732253; tt_webid=7287409391636121128; gfkadpd=24,6457; ttcid=c4e3879536db4420809677f46dd7887512; s_v_web_id=verify_lx7v7cks_7vuflmvj_53TP_4J7n_9hqn_FPVd7awq1tho; local_city_cache=%E5%AE%A3%E5%9F%8E; csrftoken=3c14e77db0d5b7020c6b3852cdbf4766; _S_DPR=1.25; _S_IPAD=0; _S_WIN_WH=950_752; tt_scid=3KPfYfJlpfltY8ya-5swfXj2OkmpPSMo2awlWps6J.uEL4Qqw0uZeh9xLFXestf.3e92; msToken=8cOzgdvmLql8JE7iWUJkWG5HfoNct9igyrFJfGkKWRzc_XyMOhnYZvAwFpOX1sku0S-5uEi7zRxl8wgI7irF6cUDK5LNz_NpprqgCUs=; _ga_QEHZPBE5HH=GS1.1.1718018747.4.1.1718019406.0.0.0"
      "User-Agent""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}
from string import Template
#发送请求
page = 0
for page in range(300,500):
    s = Template(
        'https://www.toutiao.com/article/v4/tab_comments/?aid=24&app_name=toutiao_web&offset=${page}&count=20&group_id=7367699784716796451&item_id=7367699784716796451&_signature=_02B4Z6wo00f01OdOBRAAAIDA0GrBTjUEv-znagGAAF-7DbOQ5d5qqjbPphpqUEsEO1ZcYPxyUnx-K6L6V0A35sGLfXf-dLeiSghSL6HhYUu0PlY093eLLEBC8jd1gNp8MbsCxPePvd0NBaCAaa')
    url = s.substitute(page=page)
    #print(url)
    response = requests.get(url=url,headers=headers)
    json_data = response.json()
    comment = json_data['data']
    #print(json_data['data'])
#for循环遍历
    for index in comment:
      message = index['comment']['text']     #评论
      like = index['comment']['digg_count']     #点赞
      name = index['comment']['user_name']      #昵称
      location = index['comment']['publish_loc_info']  #IP 属地

#创建字典
      dit = {
            '昵称': name,
            '点赞数': like,
            'IP属地': location,
            '评论': message
      }
      csv_writer.writerow(dit)
      #print(dit)






