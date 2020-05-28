# Copyright 2020. Huawei Technologies Co., Ltd. All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
"""
The Demo Class For SubscriptionService Order request
"""
import json
import AtDemo


class SubscriptionService:
    """Demo Service To Request To Subscription Server"""
    def __init__(self):
        # TODO: replace the (ip:port) to the real one, and if the protocol is https, you should deal with the license
        self.baseUrl = "http://ip:port"
        self.getSubscriptionUrl = "%s/sub/applications/v2/purchases/get" % self.baseUrl
        self.stopSubscriptionUrl = "%s/sub/applications/v2/purchases/stop" % self.baseUrl
        self.delaySubscriptionUrl = "%s/sub/applications/v2/purchases/delay" % self.baseUrl
        self.returnSubscriptionUrl = "%s/sub/applications/v2/purchases/returnFee" % self.baseUrl
        self.withdrawSubscriptionUrl = "%s/sub/applications/v2/purchases/withdrawal" % self.baseUrl

    def getSubscription(self, subscriptionId, purchaseToken):
        # fetch the App Level AccessToken
        appAt = AtDemo.getAppAT()
        if appAt is None or appAt == "":
            return
        # construct the Authorization in Header
        headers = AtDemo.buildAuthorization(appAt)
        # pack the request body
        bodyDict = {"subscriptionId": subscriptionId, "purchaseToken": purchaseToken}
        data = json.dumps(bodyDict)
        response = AtDemo.httpPost(self.getSubscriptionUrl, str.encode(data), headers)
        # TODO: display the response as string in console, you can replace it with your business logic.
        print(response)

    def stopSubscription(self, subscriptionId, purchaseToken):
        # fetch the App Level AccessToken
        appAt = AtDemo.getAppAT()
        if appAt is None or appAt == "":
            return
        # construct the Authorization in Header
        headers = AtDemo.buildAuthorization(appAt)
        # pack the request body
        bodyDict = {"subscriptionId": subscriptionId, "purchaseToken": purchaseToken}
        data = json.dumps(bodyDict)
        response = AtDemo.httpPost(self.stopSubscriptionUrl, str.encode(data), headers)
        # TODO: display the response as string in console, you can replace it with your business logic.
        print(response)

    def delaySubscription(self, subscriptionId, purchaseToken, currentExpirationTime, desiredExpirationTime):
        # fetch the App Level AccessToken
        appAt = AtDemo.getAppAT()
        if appAt is None or appAt == "":
            return
        # construct the Authorization in Header
        headers = AtDemo.buildAuthorization(appAt)
        # pack the request body
        bodyDict = {"subscriptionId": subscriptionId, "purchaseToken": purchaseToken,
                    "currentExpirationTime": currentExpirationTime, "desiredExpirationTime": desiredExpirationTime}
        data = json.dumps(bodyDict)
        response = AtDemo.httpPost(self.delaySubscriptionUrl, str.encode(data), headers)
        # TODO: display the response as string in console, you can replace it with your business logic.
        print(response)

    def returnFeeSubscription(self, subscriptionId, purchaseToken):
        # fetch the App Level AccessToken
        appAt = AtDemo.getAppAT()
        if appAt is None or appAt == "":
            return
        # construct the Authorization in Header
        headers = AtDemo.buildAuthorization(appAt)
        bodyDict = {"subscriptionId": subscriptionId, "purchaseToken": purchaseToken}
        data = json.dumps(bodyDict)
        response = AtDemo.httpPost(self.returnSubscriptionUrl, str.encode(data), headers)
        # TODO: display the response as string in console, you can replace it with your business logic.
        print(response)

    def withdrawSubscription(self, subscriptionId, purchaseToken):
        # fetch the App Level AccessToken
        appAt = AtDemo.getAppAT()
        if appAt is None or appAt == "":
            return
        # construct the Authorization in Header
        headers = AtDemo.buildAuthorization(appAt)
        bodyDict = {"subscriptionId": subscriptionId, "purchaseToken": purchaseToken}
        data = json.dumps(bodyDict)
        response = AtDemo.httpPost(self.withdrawSubscriptionUrl, str.encode(data), headers)
        # TODO: display the response as string in console, you can replace it with your business logic.
        print(response)

