import smtplib
import dns.resolver

def existeEmail(email):
    domain = email.split('@')[1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange
        mx_record = str(mx_record)
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo('localhost')  # Nombre de la máquina local
        server.mail('margaretgarner959@yahoo.com')  # Dirección de correo del remitente
        code, message = server.rcpt(email)
        server.quit()
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        return False

emails = [
    'ipms.oficial@gmail.com',
    'ipms.oficial.costarica@gmail.com',
    'ipms.oficial.cr@gmail.com',
    'oficial.ipms@gmail.com',
    'oficial.ipms.costarica@gmail.com',
    'oficial.ipms.cr@gmail.com',
    'oficial.costarica.ipms@gmail.com',
    'oficial.cr.ipms@gmail.com',
    'costarica.ipms@gmail.com',
    'costarica.oficial.ipms@gmail.com',
    'cr.oficial.ipms@gmail.com',
    'ipms.oficial@outlook.com',
    'ipms.oficial.costarica@outlook.com',
    'ipms.oficial.cr@outlook.com',
    'oficial.ipms@outlook.com',
    'oficial.ipms.costarica@outlook.com',
    'oficial.ipms.cr@outlook.com',
    'oficial.costarica.ipms@outlook.com',
    'oficial.cr.ipms@outlook.com',
    'costarica.ipms@outlook.com',
    'costarica.oficial.ipms@outlook.com',
    'cr.oficial.ipms@outlook.com',
]

for email in emails:
    if existeEmail(email):
        print(f'{email} ya existe.')
    else:
        print(f'{email} está disponible.')
