#!/bin/bash

pg_basebackup -h postgres-master -D /var/lib/postgresql/data -S replication_slot_slave$1 -X stream -P -U replicator -Fp -R
chmod 700 /var/lib/postgresql/data
exec postgres -c 'config_file=/etc/postgresql/postgresql.conf'
