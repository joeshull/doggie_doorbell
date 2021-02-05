from notifier import easy_sms, sms_multiple_numbers


def test_sms_multiple_numbers():
    msgs =  sms_multiple_numbers("test multiple text", ['+13038154080', '+13038154080'])
    for msg in msgs:
        assert msg.error_message is None, msg
    return msgs

def test_easy_sms():
    msg = easy_sms("test single text", '+13038154080')
    assert msg.error_message is None, msg
    return msg

if __name__ == '__main__':
    test_easy_sms()
    test_sms_multiple_numbers()
