#!/bin/bash
export LAYERNORM_TYPE=fast_layernorm
export CUDA_VISIBLE_DEVICES=0
protenix predict \
  --input rna_2.json \
  --out_dir ./output \
  --seeds 101 \
  --model_name "protenix_mini_default_v0.5.0" \
  --use_default_params false \
  --use_msa false \
