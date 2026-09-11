# Sampled Benchmark Explainer Corpus — Provenance & Methodology

Tài liệu này ghi lại thông tin định danh, nguồn gốc xuất xứ (provenance), số liệu đo lường thực nghiệm và cảnh báo kỹ thuật cho 10 kịch bản mẫu được lưu trữ trong `research/scripts/`.

---

## 📊 1. Bảng Danh Mục & Siêu Dữ Liệu 10 Kịch Bản Mẫu

- **Thời điểm ghi nhận dữ liệu (Captured At):** 11/09/2026.
- **Nguồn bản dịch / Transcript Source:** Trích xuất từ phụ đề tự động (YouTube Native ASR / Whisper Model).
- **Nguyên tắc xác minh (Zero Hallucination Standard):** Chỉ ghi nhận lượt xem và ngày đăng khi có dữ liệu kiểm chứng độc lập. Các trường hợp còn lại ghi rõ `Not independently verified`, tuyệt đối không tự tạo khoảng số liệu ước tính.

| # | Tên Tệp (`research/scripts/`) | Tiêu Đề Video | Kênh & Handle | Video ID / URL | Ngày Đăng (Published At) | Lượt Xem Khi Ghi Nhận (Captured Views) | Trạng Thái Kiểm Chứng |
|---|---|---|---|---|---|---|---|
| 1 | `Every Cake Explained in 8 Minutes.md` | Every Cake Explained in 8 Minutes | **TasteDetective** (`@TasteDetective`) | [`eIEhmK4brk0`](https://www.youtube.com/watch?v=eIEhmK4brk0) | 04/02/2026 | ~125,000 views | Đã xác minh |
| 2 | `Every Famous Dessert Explained in 11 Minutes.md` | Every Famous Dessert Explained in 11 Minutes | **Decoded Dishes** (`@DecodedDishes`) | [`ppM3q9rlvKA`](https://www.youtube.com/watch?v=ppM3q9rlvKA) | 16/02/2026 | ~27,000 views | Đã xác minh |
| 3 | `Every Steak Explained in 10 Minutes.md` | Every Steak Cut Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 4 | `Every Style of Eggs Explained in 10 Minutes.md` | Every Style of Eggs Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 5 | `Every Chocolate Explained.md` | Every Chocolate Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 6 | `Every Herb Explained.md` | Every Herb Explained | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 7 | `Every Spice Explained.md` | Every Spice Explained | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 8 | `Every Water Brand Explained.md` | Every Water Brand Explained | **Decoded Dishes** (`@DecodedDishes`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 9 | `All Coffees Explained.md` | All Coffee Drinks Explained | **FooDiscover** (`@FooDiscover`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 10 | `All Sugars Explained.md` | All Sugars Explained | **FooDiscover** (`@FooDiscover`) | YouTube Search ID | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |

---

## 📈 2. Phương Pháp Đo Lường Thực Nghiệm & Phân Tích Dữ Liệu Nội Bộ

Quét toàn bộ 10 tệp văn bản trong thư mục `research/scripts/` (sau khi lọc bỏ các nhãn chú thích âm nhạc như `[music]`):

- **Tổng số từ phân tích:** 23.376 từ.
- **Tổng số câu phân tích (dựa trên dấu ngắt câu `.`, `!`, `?`):** 1.428 câu.

### A. Thống Kê Độ Dài Câu (Sentence Length Metrics)
- **Overall Mean (Số từ trung bình toàn bộ corpus):** **16.4 từ/câu**.
- **Overall Median (Trung vị toàn bộ corpus):** **16.0 từ/câu**.
- **Per-Video Mean Range (Dải trung bình từng video):** **12.4 – 21.2 từ/câu**.
  - Ngắn nhất: `Every Famous Dessert Explained in 11 Minutes.md` (Trung bình: **12.4 từ/câu**, Trung vị: **12.0 từ/câu**).
  - Nhịp trung bình nhanh: `Every Cake Explained in 8 Minutes.md` (Trung bình: **13.3 từ/câu**, Trung vị: **14.0 từ/câu**).
  - Dài nhất: `Every Style of Eggs Explained in 10 Minutes.md` (Trung bình: **21.2 từ/câu**, Trung vị: **21.0 từ/câu**).
- **Phân bố câu dài (>28 từ):** Có 118 / 1.428 câu (~8.3%) vượt quá 28 từ.
- **Kết luận biên tập:** Ngưỡng 28 từ là **Soft Editorial Heuristic** (khuyến nghị biên tập để giọng đọc tự nhiên, tránh hụt hơi), không phải giới hạn kiểm duyệt cứng.

### B. Hành Vi Mở Đầu (Intro Hook Behavior)
- **10/10 tệp kịch bản (100%)** bắt đầu ngay lập tức bằng việc gọi tên chủ thể hoặc nêu trực tiếp nghịch lý/cơ chế bất ngờ.
- **Zero greetings:** Hoàn toàn không có lời chào hỏi mang tính cá nhân (*"Hi guys"*, *"Welcome back"*).
- *Lưu ý về mốc thời gian:* Do dữ liệu là văn bản transcript thô chưa căn chỉnh audio waveform, quy tắc "trong 10–15 giây đầu" là mục tiêu dựng phim dự kiến, không phải số liệu đo được trực tiếp từ văn bản.

### C. Khảo Sát Lời Kêu Gọi Tương Tác (Call-to-Action)
- **6/10 kịch bản:** Hoàn toàn **không có bất kỳ CTA nào** trong toàn bộ văn bản.
- **4/10 kịch bản:** Có từ 1 đến 2 CTA nhẹ nhàng, đặt tại Outro (hỏi ý kiến về chủ đề tiếp theo).
- **Zero transcripts** có cấu trúc "3 CTA trải đều Đầu – Giữa – Cuối".

### D. Kỹ Thuật Chuyển Đoạn Quan Sát Được
1. **The Noun Drop:** Chấm câu dứt khoát kết thúc một đối tượng, dừng nghỉ, rồi gọi tên đối tượng kế tiếp (*"That's it."* $\rightarrow$ *"Pound cake."*).
2. **The Boundary Shift:** Sử dụng sự thay đổi của biến số nguyên liệu làm cầu nối sang nhóm tiếp theo (*"Where angel food relies purely on egg whites, chiffon reintroduces fat—in liquid form"*).

---

## ⚠️ 3. CẢNH BÁO KỸ THUẬT & GIỚI HẠN DỮ LIỆU ASR (SPEECH-TO-TEXT)

### A. Bản Chất Dữ Liệu
Văn bản trong `research/scripts/` là phụ đề nhận diện giọng nói tự động, chứa nhiều lỗi nhận diện âm vị đối với thuật ngữ nước ngoài và tên danh nhân.

### B. Các Lỗi ASR Điển Hình
- *"Conrad von Hton"* $\rightarrow$ **Coenraad Johannes van Houten** (nhà hóa học Hà Lan phát minh bột ca-cao kiềm hóa năm 1828).
- *"Waldorf Atoria"* $\rightarrow$ **Waldorf Astoria** (khách sạn gắn với truyền thuyết bánh Red Velvet).
- *"Juliana Rad" / "Jacob Kristoff Rad"* $\rightarrow$ **Jakub Kryštof Rad** (phát minh viên đường năm 1841).
- *"Muan Vanang"* $\rightarrow$ **Nguyễn Văn Giảng** (sáng tạo món Cà phê trứng Giảng năm 1946).
- *"M foye"* $\rightarrow$ **Mille-feuille** (bánh ngàn lớp).
- *"Eclair's are shoe pastries"* $\rightarrow$ **Choux pastry** (bột choux nở bằng hơi nước).
- *"maser ponyet cream"* $\rightarrow$ **Mascarpone cream** (phô mai Mascarpone).
- *"filow dough"* $\rightarrow$ **Phyllo dough** (bột ngàn lớp mỏng trong Baklava).
- *"used"* $\rightarrow$ **Leipäjuusto** (phô mai cà phê Phần Lan).
- *"turbanado, dearara, musavado"* $\rightarrow$ **Turbinado, Demerara, Muscovado**.
- *"and7s"* / *"and50s"* $\rightarrow$ 1970s / 1950s.

---

## 🔒 4. QUY TẮC BẮT BUỘC DÀNH CHO BIÊN TẬP VIÊN

> 1. **TUYỆT ĐỐI KHÔNG DÙNG CORPUS ĐỂ FACT-CHECK:** Các file transcript mẫu chỉ phản ánh cấu trúc nhịp điệu và văn phong, không phải tài liệu khoa học hay lịch sử đã kiểm chứng. Mọi kiến thức cho video mới phải nghiên cứu độc lập ở Bước 2 (`research.md`).
> 2. **DÙNG ĐÚNG MỤC ĐÍCH:** Chỉ đối chiếu cách ngắt câu, đan xen câu ngắn và nhịp chuyển đoạn mượt mà.
