import enum


class Language(enum.IntEnum):
    kJapanese = 0
    kEnglish = 1


class Message(tuple, enum.Enum):

    language: enum.IntEnum = Language.kJapanese

    start_to_initialize = (
        'Discordサーバーの初期化を開始します。',
    )

    failed_to_initialize = (
        'Discordサーバーの初期化に失敗しました。',
    )

    succeed_to_initialize = (
        'Discordサーバーの初期化に成功しました。',
    )

    forbidden = (
        'ボットに要求された操作の権限がありません。'
    )

    change_role_colour = (
        '権限「{}」の色を{}に変更しました'
    )

    created_role = (
        '権限「{}」を作成しました。'
    )

    created_category = (
        'カテゴリー「{}」を追加しました。'
    )

    created_text_channel = (
        'テキストチャット「{}」を追加しました。'
    )

    role_already_exist = (
        '権限「{}」は既に存在しています'
    )

    category_already_exist = (
        'カテゴリー「{}」は既に存在しています'
    )

    def __str__(self) -> str:
        return self.value[Message.language.value[0].value]
