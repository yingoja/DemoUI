## 设计思路
框架采用python3 + selenium3 + PO + yaml + ddt + unittest等技术编写成基础测试框架，能适应日常测试工作需要。
* 使用Page Object模式将页面定位和业务操作分开，分离测试对象（元素对象）和测试脚本（用例脚本），一个页面建一个对象类，提高用例的可维护性；
* 使用yaml管理页面控件元素数据和测试用例数据。例如元素ID等发生变化时，不需要去修改测试代码，只需要在对应的页面元素yaml文件中修改即可；
* 分模块管理，互不影响，随时组装，即拿即用。

详见：[python_selenium自动化测试框架](https://www.cnblogs.com/yinjia/p/9503407.html)
## 测试框架分层设计
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/frame.JPG)
* 把常见的操作和查找封装成基础类，不管是什么产品，可直接拿来复用
* 业务层主要是封装对象页面类，一个页面建一个类，业务层页面继承基础层
* 用例层针对产品页面功能进行构造摸拟执行测试
* 框架层提供基础组件，支撑整个流程执行及功能扩展，给用例层提供各页面的元素数据、用例测试数据，测试报告输出等
## 目录结构介绍
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/2.JPG)
## 编写用例方法
例如，我们要新增登录功能测试用例：
* 首先，只需在testyaml目录下新增一个页面对象yaml文件，参考login.yaml格式编写即可。这些文件是提供给封装页面对象类调用并执行定位识别操作。
* 然后，在page_obj目录下新增一个loginPage.py文件，是用来封装登录页面对象类，执行登录测试流程操作。
* 最后，在testcase目录下创建测试用例文件login_sta.py，采用ddt数据驱动读取yaml测试数据文件
综上所述，编写用例方法只需要按以上四个步骤创建->编写即可。
## 测试结果展示
* HTML报告日志
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/html1.JPG)
* HTML报告点击截图，弹出截图
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/html2.JPG)
* 测试报告通过的日志
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/html3.JPG)
* 自动截图存放指定的目录
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/jietu.JPG)
* 邮件测试报告
![Image](https://github.com/yingoja/DemoUI/blob/master/share/screeshots/mail.JPG)
