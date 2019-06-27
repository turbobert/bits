#!/bin/bash

H=t

email="email@address"
imapserver="[snmtpurl]:465"
dnsname="server.full.name"
shadowaccounts="www-data root"

### echo -en "Mail Password: "
### read PW
### 
### ssh $H 'apt-get install -y postfix'
### ssh $H 'mkdir -p /etc/postfix/sasl'
### ssh $H 'cat /dev/null >/etc/postfix/sasl/sasl_passwd'
### ssh $H 'chmod 600 /etc/postfix/sasl/sasl_passwd'
### ssh $H 'chown root: /etc/postfix/sasl/sasl_passwd'
### ssh $H "echo '$imapserver $email:$PW'>>/etc/postfix/sasl/sasl_passwd"
### ssh $H "postmap /etc/postfix/sasl/sasl_passwd"
### 
### ssh $H 'cat /dev/null >/etc/postfix/generic'
### for N in $shadowaccounts; do
###     ssh $H "echo '$N@$dnsname $email'>>/etc/postfix/generic"
### done
### ssh $H "postmap /etc/postfix/generic"

(
    cat <<EOF

# added by fix me up
smtp_sasl_auth_enable = yes
smtp_sasl_security_options = noanonymous
smtp_sasl_password_maps = hash:/etc/postfix/sasl/sasl_passwd
smtp_tls_security_level = encrypt
smtp_tls_wrappermode = yes
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
smtp_generic_maps = hash:/etc/postfix/generic
message_size_limit = 100000000
EOF
) | ssh $H 'cat >> /etc/postfix/main.cf'
