#!/bin/bash 
####给读写权限，用于测试

mount1_rw(){
    echo "给读写权限"
    echo "Csec@keyL7256" | sudo -S mountrw 
}

open_core(){
    echo "打开core配置"
    echo "Csec@keyL7256" | sudo -S bash /opt/bin/open_coredump.sh  
}


jiancha(){
    aa=`cat /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf | grep "support_set_interface : true" | wc -l`
    bb=`cat /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag | grep "anp_quick_start=bash /opt/bin/anp3 start all --quick --disk" | wc -l `
    cc=`cat /opt/apolloos/app/avp/linux-arm/AVP/conf/data_source/signal_manager.conf  | grep "init_seat_proxy : false" | wc -l`
    if [[ $aa == 1 ]] ; then
        echo "模拟器配置已修改"
        cat /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf | grep "support_set_interface : true"
    else
        mount1_rw
        echo "修改模拟器配置为true。"
        sed -i 's/support_set_interface : false/support_set_interface : true/g' /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf
        sync
        sudo mountro
    
    fi
    if [[ $bb == 1 ]]; then
        echo "已修改落盘配置"
        cat /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag | grep "anp_quick_start=bash /opt/bin/anp3 start all --quick --disk"
    else 
        mount1_rw
        echo "修改自动落盘"
        sed -i '$a\--anp_quick_start=bash /opt/bin/anp3 start all --quick --disk' /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag
        sync
        sudo mountro
    fi

    if [[ $cc == 1 ]]; then
        echo "座椅信号已关闭"
        cat /opt/apolloos/app/avp/linux-arm/AVP/conf/data_source/signal_manager.conf  | grep "init_seat_proxy : false"
    else
        mount1_rw
        echo "修改座椅信号"
        sed -i 's/init_seat_proxy : true/init_seat_proxy : false/g' /opt/apolloos/app/avp/linux-arm/AVP/conf/data_source/signal_manager.conf
        sync
        sudo mountro
    fi
}


tuxiang(){
    mount1_rw
    cp /opt/data/zt/switch_datarecycle_conf.sh  /opt/anp/scripts
    cd /opt/anp/ && bash ./scripts/switch_datarecycle_conf.sh baidu
    sudo mountro
}

open_core   ##打开core配置
#mount1_rw   ##给权限       
tuxiang     ##带图像数据
jiancha     
#sudo mountro








# b="$1"



# if [[ $b == "c" ]]; then
#     echo "查看模拟器配置是否为true。 false:模拟器不可用； true:模拟器可用"
#     cat /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf
#     echo "查看落盘配置是否有--disk字段。"
#     cat /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag
# elif [[ $b == "x" ]]; then
#     mount1_rw
#     echo "修改模拟器配置为true。"
#     sed -i 's/support_set_interface : false/support_set_interface : true/g' /opt/apolloos/app/avp/linux-arm/AVP/conf/united_tool/soa_sim.conf
#     echo "修改自动落盘"
#     sed -i '$a\--anp_quick_start=bash /opt/bin/anp3 start all --quick --disk' /opt/apolloos/app/apollo-master/conf/topmanagement/topstatemachine.flag
#     open_core
#     sudo mountro
# else
#     echo '参数错误!!  c:查看原有配置信息； x:修改配置'
#     echo "修改配置:模拟器，落盘。"

# fi






# jincheng_data=`ps -aux | grep data_recycle | grep -v grep | wc -l`
# jincheng_pavaro=`ps -ef | grep _ebag.dag | grep -v grep | wc -l`


# ###判断该进程是否存在
# if [[ "$jincheng_data" != "0" ]]; then
#     echo "data_recycle,存在该进程"
# else
#     echo "数据回传进程不在，检查一下"

# fi

# ####判断pavaro中的ebag进程是否存在
# if [[ "$jincheng_pavaro" != "0" ]]; then
#     echo "ebag落盘进程已启动"
# else 
#     echo "落盘进程没有启动，检查一下是否插盘，检查一下配置是否正常"

# fi
