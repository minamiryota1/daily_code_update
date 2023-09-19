#!/bin/bash

# 配置文件的路径
#config_luopan="/opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag"
config_luopan="/opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag"
# 要插入的字符串
search_string_luopan="anp_quick"
insert_string_luopan=""

# 使用sed命令在文件最后一行插入字符串
#sed -i '' -e '$a\' "$config_file"

# 添加落盘配置，使用grep命令搜索该配置是否存在，避免反复添加
if grep -q "$search_string_luopan" "$config_luopan"; then
    echo "落盘配置已经添加"
else
    echo "落盘配置未添加"
    # 检查文件是否可写
    if [ -w "$config_luopan" ]; then
    echo "落盘配置文件已可写"
    else
    # 如果文件不可写，则挂载为可读写
    echo "落盘配置文件不可写，正在挂载为可读写..."
    mountrw
    fi
    # 使用echo命令将新值附加到文件最后一行
    echo "$insert_string_luopan" >> "$config_luopan"
    echo "落盘配置修改完成"
fi
echo "落盘配置如下"
cat /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag
#打开模拟器配置
# 使用sed命令替换指定行的文本
sudo sed -i 's/False/True/g' /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf

#打开落core配置
sudo bash /opt/bin/open_coredump.sh

#关闭防火墙
sudo systemctl stop appfirewall

sudo mountro


