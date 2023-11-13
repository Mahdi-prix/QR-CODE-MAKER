import qrcode

def generate_qr_code(input_text, file_name='qrcode.png'):
    # QR kodunu oluştur / Make QR basics
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # QR kodu için veriyi ekleyin/ Adding string for QR code
    qr.add_data(input_text)
    qr.make(fit=True)

    # QR kod resimini oluşturmak/ Create QR code picture as png.
    img = qr.make_image(fill_color="black", back_color="white")

    # QR kodunu hazırlama mesajı/ Giving massage to user after creating QR code
    img.save(file_name)

    print(f"QR kodu başarıyla oluşturuldu ve '{file_name}' adlı dosyaya kaydedildi.")

if __name__ == "__main__":
    # Kullanıcıdan bir metin veya adres alın/Get input for create QR code
    user_input = input("Metni veya adresi girin: ")

    # QR kodunu oluşturun ve varsayılan olarak 'qrcode.png' olarak kaydedin/ Calling func.
    #  and finish job
    generate_qr_code(user_input)





###NOT: Here we make qr code for any word or url , but here for using better spaces and ram
# in my pc I write new qr on ex qr. So I can create what I want in regard to taking up very 
# little space.