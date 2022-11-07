protocols = {
    'connection_type': 'dynamic',  # static or dynamic
    'data_crawler': True,
    'link_crawler': False
}

""" Protocols and Xpath of The HTML/CSS elements to find By slenium"""

title_xpth = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1'
platform_xpth = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]'
rate_xpth = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/div/div/' \
            'div[2]/div[1]/span[1]'
year_xpth1 = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[1]/a'
year_xpth2 = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[2]/a'
body_xpth = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/p/span[2]'
genre_Cls = "ipc-chip__text"
awards_xpth = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[1]/div/ul/li/a[1]'
dir_xpath = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a/text()'
actr1_xpath = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div[1]/div[2]/a'
actr2_xpath = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div[2]/div[2]/a'
actr3_xpath = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/div[2]/div[2]/div[3]/div[2]/a'
comment_xpth = '//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[9]/div[2]/div[1]/div[3]/div/div'


Base_link = 'https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fr' \
            'egistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fide' \
            'ntifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGx' \
            'lIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A' \
            '%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2' \
            '.0&tag=imdbtag_reg-20'