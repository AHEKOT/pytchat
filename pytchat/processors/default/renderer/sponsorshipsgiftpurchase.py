from .base import BaseRenderer


class LiveChatSponsorshipsGiftPurchaseAnnouncementRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "giftPurchase"

    def get_authordetails(self):
        self.chat.author.badgeUrl = ""
        (self.chat.author.isVerified,
         self.chat.author.isChatOwner,
         self.chat.author.isChatSponsor,
         self.chat.author.isChatModerator) = (
            self.get_badges(self.item["header"]["liveChatSponsorshipsHeaderRenderer"])
        )
        self.chat.author.channelId = self.item.get("authorExternalChannelId")
        self.chat.author.channelUrl = "http://www.youtube.com/channel/" + self.chat.author.channelId
        header = self.item["header"]["liveChatSponsorshipsHeaderRenderer"]
        self.chat.author.name = header["authorName"]["simpleText"]
        self.chat.author.imageUrl = header["authorPhoto"]["thumbnails"][1]["url"]
        self.chat.author.isChatSponsor = True
        dummy = [None, {"text": "0"}, None, None, None]
        if "primaryText" in header.keys():
            runs = header.get("primaryText", {}).get("runs", dummy)
        else:
            runs = dummy
        if len(runs) == 5:
            self.chat.amountString = runs[1]["text"]
            self.chat.amountValue = float(self.chat.amountString)
            self.chat.currency = "MGI"

    def get_message(self, item):
        message = ''.join([mes.get("text", "")
                       for mes in item["header"]["liveChatSponsorshipsHeaderRenderer"]["primaryText"]["runs"]])
        return message, [message]
