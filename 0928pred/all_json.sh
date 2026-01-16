#!/bin/bash
export LAYERNORM_TYPE=fast_layernorm
export CUDA_VISIBLE_DEVICES=0

# 定义JSON文件所在目录
json_dir="/home/jyjiang/Protenix/0928pred/json"

# 循环处理目录下所有.json文件（关键修复：添加/*.json匹配文件）
for input_json in "$json_dir"/*.json; do
    # 检查是否存在符合条件的文件（避免当没有json文件时执行空循环）
    if [ -f "$input_json" ]; then
        echo "开始处理文件: $input_json"
        
        protenix predict \
          --input "$input_json" \
          --out_dir /home/jyjiang/Protenix/0928pred/pdb \
          --seeds 101 \
          --model_name "protenix_mini_default_v0.5.0" \
          --use_default_params false \
          --use_msa false \
        
        echo "完成处理文件: $input_json"
        echo "----------------------------------------"
    else
        # 如果没有找到任何JSON文件，给出提示
        echo "在目录 $json_dir 中未找到任何JSON文件"
        break  # 退出循环
    fi
done

echo "所有JSON文件处理完成"
    