class ContactInfo:
    def __init__(self,name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name,self.email))

if __name__ == '__main__':
    mingyu = ContactInfo('이민규','mingyu@naver.com') 
    hanbit = ContactInfo('hanbit','noreply@co.kr')

    mingyu.print_info()
    hanbit.print_info()

#self는 java의 this랑 같은 것임