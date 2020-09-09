## 华为应用内支付服务服务端示例代码
[English](https://github.com/HMS-Core/hms-iap-serverdemo) | 中文

## 目录

 * [简介](#简介)
 * [安装](#安装)
 * [环境要求](#环境要求)
 * [配置](#配置)
 * [示例代码](#示例代码)
 * [技术支持](#技术支持)
 * [授权许可](#授权许可)
 
 
## 简介
示例代码里包含华为应用内支付服务服务端的接口，供开发者参考或使用。示例代码包如下。
    
AtDemo：AccessToken的示例代码。每个方法可以独立运行。

OrderService：OrderService的示例代码。每个方法可以独立运行。

SubscriptionService：SubscriptionService的示例代码。每个方法可以独立运行。

notification：notification的示例代码。每个方法可以独立运行。

## 安装
使用示例代码前，确认是否已安装Java环境。解压示例代码包。

将解压文件夹中的代码包拷贝到JAVAPATH指定路径下的工程目录中。刷新该项目，确保文件成功复制到目标目录。

## 环境要求
建议使用JDK 1.8及以上版本。  

## 配置
为实现示例中的功能，开发者需要在AtDemo.java文件、OrderService.java文件、SubscriptionService.java文件和AppServer.java文件中配置相关参数。

AtDemo.java中的参数说明如下:<br>
clientId：客户端ID，从应用信息中获取。<br>
clientSecret：应用的安全接入键，从应用信息中获取。<br>
tokenUrl：华为OAuth2.0服务获取token的地址，详见获取应用级AT。<br>
Notification目录下的AppServer.java文件中的参数如下。<br>
PUBLIC_KEY：RSA公钥。<br>
首先要明确accountFlag的含义。如果InappPurchaseData中的accountFlag值为1，则表示该账户属于电信运营商（TOBTOC_SITE_URL），若该值不为1，则属于华为（TOC_SITE_URL）。对于OrderService和SubscriptionService，您需要选择合适的站点。TOC_SITE_URL：在不同的站点有不同的地址，开发者应选择接入最近的站点。TOBTOC_SITE_URL：电信运营商的站点。    

## 示例代码

    示例代码中，每个方法都调用了华为应用内支付服务服务器的接口。所用方法如下。

    1). AtDemo: getAppAT()
    该方法用于获取应用级AccessToken。
    代码路径：src/main/java/com/example/demo/AtDemo.java<br>

    2). OrderService: verifyToken()
    该方法用于校验支付结果中的purchaseToken，华为支付服务器确认支付结果的准确性。
    地址：{rootUrl}/applications/purchases/tokens/verify。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Order服务地址。
    代码路径：src/main/java/com/example/demo/OrderService.java

    3). OrderService: cancelledListPurchase()
    该方法用于分页查询已取消或已退款的购买信息。
    地址：{rootUrl}/applications/{apiVersion}/purchases/cancelledList。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Order服务地址。
    代码路径：src/main/java/com/example/demo/OrderService.java

    4). SubscriptionService: getSubscription()
    该方法用于校验已购订阅商品的信息，如获取其有效期、状态等。
    地址：{rootUrl}/sub/applications/{apiVersion}/purchases/get。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Subscription服务地址。
    代码路径：src/main/java/com/example/demo/SubscriptionService.java

    5). SubscriptionService: stopSubscription()
    该方法用于取消已经订阅的商品，商品在有效期内仍然有效，但后续的续订会终止。
    地址：{rootUrl}/sub/applications/{apiVersion}/purchases/stop。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Subscription服务地址。
    代码路径：src/main/java/com/example/demo/SubscriptionService.java

    6). SubscriptionService: delaySubscription()
    该方法用于为用户续订订阅产品，推迟订阅者的下一个结算日期。
    地址：{rootUrl}/sub/applications/{apiVersion}/purchases/delay，rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Subscription服务地址。
    代码路径：src/main/java/com/example/demo/SubscriptionService.java

    7). SubscriptionService: returnFeeSubscription() 
    该方法用于将最新一次订阅退款给用户，不会取消订阅，在订阅到期之前一直有效，后续订阅也可正常进行。
    地址：{rootUrl}/sub/applications/{apiVersion}/purchases/returnFee。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Subscription服务地址。
    代码路径：src/main/java/com/example/demo/SubscriptionService.java

    8). SubscriptionService: withdrawSubscription()
    该方法用于取消订阅，相当于执行returnFeeSubscription方法，订阅商品会立即取消，同时会终止后续续订。
    地址：{rootUrl}/sub/applications/{apiVersion}/purchases/withdrawal。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Subscription服务地址。
    代码路径：src/main/java/com/example/demo/SubscriptionService.java

    9). AppServer: dealNotification()
    该方法用于处理订阅事件通知。
    信息参数从订阅事件通知中获取。
    代码路径：src/main/java/com/example/demo/notification/AppServer.java 

    10). OrderService: confirmPurchase()
    商品发货后，调用该方法确认购买。
    地址：{rootUrl}/applications/{apiVersion}/purchases/confirm。rootUrl在不同的站点有不同的地址，开发者应选择接入可访问的最近的Order服务地址。
    代码路径：OrderService.java

## 技术支持
如果您对HMS Core还处于评估阶段，可在[Reddit社区](https://www.reddit.com/r/HMSCore/)获取关于HMS Core的最新讯息，并与其他开发者交流见解。

如果您对使用HMS示例代码有疑问，请尝试：
- 开发过程遇到问题上[Stack Overflow](https://stackoverflow.com/questions/tagged/huawei-mobile-services)，在[huawei-mobile-services]标签下提问，有华为研发专家在线一对一解决您的问题。
- 到[华为开发者论坛](https://developer.huawei.com/consumer/cn/forum/blockdisplay?fid=18) HMS Core板块与其他开发者进行交流。

如果您在尝试示例代码中遇到问题，请向仓库提交[issue](https://github.com/HMS-Core/hms-iap-serverdemo/issues)，也欢迎您提交[Pull Request](https://github.com/HMS-Core/hms-iap-serverdemo/pulls)。

## 授权许可
华为应用内支付服务服务端示例代码经过[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)授权许可。
