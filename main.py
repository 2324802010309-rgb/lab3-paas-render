import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Lấy đường link kết nối Database từ biến môi trường của Render
db_url = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Tạo bảng dữ liệu User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

# Trang chủ: Đọc và hiển thị danh sách từ Database (Read)
@app.route('/')
def index():
    users = User.query.all()
    user_list = "<br>".join([f"ID: {u.id} - Tên: {u.name}" for u in users])
    return f"<h3>Hello Cloud! Bai Lab 3 - Phan 2 (Database).</h3><p>Danh sach User trong Database:</p>{user_list}<br><br><p>De them user, them duoi sau vao URL: /add?name=TenCuaBan</p>"

# Đường dẫn thêm dữ liệu vào Database (Create)
@app.route('/add')
def add_user():
    name = request.args.get('name')
    if name:
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return f"Da them thanh cong user: {name}. <br><a href='/'>Quay lai trang chu</a>"
    return "Vui long nhap ten. Vi du: /add?name=Nhi"