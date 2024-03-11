import smtplib
import email.message

def enviar_email():
    corpo_email = """
    
    """

    # Lista de destinatários
    destinatarios = []

    # Lista para armazenar os e-mails que não foram enviados
    emails_nao_enviados = []

    # Configuração das credenciais
    remetente_email = ''
    password = ''

    # Iterar sobre a lista de destinatários e enviar e-mails para cada um
    for destinatario in destinatarios:
        # Criar uma mensagem de e-mail
        msg = email.message.Message()
        msg['Subject'] = " "
        msg['From'] = remetente_email
        msg['To'] = destinatario
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(corpo_email)

        try:
            # Conectar-se ao servidor SMTP do Gmail
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()  # Iniciar TLS (Transport Layer Security) para criptografar a comunicação

            # Efetuar login com as credenciais
            s.login(msg['From'], password)

            # Enviar o e-mail
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print(f'E-mail enviado para {destinatario}')

            # Fechar a conexão com o servidor SMTP
            s.quit()
        except Exception as e:
            print(f"Erro ao enviar e-mail para {destinatario}: {str(e)}")
            emails_nao_enviados.append(destinatario)

    # Exibir a lista de e-mails que não foram enviados
    print("E-mails não enviados:", emails_nao_enviados)