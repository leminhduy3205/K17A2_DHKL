import random
import csv

# 1: Tạo bộ bài với xác suất xuất hiện khác nhau
def tao_bo_bai(xac_suat, so_cap):
    bo_bai = []
    for la_bai, xac_suat_xuat_hien in xac_suat.items():
        bo_bai.extend([la_bai] * int(xac_suat_xuat_hien * so_cap * 2))
    
    while len(bo_bai) < so_cap * 2:
        bo_bai.append(random.choice(list(xac_suat.keys())))
    
    random.shuffle(bo_bai)
    return bo_bai[:so_cap * 2]

# 2: Mô phỏng trò chơi
def mo_phong_tro_choi(bo_bai):
    random.shuffle(bo_bai)
    vi_tri_da_lat = set()
    cap_da_tim_thay = 0
    ket_qua = []

    for vi_tri in range(0, len(bo_bai), 2):
        la_bai_1, la_bai_2 = bo_bai[vi_tri], bo_bai[vi_tri + 1]
        tim_duoc_cap = la_bai_1 == la_bai_2
        cap_da_tim_thay += tim_duoc_cap
        ket_qua.append((vi_tri, vi_tri + 1, la_bai_1, la_bai_2, tim_duoc_cap))
    
    return cap_da_tim_thay, ket_qua

# 3: Tính xác suất tìm được cặp lá bài giống nhau
def tinh_xac_suat(diem, so_cap):
    return diem / so_cap

# 4: Lưu kết quả vào file CSV
def luu_ket_qua_vao_csv(ket_qua, xac_suat, ten_file='ket_qua_tro_choi.csv'):
    with open(ten_file, 'w', newline='') as csvfile:
        fieldnames = ['ViTri1', 'ViTri2', 'LaBai1', 'LaBai2', 'XacSuat1', 'XacSuat2', 'TimDuocCap']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for vi_tri_1, vi_tri_2, la_bai_1, la_bai_2, tim_duoc_cap in ket_qua:
            writer.writerow({
                'ViTri1': vi_tri_1, 'ViTri2': vi_tri_2, 
                'LaBai1': la_bai_1, 'LaBai2': la_bai_2, 
                'XacSuat1': xac_suat[la_bai_1], 'XacSuat2': xac_suat[la_bai_2], 
                'TimDuocCap': tim_duoc_cap
            })

# 5: Hiển thị kết quả
def hien_thi_ket_qua(diem, xac_suat):
    print(f"Số điểm người chơi đạt được: {diem}")
    print(f"Xác suất tìm được cặp lá bài giống nhau: {xac_suat:.2f}")

def main():
    xac_suat = {
        'A': 0.1, 'B': 0.15, 'C': 0.2, 'D': 0.1, 'E': 0.15, 'F': 0.1, 'G': 0.1, 'H': 0.1
    }
    so_cap = 8

    bo_bai = tao_bo_bai(xac_suat, so_cap)
    diem, ket_qua = mo_phong_tro_choi(bo_bai)
    xac_suat_cap = tinh_xac_suat(diem, so_cap)
    luu_ket_qua_vao_csv(ket_qua, xac_suat)
    hien_thi_ket_qua(diem, xac_suat_cap)

if __name__ == "__main__":
    main()
