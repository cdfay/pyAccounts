from classWebsites import Website

bofa = Website()

if bofa.company == 'company name':
    bofa.company = bofa.get_company()
if bofa.url == 'company url':
    bofa.url = bofa.get_company()
bofa.pw = bofa.get_pw()


print type(Website)
print bofa.company
print bofa.url
print bofa.login
print bofa.pw

#bank_of_america.pw = 'cfay123'
#print bank_of_america.pw
