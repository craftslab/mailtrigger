#!/bin/bash

python trigger.py \
  --auther-config mailtrigger/config/auther.json \
  --mailer-config mailtrigger/config/mailer.json \
  --scheduler-config mailtrigger/config/scheduler.json \
  --trigger-config mailtrigger/config/trigger.json
