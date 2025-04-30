#!/usr/bin/evn bash

tail /var/log/syslog | cut -d' ' -f5-

cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head


for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
