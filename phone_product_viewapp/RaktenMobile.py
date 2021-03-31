import ui
import appex

import urllib.request
import webbrowser

from bs4 import BeautifulSoup


# Rakten Mobile (AQUOUS)
URL = 'https://network.mobile.rakuten.co.jp/product/smartphone/aquos-sense4-lite/'
# Rakten Mobile (OPPO)
#URL = 'https://network.mobile.rakuten.co.jp/product/smartphone/a73/'

class getProductInfo(ui.View):

    def getProductStatus(self):

        link, status, product = '', '', ''

        html = urllib.request.urlopen(URL)
        soup = BeautifulSoup(html, 'html.parser')
        product_status_wait = soup.find('a', class_='c-Btn_Primary').attrs

        product = soup.title.string.split('|')[0]

        if 'aria-disabled' in product_status_wait:
            link = soup.find('a', class_='c-Btn_Primary')['href']
            status = soup.find('a', class_='c-Btn_Primary').get_text(strip=True)
            # print('製品名: {0}  Status:{1}'.format(product, status))
        else:
            link = soup.find('a', class_='c-Btn_Primary js-Modal')['href']
            status = soup.find('a', class_='c-Btn_Primary js-Modal').get_text(strip=True)
            # print('製品名: {0}  Status:{1}'.format(product, status))
        
        return product, status, link

    def __init__(self):
        
        self.product, self.status, self.link = self.getProductStatus()
        self.productText = self.product + ' : ' + self.status
        self.statusText = '販売状況:' + self.status
        self.content = ui.Label()
        # self.content_status = ui.Label()
        self.btn = ui.Button(title=' RaktenMobile製品ページへ', name=URL, action=self.button_action, bg_color='#73c239', tint_color='#fff', corner_radius=7, font=('Arial Hebrew',15))
        self.bounds = (0, 0, 300, 100)
        self.add_subview(self.content)
        self.add_subview(self.btn)

    def button_action(self, sender):
        webbrowser.open(sender.name)


    def layout(self):
        self.bounds = (0, 0, 300, 150)
        self.content.font = ('Arial Hebrew', 18)
        self.content.text = self.productText
        self.content.bounds = (0, 0, 300, 90)
        self.content.center = (150, 45)
        self.btn.bounds = (0, 0, 300, 45)
        self.btn.center = (150, 100)
        

if __name__ == '__main__':
    
    appex.set_widget_view(getProductInfo())

