import sys
from utils import mailTool

if len(sys.argv) < 2:
    print 'Usage:\n%s emails.txt' % sys.argv[0]
    sys.exit(1)

mail = mailTool.tools()
for email in open(sys.argv[2]):
    domain = mail.split('@')[1]
    mxserver = mail.getMx(domain)
    print 'MX SERVER: %s' % mxserver
    print 'EMAIL: %s' % email
    exist = mail.checkEmail(email,mxserver)
    if exist:
        print 'EMAIL EXIST\n'
        open('validEmails.txt','a').write(email+'\n')
    else:
        print 'NOT VALID\n'
