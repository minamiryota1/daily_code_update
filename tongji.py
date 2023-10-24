import pandas as pd
import warnings
import re

def result_computing(df):
# 计算泊车时间
    df['泊车时间'] = (df['完成时间'] - df['R档开始时间'])
#计算平均揉库次数和中值泊车时间
    median_parking_time = df[df["结果"] == "通过"]['泊车时间'].median()
    Rub_Count_mean = df['揉库次数'].mean()
    print("揉库次数的平均值：",Rub_Count_mean)
    print("泊车时间的中位数：", median_parking_time)
# 进行筛选操作
    total_pass_count = df[df["结果"] == "通过"].shape[0]
    total_count = df[df["结果"].notnull()].shape[0]
#计算通过率
    print("共计泊车次数为：",total_count)
    print("通过的次数为：",total_pass_count)   
    print("泊车成功率为：",total_pass_count / total_count*100,'%')  
# 将结果写入到表格,写入会报错，提示列过大
    # df.to_excel(outfilename, index=False)
    return 1

def info_output(pattern,df):
    df_select = df[df['车位类型'].str.contains(pattern,regex=True,na=False)]
    warnings.filterwarnings('ignore')
    result_computing(df_select)
    print("{}已经输出完毕\n".format(pattern))

# 读取原始表格数据
filename = input("请输入文件名：")
sheetname = input("请输入sheet_name:")
df = pd.read_excel(filename,sheet_name=sheetname)
#输出有多少列以及每列的名字
print(df.columns)
#生成一个字典，这个字典的key是随机的自然数。但是value是我们要的各种不同车位类型
df_select_all=df["车位类型"].drop_duplicates().to_dict()
for parkspace_type in df_select_all.values():
    parkspace_type = str(parkspace_type)
    try :
        print(parkspace_type)
        info_output(parkspace_type,df)
    except ZeroDivisionError:
        print("{}还没跑呢\n".format(parkspace_type))

#使用泊车数据处理函数
result_computing(df)
print("总的泊车统计数据已经输出完毕\n")

#这个操作可以把时间差值显示为人类可以看懂的时间，但是无法用于median（）的输入
#df['泊车时间'] = df['泊车时间'].apply(lambda x: str(x).split(" ")[-1]) 

###计算垂直线车位的统计数据####
#筛选出垂直线车位相关的数据
pattern = r'垂直(?!.*空间)'
###计算平行线车位的统计数据####
#筛选出平行线车位相关的数据
pattern = r'水平|平行(?!.*空间)'


