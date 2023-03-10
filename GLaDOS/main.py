from os import environ
from logger import logger
from Check import CheckIn
from push import send_msg_serverJ , send_msg_pushplus


def main():
    # 获取actions secrets配置的cookie SendKey
    ck = environ["cookie"]
    SendKey = environ.get('SendKey')
    isServerJpush = int(environ.get('isServerJpush'))
    token = environ.get('token')
    ispushpluspush = int(environ.get('ispushpluspush'))


    if not ck:
        logger.info('请先配置GLADOS_COOKIE！')
        return

    try:

        title, Text = CheckIn(ck)
        logger.info('GLaDOS 签到成功！')

    except Exception as err:
        logger.error('程序运行出错！')
        title = '程序运行出错！'
        Text = err

    finally:
        tmp = Text.split('\n')
        for i in tmp:
            logger.info(i)

        if isServerJpush:
            # 推送消息，无SendKey不推送
            rsp1 = send_msg_serverJ(SendKey, title, Text)
            logger.info(rsp1)
        if ispushpluspush:
            # 推送消息，无token不推送
            rsp2 = send_msg_pushplus(token, title, Text)
            logger.info(rsp2)


if __name__ == '__main__':
    main()