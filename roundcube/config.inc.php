<?php

$config = array();
$config['db_dsnw'] = 'sqlite:////data/roundcube.db';
$config['smtp_server'] = 'tls://%h';
$config['smtp_port'] = 25;
$config['smtp_user'] = '%u';
$config['smtp_pass'] = '%p';
$config['support_url'] = '';
$config['address_book_type'] = '';
$config['skin'] = 'larry';

{% for k, v in options.iteritems() %}
$config['{{ k }}'] = {{ v }};
{% endfor %}
