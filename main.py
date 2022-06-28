import asyncio
import websockets
import json
import time

token = "token";



async def connect():
	async with websockets.connect("wss://gateway.discord.gg/?v=6&encoding=json") as s:
		while True:
			m = await s.recv()
			init_m = json.loads(str(m))
			hb_int = init_m['d']['heartbeat_interval']
			hb_int = int(hb_int) / 1000

			global token;

			await s.send('{\n\t"op": 2,\n\t"d": {\n\t\t"token": "'+token+'",\n\t\t"intents": 513,\n\t\t"properties": {\n\t\t\t"os": "varied",\n\t\t\t"browser": "my_library",\n\t\t\t"device": "my_library"\n\t\t}\n\t}\n}')

			for i in range(10):
				m = await s.recv()
				global msg;
				msg = m;

				print(msg)
				

				while True:
					var = '{\n\t"op": 1,\n\t"d": null\n}'
					await s.send(var)
					print(var)
					while True:
						m = await s.recv()
						print(m)
						time.sleep(hb_int / 80)
						await s.send(var)

						# get last message
						a = 2;
						for i in str(m).split('"'):
							a = a + 1;
							if i == "content":
								print(i + "message get success" + str(a))
								m_content = (str(m).split('"')[a - 1])

								if m_content == ".ping":
									print(m_content)

					asyncio.sleep(hb_int)







asyncio.get_event_loop().run_until_complete(connect())
