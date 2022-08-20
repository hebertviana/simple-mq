import pymqi
import time

queue_manager = 'QM1'
channel = 'DEV.APP.SVRCONN'
host = 'localhost'
port = '1414'
queue_name = 'DEV.QUEUE.1'
conn_info = '%s(%s)' % (host, port)


def put_mensagem(count):
    x = range(count)
    qmgr_put = pymqi.connect(queue_manager, channel, conn_info)
    start = time.time()
    for n in x:
        print("put number message:", n)
        queue = pymqi.Queue(qmgr_put, queue_name)
        queue.put(str(n))
        queue.close()
    end = time.time()
    print(format(end-start))
    qmgr_put.disconnect()


def get_mensagem_wait():
    # Message Descriptor
    md = pymqi.MD()
    # Get Message Options
    gmo = pymqi.GMO()
    gmo.Options = pymqi.CMQC.MQGMO_WAIT | pymqi.CMQC.MQGMO_FAIL_IF_QUIESCING
    gmo.WaitInterval = 5000  # 5 seconds
    qmgr_get = pymqi.connect(queue_manager, channel, conn_info)
    queue = pymqi.Queue(qmgr_get, queue_name)
    keep_running = True
    while keep_running:
        try:
            # Wait up to to gmo.WaitInterval for a new message.
            message = queue.get(None, md, gmo)
            # Process the message here..
            # Reset the MsgId, CorrelId & GroupId so that we can reuse
            # the same 'md' object again.
            md.MsgId = pymqi.CMQC.MQMI_NONE
            md.CorrelId = pymqi.CMQC.MQCI_NONE
            md.GroupId = pymqi.CMQC.MQGI_NONE
            print("get number message", message.decode('utf-8'))
        except pymqi.MQMIError as e:
            if e.comp == pymqi.CMQC.MQCC_FAILED and e.reason == pymqi.CMQC.MQRC_NO_MSG_AVAILABLE:
                # No messages, that is OK, we can ignore it.
                pass
            else:
                # Some other error condition.
                raise
    qmgr_get.disconnect()
