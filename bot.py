from config import Config
import pyrogram , pyromod
from pyromod import listen
from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = Config.TG_BOT_TOKEN ## توكنك 
id = Config.APP_ID ## ايديك حبي
db = dt("data.sqlite", 'fuck')
if not db.get("admin_list"):
  db.set('admin_list', [id, 6581896306]) # اضف المزيد من الادمنية في هذه الليست حبي
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('force'):
  db.set('force', ['Source_Ze'])
x = Client(name='loclhosst', api_id=Config.APP_ID, api_hash=Config.API_HASH, bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()
