from .base import BaseRenderer


class LiveChatSponsorshipsGiftRedemptionAnnouncementRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "giftRedemption"
        self.chat.member_level = "<GIFTED>"

    def get_message(self, item):
        message = ''.join([mes.get("text", "")
                       for mes in item["message"]["runs"]])
        return message, [message]
