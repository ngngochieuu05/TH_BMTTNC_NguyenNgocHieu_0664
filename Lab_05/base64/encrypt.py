import base64

def main():
    input_string = input("Nhập thông tin cần mã hóa: ")
    
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    
    with open("M:/BMTTNC_NgNgocHieu_0664/TH_BMTTNC_NguyenNgocHieu_0664/Lab_05/base64/data.txt", "w") as file:
        file.write(encoded_string)
        
    print("Đã mã hóa và ghi vào tệp data.txt")
    
if __name__ == "__main__":
    main()