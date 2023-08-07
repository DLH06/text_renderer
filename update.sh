#!/usr/bin/env bash

set - e

python3 main.py \
--config example_data/example.py \
--dataset img \
--num_processes 5 \
--log_period 100

# python3 tools/prepare_effect_layout_example.py


