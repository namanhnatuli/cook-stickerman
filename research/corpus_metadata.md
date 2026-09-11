# Research Corpus Metadata, Benchmark Provenance & Technical Caveats

Tài liệu này ghi lại thông tin định danh, nguồn gốc xuất xứ (provenance), số liệu đo lường thực nghiệm và cảnh báo kỹ thuật cho 10 kịch bản mẫu được lưu trữ trong `research/scripts/`.

---

## 📊 1. Bảng Danh Mục & Siêu Dữ Liệu 10 Kịch Bản Mẫu

- **Thời điểm thu thập dữ liệu (Snapshot Date):** Quý 3/2024 – Đầu 2025.
- **Công cụ trích xuất (Extraction Tool):** YouTube Native Automated Captions / Whisper Speech-to-Text Model.
- **Tổng dung lượng corpus:** 23.408 từ across ~1.422 câu được phân tích.

| # | Tên Tệp (`research/scripts/`) | Tiêu Đề Video Gốc | Kênh YouTube & Kênh Handle | Độ Dài & Số Từ | Khoảng View Ước Tính (Tại thời điểm cào) | Định Dạng & Lý Do Chọn Vào Corpus |
|---|---|---|---|---|---|---|
| 1 | `Every Cake Explained in 8 Minutes.md` | Every Cake Explained in 8 Minutes | **TasteDetective** (`@TasteDetective`) | 1,088 từ (~8 phút) | 500K – 800K views | Mẫu mực về taxonomy bánh ngọt, nhịp dẫn siêu nhanh (12.6 từ/câu), zero filler greeting, giải thích công thức cốt lõi và lịch sử thương mại. |
| 2 | `Every Famous Dessert Explained in 11 Minutes.md` | Every Famous Dessert Explained in 11 Minutes | **Decoded Dishes** (`@DecodedDishes`) | 1,569 từ (~11 phút) | 1M – 1.5M views | Điển hình về giải thích cơ chế vật lý (đông tụ, caramel hóa, nở bằng hơi nước, nhũ hóa) và cấu trúc đối lập crust vs. crumb. |
| 3 | `Every Steak Explained in 10 Minutes.md` | Every Steak Cut Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | 1,512 từ (~10 phút) | 800K – 1.2M views | Mẫu mực về phân tích cấu trúc vật lý (thớ cơ, collagen, mỡ dắt) và kỹ thuật đối phó với nhiệt độ cao. |
| 4 | `Every Style of Eggs Explained in 10 Minutes.md` | Every Style of Eggs Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | 1,527 từ (~10 phút) | 1.2M – 1.8M views | Cách giải thích protein biến tính (denaturation) và nhiệt độ đông tụ của lòng đỏ/trắng cực kỳ trực quan, dễ hiểu. |
| 5 | `Every Chocolate Explained.md` | Every Chocolate Explained in 10 Minutes | **Decoded Dishes** (`@DecodedDishes`) | 1,109 từ (~8–10 phút) | 400K – 600K views | Phân tích tỷ lệ bơ ca-cao, đường, sữa, tinh thể hóa (tempering) và sự khác biệt giữa các dòng sô-cô-la thương mại. |
| 6 | `Every Herb Explained.md` | Every Herb Explained | **Decoded Dishes** (`@DecodedDishes`) | 1,505 từ (~10 phút) | 600K – 900K views | Kỹ thuật chuyển đoạn bằng điểm dừng dứt khoát (The Noun Drop), giải thích tinh dầu thơm và cách tương tác với nhiệt độ. |
| 7 | `Every Spice Explained.md` | Every Spice Explained | **Decoded Dishes** (`@DecodedDishes`) | 2,743 từ (~18 phút) | 900K – 1.3M views | Mở rộng danh mục gia vị, cân bằng giữa nguồn gốc địa lý lịch sử và hợp chất hóa học tạo vị cay/nồng. |
| 8 | `Every Water Brand Explained.md` | Every Water Brand Explained | **Decoded Dishes** (`@DecodedDishes`) | 2,910 từ (~19 phút) | 1.5M – 2.2M views | Nghệ thuật bóc tách chiêu trò marketing, so sánh chỉ số khoáng chất TDS và nguồn nước ngầm. |
| 9 | `All Coffees Explained.md` | All Coffee Drinks Explained | **FooDiscover** (`@FooDiscover`) | 5,962 từ (~40 phút) | 2M – 3.5M views | Bách khoa toàn thư dài tập về đồ uống cà phê, tỷ lệ sữa/espresso, áp suất chiết xuất và văn hóa bản địa. |
| 10 | `All Sugars Explained.md` | All Sugars Explained | **FooDiscover** (`@FooDiscover`) | 3,483 từ (~24 phút) | 1M – 1.7M views | Deep-dive toàn diện về 8.000 năm lịch sử mía đường, hóa học sucrose/glucose/fructose và cơ chế hút ẩm hygroscopic. |

---

## 📈 2. Phương Pháp Đo Lường Thực Nghiệm & Phân Tích Dữ Liệu (Methodology)

### A. Độ Dài Câu & Nhịp Điệu (Sentence Rhythm)
- **Phương pháp đo:** Quét toàn bộ corpus qua dấu ngắt câu (`.`, `?`, `!`) sau khi loại trừ các ký tự viết tắt chuẩn.
- **Kết quả:**
  - Tổng số câu được phân tích: ~1.422 câu.
  - Trung bình từng video: Dao động từ **12.6 từ/câu** (video ngắn, nhịp dồn dập của *TasteDetective*) đến **21.2 từ/câu** (video tài liệu lịch sử chuyên sâu của *FooDiscover*).
  - Độ dài phổ biến nhất (median): **14–18 từ/câu**.
  - Tần suất vượt 28 từ: Có khoảng 120/1.422 câu (~8.4%) vượt quá 28 từ (thường rơi vào các câu mô tả lịch sử phức tạp hoặc điều kiện chế biến).
  - **Kết luận biên tập:** Quy tắc tách câu trên 28 từ là **Soft Editorial Heuristic** (khuyến nghị biên tập để người đọc voiceover không bị hụt hơi và khán giả dễ tiếp thu), không phải cổng kiểm duyệt tuyệt đối.

### B. Hành Vi Mở Đầu (Intro Hook)
- **Kết quả:** 10/10 video mẫu (100%) **hoàn toàn không có lời chào cá nhân** (*"Hi guys"*, *"Welcome back to my channel"*).
- 100% video mở đầu trực tiếp bằng việc nêu tên chủ thể kèm một nghịch lý, một sự thật phản trực giác hoặc câu hỏi tò mò trong vòng 10–15 giây đầu tiên.

### C. Khảo Sát Lời Kêu Gọi Tương Tác (CTA Analysis)
- **Phương pháp đo:** Tìm kiếm các từ khóa tương tác (*"subscribe"*, *"like"*, *"comment"*, *"let us know"*, *"tell us"*).
- **Kết quả:**
  - 6/10 video **hoàn toàn không có bất kỳ CTA nào** trong toàn bộ kịch bản.
  - 4/10 video chỉ có **1–2 CTA nhẹ nhàng**, hầu hết đặt ở câu kết video (Outro: hỏi ý kiến khán giả về món tiếp theo hoặc chia sẻ sở thích hương vị).
  - **Zero video** nào sử dụng cấu trúc gượng ép "3 CTA trải đều Đầu – Giữa – Cuối".
  - **Kết luận biên tập:** Kênh áp dụng tối đa 1 CTA ở Outro và tùy chọn 1 câu hỏi tương tác tự nhiên trong thân bài; tuyệt đối không chèn CTA cưỡng ép để đủ số lượng.

### D. Kỹ Thuật Chuyển Đoạn (Transitions)
- Các video không dùng từ nối khuôn mẫu của dạng listicle (*"Next up on our list..."*).
- Kỹ thuật chủ đạo:
  1. **The Noun Drop:** Kết thúc ý trước bằng một câu đấm ngắn, nghỉ 1 nhịp, rồi gọi thẳng tên món tiếp theo (*"That's it."* $\rightarrow$ *"Pound cake."*).
  2. **The Boundary Shift:** Dùng sự thay đổi của một biến số làm cầu nối (*"Where angel food relies purely on egg whites, chiffon reintroduces fat—in liquid form"*).

---

## ⚠️ 3. CẢNH BÁO KỸ THUẬT & GIỚI HẠN DỮ LIỆU ASR (SPEECH-TO-TEXT)

### A. Bản Chất Dữ Liệu
Văn bản trong `research/scripts/` là phụ đề tự động nhận diện từ giọng nói (Automated Speech Recognition), không phải văn bản xuất bản chính thức của tác giả. Do đó, có độ sai lệch âm vị học (phonetic mismatch) đáng kể đối với thuật ngữ ngoại quốc và tên riêng.

### B. Danh Mục Lỗi ASR Điển Hình Được Nhận Diện Trong Corpus
| Thuật Ngữ Trong Transcript ASR | Từ Gốc Đúng Về Mặt Lịch Sử / Ẩm Thực | Ý Nghĩa Chính Xác Cần Dùng Trong Nghiên Cứu |
|---|---|---|
| *"Conrad von Hton"* | **Coenraad Johannes van Houten** | Nhà hóa học Hà Lan phát minh bột ca-cao kiềm hóa (Dutch-processed cocoa) năm 1828. |
| *"Waldorf Atoria"* | **Waldorf Astoria** | Khách sạn New York gắn liền với truyền thuyết thương mại bánh Red Velvet. |
| *"Juliana Rad" / "Jacob Kristoff Rad"* | **Jakub Kryštof Rad** | Giám đốc nhà máy đường người Thụy Sĩ/Áo phát minh ra viên đường (sugar cube) năm 1841 sau tai nạn của vợ. |
| *"Muan Vanang"* | **Nguyễn Văn Giảng** | Nhân viên pha chế tại khách sạn Metropole Hà Nội sáng tạo ra món Cà phê trứng năm 1946. |
| *"M foye"* | **Mille-feuille** | Bánh ngàn lớp kinh điển của Pháp làm từ bột ngàn lớp lamination. |
| *"Eclair's are shoe pastries"* | **Choux pastry** (*pâte à choux*) | Loại bột nấu nở phồng hoàn toàn bằng hơi nước (steam leavening). |
| *"maser ponyet cream"* | **Mascarpone cream** | Phô mai Mascarpone béo mịn của Ý dùng trong Tiramisu. |
| *"filow dough"* | **Phyllo / Filo dough** | Lớp bột mỏng như giấy dùng trong bánh Baklava. |
| *"used"* (trong Finnish coffee) | **Leipäjuusto** | Phô mai nướng đặc sản Phần Lan dùng uống cùng cà phê (*kaffeost*). |
| *"turbanado, dearara, musavado"* | **Turbinado, Demerara, Muscovado** | Các loại đường thô (raw sugars) giữ lại tỷ lệ mật mía tự nhiên khác nhau. |
| *"and7s"* / *"and50s"* | **1970s / 1950s** | Các thập niên bị AI ASR ghép dính chữ. |
| *"artisal"* | **Artisanal** | Thuật ngữ thủ công bị nhận diện sai chính tả. |

---

## 🔒 4. QUY TẮC BẮT BUỘC DÀNH CHO BIÊN TẬP VIÊN VÀ AI

> 1. **CẤM DÙNG CORPUS LÀM BẰNG CHỨNG SỰ THẬT:** Tuyệt đối không trích dẫn các câu chuyện lịch sử, năm tháng, hay cơ chế hóa học từ 10 kịch bản mẫu này vào video mới của Cook Stickerman. Mọi thông tin khoa học bắt buộc phải được nghiên cứu và kiểm chứng độc lập ở Bước 2 (`research.md`).
> 2. **CHỈ SỬ DỤNG CHO PHÂN TÍCH NHỊP ĐIỆU:** Các tệp corpus này chỉ phục vụ mục đích học hỏi về cấu trúc câu ngắn, nhịp kể dồn dập, cách ngắt nhịp và kỹ thuật chuyển đoạn.
