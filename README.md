#checkEmail
Generate possible e-mails and test it.

#Install

```Bash
git clone
cd checkEmail
pip install dnspython
```

#Usage
To generate e-mails you need a file with names, like the example.

```Bash
bash-3.2$ cat names.txt
Silvio Santos
Serginho Malandro
Sidney Magal
Marcondes Falcao Maia
Francisco Everardo Oliveira Silva
```

Now just execute the generateEmails.py, like the example, you need to specify the domain and the file with names.

```Bash
bash-3.2$ python generateEmails.py soosloco.com.br names.txt
silvio@soosloco.com.br
silvio.santos@soosloco.com.br
ssantos@soosloco.com.br
serginho@soosloco.com.br
serginho.malandro@soosloco.com.br
smalandro@soosloco.com.br
sidney@soosloco.com.br
sidney.magal@soosloco.com.br
smagal@soosloco.com.br
marcondes@soosloco.com.br
marcondes.falcao@soosloco.com.br
mfalcao@soosloco.com.br
marcondes.maia@soosloco.com.br
mmaia@soosloco.com.br
francisco@soosloco.com.br
francisco.everardo@soosloco.com.br
feverardo@soosloco.com.br
francisco.oliveira@soosloco.com.br
foliveira@soosloco.com.br
francisco.silva@soosloco.com.br
fsilva@soosloco.com.br
```

The script will save a file named emails.txt, where all the possible e-mails are saved, now just run the checkEmail.py like the example, you need to specify the file with names.

```Bash
bash-3.2$ python checkEmail.py emails.txt
MX SERVER: mx.soosloco.com.br
EMAIL: silvio.santos@soosloco.com.br
NOT VALID

MX SERVER: mx.soosloco.com.br
EMAIL: silvio.santos@soosloco.com.br
NOT VALID

MX SERVER: mx.soosloco.com.br
EMAIL: ssantos@soosloco.com.br
EMAIL EXIST

....

MX SERVER: mx.soosloco.com.br
EMAIL: fsilva@soosloco.com.br
EMAIL EXIST
```

And then a file named validEmails.txt will be created, with all valid e-mails.
