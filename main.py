import library


def main():
    recipients = ['timurka.t.r@gmail.com']
    mail_body = 'anonymous'
    mail_subject = "Я люблю свою маму, ії звати Дана"
    # attachment

    library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject,
    )


if __name__ == '__main__':
    main()
