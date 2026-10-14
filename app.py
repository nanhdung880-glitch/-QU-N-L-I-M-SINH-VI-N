
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ và tên": [
        "Hà Danh Bảo", "Trần Văn Bình",
        "Lê Hoàng Hậu", "Phạm Minh Đức",
        "Phạm Quốc Huy", "Đặng Quốc Huy",
        "Bùi Ngọc Lan", "Nguyễn Anh Dũng",
        "Nguyễn Đình Nam", "Lê Hồng Anh"
    ],
    "Điểm chuyên cần": [9, 8, 10, 7, 9, 6, 8, 10, 5, 9],
    "Điểm giữa kỳ": [8, 7, 9, 6, 8, 5, 7, 9, 4, 8],
    "Điểm cuối kỳ": [9, 8, 9, 7, 9, 6, 8, 10, 5, 9]
}

df = pd.DataFrame(data)

df["Tổng kết"] = (
    0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
).round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.subheader("Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

st.subheader("Thống kê")
st.metric("Điểm trung bình", f"{df['Tong_ket'].mean():.2f}")

sv_max = df.loc[df["Tổng kết"].idxmax()]
sv_min = df.loc[df["Tổng kết"].idxmin()]

st.write("Điểm cao nhất:", sv_max["Họ và tên"], sv_max["Tổng kết"])
st.write("Điểm thấp nhất:", sv_min["Họ và tên"], sv_min["Tổng kết"])
st.write("Số sinh viên đạt:", int((df["Tổng kết"] >= 5).sum()))

st.subheader("Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ và tên"].tolist())
sv = df[df["Họ và tên"] == ten].iloc[0]

st.write("Chuyên cần:", sv["Điểm chuyên cần"])
st.write("Giữa kỳ:", sv["Điểm giữa kỳ"])
st.write("Cuối kỳ:", sv["Điểm cuối kỳ"])
st.write("Tổng kết:", sv["Tổng kết"])
st.write("Xếp loại:", sv["Xếp loại"])

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Họ và tên"], df["Tổng kết"])
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.xticks(rotation=45, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

st.caption("Người tạo: NGUYỄN ANH DŨNG | MSSV: 040208015392")
