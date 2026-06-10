patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


# ====================== HELPER FUNCTIONS ======================

def validate_gender(gender_input: str) -> bool:
    """Kiểm tra giới tính hợp lệ (Nam hoặc Nu)"""
    cleaned = gender_input.strip().lower()
    return cleaned in ["nam", "nu"]


def find_patient_index(patient_list: list, patient_id: str) -> int:
    """Tìm index của bệnh nhân theo mã BN, trả về -1 nếu không tìm thấy"""
    pid = patient_id.strip().upper()
    if not pid:
        return -1
    for i, patient in enumerate(patient_list):
        if patient[0] == pid:
            return i
    return -1


# ====================== CHỨC NĂNG ======================

def display_patients(patient_list: list):
    """Chức năng 1: Hiển thị danh sách bệnh nhân"""
    print("\n----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    for i, p in enumerate(patient_list, 1):
        print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")


def add_patient(patient_list: list):
    """Chức năng 2: Tiếp nhận bệnh nhân mới"""
    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")
    
    ma_bn = input("Nhập mã bệnh nhân: ").strip().upper()
    if not ma_bn:
        print("Mã bệnh nhân không được để trống!")
        return
    
    if find_patient_index(patient_list, ma_bn) != -1:
        print(f"Mã bệnh nhân {ma_bn} đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return
    
    ten_bn = input("Nhập tên bệnh nhân: ").strip()
    if not ten_bn:
        print("Tên bệnh nhân không được để trống!")
        return
    ten_bn = ten_bn.title()
    
    while True:
        gioi_tinh = input("Nhập giới tính Nam/Nu: ").strip()
        if validate_gender(gioi_tinh):
            gioi_tinh = "Nam" if gioi_tinh.strip().lower() == "nam" else "Nu"
            break
        else:
            print("Giới tính không hợp lệ, vui lòng nhập lại!")
    
    chan_doan = input("Nhập chẩn đoán bệnh: ").strip()
    if not chan_doan:
        print("Chẩn đoán bệnh không được để trống!")
        return
    chan_doan = chan_doan.capitalize()
    
    patient_list.append([ma_bn, ten_bn, gioi_tinh, chan_doan])
    print("Tiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list: list):
    """Chức năng 3: Cập nhật chẩn đoán bệnh"""
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    if not ma_bn:
        print("Mã bệnh nhân không được để trống!")
        return
    
    index = find_patient_index(patient_list, ma_bn)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {ma_bn}!")
        return
    
    patient = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")
    
    chan_doan_moi = input("Nhập chẩn đoán mới: ").strip()
    if not chan_doan_moi:
        print("Chẩn đoán bệnh không được để trống!")
        return
    
    patient[3] = chan_doan_moi.capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list: list):
    """Chức năng 4: Tìm kiếm theo tên bệnh"""
    print("\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
    
    keyword_lower = keyword.lower()
    results = [p for p in patient_list if keyword_lower in p[3].lower()]
    
    if results:
        print("Kết quả tìm kiếm:")
        for i, p in enumerate(results, 1):
            print(f"{i}. Mã: {p[0]} | Tên: {p[1]} | Giới tính: {p[2]} | Bệnh: {p[3]}")
        print(f"\nCó tổng cộng {len(results)} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")
    else:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        print(f"Có tổng cộng 0 bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


# ====================== MENU CHÍNH (KHÔNG DÙNG IF-ELSE) ======================
def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
        match choice:
            case "1":
                display_patients(patients)
            case "2":
                add_patient(patients)
            case "3":
                update_diagnosis(patients)
            case "4":
                search_by_disease(patients)
            case "5":
                print("\nCảm ơn bác sĩ đã sử dụng hệ thống!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")


if __name__ == "__main__":
    main()
