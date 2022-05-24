from pypresence import Presence
import time


client_id = "977923826358845440"

RPC = Presence(client_id=client_id)
RPC.connect()

RPC.update(state="Beeing the best Developer",details="yeah just causally beeing the best Python Dev you can find!",large_image="unknown",small_image="tctd2_icon_hyenas_symbol_01",start=time.time(),buttons=[{"label":"Follow me on Twitch", "url":"https://www.twitch.tv/gsgaming05"}])
while 1:
    time.sleep(15)
