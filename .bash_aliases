alias py='source /srv/viidya/venv/bin/activate'
alias go='touch /srv/viidya/app/webapp/wsgi.py'
alias goapache='sudo apache2ctl -k graceful'
alias manage='sudo python /srv/viidya/app/manage.py'
alias gocelery='sudo manage celeryd -l INFO'
alias install-rabbit1='wget http://www.rabbitmq.com/releases/rabbitmq-server/v2.8.6/rabbitmq-server_2.8.6-1_all.deb'
alias install-rabbit2='sudo dpkg -i rabbitmq-server_2.8.6-1_all.deb'
alias install-rabbit3='sudo apt-get --fix-broken install'
