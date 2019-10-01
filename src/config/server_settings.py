import discord


class ServerSettings:

    @classmethod
    def getBotCategoryName(cls) -> str:
        return 'BOT'

    @classmethod
    def getBotStatusChannelName(cls) -> str:
        return 'bot-status'

    @classmethod
    def getBotControlChannelName(cls) -> str:
        return 'bot-control'

    @classmethod
    def getEntryChannelName(cls) -> str:
        return 'entry'

    @classmethod
    def getSubmitChannelName(cls) -> str:
        return 'submit'

    @classmethod
    def getBotAdminRoleName(cls) -> str:
        return 'Bot Admin'

    @classmethod
    def getBotAdminRoleColour(cls) -> discord.Colour:
        return discord.Colour.blurple()

    @classmethod
    def getBotRoleColour(cls) -> discord.Colour:
        return discord.Colour.orange()  # 0xe67e22

    @classmethod
    def getExhibitorRoleName(cls) -> str:
        return '出展者'
