import requests



def weibo(cookie, custom, uid, flag):
    url = 'https://weibo.com/ajax/profile/info?'
    completeUrl = url + 'custom=' + custom if flag else url + 'uid=' + uid
    print(completeUrl)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
                      'Safari/537.36 Edg/111.0.1661.44 ',
        'cookie': cookie
    }
    response = requests.get(url=completeUrl, headers=headers)

    data = response.json()['data']
    user = data['user']
    # 微博名
    screen_name = user['screen_name']
    # 认证信息
    verified_reason = user['verified_reason']
    # 描述
    description = user['description']
    # 粉丝数
    followers_count = user['followers_count']
    # 关注数
    friends_count = user['friends_count']
    # 微博数
    statuses_count = user['statuses_count']

    # 保存到excel
    import pandas as pd
    import openpyxl

    df = pd.DataFrame(
        {'微博名': [screen_name], '认证信息': [verified_reason], '描述': [description], '粉丝数': [followers_count],
         '关注数': [friends_count], '微博数': [statuses_count]})
    df.to_excel('./target/output.xlsx', index=False)

    # 保存到json
    df.to_json('./target/output.json', orient='records', force_ascii=False)


def main():
    cookie = 'SINAGLOBAL=3755203434675.023.1646575649752;,login.sina.com.cn; XSRF-TOKEN=rKikJXNe0xvBg9CnqqI-Qy-d; login_sid_t=872975dbfd4d93d7e49664cc2856f4f9; cross_origin_proto=SSL; wb_view_log=1920*10801; _s_tentry=weibo.com; Apache=8912130923239.469.1680663980827; ULV=1680663980829:58:1:2:8912130923239.469.1680663980827:1680075391697; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5o2ZWiFMwNcgDRmhPpEMj35JpX5o275NHD95QNS0z0e0.ESo27Ws4DqcjTxc8jdsLJMJH4eoet; SSOLoginState=1680677285; SCF=AiqX7qMCq-C3vrGXMAxU-wtpvtf4gGZUbnTdJ9WBBVq5Z7-M8T96pIloqgmBIjD0T7splJ7GbMPv278Hz0RlyAI.; SUB=_2A25JKWn2DeRhGeFJ6VES-SzKyjyIHXVqX9w-rDV8PUNbmtAGLU7bkW9NfHefmp9Zwotvtwx3tqS2jIO4fQJGQlhm; ALF=1712213285; WBPSESS=Dt2hbAUaXfkVprjyrAZT_FkFxVU7RyIQqYwKlmTgFK5Cx_9KD2FWTVUYBj_gjnlm0vD16j9ZdHC33uGCdGptCamE5aZtlWYM1SOjFqBuk6sW-CFBetODEpfVEwKF3EWbMwEGP3-o7Op3BkzG2soDNqYr5hGYuII_W7IlI5xIHEOzOIfvvWMkWFa-Ug67nG37oaKKyBHwNOeATo8uai8LVw=='
    custom = '234045825'
    uid = '7590570074'
    flag = True

    weibo(cookie, custom, uid, flag)


if __name__ == '__main__':
    main()
