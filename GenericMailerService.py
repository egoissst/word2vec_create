#!/usr/bin/env python
# coding: utf-8

import requests

GENERIC_MAILER_BASE_URL = "http://cmsgenericmailer.indiatimes.com/MailServiceWeb/messages/sendMail"

# senderEmail = "mailerservice@timesofindia.com"
# to = "yash.dalmia@timesinternet.in";
# subject = "hll";
# body = "aksldfjlsjdfklsdfjsdkflsdjf ksdfjlsdjflsd flksdjf dskfj lsdjfk sldf jkl ";


class MailerObject:
    """
    Generic mailer object to store the fields to be sent in the parameters when hitting generic mailer service
    """

    def __init__(self, recipient_mail, sender_mail, subject, mail_body, cc_mail_list=None, bbc_mail_list=None,
                 sender_name=None):
        self.recp = recipient_mail
        self.sender = sender_mail
        self.sub = subject
        self.body = mail_body
        self.cc = cc_mail_list
        self.bcc = bbc_mail_list
        self.sender_name = sender_name


def send_mailer(mail_obj):
    """
    sends mailer given the mailer object
    """
    mail_type_val = '9'
    host_id = '83'
    params = {'RECP': mail_obj.recp,
              'SENDER': mail_obj.sender,
              'SUB': mail_obj.sub,
              'BODY': mail_obj.body,
              'MAIL_TP': mail_type_val,
              'H_ID': host_id,
              'CC': mail_obj.cc,
              'BCC': mail_obj.bcc,
              'SENDER_NM': mail_obj.sender_name
              }
    resp = requests.post(url=GENERIC_MAILER_BASE_URL, json=params)
    if resp.status_code == 200:
        print('mail sent successfully to {}'.format(mail_obj.recp))
        return True
    else:
        print('failure to send mail with status code: {}'.format(resp.status_code))
        return False


# mail_obj = MAILER_OBJECT(recipient_mail = to, sender_mail = senderEmail, subject = 'sub', mail_body = body)

def get_mailer_object_for_ml_process_alert(mail_body):
    """
    creates the mailer object that will be used to trigger the mail
    """
    to = "yash.dalmia@timesinternet.in"
    subject = "ML77 server process complete"
    body = mail_body
    sender_email = 'deeplearningAlert@gmail.com'
    mail_obj = MailerObject(recipient_mail=to, sender_mail=sender_email, subject=subject
                                                  , mail_body=body)
    return mail_obj

def test_func():
    print('run test_func')
