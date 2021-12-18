dev:
	hypercorn rktpi.main:app --reload
	
server:
	celery -A tasks worker --loglevel=INFO

start:
	python3 -m celeryconfig

flower:
	celery -A tasks worker flower

rabbit:
	sudo rabbitmq-server -detached

update:
	sudo apt-get install -y \
		build-essential cmake libtool autoconf \
		python3.7 python3-pip python3.7-venv \
		rabbitmq-server librabbitmq4 librabbitmq-dev \
		hugo ansible
	ansible-galaxy install fubarhouse.golang
	# https://github.com/fubarhouse/ansible-role-golang
	ansible-playbook ansible/main.yml

nsq:
	../nsq/apps/nsqlookupd/nsqlookupd &
	../nsq/apps/nsqd/nsqd --lookupd-tcp-address=127.0.0.1:4160 --verbose &
	../nsq/apps/nsqadmin/nsqadmin --lookupd-http-address=127.0.0.1:4161 &

nsqkill:
	pkill nsqadmin
	pkill nsqd
	pkill nsqlookupd

nsqmsg:
	curl -d 'hello world 1' 'http://127.0.0.1:4151/pub?topic=test'
