import sys
import time
import socket
import requests
import dns.resolver

class tools():
    def getMx(self,domain):
        mxServers = dns.resolver.query(domain, 'MX')[0].to_text().split(' ')[1]
        return mxServers

    def checkEmail(self,email,mxserver):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((mxserver,465))
        s.recv(1024)
        time.sleep(0.3)

        cmd = 'HELO domain.com\n'
        s.send(cmd)
        time.sleep(0.3)
        s.recv(1024)

        cmd = 'MAIL FROM: <testeemail@domain.com>\n'
        s.send(cmd)
        time.sleep(0.3)
        s.recv(1024)

        cmd = 'RCPT TO: <%s>\n' %  email
        s.send(cmd)
        time.sleep(0.3)
        result = s.recv(1024)
        return self.checkResult(result,email)

    def checkResult(self,result,email):
        if '250' in result:
            return True
        else:
            return False
