import pandas as pd
import warnings
import re

def result_computing(df,outfilename):
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
# 将结果写入到表格
    df.to_excel(outfilename, index=False)
    return 1

# 读取原始表格数据
filename = input("请输入文件名：")
df = pd.read_excel(filename)
#输出有多少列以及每列的名字
print(df.columns)
#使用泊车数据处理函数
result_computing(df,'out1.xlsx')
print("总的泊车统计数据已经输出完毕，接下来输出垂直线车位的统计数据")

#这个操作可以把时间差值显示为人类可以看懂的时间，但是无法用于median（）的输入
#df['泊车时间'] = df['泊车时间'].apply(lambda x: str(x).split(" ")[-1]) 

###计算垂直线车位的统计数据####
#筛选出垂直线车位相关的数据
pattern = r'垂直(?!.*空间)'
df_chuizhi_line = df[df['车位类型'].str.contains(pattern,regex=True,na=False)]
warnings.filterwarnings('ignore')
result_computing(df_chuizhi_line,'out2.xlsx')
print("垂直线车位泊车统计数据已经输出完毕，接下来输出水平线车位的统计数据")

###计算平行线车位的统计数据####
#筛选出平行线车位相关的数据
pattern = r'水平|平行(?!.*空间)'
df_pingxing_line = df[df['车位类型'].str.contains(pattern,regex=True,na=False)]
warnings.filterwarnings('ignore')
result_computing(df_pingxing_line,'out3.xlsx')
print("水平线车位统计数据已经输出完毕")

