class Website:
    def __init__(self,  company='company name',
                        url='company url',
                        login='login/username',
                        pw='password',
                        balance='not defined',
                        monthly='not defined'):
        self.company = company
        self.url = url
        self.login = login
        self.pw = pw
        self.balance = balance
        self.monthly = monthly

    @classmethod
    def get_company(cls):
        company = raw_input('Please Enter Company Name: ')
        return company

    @classmethod
    def get_url(cls):
        url = raw_input('Please Enter URL: ')
        return url

    @classmethod
    def get_login(cls):
        login = raw_input('Please Enter your LOGIN: ')
        return login

    @classmethod
    def get_pw(cls):
        pw = raw_input('Please Enter Your Password: ')
        return pw
