from sqlalchemy import create_engine, text

import qrcode

engine = create_engine(
    "mysql+pymysql://admin:inventory@demo-db.cm4jgbbqqnra.eu-north-1.rds.amazonaws.com/Inventory_management?charset=utf8mb4"
)

#def load_data_from_db():
with engine.connect() as conn:
  result = conn.execute(text("select * from Inventory_data"))

  inventory_dicts = []

  for row in result.all():
    #inventory_dicts.append(dict(row))
    inventory_dicts = row._mapping
  print(inventory_dicts)
# return inventory

data = str(inventory_dicts)
img = qrcode.make(data)
img.save('Qr_code')
# Creating an instance of QRCode class
#qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Adding data to the instance 'qr'
#qr.add_data(data)

#qr.make(fit=True)
#img = qr.make_image(fill_color='red', back_color='white')

#img.save('MyQRCode2.png')
