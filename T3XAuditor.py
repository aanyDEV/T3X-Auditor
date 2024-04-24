from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests  
import pandas as pd
import sys
from termcolor import colored
from datetime import datetime
import threading
import telnetlib
import re 
import os

def Tektektek():
    dcuser = ""
    dcpasswd = ""
    whmuser = ""
    dcurl = "https://dcim.domain.com/dcim/device-types/"
    whmpasswd = ""
    whmlokasi = "scripts7/clusterstatus"
    zcemail = ""
    zcpasswd = ""
    zcurl = "https://zoneadmin.domain.com/"
    dauser = ""
    dapasswd = ""
    vluser = ""
    vlpasswd = ""
    rocore = ""
    rocore2 = ""
    rocorehost = ""
    mktikuser = ""
    mktikpsswd = ""
    mktikport = ""
    sm1=""
    passm1=""
    sm2=""
    passm2=""
    bcrnlokasi = "cgi/acronisbackup/index.php"
    bcjetbackup = "cgi/addons/jetbackup/index.cgi#!/backupManager"
    litespeedloc = "cgi/lsws/lsws.cgi"
    imunifyloc = "cgi/imunify/handlers/index.cgi#/360/admin/dashboard?timeframe=30d"
    patchman = "patchman.domain.com"
    patpage = "https://patchman.domain.com/hosts/"
    upm = ""
    listaccwhm = "scripts4/listaccts"
    passpm = ""
    patdashboard = "https://patchman.domain.com/dashboard/"
    pathost = "https://patchman.domain.com/hosts/"
    tanggal = datetime.now()
    

    def pm():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver,options=options)
        driver.get(url1)
        time.sleep(1)
        saiki = driver.current_url
        halaman = driver.page_source
        madakno = re.search(r"Please enter your username and password to login.",halaman)
        if (madakno != None and saiki == patdashboard) or (madakno != None and saiki == pathost):
            try:
                ngetik = driver.find_element(By.XPATH,'//a[normalize-space()=\'Hosts\']')
                ngetik.click()
                time.sleep(1)
                bb == driver.current_url
                halaman = driver.page_source
                nyekrop = BeautifulSoup(halaman, "html.parser")
                ul = nyekrop.find("ul", class_="pagination pagination-sm")
                lii = []
                if ul:
                    alla = ul.find_all("a")
                    for a in alla:
                        link = a.get("href")
                        lii.append(link)
                    a1 = driver.current_url
                    a2 = patpage+lii[2]
                    a3 = patpage+lii[3]
                    print(str(a1))
                    print(str(a2))
                    print(str(a3))
                    alamat = []
                    alamat.append(a1)
                    alamat.append(str(a2))
                    alamat.append(str(a3))
                    print(colored("---------Audit Patchman---------","cyan"))
                    uu = 1
                    for uwu in alamat:
                        try:
                            if uu <= len(alamat) + 1:
                                driver.get(uwu)
                                halaman = driver.page_source
                                nyekrop = BeautifulSoup(halaman, "html.parser")
                                awak = nyekrop.select_one('table > tbody')
                                target = awak.find_all("tr")
                                for row in target:
                                    td1 = row.select_one('td:nth-of-type(1)')
                                    td3 = row.select_one('td:nth-of-type(3)')
                                    val1 = td1.get_text()
                                    val2 = td3.get_text()
                                    if int(val2) >= 500:
                                        print("Hostname      : ", val1)
                                        print("Jumlah updates: ", val2)
                        except:
                            print(colored("---------------------","yellow"))
            except ValueError:
                pass
            
        else:
            try:
                ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/input[1]')
                ngetik.send_keys(upm)
                
                ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/input[2]')
                ngetik.send_keys(passpm)
                
                ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[2]/div/form/div/button')
                ngetik.click()
                time.sleep(1)
                bb = driver.current_url
                print(colored("---------Audit Patchman---------","cyan"))
                if url1 == bb and sc.status_code == 200:
                    print("Username dan password salah")
                elif url1 != bb and sc.status_code == 200:
                    try:
                        ngetik = driver.find_element(By.XPATH,'//a[normalize-space()=\'Hosts\']')
                        ngetik.click()
                        time.sleep(1)
                        bb == driver.current_url
                        halaman = driver.page_source
                        nyekrop = BeautifulSoup(halaman, "html.parser")
                        ul = nyekrop.find("ul", class_="pagination pagination-sm")
                        lii = []
                        if ul:
                            alla = ul.find_all("a")
                            for a in alla:
                                link = a.get("href")
                                lii.append(link)
                            # print(lii[2], lii[3])
                            a1 = driver.current_url
                            a2 = patpage+lii[2]
                            a3 = patpage+lii[3]
                            alamat = []
                            alamat.append(a1)
                            alamat.append(str(a2))
                            alamat.append(str(a3))
                            uu = 1
                            print(colored(f"----------Halaman ke {uu}----------","yellow"))
                            for uwu in alamat:
                                try:
                                    if uu <= len(alamat) + 1:
                                        driver.get(uwu)
                                        halaman = driver.page_source
                                        nyekrop = BeautifulSoup(halaman, "html.parser")
                                        awak = nyekrop.select_one('table > tbody')
                                        target = awak.find_all("tr")
                                        for row in target:
                                            td1 = row.select_one('td:nth-of-type(1)')
                                            td3 = row.select_one('td:nth-of-type(3)')
                                            val1 = td1.get_text()
                                            val2 = td3.get_text()
                                            if int(val2) >= 500:
                                                print("Hostname      : ", val1)
                                                print("Jumlah updates: ", val2)
                                except:
                                    uu += 1
                                    print(colored(f"----------Halaman ke {uu}----------","yellow"))
                    except ValueError:
                        pass
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
    
    def locdetect():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(2)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + bcrnlokasi
        time.sleep(1)
        driver.get(urlbaru)
        time.sleep(2)
        halaman = driver.page_source
        madakno = re.search(r"Animates the first entrance of the slideout's tab. Sometimes it will be",halaman)
        
        if madakno != None:
            print(colored(f"\nServer {subdomain} terletak di Jakarta\n","green"))
        else:
            print(colored(f"\nServer {subdomain} terletak di Surabaya\n","yellow"))
    
    def bcacrn():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(2)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + bcrnlokasi
        time.sleep(1)
        driver.get(urlbaru)
        time.sleep(2)
        halaman = driver.page_source
        madakno = re.search(r"Animates the first entrance of the slideout's tab. Sometimes it will be",halaman)
        
        if madakno != None:
            print(colored(f"\n{subdomain} ada backup acronis\n","green"))
        else:
            print(colored(f"\n{subdomain} tidak ada backup acronis\n","red"))

    def authSm(enum1,c):
        user = []
        user.append(sm1)
        user.append(sm2)
        passwd = []
        passwd.append(passm1)
        passwd.append(passm2)

        ai = 0
        for cred1, cred2 in zip(user,passwd):
            devSupermicro = pd.read_csv('devSupermicro.csv')
            lholho = devSupermicro.iloc[c].to_string(index=False)
            nama = lholho.split('\n')
            naaa = nama[0]
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument('--silent')
            options.add_argument('--log-level=3')
            options.set_capability('unhandledPromptBehavior', 'accept')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
            driver = webdriver.Chrome(chrome_driver, options=options)
            ai += 1
            print(colored(f"Tes Auth ke {ai}","cyan"))
            print("Target: ",naaa)
            print("IP    : ",nakniknuk)
            # print(enum1)
            try:
                driver.get(enum1)
                lapo = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[1]')
                lapo.send_keys(cred1)
                
                lapo = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[2]')
                lapo.send_keys(cred2)
                
                lapo = driver.find_element(By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/form/input[3]')
                lapo.click()
                time.sleep(3)
                anjay = driver.current_url
                time.sleep(1)
                sc = requests.get(enum1)
                if anjay == enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
                elif anjay != enum1 and sc.status_code == 200:
                    print(colored(f"Auth menggunakan akun {cred1} sukses\n", "green"))
                elif anjay == enum1 and sc.status_code != 200:
                    print(colored(f"Silahkan cek koneksi terlebih dahulu\n", "red"))
                else:
                    print(colored(f"Auth menggunakan akun {cred1} gagal\n", "red"))
            except requests.exceptions.ConnectionError:
                print(colored(f"Auth menggunakan akun {cred1} gagal", "red"))
            driver.quit()
    
    def lbacrn():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(2)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + bcrnlokasi
        time.sleep(1)
        driver.get(urlbaru)
        time.sleep(5)
        halaman = driver.page_source
        madakno = re.search(r"Animates the first entrance of the slideout's tab. Sometimes it will be",halaman)
        
        if madakno != None:
            ngetik = driver.find_element(By.XPATH, '//*[@id="analytics-close-button"]/i')
            ngetik.click()
            
            ngetik = driver.find_element(By.XPATH, '//*[@id="ab-last-backup-date"]/div[1]/span')
            a = ngetik.text
            
            lapo = driver.find_element(By.XPATH, '//*[@id="ab-last-backup-date"]/div[2]/span')
            b = lapo.text
            
            print(colored(f"\n{subdomain}:","green"))
            print(colored(f"Last Backup:{a}{b}\n","green"))
        else:
            print(colored(f"\n{subdomain} tidak ada backup acronis\n","red"))
    
    def litespeed():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(2)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + litespeedloc
        time.sleep(1)
        driver.get(urlbaru)
        time.sleep(5)
        halaman = driver.page_source
        # print(halaman)
        madakno = re.search(r"LiteSpeed Web Server - WHM Plugin",halaman)
        
        if madakno != None:
            ngetik = driver.find_element(By.XPATH, '//a[@title=\'Version Management: upgrade/downgrade/force reinstall.\']//span[@class=\'itemTextWrapper\']')
            a = ngetik.text
            print(colored(f"\n{subdomain}","green"))
            print(colored(f"LiteSpeed/{a} Enterprise\n","green"))
        else:
            print(colored(f"\n{subdomain} tidak ada LiteSpeed\n","red"))
    
    def bchosting():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(2)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + bcjetbackup
        time.sleep(1)
        driver.get(urlbaru)
        time.sleep(5)
        halaman = driver.page_source
        madakno = re.search(r"Animates the first entrance of the slideout's tab. Sometimes it will be",halaman)
        
        if madakno != None:
            ngetik = driver.find_element(By.XPATH, '//div[@class=\'ng-binding ng-scope\']')
            a = ngetik.text
            print(colored(f"\n{subdomain}","green"))
            print(colored(f"Last Backup: {a}\n","green"))
        else:
            print(colored(f"\n{subdomain} tidak ada backup hosting\n","red"))
    
    def cpanelver():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(3)
        gm = ngetik.count("/")
        if gm <= 4:
            mbuhwes = "#wrap > div.cp-layout-wrapper > header > cp-whm-header-stats-control"
            gakpaham = """
                const shadowRoot = document.querySelector(arguments[0]).shadowRoot;
                const emakemak = shadowRoot.querySelector("div > div.cpanel-whm-header-stats__cell4 > div.cpanel-whm-header-stats__cell_data > span > div > a");
                return emakemak.textContent;
            """

            teks = driver.execute_script(gakpaham, mbuhwes)
            print(colored(f"\n{subdomain}","green"))
            print(colored(f"{teks}\n","green"))
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
            urlbaru = urlterfilter + listaccwhm
            time.sleep(1)
            driver.get(urlbaru)
            mbuhwes = "#wrap > div.cp-layout-wrapper > header > cp-whm-header-stats-control"
            gakpaham = """"
                const shadowRoot = document.querySelector(arguments[0]).shadowRoot;
                const mbahmu = shadowRoot.querySelector("div > div.cpanel-whm-header-stats__cell4 > div.cpanel-whm-header-stats__cell_data > span > div > a");
                return mbahmu.textContent;
            """
            owalah = driver.execute_script(gakpaham, mbuhwes)
            print(f"\n{subdomain}","green")
            print(f"{owalah}\n","green")
    
    def cekmk():
        target = []
        target.append(rocore)
        target.append(rocore2)
        target.append(rocorehost)
        
        for bb in target:
            tess = os.system("ping " + bb)
            if tess == 0:
                print(f"\n{bb}")
                print(colored("Koneksi OK :*\n","green"))
            else:
                print(f"\n{bb}")
                print(colored("Koneksi Bermasalah\n","red"))
    
    def mk1():
        target = []
        target.append(rocore)
        target.append(rocore2)
        target.append(rocorehost)
        
        for aa in target:
            telnet = telnetlib.Telnet(aa,mktikport)
            
            try:
                telnet.read_until(b'Login: ')
                telnet.write(mktikuser.encode('ascii') + b'\n')
                telnet.read_until(b'Password: ')
                telnet.write(mktikpsswd.encode('ascii') + b'\n')
                cek = telnet.read_until(b'>')
                if b'>\r\n' in cek:
                    print(colored(f"Auth {aa} Sukses Boskuh :*\n","green"))
                else:
                    print(colored(f"Auth {aa} Gagal\n","red"))
            except:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))

    def dcim3():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(dcurl)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(dcuser)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(dcpasswd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        td2s = driver.find_elements(By.XPATH, '//td[2]')
        tttt = []
        td7s = driver.find_elements(By.XPATH, '//td[7]')
        ttt = []
        
        for t2 in td2s:
            macul2 = t2.find_element(By.TAG_NAME, 'a')
            auau = macul2.text
            tttt.append(auau)
        
        for t7 in td7s:
            macul = t7.find_element(By.TAG_NAME, 'a')
            link = macul.get_attribute('href')    
            ttt.append(link)
        
        b = 0
        for tek, tektek in zip(ttt, tttt):
            a = 0    
            print("\n\n",tektek)
            
            driver.get(tek)
            halaman = driver.page_source
            nyekrop = BeautifulSoup(halaman, "html.parser")
            awak = nyekrop.select_one('table > tbody')
            target = awak.find_all("tr")    
            
            for row in target:
                td1 = row.select_one('td:nth-of-type(2)')
                td2 = row.select_one('td:nth-of-type(3)')
                td7 = row.select_one('td:nth-of-type(11)')
                if td1 and td2 and td7:
                    a += 1
                    b += 1
                    val1 = td1.get_text()
                    val2 = td2.get_text()
                    val3 = td7.get_text()
                    teks1 = re.sub(r'\s{2,}',' ',val1)
                    teks2 = re.sub(r'\s{2,}',' ',val2)
                    print("====================")
                    print("Nama   :",teks1)
                    print("Status : ",teks2)
                    print("IP     : ",val3)
            print("====================")
            print(" Jumlah Instances:", a)
        print("\n/=================================================\\")
        print("| Total Keseluruhan Instances: ", b, "bossqueee :V")
        print("\=================================================/\n")
        
    def dcim2():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(dcurl)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(dcuser)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(dcpasswd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        halaman = driver.page_source
        nyekrop = BeautifulSoup(halaman, "html.parser")
        awak = nyekrop.select_one('table > tbody')
        target = awak.find_all("tr")
        
        for row in target:
            td1 = row.select_one('td:nth-of-type(2)')
            td2 = row.select_one('td:nth-of-type(3)')
            td7 = row.select_one('td:nth-of-type(7)')
            if td1 and td2 and td7:
                val1 = td1.get_text()
                val2 = td2.get_text()
                val3 = td7.get_text()
                print("Device Type: ", val1)
                print("Manufacture: ", val2)
                print("Instances  : ", val3)
        print("\n")
        
    
    def dcim1():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(dcurl)
        time.sleep(1)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[3]')
        lapo.send_keys(dcuser)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/input[4]')
        lapo.send_keys(dcpasswd)
        
        lapo = driver.find_element(By.XPATH,'/html/body/main/div/form/button')
        lapo.click()
        time.sleep(5)
        
        halaman = driver.page_source
        nyekrop = BeautifulSoup(halaman, "html.parser")
        target = nyekrop.find_all("span", class_='badge bg-secondary')
        for tulisan in target:
            print("\nJumlah Device-Type DCIM:",tulisan.text,"\n")
        
    def monitoring():
        a = 0
        try:
            while True:
                if a != 25:
                    serverwithAgent()
                    a += 1
                    # print(f"monitor ke {a}")
                    time.sleep(5)
                    print(tanggal)
                elif a == 25:
                    takon = str(input("Apakah anda ingin lanjut melakukan monitoring Y/N ?? "))
                    if takon == "Y" or takon == "y":
                        monitoring()
                    elif takon == "N" or takon == "n":
                        print("Terimakasih telah menggunakan aplikasi ini boskuh :V")
                        
                    else:
                        print(colored("Maaf inputan tidak jelas, program auto close ya :V","magenta"))
                        
        except Exception or KeyboardInterrupt:
            takon = str(input("Apakah anda ingin keluar dari monitoring Y/N ?? "))
            if takon == "Y" or takon == "y":
                print(colored("\nTerimakasih salam Tektektek :)\n","magenta"))

            elif takon == "N" or takon == "n":
                monitoring()
            else:
                print(colored("Maaf inputan tidak jelas, program auto close ya :V","magenta"))
                
    t = threading.Thread(target=monitoring)

    def nggoleki3():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div/div/div[2]/form/div[1]/input')
        ngetik.send_keys(vluser)

        ngetik = driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div/div/div[2]/form/div[2]/input')    
        ngetik.send_keys(vlpasswd)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/section/div/div[2]/div/div/div[2]/form/div[3]/input')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(1)

        sc = requests.get(ngetik)
        if sc.status_code == 200 :
            print(f"\n{subdomain}")
            print(colored("Auth Sukses Boskuh :*\n","green"))
        else:
            print(f"\n{subdomain}")
            print(colored("Auth Gagal\n","red"))

    def nggoleki2():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[2]/div[1]/input')
        ngetik.send_keys(dauser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[2]/div[2]/input')    
        ngetik.send_keys(dapasswd)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div[1]/div[2]/button')
        driver.execute_script("arguments[0].click();", ngetik)
        # ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(1)
        
        sc = requests.get(ngetik)
        if sc.status_code == 200 :
            print(f"\n{subdomain}")
            print(colored("Auth Sukses Boskuh :*\n","green"))
        else:
            print(f"\n{subdomain}")
            print(colored("Auth Gagal\n","red"))

    def nggoleki():    
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url6)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[2]/input')
        ngetik.send_keys(whmuser)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[4]/input')    
        ngetik.send_keys(whmpasswd)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[3]/div/div/div[2]/div[2]/form/div[5]/div/button')
        ngetik.click()
        time.sleep(1)

        ngetik = driver.current_url
        time.sleep(1)
        gm = ngetik.count("/")
        
        if gm <= 4:
            parseurl = urlparse(ngetik)
            urlterfilter = parseurl.scheme + "://" + parseurl.netloc + parseurl.path
        else:
            akhir_gm = ngetik.rindex("/")
            urlterfilter = ngetik[:akhir_gm - 8]
        urlbaru = urlterfilter + whmlokasi
        time.sleep(1)
        driver.get(urlbaru)
        sc = requests.get(urlbaru)
        if sc.status_code == 200 :
            print(f"\n{subdomain}")
            print(colored("Auth Sukses Boskuh :*\n","green"))
        else:
            print(f"\n{subdomain}")
            print(colored("Auth Gagal\n","red"))

    def serverwithAgent():    
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url1)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/input')
        ngetik.send_keys(zcemail)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/input')    
        ngetik.send_keys(zcpasswd)
        
        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/button')
        ngetik.click()
        time.sleep(1)
        print("\n")

        halaman = driver.page_source
        soup = BeautifulSoup(halaman, "html.parser")
        tdbody = soup.select_one('table > tbody')
        if tdbody:
            target = tdbody.find_all("tr")
            print("================================================\n")
            for row in target:
                td1 = row.select_one('td:nth-of-type(1)')
                td2 = row.select_one('td:nth-of-type(2)')
                
                if td1 and td2 :
                    val1 = td1.get_text()
                    val2 = td2.get_text()
                    print("Nama Server = ", val1)
                    print("Last Seen   = ", val2, "\n")

    def  ngeceksuimpel():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--silent')
        options.add_argument('--log-level=3')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_driver = "C:\chromedriver_win32\chromedriver114-2.exe"
        driver = webdriver.Chrome(chrome_driver, options=options)
        driver.get(url1)
        time.sleep(1)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/input')
        ngetik.send_keys(zcemail)

        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/input')    
        ngetik.send_keys(zcpasswd)
        
        ngetik = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/button')
        ngetik.click()
        time.sleep(1)
        print("\n")

        ngetik = driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div/div/div[3]/div[2]/div[2]/div[2]')
        tulisan = ngetik.text
        if tulisan.find("No problems found") != -1:
            print(colored("Zcloud aman boskuh :*\n","green"))
        else:
            print(colored(f"Zcloud rodok goyang, satset {zcurl}","red"))
            
    # print(colored("\n / *******                ( t ) \\","magenta"))
    # print(colored(" \  | * t   */>    <\   ( t ( t /","magenta"))
    # print(colored(" *) t * |    \ t*   /      TtTt(*","magenta"))
    # print(colored("  \\===*===  T|\\\\","magenta").ljust(16),end='')
    # print(colored("98","green").ljust(11),end='')
    # print(colored("//|TtT  /TtTt/","magenta"),end='')
    # print(colored("\n/  |/=========\\\Tt//=========\|  \ ","magenta"))
    # print(colored(" \/=","magenta").ljust(16),end='') 
    # print(colored("Tektektek Auditor v3","green").ljust(32),end='')
    # print(colored("=\/","magenta"),end='')
    # print(colored("\n  /\\\========================//\\","magenta"))
    # print(colored("  \         /        \         /","magenta"))
    # print(colored("            \        /\n","magenta"))
    print(colored("\n    ___  _____  ___    ___","magenta"))
    print(colored("   /  / /___  \ \  \  /  /","magenta"))
    print(colored("  /  /__  __|  | \  \/  /","magenta").ljust(15),end='')
    print(colored(" /\\\\","green"))
    print(colored(" /  ___/ /__  <   >    <","magenta").ljust(15),end='')
    print(colored(" < o|==========o>>>","green"))
    print(colored("/  /__  ____|  | /  /\\  \\","magenta").ljust(15),end='')
    print(colored(" \\//","green"))
    print(colored("\\____/  \_____/ /__/  \\__\\","magenta"))
    print(colored(" <--------AUDITOR-------->\n","green"))
    if len(sys.argv) < 2:
        print("1. Tes Koneksi All Server Production")
        print("2. Tes Koneksi All Server Cpanel")
        print("3. Tes Koneksi All Server Directadmin")
        print("4. Tes Koneksi All Server Virtualizor")
        print("5. Tes WHM Auth")
        print("6. Tes Directadmin Auth")
        print("7. Tes Virtualizor Auth")
        print("8. Cek All Server Agent - Zcloud")
        print("9. Simple Cek Agent - Zcloud")
        print("10. Monitoring All Agent - Zcloud")
        print("11. Cek Jumlah Device Types - DCIM")
        print("12. Cek Semua Detail Device Types - DCIM")
        print("13. Cek Detail Setiap Instances - DCIM")
        print("14. Tes Koneksi All Mikrotik")
        print("15. Tes All Mikrotik Auth")
        print("16. Tes Auth SuperMicro - IPMI")
        print("17. Tes All Auth IPMI (onprogress)")
        print("18. Cek All Server Cpanel dengan backup Acronis")
        print("19. Cek Lokasi All Server Cpanel")
        print("20. Cek hostname update >= 500 - Patchman")
        print("21. Cek Last Backup Acronis All Server Cpanel")
        print("22. Cek Last Backup Hosting All Server Cpanel")
        print("23. Cek Versi Cpanel All Server Cpanel")
        print("24. Cek Versi Litespeed All Server Cpanel")
        print("Ketik help untuk bantuan")
        print("Ketik close untuk keluar")
        print("\nCara penggunaan: python3 tttTester.py [menu]")
        print("                 python3 tttTester.py 1\n")
        print(colored("Silahkan masukan inputan sesuai menu, program auto close ya.....\n","yellow"))
        
    elif str(sys.argv[1]) == "1":
        try:
            i=0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Cpanel ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":2087/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Cpanel Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
            
            i=0
            data2 = pd.read_csv('serverDirectAdmin.csv')
            diulang = data2.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Directadmin ke ",i+1)
                alamat = data2.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":2222/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Directadmin Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue

            i=0
            data = pd.read_csv('serverVirtualizor.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Virtualizor ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":4085/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Virtualizor Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "2":
        try:
            i=0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Cpanel ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":2087/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Cpanel Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "3":
        try:
            i=0
            data2 = pd.read_csv('serverDirectAdmin.csv')
            diulang = data2.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Directadmin ke ",i+1)
                alamat = data2.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":2222/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Directadmin Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "4":
        try:
            i=0
            data = pd.read_csv('serverVirtualizor.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Virtualizor ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":4085/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                print(f"\n{subdomain}")
                                print(colored("Server Virtualizor Jos :*\n","green"))
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
            
    elif str(sys.argv[1]) == "5":
        try:
            i = 0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Auth WHM All Server ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                nggoleki()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    nggoleki()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        nggoleki()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            nggoleki()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "6":
        try:
            i = 0
            data = pd.read_csv('serverDirectAdmin.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Auth Directadmin Server ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2222/"
                        url3 = "https://" + url + ":2222/"
                        url4 = "http://" + url + ":2222/evo/"
                        url5 = "https://" + url + ":2222/evo/"
                        subdomain = url.split('.')[0].upper()
                        
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                nggoleki2()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    nggoleki2()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        nggoleki2()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            nggoleki2()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    
    elif str(sys.argv[1]) == "7":
        try:
            i=0
            data = pd.read_csv('serverVirtualizor.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Tes Koneksi Server Virtualizor ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "https://" + url + ":4085/"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                nggoleki3()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "8":
        try:
            try:
                sc = requests.get(zcurl)
                if sc.status_code == 200 :
                    url1 = zcurl
                    serverwithAgent()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "9":
        try:
            try:
                sc = requests.get(zcurl)
                if sc.status_code == 200 :
                    url1 = zcurl
                    ngeceksuimpel()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "10":
        try:
            try:
                sc = requests.get(zcurl)
                if sc.status_code == 200 :
                    url1 = zcurl
                    t.start()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "11":
        try:
            try:
                sc = requests.get(dcurl)
                if sc.status_code == 200:
                    dcim1()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "12":
        try:
            try:
                sc = requests.get(dcurl)
                if sc.status_code == 200:
                    dcim2()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "13":
        try:
            try:
                sc = requests.get(dcurl)
                if sc.status_code == 200:
                    dcim3()
            except requests.exceptions.ConnectionError:
                print(colored("Request Gagal, cek jaringan dan vpn bosqueee :V \n","yellow"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "14":
        try:
            cekmk()
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "15":
        try:
            mk1()
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "help":
        print("1. Tes Koneksi All Server Production")
        print("2. Tes Koneksi All Server Cpanel")
        print("3. Tes Koneksi All Server Directadmin")
        print("4. Tes Koneksi All Server Virtualizor")
        print("5. Tes WHM Auth")
        print("6. Tes Directadmin Auth")
        print("7. Tes Virtualizor Auth")
        print("8. Cek All Server Agent - Zcloud")
        print("9. Simple Cek Agent - Zcloud")
        print("10. Monitoring All Agent - Zcloud")
        print("11. Cek Jumlah Device Types - DCIM")
        print("12. Cek Semua Detail Device Types - DCIM")
        print("13. Cek Detail Setiap Instances - DCIM")
        print("14. Tes Koneksi All Mikrotik")
        print("15. Tes All Mikrotik Auth")
        print("16. Tes Auth SuperMicro - IPMI")
        print("17. Tes All Auth IPMI (onprogress)")
        print("18. Cek All Server Cpanel dengan backup Acronis")
        print("19. Cek Lokasi All Server Cpanel")
        print("20. Cek hostname update >= 500 - Patchman")
        print("21. Cek Last Backup Acronis All Server Cpanel")
        print("22. Cek Last Backup Hosting All Server Cpanel")
        print("23. Cek Versi Cpanel All Server Cpanel")
        print("24. Cek Versi Litespeed All Server Cpanel")
        print("Ketik close untuk keluar")
        print("\nCara penggunaan: python3 tttTester.py [menu]")
        print("                 python3 tttTester.py 1\n")
        print(colored("Silahkan masukan inputan sesuai menu, program auto close ya.....\n","yellow"))
    elif str(sys.argv[1]) == "16":
        try:
            i=0
            ipSupermicro = pd.read_csv('ipSupermicro.csv')
            ipS = ipSupermicro.shape[0]
            for tektek in range(ipS):
                i += 1
                if i <= 68:
                    print(colored("\n------------------------------------------------------------------------------","magenta"))
                    print(colored(f"--------------------------------Tes Auth ke {i}--------------------------------","yellow"))
                    alamat = ipSupermicro.iloc[i]['target']
                    if pd.notnull(alamat):
                        tektek = alamat.split(',')
                        for url in tektek:
                            url = url.strip()
                            url2 = "http://" + url + "/"
                            url3 = "http://" + url + ":80"
                            nakniknuk = url
                            try:
                                sc = requests.get(url2)
                                if sc.status_code == 200 :
                                    enum = url2
                                    authSm(enum, i)
                                else:
                                    cek2 = url3
                                    sc = requests.get(cek2)
                                    if sc.status_code == 200 :
                                        enum = url3
                                        authSm(enum, i)
                            except requests.exceptions.ConnectionError:
                                print(f"\n{nakniknuk}")
                                print(colored("IP tidak bisa di kunjungi bosqiuu :V\n","red"))
                        continue
                else:
                    sys.exit()
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "18":
        try:
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("\nCek Lokasi Server ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                bcacrn()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    bcacrn()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        bcacrn()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            bcacrn()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
        
    elif str(sys.argv[1]) == "19":
        try:
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("\nCek Lokasi All Server cPanel ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                locdetect()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    locdetect()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        locdetect()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            locdetect()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
            
    elif str(sys.argv[1]) == "20":
        try:
            url1 = "https://"+patchman
            try:
                sc = requests.get(url1)
                if sc.status_code == 200:
                    pm()
            except requests.exceptions.ChunkedEncodingError:
                print(f"\n{subdomain}")
                print(colored("SERVER NONAKTIF\n","red"))
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
            
    elif str(sys.argv[1]) == "21":
        try:
            i = 0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Cek Last Backup Acronis ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                lbacrn()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    lbacrn()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        lbacrn()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            lbacrn()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "22":
        try:
            i = 0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Cek Last Backup Hosting ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                bchosting()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    bchosting()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        bchosting()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            bchosting()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "23":
        try:
            i = 0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Cek Versi Cpanel ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                cpanelver()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    cpanelver()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        cpanelver()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            cpanelver()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "24":
        try:
            i = 0
            data = pd.read_csv('serverCpanel.csv')
            diulang = data.shape[0]
            for i in range(diulang):
                print("Cek Versi LiteSpeed ke ",i+1)
                alamat = data.iloc[i]['target']
                if pd.notnull(alamat):
                    url_list = alamat.split(',')
                    for url in url_list:
                        url = url.strip()
                        url2 = "http://" + url + ":2087/"
                        url3 = "https://" + url + ":2087/"
                        url4 = "http://" + url + "/whm"
                        url5 = "https://" + url + "/whm"
                        subdomain = url.split('.')[0].upper()
                        try:
                            sc = requests.get(url2)
                            if sc.status_code == 200 :
                                url6 = url2
                                litespeed()
                            else:
                                cek2 = url3
                                sc = requests.get(cek2)
                                if sc.status_code == 200 :
                                    url6 = url3
                                    litespeed()
                                else:
                                    cek3 = url4
                                    sc = requests.get(cek3)
                                    if sc.status_code == 200 :
                                        url6 = url4
                                        litespeed()
                                    else:
                                        cek4 = url5
                                        sc = requests.get(cek4)
                                        if sc.status_code == 200 :
                                            url6 = url5
                                            litespeed()
                        except requests.exceptions.ConnectionError:
                            print(f"\n{subdomain}")
                            print(colored("SERVER NONAKTIF\n","red"))
                continue
        except KeyboardInterrupt:
            print(colored("Terimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    elif str(sys.argv[1]) == "close":
        print(colored("Terimakasih salam Tektektek :)\n","magenta"))
    else:
        print(colored("Silahkan masukan inputan dengan benar XD, program auto close ya.....\n","yellow"))

Tektektek()
