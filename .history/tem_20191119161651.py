import time

# t=time.time()
# print(t)

# localtime = time.localtime(time.time())
# print ("本地时间为 :", localtime)

# # 格式化成2016-03-20 11:45:39形式
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# # 格式化成Sat Mar 28 22:24:24 2016形式
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# # 将格式字符串转换为时间戳
# a = "22:24:24 2016"
# print (time.strptime(a,"%H:%M:%S %Y"))


riqi=r'''

<\p>python提供了一种方式让我们可以输入一些不太好通过键盘输入的字符，比如换行符缩进符之类的。这种特殊的字符组合我们可以称之为转义序列(escape sequences)，详情可以参考<a href="https://docs.python.org/3/reference/lexical_analysis.html">官方文档</a>。</p>

<\\p>我们经常使用的有</p>

</ul>
<//li>\n: 换行</li>
<li>\t: tab，可以当成是缩进</li>
<li>\: 反斜杠</li>
<li>\&#39;: 单引号，可以在单引号字符串中打印出单引号</li>
<li>\&quot;: 双引号，可以在双引号字符串中打印出双引号</li>
</ul>

<h3>多行文本</h3>

<p>python中3个引号开头的字符串中可以包含多行文本，比如</p>

<pre><code class="python">
my_str=&quot;&quot;&quot;
this is the first line
this is the second line
this is the last line
&quot;&quot;&quot;
</code></pre>

<h3>背景</h3>

<p>这一节里，我们强化一下转义序列和多行文本的使用和写法。</p>

<h3>代码实现</h3>

<p>新建名为<code>print_test_case.py</code>，内容如下</p>

<pre><code class="python">
test_scenario = &quot;登录场景\n&quot;

test_case_name = &quot;\t正常登录: \n&quot;

# two tabs
tt = &quot;\t\t&quot;

test_step = f&quot;{tt}1.打开chrome浏览器\n{tt}2.输入www.itest.info\n{tt}3.在登录表单中输入用户名:example，密码:example\n{tt}4.登记登录按钮\n&quot;

test_assert = f&quot;{tt}应该跳转到www.itest.info/login_success页面，并出现\&quot;登录成功\&quot;的提示&quot;

print(test_scenario + test_case_name + test_step + test_assert)

test_login_failed = &quot;&quot;&quot;
        密码错误:
                1.打开chrome浏览器
                2.输入www.itest.info
                3.在登录表单中输入用户名:example，密码:incorrect
                4.登记登录按钮
                页面不发生跳转，并出现\&quot;登录失败\&quot;的提示
&quot;&quot;&quot;
print(test_login_failed)
</code></pre>

<h3>运行</h3>

<p>在命令行中使用下面的命令去执行代码</p>

<pre><code>$python print_test_case.py

</code></pre>

'''

print(riqi)