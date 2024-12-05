import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import cv2

image = cv2.imread('image.jpg')


# 示例函数 f(n) 和 g(n)
def f(quality):
    param = [cv2.IMWRITE_JPEG_QUALITY, quality]
    return cv2.imencode('.jpg', image, param)[1].nbytes


def g(quality):
    param = [cv2.IMWRITE_WEBP_QUALITY, quality]
    return cv2.imencode('.webp', image, param)[1].nbytes


# 存储 n 和对应的执行时间
n_values = range(10, 91, 10)  # 10, 20, ..., 90
f_execution_times = []
g_execution_times = []

for n in n_values:
    # 测量 f(n) 的执行时间
    f_execution_times.append(f(n) / 1024)

    # 测量 g(n) 的执行时间
    g_execution_times.append(g(n) / 1024)

# 创建 DataFrame
data = pd.DataFrame({
    'n': n_values,
    'JPEG': f_execution_times,
    'WEBP': g_execution_times
})

# 将数据转换为长格式以便绘图
data_melted = data.melt(id_vars='n',
                        value_vars=['JPEG', 'WEBP'],
                        var_name='Format',
                        value_name='Execution Time')

# 绘制 Seaborn 曲线图
sns.lineplot(data=data_melted, x='n', y='Execution Time', hue='Format')
plt.title('Size Comparison')
plt.xlabel('Quality')
plt.ylabel('Size (KB)')
plt.legend(title='Format')
plt.show()
