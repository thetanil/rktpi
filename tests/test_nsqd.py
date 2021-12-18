import functools
import logging
import time
import ssl
import nsq
import tornado
import pytest
import tornado.testing
import tornado.web
import asyncio


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")


# application = tornado.web.Application(
#     [
#         (r"/", MainHandler),
#     ]
# )


# @pytest.fixture
# def app():
#     return application


# def test_hello_world(http_client, base_url):
#     response = yield http_client.fetch(base_url)
#     assert response.code == 200


def handler(message):
    print(message)
    return True


async def reader():
    return


async def run():
    nsq.run()


def test_reader():
    def handler(message):
        print(message)
        # message.enable_async()
        # message.finish()
        # sync handler just returns true
        return True

    # topic = "ping_%s" % time.time()
    topic = "ping"

    r = nsq.Reader(
        message_handler=handler,
        lookupd_http_addresses=["http://127.0.0.1:4161"],
        topic=topic,
        channel="async",
        lookupd_poll_interval=15,
    )

    # identify_options = {
    #     "user_agent": "sup",
    #     "snappy": False,
    #     "tls_v1": False,
    #     "tls_options": {"cert_reqs": ssl.CERT_NONE},
    #     "heartbeat_interval": 10,
    #     "output_buffer_size": 4096,
    #     "output_buffer_timeout": 50,
    # }
    # w = nsq.Writer(nsqd_tcp_addresses=["127.0.0.1:4150"], **identify_options)
    # w.pub(topic, "ping")

    nsq.run()


def test_constructor():
    name = "test"
    reconnect_interval = 10.0
    writer = nsq.Writer(
        nsqd_tcp_addresses=["127.0.0.1:4150"],
        reconnect_interval=reconnect_interval,
        name=name,
    )
    assert writer.name == name
    assert len(writer.conn_kwargs) == 0
    assert writer.reconnect_interval == reconnect_interval


# class TestIntegration:
#     identify_options = {
#         "user_agent": "sup",
#         "snappy": False,
#         "tls_v1": False,
#         "tls_options": {"cert_reqs": ssl.CERT_NONE},
#         "heartbeat_interval": 10,
#         "output_buffer_size": 4096,
#         "output_buffer_timeout": 50,
#     }

#     topic = "test_integrator_%s" % time.time()
#     done = False

#     def pong(self, msg):
#         if msg is not None:
#             w.pub(self.topic, "pong")
#         else:
#             self.done == True

#     def listen(self):
#         c = nsq.AsyncConn("127.0.0.1", 4150)
#         c.on(self.topic, self.pong)
#         c.connect()

#     def test_integration(self):
#         self.listen()
#         while not self.done:
#             time.sleep(1)


class TestWriter(tornado.testing.AsyncTestCase):
    identify_options = {
        "user_agent": "sup",
        "heartbeat_interval": 10,
        "output_buffer_size": 4096,
        "output_buffer_timeout": 50,
    }

    def test_writer_await_pub(self):
        topic = "test_writer_await_pub_%s" % time.time()

        w = nsq.Writer(
            nsqd_tcp_addresses=["127.0.0.1:4150"], **self.identify_options
        )

        @tornado.gen.coroutine
        def trypub():
            yield w.pub(topic, b'{"one": 1}')
            yield w.pub(topic, b'{"two": 2}')
            self.stop("OK")

        self.io_loop.call_later(0.1, trypub)
        result = self.wait()
        assert result == "OK"


class TestReader(tornado.testing.AsyncTestCase):
    identify_options = {
        "user_agent": "sup",
        "snappy": False,
        "tls_v1": False,
        "tls_options": {"cert_reqs": ssl.CERT_NONE},
        "heartbeat_interval": 10,
        "output_buffer_size": 4096,
        "output_buffer_timeout": 50,
    }

    def test_conn_identify(self):
        c = nsq.AsyncConn("127.0.0.1", 4150)
        c.on("identify_response", self.stop)
        c.connect()
        response = self.wait()
        print(response)
        assert response["conn"] is c
        assert isinstance(response["data"], dict)

    def test_conn_identify_options(self):
        c = nsq.AsyncConn("127.0.0.1", 4150, **self.identify_options)
        c.on("identify_response", self.stop)
        c.connect()
        response = self.wait()
        print(response)
        assert response["conn"] is c
        assert isinstance(response["data"], dict)
        assert response["data"]["snappy"] is False
        assert response["data"]["tls_v1"] is False  # TODO: no certs in test

    def test_conn_subscribe(self):
        topic = "test_conn_suscribe_%s" % time.time()
        c = nsq.AsyncConn("127.0.0.1", 4150, **self.identify_options)

        def _on_ready(*args, **kwargs):
            c.on("response", self.stop)
            print("************* me")
            c.send(nsq.protocol.subscribe(topic, "ch"))

        c.on("ready", _on_ready)
        c.connect()
        response = self.wait()
        print(response)
        assert response["conn"] is c
        assert response["data"] == b"OK"
