import string
from password.new_password import generate_password

def test_password_characters():
    """Tes untuk memastikan hanya karakter yang diizinkan yang digunakan dalam pembuatan password"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Membuat password yang panjang untuk pengujian yang lebih akurat
    for char in password:
        assert char in valid_characters

# -------------------------
# Tugas siswa dimulai dari sini
# Lengkapi isi fungsi test yang sesuai dengan nama dan petunjuknya.
# Jangan mengubah fungsi lain selain milikmu sendiri.
# -------------------------

def test_password_length_matches_input():
    """
    Buat tes untuk memastikan panjang password sesuai dengan input.
    Hint: Gunakan len(password) dan bandingkan dengan panjang yang diminta.
    """
    pass

def test_passwords_are_random():
    """
    Buat tes untuk memastikan dua password yang dibuat berturut-turut tidak sama.
    Hint: Panggil generate_password() dua kali, lalu bandingkan hasilnya.
    """
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2, "Password yang dihasilkan tidak acak, keduanya sama."

def test_password_is_not_empty_when_length_positive():
    """
    Buat tes untuk memastikan password tidak kosong jika panjang lebih dari 0.
    Hint: Password seharusnya bukan string kosong jika length > 0.
    """
    pass

def test_password_is_empty_when_length_zero():
    """
    Buat tes untuk memastikan jika panjang = 0, password yang dihasilkan adalah string kosong.
    Hint: Panggil generate_password(0) dan cek apakah hasilnya == "".
    """
    pass

def test_password_default_length_is_12():
    """
    Buat tes untuk memastikan default panjang password adalah 12 jika tidak diberi argumen.
    Hint: Panggil generate_password() tanpa argumen, lalu cek panjang hasilnya.
    """
    pass

def test_password_contains_uppercase_letter():
    """
    Buat tes untuk memastikan password mengandung setidaknya satu huruf kapital.
    Hint: Gunakan any(char.isupper() for char in password).
    """
    pass

def test_password_contains_lowercase_letter():
    """
    Buat tes untuk memastikan password mengandung setidaknya satu huruf kecil.
    Hint: Gunakan any(char.islower() for char in password).
    """
    password = generate_password(12)
    assert any(char.islower() for char in password), "Password harus mengandung setidaknya satu huruf kecil"

def test_password_contains_digit():
    """
    Buat tes untuk memastikan password mengandung setidaknya satu digit (angka).
    Hint: Gunakan any(char.isdigit() for char in password).
    """
    password = generate_password()
    assert any(char.isdigit() for char in password)
    pass

def test_password_contains_symbol():
    """
    Buat tes untuk memastikan password mengandung setidaknya satu simbol (karakter spesial).
    Hint: Gunakan any(char in string.punctuation for char in password).
    """
    password = generate_password()
    assert any(char in string.punctuation for char in password)
    pass