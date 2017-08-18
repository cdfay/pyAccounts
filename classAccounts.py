class Account(object):

    def __init__(self, company='company', url='url', login='login', pw='pw'):
        self.company = company
        self.url = url
        self.login = login
        self.pw = pw

    def get_company(self):
        if self.company == 'company':
            company = raw_input('Please Enter Account NAME: ')
            return company
        else:
            return self.company

    def get_url(self):
        if self.url == 'url':
            url = raw_input('Please Enter Account URL: ')
            return url
        else:
            return self.url

    def get_login(self):
        if self.login == 'login':
            login = raw_input('Please Enter Account LOGIN: ')
            return login
        else:
            return self.login

    def get_pw(self):
        if self.pw == 'pw':
            pw = raw_input('Please Enter Account PW: ')
            return pw
        else:
            return self.pw
