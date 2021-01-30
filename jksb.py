# encoding:UTF-8
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as wait


def Wechat(title, content):
    if 'api' in os.environ:
        api = 'https://sc.ftqq.com/'+os.environ['api']+'.send'
        data = {
            'text': title,
            'desp': content
        }
        requests.post(api, data=data)


class Log:
    def __init__(self):
        self.uid = os.environ['username']
        self.pwd = os.environ['password']
        self.loc = False
        if 'location' in os.environ:
            self.loc = os.environ['location'].split(',')

        option = webdriver.ChromeOptions()
        option.add_experimental_option(
            'mobileEmulation', {'deviceName': 'iPhone X'})
        option.add_argument('--disable-infobars')
        option.add_argument('--disable-extensions')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--no-sandbox')
        option.add_argument('--headless')

        self.wd = webdriver.Chrome(options=option)
        self.wd.set_window_size(600, 800)
        if self.loc:
            self.wd.execute_cdp_cmd("Page.setGeolocationOverride", {
                                    "latitude": int(self.loc[0]), "longitude": float(self.loc[1]), "accuracy": 1})

    def loginProcesser(self) -> bool:
        self.wd.get('http://jksb.zzu.edu.cn/')
        self.wd.switch_to.frame(0)
        wait(self.wd, 30).until(ec.presence_of_element_located(
            (By.NAME, 'uid'))).send_keys(self.uid)
        wait(self.wd, 10).until(ec.presence_of_element_located(
            (By.NAME, 'upw'))).send_keys(self.pwd)
        wait(self.wd, 10).until(
            ec.element_to_be_clickable((By.NAME, 'smbtn'))).submit()
        time.sleep(3)
        self.wd.switch_to.frame('zzj_top_6s')
        if '今日您已经填报过了' in self.wd.page_source:
            message = '{} 已经上报过了'.format(time.strftime(
                '%Y-%m-%d  %H : %M: %S', time.localtime(time.time() + 8*3600)))
            print(message)
            Wechat('上报过了', message)
            return True
        wait(self.wd, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,\'本人填报\')]"))).click()
        wait(self.wd, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,\'提交表格\')]"))).click()
        time.sleep(3)
        notis = self.wd.page_source
        if ('感谢' in notis) or ('已经填报' in notis):
            message = '{}打卡成功'.format(str(time.strftime(
                '%Y-%m-%d  %H : %M: %S', time.localtime(time.time() + 8*3600))))
            print(message)
            Wechat('打卡成功', message)
            return True
        return False

    def login(self):
        for i in range(3):
            try:
                result = self.loginProcesser()
                print(result)
                if result:
                    self.wd.quit()
                    return
                print('第{}次打卡失败'.format(i+1))
            except:
                print('第{}次打卡失败'.format(i+1))
                pass
        message = '{}打卡失败'.format(str(time.strftime(
            '%Y-%m-%d  %H : %M: %S', time.localtime(time.time() + 8*3600))))
        Wechat('打卡失败', message)
        return


if __name__ == '__main__':
    Log().login()
