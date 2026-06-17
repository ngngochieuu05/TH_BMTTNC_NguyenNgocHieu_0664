# Bài Tổng Hợp Lab 01 -> Lab 05

Đây là chương trình tổng hợp để ôn tập cho bài kiểm tra, gom gần như toàn bộ ý chính từ `lab_01` đến `lab_05` vào một nơi.

Thư mục gốc:

- `D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex`

## Mục tiêu của chương trình

- Ôn lại bài cơ bản Python từ `lab_01`
- Thực hành các thuật toán mã hóa cổ điển từ `lab_02`
- Thực hành RSA, ECC, chữ ký số và API từ `lab_03`
- Thực hành hàm băm, Diffie-Hellman, chat socket AES/RSA và WebSocket từ `lab_04`
- Thực hành Base64, Blockchain, giấu tin trong ảnh và SSL chat từ `lab_05`

## Cấu trúc thư mục

- [app.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\app.py)
  - file chạy web app chính
- `mix_portal/`
  - chứa toàn bộ logic chương trình
- `scripts/`
  - chứa các demo riêng chạy bằng terminal
- `data/students.json`
  - nơi lưu dữ liệu sinh viên
- `mix_portal/keys/`
  - nơi lưu khóa RSA và ECC
- `mix_portal/certificates/`
  - chứa chứng chỉ cho SSL chat

## Chuẩn bị môi trường

Bạn có thể chạy bằng một trong hai môi trường sau:

1. `.venv` ở root repo:
```powershell
D:\Thuc_Hanh\TH_BMTTNC\.venv
```

2. `.venv` riêng của `mix_ex`:
```powershell
D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\.venv
```

Nếu cần tạo mới môi trường riêng cho `mix_ex`:

```powershell
cd D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Chạy web app

### Cách 1: dùng `.venv` của `mix_ex`

```powershell
& D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\.venv\Scripts\python.exe D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\app.py
```

### Cách 2: dùng `.venv` ở root repo

```powershell
& D:\Thuc_Hanh\TH_BMTTNC\.venv\Scripts\python.exe D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\app.py
```

Mở trình duyệt tại:

- `http://127.0.0.1:5050`

## Chức năng trên giao diện web

### 1. Tổng quan

Mục này gọi API:

- `GET /api/overview`

Tác dụng:

- Hiển thị tóm tắt các nhóm nội dung của từng lab

### 2. WebSocket từ ngẫu nhiên

Mục này mô phỏng phần `websocket` của `lab_04`.

Cách dùng:

1. Bấm `Kết nối`
2. Mỗi 3 giây hệ thống sẽ đẩy về một từ ngẫu nhiên
3. Bấm `Ngắt kết nối` để dừng

Route WebSocket:

- `/ws/random-words`

### 3. Lab 01 cơ bản

Các chức năng:

- Chào người dùng
- Tính diện tích hình tròn
- Kiểm tra chẵn lẻ
- Tính tổng số chẵn trong dãy
- Đảo chuỗi

API tương ứng:

- `POST /api/basics/greet`
- `POST /api/basics/circle-area`
- `POST /api/basics/parity`
- `POST /api/basics/even-sum`
- `POST /api/basics/reverse`
- `POST /api/basics/to-tuple`

Ví dụ:

```json
POST /api/basics/greet
{
  "name": "Hieu",
  "age": 21
}
```

Kết quả:

```json
{
  "message": "Xin chào Hieu, bạn 21 tuổi"
}
```

### 4. Quản lý sinh viên

Mục này phát triển từ bài quản lý sinh viên của `lab_01`.

Chức năng:

- Thêm sinh viên
- Cập nhật sinh viên
- Xóa sinh viên
- Xem danh sách
- Tìm kiếm theo tên
- Sắp xếp theo tên
- Sắp xếp theo điểm

API:

- `GET /api/students`
- `POST /api/students`
- `PUT /api/students/<student_id>`
- `DELETE /api/students/<student_id>`
- `GET /api/students/search?q=<tu_khoa>`
- `GET /api/students/sort/name`
- `GET /api/students/sort/score`

Dữ liệu lưu tại:

- `data/students.json`

### 5. Mã hóa cổ điển

Nhóm này tổng hợp từ `lab_02`.

Thuật toán có sẵn:

- Caesar
- Vigenere
- Playfair
- Rail Fence
- Chuyển vị

API:

- `POST /api/classical`

Payload:

```json
{
  "algorithm": "caesar",
  "action": "encrypt",
  "text": "ABC",
  "key": "3"
}
```

Ví dụ kết quả:

```json
{
  "result": "DEF"
}
```

### 6. Hàm băm và Base64

Chức năng:

- Băm MD5
- Băm SHA-256
- Băm SHA3-256
- Băm BLAKE2b
- Mã hóa Base64
- Giải mã Base64

API:

- `POST /api/hash`
- `POST /api/base64/encode`
- `POST /api/base64/decode`

Ví dụ:

```json
POST /api/hash
{
  "algorithm": "md5",
  "text": "hello"
}
```

Kết quả:

```json
{
  "result": "5d41402abc4b2a76b9719d911017c592"
}
```

### 7. RSA và ECC

Nhóm này tổng hợp từ `lab_03`.

#### RSA

Chức năng:

- Tạo khóa
- Mã hóa
- Giải mã
- Ký
- Xác minh chữ ký

API:

- `POST /api/rsa/generate`
- `POST /api/rsa/encrypt`
- `POST /api/rsa/decrypt`
- `POST /api/rsa/sign`
- `POST /api/rsa/verify`

Khóa lưu tại:

- `mix_portal/keys/rsa_private_key.pem`
- `mix_portal/keys/rsa_public_key.pem`

#### ECC

Chức năng:

- Tạo khóa
- Mã hóa
- Giải mã
- Ký
- Xác minh chữ ký

API:

- `POST /api/ecc/generate`
- `POST /api/ecc/encrypt`
- `POST /api/ecc/decrypt`
- `POST /api/ecc/sign`
- `POST /api/ecc/verify`

Khóa lưu tại:

- `mix_portal/keys/ecc_private_key.pem`
- `mix_portal/keys/ecc_public_key.pem`

### 8. Blockchain

Mục này mô phỏng blockchain cơ bản từ `lab_05`.

Chức năng:

- Xem trạng thái chuỗi khối
- Thêm giao dịch
- Đào khối mới
- Kiểm tra chuỗi hợp lệ

API:

- `GET /api/blockchain`
- `POST /api/blockchain/transactions`
- `POST /api/blockchain/mine`

Ví dụ thêm giao dịch:

```json
{
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 10
}
```

### 9. Giấu tin trong ảnh

Mục này tổng hợp từ `lab_05/img-hidden`.

Chức năng:

- Nhúng thông điệp vào ảnh
- Đọc lại thông điệp từ ảnh đã nhúng

API:

- `POST /api/steganography/encode`
- `POST /api/steganography/decode`

Lưu ý:

- Khi mã hóa ảnh, hệ thống sẽ trả về file `encoded_image.png`
- Khi giải mã ảnh, hệ thống trả về nội dung thông điệp
- Logic sentinel đã được sửa để giải mã ổn định hơn bài gốc

### 10. Script mô phỏng

Mục này không chạy trực tiếp trong web mà hiển thị lệnh để bạn chạy terminal.

API:

- `GET /api/scripts`

## Chạy các script terminal

### 1. Diffie-Hellman demo

```powershell
cd D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex
.\.venv\Scripts\python.exe scripts\dh_demo.py
```

Ý nghĩa:

- Sinh cặp khóa phía server
- Sinh cặp khóa phía client
- Tính shared secret ở cả hai phía
- Kiểm tra hai bên có cùng khóa chung hay không

### 2. Chat AES/RSA socket

#### Chạy server

```powershell
cd D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex
.\.venv\Scripts\python.exe scripts\aes_rsa_chat_server.py
```

#### Chạy client 1

```powershell
.\.venv\Scripts\python.exe scripts\aes_rsa_chat_client.py
```

#### Chạy client 2

```powershell
.\.venv\Scripts\python.exe scripts\aes_rsa_chat_client.py
```

Ý nghĩa:

- Trao đổi khóa RSA
- Server phát sinh khóa AES cho từng client
- Chat qua socket với dữ liệu được mã hóa AES

### 3. Chat SSL

#### Chạy server

```powershell
cd D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex
.\.venv\Scripts\python.exe scripts\ssl_chat_server.py
```

#### Chạy client

```powershell
.\.venv\Scripts\python.exe scripts\ssl_chat_client.py
```

Ý nghĩa:

- Tạo kết nối TLS/SSL
- Chat giữa nhiều client qua server

## Gợi ý test nhanh trước kiểm tra

### Bài cơ bản

- Tên `Hieu`, tuổi `21`
- Bán kính `2`
- Số nguyên `7`
- Dãy `1,2,3,4,5,6`
- Chuỗi `HELLO`

### Mã hóa cổ điển

- Caesar:
  - text `ABC`, key `3` -> `DEF`
- Vigenere:
  - text `HELLO`, key `KEY`
- Playfair:
  - text `HELLO`, key `SECRET`
- Rail Fence:
  - text `HELLOWORLD`, key `3`
- Chuyển vị:
  - text `HELLOWORLD`, key `ZEBRA`

### Hash và Base64

- MD5 của `hello` phải là:
  - `5d41402abc4b2a76b9719d911017c592`
- Base64 của `hello` phải là:
  - `aGVsbG8=`

### RSA và ECC

- Tạo khóa trước
- Dùng thông điệp:
  - `BMTTNC`
- Kiểm tra:
  - mã hóa xong giải mã lại đúng
  - ký xong xác minh trả về `true`

### Blockchain

1. Thêm giao dịch `Alice -> Bob`
2. Đào 1 khối
3. Xem chain
4. Kỳ vọng:
   - có thêm block mới
   - `is_valid = true`

### Steganography

1. Chọn một ảnh PNG/JPG nhỏ
2. Nhập thông điệp `MATMA`
3. Mã hóa vào ảnh
4. Dùng ảnh vừa tải về để giải mã
5. Kỳ vọng:
   - đọc lại đúng `MATMA`

## Testcase chi tiết theo từng chức năng

Phần này dùng để ôn theo kiểu “đề có thể hỏi gì thì thử cái đó”.

### 1. Testcase cho phần cơ bản Lab 01

#### 1.1. Chào người dùng

Cách test trên giao diện:

1. Nhập `Tên = Hiếu`
2. Nhập `Tuổi = 21`
3. Bấm `Chào người dùng`

Kết quả mong đợi:

```json
{
  "message": "Xin chào Hiếu, bạn 21 tuổi"
}
```

Test API:

```json
POST /api/basics/greet
{
  "name": "Hiếu",
  "age": 21
}
```

#### 1.2. Tính diện tích hình tròn

Input:

- `Bán kính = 2`

Kết quả mong đợi:

```json
{
  "area": 12.56
}
```

Test API:

```json
POST /api/basics/circle-area
{
  "radius": 2
}
```

#### 1.3. Kiểm tra chẵn lẻ

Case 1:

- Input: `8`
- Output mong đợi:

```json
{
  "parity": "chẵn"
}
```

Case 2:

- Input: `7`
- Output mong đợi:

```json
{
  "parity": "lẻ"
}
```

#### 1.4. Tính tổng số chẵn

Input:

- `1,2,3,4,5,6`

Kết quả mong đợi:

```json
{
  "sum": 12
}
```

Vì:

- `2 + 4 + 6 = 12`

#### 1.5. Đảo chuỗi

Input:

- `HELLO`

Kết quả mong đợi:

```json
{
  "reversed": "OLLEH"
}
```

#### 1.6. Chuyển list sang tuple

Test API:

```json
POST /api/basics/to-tuple
{
  "values": [1, 2, 3, 4]
}
```

Kết quả mong đợi:

```json
{
  "tuple": [1, 2, 3, 4]
}
```

Lưu ý:

- JSON không có kiểu tuple thật, nên kết quả hiển thị ra mảng
- Ý nghĩa bài là kiểm tra xử lý cấu trúc dữ liệu

### 2. Testcase cho quản lý sinh viên

#### 2.1. Thêm sinh viên

Input:

- Tên: `Nguyễn Văn A`
- Giới tính: `Nam`
- Chuyên ngành: `ATTT`
- Điểm trung bình: `8.6`

Kết quả mong đợi:

- Hệ thống tạo `student_id`
- `hoc_luc` phải là `Giỏi`

Ví dụ response:

```json
{
  "student_id": 1,
  "name": "Nguyễn Văn A",
  "sex": "Nam",
  "major": "ATTT",
  "diem_tb": 8.6,
  "hoc_luc": "Giỏi"
}
```

#### 2.2. Phân loại học lực

Các mốc cần nhớ:

- `>= 9`: `Xuất sắc`
- `>= 8`: `Giỏi`
- `>= 7`: `Khá`
- `>= 5`: `Trung bình`
- `< 5`: `Yếu`

Test nhanh:

1. `9.2` -> `Xuất sắc`
2. `8.0` -> `Giỏi`
3. `7.5` -> `Khá`
4. `5.5` -> `Trung bình`
5. `4.9` -> `Yếu`

#### 2.3. Tìm kiếm theo tên

Chuẩn bị:

- Thêm 3 sinh viên:
  - `Nguyễn Văn A`
  - `Trần Văn B`
  - `Nguyễn Thị C`

Input tìm kiếm:

- `Nguyễn`

Kết quả mong đợi:

- trả về 2 sinh viên có tên chứa `Nguyễn`

#### 2.4. Sắp xếp theo tên

Chuẩn bị:

- `Bình`
- `An`
- `Cường`

Kết quả mong đợi khi gọi:

- `GET /api/students/sort/name`

Thứ tự:

1. `An`
2. `Bình`
3. `Cường`

#### 2.5. Sắp xếp theo điểm

Chuẩn bị:

- `A`: `8.0`
- `B`: `9.1`
- `C`: `7.2`

Kết quả mong đợi:

1. `B`
2. `A`
3. `C`

### 3. Testcase cho mã hóa cổ điển

#### 3.1. Caesar

Test mã hóa:

```json
POST /api/classical
{
  "algorithm": "caesar",
  "action": "encrypt",
  "text": "ABC",
  "key": "3"
}
```

Kết quả mong đợi:

```json
{
  "result": "DEF"
}
```

Test giải mã:

```json
POST /api/classical
{
  "algorithm": "caesar",
  "action": "decrypt",
  "text": "DEF",
  "key": "3"
}
```

Kết quả mong đợi:

```json
{
  "result": "ABC"
}
```

#### 3.2. Vigenere

Input:

- text: `HELLO`
- key: `KEY`

Cách kiểm tra:

1. Mã hóa trước
2. Lấy kết quả mã hóa đó đem giải mã lại

Kết quả mong đợi:

- sau khi giải mã phải ra lại `HELLO`

#### 3.3. Playfair

Input:

- text: `HELLO`
- key: `SECRET`

Cách kiểm tra:

1. Mã hóa
2. Giải mã

Kết quả mong đợi:

- kết quả giải mã sẽ gần với bản gốc
- có thể xuất hiện `X` chèn thêm do đặc thù Playfair

Lưu ý:

- đây là điểm hay bị hỏi trong kiểm tra lý thuyết
- Playfair có thể biến `HELLO` thành các cặp như `HE LX LO`

#### 3.4. Rail Fence

Input:

- text: `HELLOWORLD`
- key: `3`

Cách kiểm tra:

1. Mã hóa
2. Giải mã

Kết quả mong đợi:

- bản giải mã phải quay về `HELLOWORLD`

#### 3.5. Chuyển vị

Input:

- text: `HELLOWORLD`
- key: `ZEBRA`

Cách kiểm tra:

1. Mã hóa
2. Giải mã

Kết quả mong đợi:

- giải mã quay về nội dung ban đầu hoặc bản đã được chuẩn hóa chữ cái

### 4. Testcase cho hàm băm

#### 4.1. MD5

Input:

- `hello`

Kết quả chuẩn:

```text
5d41402abc4b2a76b9719d911017c592
```

#### 4.2. SHA-256

Input:

- `hello`

Kết quả chuẩn:

```text
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

#### 4.3. SHA3-256

Input:

- `hello`

Kết quả mong đợi:

- trả về chuỗi hex dài `64` ký tự

#### 4.4. BLAKE2b

Input:

- `hello`

Kết quả mong đợi:

- trả về chuỗi hex dài `128` ký tự

#### 4.5. Tính chất cần kiểm tra

Cho cùng một input:

- băm lại nhiều lần phải ra cùng một kết quả

Cho input khác nhau:

- `hello`
- `Hello`

Kết quả mong đợi:

- hash phải khác nhau

### 5. Testcase cho Base64

#### 5.1. Mã hóa

Input:

- `hello`

Kết quả mong đợi:

```json
{
  "result": "aGVsbG8="
}
```

#### 5.2. Giải mã

Input:

- `aGVsbG8=`

Kết quả mong đợi:

```json
{
  "result": "hello"
}
```

### 6. Testcase cho RSA

#### 6.1. Tạo khóa

Thao tác:

1. Bấm `Tạo khóa RSA`

Kết quả mong đợi:

- xuất hiện file:
  - `mix_portal/keys/rsa_private_key.pem`
  - `mix_portal/keys/rsa_public_key.pem`

#### 6.2. Mã hóa và giải mã

Input:

- `BMTTNC`

Thao tác:

1. Bấm `Mã hóa RSA`
2. Bấm `Giải mã RSA`

Kết quả mong đợi:

- sau giải mã phải thu lại `BMTTNC`

#### 6.3. Ký và xác minh

Input:

- `BMTTNC`

Thao tác:

1. Bấm `Ký RSA`
2. Bấm `Xác minh RSA`

Kết quả mong đợi:

```json
{
  "result": true
}
```

Case âm:

1. Ký với message `BMTTNC`
2. Sau đó đổi message thành `BMTTNC123`
3. Bấm `Xác minh RSA`

Kết quả mong đợi:

```json
{
  "result": false
}
```

### 7. Testcase cho ECC

#### 7.1. Tạo khóa

Kết quả mong đợi:

- tạo được:
  - `mix_portal/keys/ecc_private_key.pem`
  - `mix_portal/keys/ecc_public_key.pem`

#### 7.2. Mã hóa và giải mã

Input:

- `ECC_TEST`

Kết quả mong đợi:

- giải mã phải ra lại `ECC_TEST`

#### 7.3. Ký và xác minh

Input:

- `ECC_SIGN`

Kết quả mong đợi:

- verify trả về `true`

Case âm:

- đổi message sau khi ký
- verify phải trả về `false`

### 8. Testcase cho Blockchain

#### 8.1. Trạng thái ban đầu

Gọi:

- `GET /api/blockchain`

Kết quả mong đợi:

- có `chain`
- có ít nhất `1` block genesis
- `is_valid = true`

#### 8.2. Thêm giao dịch

Input:

```json
{
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 10
}
```

Kết quả mong đợi:

- hệ thống báo giao dịch sẽ được đưa vào block kế tiếp

#### 8.3. Đào khối

Thao tác:

1. Thêm 1 hoặc nhiều giao dịch
2. Gọi `POST /api/blockchain/mine`

Kết quả mong đợi:

- có block mới
- block đó có danh sách transaction
- có transaction thưởng:
  - `System -> Miner`

#### 8.4. Kiểm tra tính hợp lệ

Sau khi đào khối:

- `GET /api/blockchain`

Kết quả mong đợi:

```json
{
  "is_valid": true
}
```

### 9. Testcase cho giấu tin trong ảnh

#### 9.1. Mã hóa ảnh

Chuẩn bị:

- một ảnh PNG hoặc JPG nhỏ

Input:

- message: `MATMA123`

Kết quả mong đợi:

- hệ thống tải về file `encoded_image.png`

#### 9.2. Giải mã ảnh

Thao tác:

1. Dùng đúng file `encoded_image.png` vừa tạo
2. Bấm `Giải mã từ ảnh`

Kết quả mong đợi:

```json
{
  "result": "MATMA123"
}
```

#### 9.3. Case lỗi nên thử

1. Chọn ảnh nhưng để trống thông điệp
2. Chọn ảnh quá nhỏ nhưng nhập thông điệp quá dài

Kết quả mong đợi:

- hệ thống báo lỗi

### 10. Testcase cho WebSocket

#### 10.1. Kết nối thành công

Thao tác:

1. Mở trang web
2. Bấm `Kết nối`

Kết quả mong đợi:

- cứ khoảng 3 giây nhận thêm một từ mới

#### 10.2. Ngắt kết nối

Thao tác:

1. Sau khi đã nhận dữ liệu vài lần
2. Bấm `Ngắt kết nối`

Kết quả mong đợi:

- không nhận thêm dữ liệu mới nữa

### 11. Testcase cho script Diffie-Hellman

Chạy:

```powershell
.\.venv\Scripts\python.exe scripts\dh_demo.py
```

Kết quả mong đợi:

- in ra khóa công khai server
- in ra bí mật chung phía server
- in ra bí mật chung phía client
- dòng cuối:

```text
Hai bên khớp khóa chung: True
```

### 12. Testcase cho chat AES/RSA

#### 12.1. Kết nối 2 client

Thao tác:

1. Chạy server
2. Mở client 1
3. Mở client 2

Kết quả mong đợi:

- server báo 2 kết nối thành công

#### 12.2. Gửi tin nhắn

Input:

- client 1 gửi: `xin chao`

Kết quả mong đợi:

- client 2 nhận được:

```text
Nhận: xin chao
```

#### 12.3. Thoát

Input:

- gõ `exit`

Kết quả mong đợi:

- client đóng
- server báo ngắt kết nối

### 13. Testcase cho chat SSL

#### 13.1. Khởi động

1. Chạy `ssl_chat_server.py`
2. Chạy 2 cửa sổ `ssl_chat_client.py`

Kết quả mong đợi:

- server in ra thông báo đang lắng nghe
- client kết nối không lỗi

#### 13.2. Nhắn tin

Input:

- client A gửi: `hello ssl`

Kết quả mong đợi:

- client B nhận:

```text
Nhận: hello ssl
```

## Mẫu đề tự luyện

### Đề 1

1. Tính diện tích hình tròn bán kính `3.5`
2. Kiểm tra số `17` là chẵn hay lẻ
3. Mã hóa Caesar chuỗi `SECURITY` với khóa `5`
4. Băm SHA-256 chuỗi `BMTTNC`
5. Mã hóa Base64 chuỗi `NguyenNgocHieu`

### Đề 2

1. Thêm 3 sinh viên
2. Sắp xếp theo điểm
3. Tìm sinh viên theo tên
4. Tạo khóa RSA
5. Ký và xác minh thông điệp `ATTT`

### Đề 3

1. Tạo khóa ECC
2. Mã hóa và giải mã `HELLO_ECC`
3. Thêm 2 giao dịch blockchain
4. Đào 1 khối
5. Kiểm tra chuỗi hợp lệ

### Đề 4

1. Mã hóa một ảnh với thông điệp `SECRET2026`
2. Giải mã lại ảnh đó
3. Chạy WebSocket và quan sát dữ liệu đẩy về
4. Chạy DH demo và giải thích vì sao 2 shared secret giống nhau

## Các file quan trọng cần nhớ

- [app.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\app.py)
- [server.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\server.py)
- [algorithms.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\algorithms.py)
- [modern.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\modern.py)
- [hashing.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\hashing.py)
- [blockchain_tools.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\blockchain_tools.py)
- [steganography.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\steganography.py)
- [students.py](D:\Thuc_Hanh\TH_BMTTNC\Lab_05\mix_ex\mix_portal\students.py)

## Ghi chú cuối

- Chương trình này là bản tổng hợp để ôn bài, không phải hệ thống production
- Một số phần network được giữ ở dạng script riêng vì phù hợp kiểu bài lab hơn giao diện web
- Nếu bạn kiểm tra bằng terminal, nên ưu tiên chạy cả web app lẫn các script socket để quen thao tác
