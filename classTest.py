class Cfay:
    first_name = 'Chris'
    last_name = 'Fay'
    middle_name = ''

    def get_middle_name(self):
        middle_name = raw_input('What\'s your middle name:')
        return middle_name


test = Cfay()
test.middle_name = test.get_middle_name()
print test.first_name + ' ' + test.middle_name + ' ' + test.last_name

