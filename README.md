С помощью данной программы вы сможете шифровать свои текстовые сообщения на русском или английском языках. В программу вшита работа через Telegram, но также можно пересылать зашифрованные сообщения и в другие мессенджеры или по электронной почте. Для максимальной безопасности я решил, что передача ключа должна быть исключительно лично (сейчас в разработке всё же идет включение функции обмена ключей "онлайн", но это менее безопасно, нежели передать своему собеседнику флешку/бумажку с ключом)

Инструкция к CryptoGram

	Инструкция к шифрованию сообщения:
		1. Установите последнюю версию Python на свой компьютер.
		2. Изучите папку «configs», в ней будет будет файл «input.txt» в котором три параметра (и четвертый необязательный!):
			1 строка - текст (на русском или английском языке)
			2 строка - длина блока в шифре (лучше всего ставить от 8 до ∞)
			3 строка - параметр языка («rus», либо «eng» и никак иначе!!!)
			*4 строка - (необязательна и только если есть уже ключ шифрования) написать 1, если есть ключ шифрования (по умолчанию каждый раз при шифровании сообщения генерируется новый ключ)
			!!!Если уже есть ключ шифрования, то его нужно вставить в файл "key.txt" в папке "configs".
		3. Запустите из командной строки файл «encrypt.py» и дальше следуйте инструкциям на экране.
		4. Можно после шифрования отправить файл "output_encrypt.txt" через любой мессенджер/канал связи (сразу после шифрования программа предлагает Вам отправить ваше сообщение через Telegram, используя ID пользователя)
			!!!Перед отправкой сообщения, убедитесь в том, что ваш собеседник запускал/не блокировал бота (https://t.me/defqy_cryptogram_chat_bot) или же можно просто использовать своего бота (нужно поменять API-ключ в файле bot_sender.py, 11 строка)

	Инструкция к расщифрованию сообщения:
		1. Убедитесь в том, что в файле "output_encrypt.txt" есть информация для расшифровки (предварительно перед расшифровкой надо иметь данный файл + ключ шифрования, которым вы обменялись лично)
		2. Запустите файл "decrypt.py"
		3. На экране отобразится расшифрованное сообщение, а также вся информация продублируется в файле "output_decrypt.txt"
		
		Также появилась возможность генерировать ключ не запуская файл "encrypt.py", а только лишь "generate.py"
		1. Запускаете файл "generate.py"
		2. Вводите длину вашего ключа
		3. Готово! Теперь ключ сохранен в файл "key.txt".
