# Sampled Benchmark Explainer Corpus — Provenance & Methodology

Tài liệu này ghi lại thông tin định danh, nguồn gốc xuất xứ (provenance), số liệu đo lường thực nghiệm và cảnh báo kỹ thuật cho 10 kịch bản mẫu được lưu trữ trong `research/scripts/`.

---

## 📊 1. Bảng Danh Mục & Siêu Dữ Liệu 10 Kịch Bản Mẫu

- **Thời điểm ghi nhận dữ liệu (Captured At):** 11/09/2026.
- **Công cụ tạo phụ đề:** Tệp transcript nhập khẩu cục bộ; các lỗi âm vị học phản ánh trích xuất tự động qua YouTube Native ASR hoặc Whisper Model, tuy nhiên phiên bản công cụ cụ thể cho từng tệp chưa được xác minh độc lập.
- **Nguyên tắc xác minh (Zero Hallucination Standard):** Chỉ ghi nhận lượt xem, ngày đăng và Video ID khi có dữ liệu kiểm chứng độc lập. 8 tệp còn lại ghi nhận rõ `Not independently verified` và kênh phân bổ dựa trên tên tệp/metadata nhập khẩu chưa kiểm chứng, tuyệt đối không tự tạo số liệu ước tính.

| # | Tên Tệp (`research/scripts/`) | Tiêu Đề Video Khai Báo | Phân Bổ Kênh (Channel Attribution) | Video ID / URL | Ngày Đăng (Published At) | Lượt Xem Khi Ghi Nhận (Captured Views) | Trạng Thái Kiểm Chứng |
|---|---|---|---|---|---|---|---|
| 1 | `Every Cake Explained in 8 Minutes.md` | Every Cake Explained in 8 Minutes | **TasteDetective** (`@TasteDetective`) | [`eIEhmK4brk0`](https://www.youtube.com/watch?v=eIEhmK4brk0) | 04/02/2026 | ~125,000 views | Đã xác minh độc lập |
| 2 | `Every Famous Dessert Explained in 11 Minutes.md` | Every Famous Dessert Explained in 11 Minutes | **Decoded Dishes** (`@DecodedDishes`) | [`ppM3q9rlvKA`](https://www.youtube.com/watch?v=ppM3q9rlvKA) | 16/02/2026 | ~27,000 views | Đã xác minh độc lập |
| 3 | `Every Steak Explained in 10 Minutes.md` | Every Steak Cut Explained in 10 Minutes | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 4 | `Every Style of Eggs Explained in 10 Minutes.md` | Every Style of Eggs Explained in 10 Minutes | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 5 | `Every Chocolate Explained.md` | Every Chocolate Explained in 10 Minutes | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 6 | `Every Herb Explained.md` | Every Herb Explained | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 7 | `Every Spice Explained.md` | Every Spice Explained | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 8 | `Every Water Brand Explained.md` | Every Water Brand Explained | Claimed by imported metadata: *Decoded Dishes* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 9 | `All Coffees Explained.md` | All Coffee Drinks Explained | Claimed by imported metadata: *FooDiscover* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |
| 10 | `All Sugars Explained.md` | All Sugars Explained | Claimed by imported metadata: *FooDiscover* | *Not independently verified* | *Not independently verified* | *Not independently verified* | Chưa kiểm chứng độc lập |

---

## 📈 2. Phương Pháp Đo Lường Thực Nghiệm & Tái Lập Thống Kê (Reproducible Methodology)

Số liệu dưới đây được tạo tự động bởi script [`research/analyze_corpus.py`](analyze_corpus.py) chạy trên Python 3.

> **LƯU Ý VỀ PHẠM VI TOKENIZER & ĐO LƯỜNG:**
> Thuật toán tách từ và ngắt câu trong script là một **giải pháp kỹ thuật heuristic** (Engineering Heuristic) được thiết kế tối ưu phục vụ phân tích word count, nhịp câu và làm dữ liệu đầu vào cho ước tính tốc độ nói WPM trong kịch bản ẩm thực (chứ không trực tiếp đo audio duration thực tế). Đây không phải mô hình phân đoạn ngôn ngữ học chuyên sâu (NLP parsing model). Đối với một số trường hợp ngoại lệ chứa từ viết tắt đứng trước danh từ riêng/viết hoa ở ranh giới câu (ví dụ: `...in the U.S. Bakers elsewhere...`), heuristic ưu tiên vai trò bổ ngữ nên test suite ghi nhận bằng `@unittest.expectedFailure` nhằm khẳng định chuẩn ngôn ngữ học 2 câu thay vì đóng băng sai sót; điều này không ảnh hưởng đến số liệu chuẩn do 10 file transcript mẫu không chứa các cấu trúc trên.

### Quy Tắc Xử Lý Dữ Liệu (Tokenization Rules):
1. **Lọc thẻ âm thanh theo danh sách cho phép (Allowlist):** Chỉ loại bỏ các thẻ chỉ dẫn âm thanh thực sự không đọc (`[music]`, `[background-music]`, `[snorts]`, `[applause]`, `[laughter]`, `[inaudible]`, `[noise]`). Giữ nguyên các thẻ nội dung có ý nghĩa phân đoạn (ví dụ: `[Chapter 1]`).
2. **Bảo vệ số thập phân:** Số có dấu chấm (ví dụ: `2.3 million`, `120.5 C`) được bảo vệ để không bị ngắt câu sai.
3. **Bảo vệ từ viết tắt theo ngữ cảnh:**
   - Các chức danh/từ viết tắt đơn (`vs.`, `Dr.`, `Mr.`, `Mrs.`, `Prof.`, `Jr.`): bảo vệ dấu chấm không làm dấu ngắt câu.
   - Từ viết tắt liệt kê `etc.`: bảo vệ dấu chấm ở giữa câu (khi theo sau là dấu phẩy/chấm phẩy hoặc từ viết thường: `etc., then bake`), nhưng giữ làm dấu ngắt câu nếu theo sau là từ viết hoa/mở đầu câu mới (`etc. Then bake`) hoặc ở cuối văn bản.
   - Các từ viết tắt nhiều dấu chấm (`B.C.E.`, `C.E.`, `U.S.`, `U.S.A.`, `e.g.`, `i.e.`): bảo vệ dấu chấm nội bộ; dấu chấm cuối cùng được đánh giá theo ngữ cảnh (giữ làm dấu ngắt câu nếu theo sau là từ mở đầu câu mới; bảo vệ nếu đóng vai trò tính từ/bổ ngữ như `U.S. Market` hoặc nằm trong mệnh đề ví dụ).
4. **Ngắt câu:** Tách câu theo dấu ngắt chuẩn (`.`, `!`, `?`). Bỏ qua các chuỗi rỗng.
5. **Đếm từ & Tái lập thống kê:** Tách theo khoảng trắng (`split()`) sau khi hoàn nguyên các token được bảo vệ. Logic tổng hợp dữ liệu dùng chung (`aggregate_results`) giữa production và bộ kiểm thử tự động `unittest` (`python3 research/analyze_corpus.py --test`).

### Bảng Kết Quả Đo Lường Chi Tiết:

| # | Tên Tệp | Số Từ | Số Câu | Trung Bình (Mean) | Trung Vị (Median) | Số Câu >28 từ | % Câu >28 từ |
|---|---|---|---|---|---|---|---|
| 1 | `All Coffees Explained.md` | 5,962 | 348 | 17.1 | 17.0 | 46 | 13.2% |
| 2 | `All Sugars Explained.md` | 3,483 | 198 | 17.6 | 17.5 | 16 | 8.1% |
| 3 | `Every Cake Explained in 8 Minutes.md` | 1,088 | 82 | 13.3 | 13.5 | 1 | 1.2% |
| 4 | `Every Chocolate Explained.md` | 1,110 | 68 | 16.3 | 17.0 | 3 | 4.4% |
| 5 | `Every Famous Dessert Explained in 11 Minutes.md` | 1,553 | 125 | 12.4 | 12.0 | 1 | 0.8% |
| 6 | `Every Herb Explained.md` | 1,501 | 110 | 13.6 | 12.5 | 7 | 6.4% |
| 7 | `Every Spice Explained.md` | 2,743 | 172 | 15.9 | 15.0 | 12 | 7.0% |
| 8 | `Every Steak Explained in 10 Minutes.md` | 1,501 | 80 | 18.8 | 18.0 | 7 | 8.8% |
| 9 | `Every Style of Eggs Explained in 10 Minutes.md` | 1,525 | 72 | 21.2 | 21.0 | 7 | 9.7% |
| 10 | `Every Water Brand Explained.md` | 2,911 | 169 | 17.2 | 16.0 | 18 | 10.7% |
| **Tổng** | **Toàn bộ Corpus (10 video)** | **23,377** | **1,424** | **16.4** | **16.0** | **118** | **8.3%** |

### Kết Luận Biên Tập Từ Dữ Liệu:
- **Mean & Median:** Trung bình toàn corpus là **16.4 từ/câu**, trung vị là **16.0 từ/câu**. Dải trung bình dao động từ **12.4** (`Every Famous Dessert`) đến **21.2** (`Every Style of Eggs`).
- **Ngưỡng 28 từ:** Chỉ chiếm **8.3%** tổng số câu (118/1.424 câu). Đây là **Soft Editorial Heuristic**, chỉ dùng để rà soát các câu quá dài gây khó thở khi thu âm, không phải cổng chặn bắt buộc.
- **Hành vi mở đầu:** 10/10 tệp (100%) vào thẳng chủ thể, hoàn toàn không có lời chào cá nhân (*"Hi guys"*). Do transcript thô chưa căn chỉnh waveform, quy tắc "trong 10–15s đầu" là mục tiêu dựng rough cut, không phải số liệu đo từ văn bản.
- **Tần suất CTA:** 6/10 kịch bản có 0 CTA; 4/10 kịch bản có 1–2 CTA nhẹ ở outro; 0 kịch bản nào dùng công thức "3 CTA trải đều".

### Kỹ Thuật Chuyển Đoạn Quan Sát Được:
1. **The Boundary Shift (Biến đổi ranh giới nguyên liệu):**
   - *Trích dẫn nguyên văn từ corpus (`All Sugars Explained.md`, đoạn 2):*
     > *"Brown sugar is essentially white sugar that either never had all its molasses removed or had molasses added back in after refining."*
   - *Ví dụ minh họa biên tập (Constructed editorial example — not a verbatim quote):*
     > *"Where angel food relies purely on egg whites, chiffon reintroduces fat—in liquid form."*
2. **The Noun Drop / The Hard Shift (Chuyển tiếp gãy gọn):**
   - *Trích dẫn nguyên văn từ corpus (`Every Famous Dessert Explained in 11 Minutes.md`):*
     > *"Move the ratio even slightly and you land in a different dessert. Tiramisu is a cold layered Italian dessert built from espresso soaked lady fingers..."*
   - *Ví dụ minh họa biên tập (Constructed editorial example — not a verbatim quote):*
     > *"That's it. Pound cake."*

---

## ⚠️ 3. CẢNH BÁO KỸ THUẬT & GIỚI HẠN DỮ LIỆU ASR (SPEECH-TO-TEXT)

### A. Bản Chất Dữ Liệu
Văn bản trong `research/scripts/` là phụ đề nhận diện giọng nói tự động, chứa nhiều lỗi nhận diện âm vị đối với thuật ngữ nước ngoài và tên danh nhân.

### B. Chuẩn Hóa Âm Vị / Chính Tả Dự Đoán (Probable Phonetic / Spelling Normalization)
*(Chỉ nhằm phục vụ ngữ cảnh ngôn ngữ học và hiểu văn bản transcript thô. Toàn bộ tên riêng, năm lịch sử và phát minh gắn liền đều KHÔNG được xem là sự thật đã xác minh mà bắt buộc phải qua khâu nghiên cứu độc lập tại Bước 2 / `research.md`).*
- *"Conrad von Hton"* $\rightarrow$ Chuẩn hóa chính tả dự đoán: **Coenraad Johannes van Houten** [Cần kiểm chứng độc lập về lịch sử/năm nếu đưa vào video mới].
- *"Waldorf Atoria"* $\rightarrow$ Chuẩn hóa chính tả dự đoán: **Waldorf Astoria** (truyền thuyết bánh Red Velvet).
- *"Juliana Rad" / "Jacob Kristoff Rad"* $\rightarrow$ Chuẩn hóa chính tả dự đoán: **Jakub Kryštof Rad** [Cần kiểm chứng độc lập về lịch sử/năm nếu đưa vào video mới].
- *"Muan Vanang"* $\rightarrow$ Chuẩn hóa âm vị dự đoán: **Nguyễn Văn Giảng** [Cần kiểm chứng độc lập về nguồn gốc nếu đưa vào video mới].
- *"M foye"* $\rightarrow$ Chuẩn hóa âm vị: **Mille-feuille** (bánh ngàn lớp kiểu Pháp).
- *"Eclair's are shoe pastries"* $\rightarrow$ Lỗi nhận diện âm vị cho **Choux pastry** (bột choux nở bằng hơi nước, phát âm tiếng Pháp /ʃu/).
- *"maser ponyet cream"* $\rightarrow$ Lỗi nhận diện âm vị cho **Mascarpone cream** (phô mai Mascarpone).
- *"filow dough"* $\rightarrow$ Lỗi chính tả âm vị cho **Phyllo dough** (bột ngàn lớp Baklava).
- *"used"* $\rightarrow$ Lỗi nhận diện ASR cho phô mai nướng Phần Lan **Leipäjuusto** (trong ngữ cảnh cà phê Phần Lan, thường rút gọn là "juusto").
- *"turbanado, dearara, musavado"* $\rightarrow$ Chuẩn hóa chính tả: **Turbinado, Demerara, Muscovado** (các loại đường mía thô/bán tinh luyện).
- *"and7s"* / *"and50s"* $\rightarrow$ Lỗi dính số của ASR cho các thập niên: 1970s / 1950s.

---

## 🔒 4. QUY TẮC BẮT BUỘC DÀNH CHO BIÊN TẬP VIÊN

> 1. **TUYỆT ĐỐI KHÔNG DÙNG CORPUS ĐỂ FACT-CHECK:** Các file transcript mẫu chỉ phản ánh cấu trúc nhịp điệu và văn phong, không phải tài liệu khoa học hay lịch sử đã kiểm chứng. Mọi kiến thức cho video mới phải nghiên cứu độc lập ở Bước 2 (`research.md`).
> 2. **DÙNG ĐÚNG MỤC ĐÍCH:** Chỉ đối chiếu cách ngắt câu, đan xen câu ngắn và nhịp chuyển đoạn tự nhiên.
