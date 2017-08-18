from classAccounts import Account
from selenium import webdriver
import constantAccounts


bofa = Account('BOFA', 'https://bankofamerica.com')
#bofa = Account()
#bofa.company = bofa.get_company()
#bofa.url = bofa.get_url()
#bofa.login = bofa.get_login()
#bofa.pw = bofa.get_pw()

#print 'Company = ' + bofa.company
#print 'URL = ' + bofa.url
#print 'Login = ' + bofa.login
#print 'PW = ' + bofa.pw

wf = Account('Wells Fargo', 'https://wellsfargo.com')
wf.company = wf.get_company()
wf.url = wf.get_url()
wf.login = wf.get_login()
wf.pw = wf.get_pw()

print 'Company = ' + wf.company
print 'URL = ' + wf.url
print 'Login = ' + wf.login
print 'PW = ' + wf.pw

wfdriver = webdriver.Chrome()
wfdriver.get(wf.url)
wfdriver.maximize_window()

wfdriver.find_element_by_name(constantAccounts.con_wf_login).click()
wfdriver.find_element_by_name(constantAccounts.con_wf_login).send_keys(wf.login)

wfdriver.find_element_by_name(constantAccounts.con_wf_pw).click()
wfdriver.find_element_by_name(constantAccounts.con_wf_pw).send_keys(wf.pw)

wfdriver.find_element_by_name(constantAccounts.con_wf_sign_in_btn).click()


#bofadriver = webdriver.Chrome()
#bofadriver.get(bofa.url)
#bofadriver.maximize_window()

#bofadriver.find_element_by_id(constantAccounts.con_bofa_login).click()
#bofadriver.find_element_by_id(constantAccounts.con_bofa_login).send_keys(bofa.login)

#bofadriver.find_element_by_id(constantAccounts.con_bofa_pw).click()
#bofadriver.find_element_by_id(constantAccounts.con_bofa_pw).send_keys(bofa.pw)

#bofadriver.find_element_by_id(constantAccounts.con_bofa_sign_in_btn).click()
