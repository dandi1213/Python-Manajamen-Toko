from flask import Flask, render_template,request,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import MONGO_URI, DATABASE_NAME, PRODUK_COLLECTION,SUPPLIER_COLLECTION, KATEGORI_COLLECTION, TRANSAKSI_COLLECTION, USER_COLLECTION

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection_produk = db[PRODUK_COLLECTION]
collection_supplier = db[SUPPLIER_COLLECTION]
collection_kategori = db[KATEGORI_COLLECTION]
collection_transaksi = db[TRANSAKSI_COLLECTION]
user_collection = db[USER_COLLECTION]

#                   LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['i_username']
        password = request.form['i_password']
        print(username)
        print(password)

        user = user_collection.find_one(
            {
            'username': username,
            'password': password
            }
            )
        print(user)
        if user:
            return render_template('form.html')
        else:
            return render_template('login.html')

    return render_template('login.html')


#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                       REGISTER
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['i_username']
        password = request.form['i_password']
        data = {
            'username': username,
            'password': password
        }
        user_collection.insert_one(data)
        return render_template('register.html')
    return render_template('register.html')



#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                    FORM PRODUK
@app.route('/form_p', methods = ['GET','POST'])
def form_p():
    if request.method == 'POST':
        return render_template('produk.html')
    return render_template('produk.html')

#                    FORM KATEGORI
@app.route('/form_k', methods = ['GET','POST'])
def form_k():
    if request.method == 'POST':
        return render_template('kategori.html')
    return render_template('kategori.html')

#                    FORM SUPPLIER
@app.route('/form_s', methods = ['GET','POST'])
def form_s():
    if request.method == 'POST':
        return render_template('supplier.html')
    return render_template('supplier.html')

#                    FORM TRANSAKSI
@app.route('/form_t', methods = ['GET','POST'])
def form_t():
    if request.method == 'POST':
        return render_template('transaksi.html')
    return render_template('transaksi.html')


#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                   INPUT PRODUK
@app.route('/produk', methods=['GET','POST'])
def produk():

    data_list_produk = collection_produk.find()

    if request.method == 'POST':
        nama = request.form['i_nama']
        kategori = request.form['i_kategori']
        harga = request.form['i_harga']
        stok = request.form['i_stok']
        deskripsi = request.form['i_deskripsi']
        gambar = request.form['i_gambar']
        data = {
            'nama': nama,
            'kategori': kategori,
            'harga': harga,
            'stok': stok,
            'deskripsi': deskripsi,
            'gambar': gambar
            }
        collection_produk.insert_one(data)
        return render_template('produk.html', data_produk = data_list_produk)
    return render_template('produk.html', data_produk = data_list_produk)


@app.route('/list_produk')
def get_list_produk():
    list_data_produk = {}
    list_data_produk = collection_produk.find()

    return render_template("list_produk.html", data_produk = list_data_produk)

@app.route('/update_produk/<id>',methods=['POST'])
def update_produk(id):
        nama = request.form['i_nama']
        kategori = request.form['i_kategori']
        harga = request.form['i_harga']
        stok = request.form['i_stok']
        deskripsi = request.form['i_deskripsi']
        gambar = request.form['i_gambar']
        data = {
            'nama': nama,
            'kategori': kategori,
            'harga': harga,
            'stok': stok,
            'deskripsi': deskripsi,
            'gambar': gambar
            }
        collection_produk.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
            )   
        return redirect('/list_produk')

@app.route('/edit_produk/<id>')
def edit_produk(id):
    data_list_produk = collection_produk.find()
    produk = collection_produk.find_one(   
        {
            '_id': ObjectId(id)
        }
    )
    return render_template('edit_produk.html', produk=produk, list_produk=data_list_produk)

@app.route('/delete_produk/<id>')
def delete_produk(id):
     collection_produk.delete_one({"_id":ObjectId(id)})
     return redirect("/list_produk")

#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                   INPUT KATEGORI
@app.route('/kategori', methods=['GET','POST'])
def kategori():

    data_list_kategori = collection_kategori.find()

    if request.method == 'POST':
        nama = request.form['i_nama']
        deskripsi = request.form['i_deskripsi']
        data = {
            'nama': nama,
            'deskripsi': deskripsi
            }
        collection_kategori.insert_one(data)
        return render_template('kategori.html', data_kategori = data_list_kategori)
    return render_template('kategori.html', data_kategori = data_list_kategori)

@app.route('/list_kategori')
def get_list_kategori():
    list_data_kategori = {}
    list_data_kategori = collection_kategori.find()
    return render_template("list_kategori.html", data_kategori = list_data_kategori)

@app.route('/update_kategori/<id>',methods=['POST'])
def update_kategori(id):
        nama = request.form['i_nama']
        deskripsi = request.form['i_deskripsi']
        data = {
            'nama': nama,
            'deskripsi': deskripsi
            }
        collection_kategori.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
            )   
        return redirect('/list_kategori')

@app.route('/edit_kategori/<id>')
def edit_kategori(id):
    data_list_kategori = collection_kategori.find()
    kategori = collection_kategori.find_one(   
        {
            '_id': ObjectId(id)
        }
    )
    return render_template('edit_kategori.html', kategori = kategori, list_kategori = data_list_kategori)

@app.route('/delete_kategori/<id>')
def delete_kategori(id):
     collection_kategori.delete_one({"_id":ObjectId(id)})
     return redirect("/list_kategori")


#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                           SUPPLIER
@app.route('/supplier', methods=['GET','POST'])
def supplier():

    data_list_supplier = collection_supplier.find()

    if request.method == 'POST':
        nama = request.form['i_nama']
        alamat = request.form['i_alamat']
        telepon = request.form['i_telepon']
        data = {
            'nama': nama,
            'alamat': alamat,
            'telepon': telepon
            }
        collection_supplier.insert_one(data)
        return render_template('supplier.html', data_supplier = data_list_supplier)
    return render_template('supplier.html', data_supplier = data_list_supplier)

@app.route('/list_supplier')
def get_list_supplier():
    list_data_supplier = {}
    list_data_supplier = collection_supplier.find()
    return render_template("list_supplier.html", data_supplier = list_data_supplier)

@app.route('/update_supplier/<id>',methods=['POST'])
def update_supplier(id):
        nama = request.form['i_nama']
        alamat = request.form['i_alamat']
        telepon = request.form['i_telepon']
        data = {
            'nama': nama,
            'alamat': alamat,
            'telepon': telepon
            }
        collection_supplier.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
            )   
        return redirect('/list_supplier')

@app.route('/edit_supplier/<id>')
def edit_supplier(id):
    data_list_supplier = collection_supplier.find()
    supplier = collection_supplier.find_one(   
        {
            '_id': ObjectId(id)
        }
    )
    return render_template('edit_supplier.html', supplier = supplier, list_supplier = data_list_supplier)

@app.route('/delete_supplier/<id>')
def delete_supplier(id):
     collection_supplier.delete_one({"_id":ObjectId(id)})
     return redirect("/list_supplier")

#--------------------------------------------------------------------
#--------------------------------------------------------------------


#                               TRANSAKSI

@app.route('/transaksi', methods=['GET','POST'])
def transaksi():

    data_list_transaksi = collection_transaksi.find()
    data_list_kategori = collection_kategori.find()
    data_list_supplier = collection_supplier.find()

    if request.method == 'POST':
        tanggal_transaksi = request.form['i_tanggal_transaksi']
        produk = request.form['i_produk']
        jumlah = request.form['i_jumlah']
        total_harga = request.form['i_total_harga']
        kategori = request.form['i_kategori']
        data = {
            'tanggal_transaksi': tanggal_transaksi,
            'produk': produk,
            'jumlah': jumlah,
            'total_harga': total_harga,
            'kategori': kategori
            }
        collection_transaksi.insert_one(data)
        return redirect('/transaksi')
    return render_template('transaksi.html', data_transaksi = data_list_transaksi, data_kategori = data_list_kategori, data_supplier = data_list_supplier)

@app.route('/list_transaksi')
def get_list_transaksi():
    list_data_transaksi = {}
    list_data_transaksi = collection_transaksi.find()
    return render_template("list_transaksi.html", data_transaksi = list_data_transaksi)

@app.route('/update_transaksi/<id>',methods=['POST'])
def update_transaksi(id):
        tanggal_transaksi = request.form['i_tanggal_transaksi']
        produk = request.form['i_produk']
        jumlah = request.form['i_jumlah']
        total_harga = request.form['i_total_harga']
        kategori = request.form['i_kategori']
        data = {
            'tanggal_transaksi': tanggal_transaksi,
            'produk': produk,
            'jumlah': jumlah,
            'total_harga': total_harga,
            'kategori': kategori
            }
        collection_transaksi.update_one(
            {'_id': ObjectId(id)},
            {'$set': data}
            )   
        return redirect('/list_transaksi')

@app.route('/edit_transaksi/<id>')
def edit_transaksi(id):
    data_list_transaksi = collection_transaksi.find()
    data_list_kategori = collection_kategori.find()
    transaksi = collection_transaksi.find_one(   
        {
            '_id': ObjectId(id)
        }
    )
    return render_template('edit_transaksi.html', transaksi =  transaksi, list_transaksi = data_list_transaksi, list_kategori = data_list_kategori)

@app.route('/delete_transaksir/<id>')
def delete_transaksi(id):
     collection_transaksi.delete_one({"_id":ObjectId(id)})
     return redirect("/list_transaksi")



if __name__ == '__main__':
    app.run(debug=True)


