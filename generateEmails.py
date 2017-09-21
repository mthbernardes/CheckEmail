import sys

def mailFormat(name,domain):
    mails = list()
    mails.append("%s@%s" % (name[0],domain))
    for x in range(1,len(name)):
        mails.append("%s.%s@%s" % (name[0],name[x],domain))
        mails.append("%s%s@%s" % (name[0][0],name[x],domain))
    return mails

if len(sys.argv) < 3:
    print 'Usage:\n%s domain.com names.txt' % sys.argv[0]
    sys.exit(1)

domain = sys.argv[1]
for data in open(sys.argv[2]):
    name = data.strip().lower().split()
    mails = mailFormat(name,domain)
    if mails:
        for mail in mails:
            print mail
            open('emails.txt','a').write(mail+'\n')
