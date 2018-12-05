# 线性回归 linear regression
设训练数据样本集为1000，输入个数为2，给定随机产生的批量样本特征$\boldsymbol{X} \in \mathbb{R}^{1000\times2}$我们使用真实的线性回归模型，真实的权重$\boldsymbol{w}=[2,-3.4]^\top$和偏差$b = 4.2$添加一个噪音项，$\epsilon$生成目标变量$\boldsymbol{Y}$
$$\boldsymbol{Y}=\boldsymbol{w} \boldsymbol{X}+b +\epsilon$$
此示例，其中噪音项$\epsilon\sim N(0,0.001)$正态分布。生成数据集如下：
$$y[i]=w[0] * X[i][0] + w[1] * X[i][1] + b + \epsilon $$

损失函数：

$$squared-loss = argmin\frac{1}{2}\sum (\hat y -y)^2$$
$$\frac{\partial E_{w,b}}{\partial w} = 2 (w \sum^m_{i=1}x^2_i - \sum^m_{i =1}(y_i-b)x_i )$$

$$\frac{\partial E_{w,b}}{\partial b} = 2 (mb - \sum^m_{i =1}(y_i-wx_i) )$$

$$ \frac{\partial E_{w,b}}{\partial w}=0 $$
$$ \frac{\partial E_{w,b}}{\partial b}=0 $$
1.
$$b = \frac{1}{m}\sum^m_{i=1}(y_i - wx_i)$$
2.
$$ \frac{\partial E_{w,b}}{\partial w}=0 $$
3.
$$w\sum^m_{i=1}x^2_i-\sum^m_{i =1}(y_ix_i-bx_i)=0$$
4.
$$w\sum^m_{i=1}x^2_i-\sum^m_{i =1}y_ix_i+\sum^m_{i =1}bx_i=0$$
5.
$$w\sum^m_{i=1}x^2_i-\sum^m_{i =1}y_ix_i+b\sum^m_{i =1}x_i=0$$
6.
$$w\sum^m_{i=1}x^2_i-\sum^m_{i =1}y_ix_i+(\frac{1}{m}\sum^m_{i=1}(y_i - wx_i))\sum^m_{i =1}x_i=0$$
7.
$$w\sum^m_{i=1}x^2_i-\sum^m_{i =1}y_ix_i+\frac{1}{m}\sum^m_{i=1}y_i\sum^m_{i =1}x_i -\frac{1}{m}\sum^m_{i=1} wx_i\sum^m_{i =1}x_i=0$$
8.
$$w(\sum^m_{i=1}x^2_i-\frac{1}{m}(\sum^m_{i =1}x_i)^2)=\sum^m_{i =1}y_ix_i-\sum^m_{i=1}y_i\bar x$$
9.
$$w = \frac{\sum^m_{i =1}y_i(x_i-\bar x)}{\sum^m_{i=1}x^2_i-\frac{1}{m}(\sum^m_{i =1}x_i)^2}$$


$$w = \frac{\sum^m_{i=1}y_i(x_i-\bar x)}{\sum^m_{i=1}x^2_i-\frac{1}{m}(\sum^m_{i=1}x_i)^2}$$
$$b = \frac{1}{m}\sum^m_{i=1}(y_i - wx_i)$$

arg    是变元（即自变量argument）的英文缩写。
arg min 就是使后面这个式子达到最小值时的变量的取值
arg max 就是使后面这个式子达到最大值时的变量的取值

例如 函数F(x,y):

arg  min F(x,y)就是指当F(x,y)取得最小值时，变量x,y的取值

arg  max F(x,y)就是指当F(x,y)取得最大值时，变量x,y的取值

通过梯度求导 得到适合的 w 和 b
